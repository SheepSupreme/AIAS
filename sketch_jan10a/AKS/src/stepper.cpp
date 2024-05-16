
#include "stepper.h"

Stepper::Stepper(int pin_dir, int pin_step, int pin_nEnable, int pin_M0, int pin_M1, int pin_M2, int es1_pin, int es2_pin){
    step_pin = pin_step;
    direction_pin = pin_dir;
    nEnable_pin = pin_nEnable;
    M0 = pin_M0;
    M1 = pin_M1;
    M2 = pin_M2; 
    _speed = 200;
    _accel = 200;
    endstop1_pin = es1_pin;
    endstop2_pin = es2_pin;

    pinMode(step_pin,OUTPUT);
    digitalWrite(step_pin,LOW);
    pinMode(direction_pin,OUTPUT);
    digitalWrite(direction_pin,LOW);
    pinMode(nEnable_pin,OUTPUT);
    digitalWrite(nEnable_pin,HIGH);

    pinMode(endstop1_pin, INPUT_PULLUP);
    pinMode(endstop2_pin, INPUT_PULLUP);
}

void Stepper::change_microstep_resolution(short int resolution)
{
    endstop_position = endstop_position*(_microstep_resolution/(1.0f/microstep_table[resolution][3]));
    _speed_calibration = _speed_calibration*(_microstep_resolution/(1.0f/microstep_table[resolution][3]));
    _current_position = _current_position*(_microstep_resolution/(1.0f/microstep_table[resolution][3]));

    _microstep_resolution = 1.0f/microstep_table[resolution][3]; //current resolution e.g. 1/4
    digitalWrite(M0, microstep_table[resolution][0]);
    digitalWrite(M1, microstep_table[resolution][1]);
    digitalWrite(M2, microstep_table[resolution][2]);
}

void Stepper::change_profile(int speed, int accel)
{
    _speed = speed;
    _accel = accel;
}

void Stepper::calibration_direction(int endstop_offset, int direction, double max_calibration_travel)
{   
    //1. Annäherungsphase
    move_relative(direction*max_calibration_travel);
    //2. Rückziehphase
    move_relative(-direction*1E3);
    //3. Sicherheitsabstandeinstellung
    move_relative(-direction*endstop_offset);
    //Einspeicherung der Position für die Grenzen
    if(direction == 1){
      endstop_position = _current_position;
    }
    if(direction == -1){
      _current_position = 0;
    }
}


void Stepper::calibration(unsigned int endstop_offset)
{   

    double _speed_copy = _speed;
    _speed = _speed_calibration;

    calibration_direction(endstop_offset/_microstep_resolution, -1, 1E5);

    calibration_direction(endstop_offset/_microstep_resolution, 1, 1E5);

    _speed = _speed_copy;
}


void Stepper::setup_move(double absolute_pos)
{
    absolute_position = absolute_pos;

    //Test ob sich Zielposition im kalibrierten Bereich befindet
    if(absolute_position < 0 || absolute_position > endstop_position){
      out_ofRange();
    }
    
    this_move_period = 1000000.0/sqrt(2.0*_accel); // Erste Periode in US
    running_period_US = 1000000.0/_speed; // Perioden nach Erreichen der Geschwindigkeit
    deceleration_distance = (_speed*_speed)/(2.0*_accel); //Bremsdistanz

    //Vergabe des Wertes für die Richtung in die gefahren wird
    relative_distance = absolute_position - _current_position; 
    if (relative_distance < 0){
        _dir = -1;
    }
    else if(relative_distance > 0){
        _dir = 1;
    }
    //Umrechnung der Bremsdistanz falls nicht ausreichend
    if (abs(relative_distance)/2 < deceleration_distance){
        deceleration_distance = abs(relative_distance)/2;
    }
    new_move = true;
}

void Stepper::out_ofRange(){
    absolute_position = _current_position;
    Serial.println("outofrange"); 
}

void Stepper::move_relative(double relative_steps)
{
  setup_move(_current_position + relative_steps);
  digitalWrite(nEnable_pin,LOW);
  while(!move()){}
  digitalWrite(nEnable_pin,HIGH);
}

void Stepper::move_absolute(uint32_t position){
  setup_move(position);
  digitalWrite(nEnable_pin,LOW);
  while(!move()){}
  digitalWrite(nEnable_pin,HIGH);
}

bool Stepper::buttonPressed(int btn_pin,bool &btn_state){
  bool* last_state = &btn_state;  // Übernahme des Letzten Endschalter Wertes
  int endstop_pin = btn_pin;    // Übernahme des Letzten Endschalter PINs
  int endstop_State = digitalRead(endstop_pin); //Lesen des aktuellen Wertes
  lastDebounceTime = millis();  // Zeitmessung letzte Prellung
  if(endstop_State != *last_state){
    // Erkennung ob die nötige Zeit ohne Prellung erreicht wurde
    while((millis() - lastDebounceTime) < DEBOUNCE_DELAY){
      int _read = digitalRead(endstop_pin);
      if(_read != *last_state){
        //Wenn sich der Wert ändert wird die Zeit zurückgesetzt
        lastDebounceTime = millis();
        *last_state = _read;
      }
      *last_state = _read;
    }
    return true; //Nötige Zeit ohne Prellung erreicht
  }
  return false;
}

bool Stepper::move()
{
    unsigned int period_last_step;//Periodendauer des vorigen Schrittes
    unsigned int current_time_US;//aktuelle Zeit in US
    int distance_2_target;//Distanz zur Zielposition 

    //Erreichen der Zielposition
    if(_current_position == absolute_position)
    {   
        return true;
    }

    //Auslösen des Endschalters 1.
    if(buttonPressed(endstop1_pin, endstop1_lastState))
    {   
        return true;
    }

    //Auslösen des Endschalters 2.
    if(buttonPressed(endstop2_pin, endstop2_lastState))
    {   
        return true;
    }

    if(new_move){
        multiplier = 1; //Beschleunigung --> 1; Bremsvorgang -->0;
        last_move_time_US = micros(); //Zeit des letzten Schrittes zurückgesetzt
        new_move = false;  // if-statement soll nur 1. Mal durchgeführt werden
    }

    //Umwandlung der Richtungsvariable "_dir" in eine Boolean und Ausgabe dieses Zustandes am Ausgang des DIR PINS
    digitalWrite(direction_pin,abs(min(0,_dir)));
    
    current_time_US = micros();
    period_last_step = current_time_US - last_move_time_US; //Berechnung für Periodendauer seit letztem Schritt

    //Falls die Periodenauer seit dem letzten Schritt kleiner als die Periodendauer ist, die benötigt wird um die Geschwindigkeit für den jetzigen Schritt zu erzielen, wird die Methode unterbrochen und von neu begonnen.
    if(period_last_step < this_move_period){
        return false;
    }
    //Es ist Zeit für den nächsten Schritt
    last_move_time_US = micros();

    //Berechnung der Distanz zu der Zielposition
    distance_2_target = abs(absolute_position - _current_position);

    //Einleitung der Bremsphase
    if(distance_2_target == deceleration_distance){
        multiplier = -1;
    }

    //Geschwindigkeit halten
    if(this_move_period < running_period_US){
        this_move_period = running_period_US;
        multiplier = 0; //Einhalten einer Gleichbleibenden Geschwindigkeit
    }

    digitalWrite(step_pin,HIGH);//Positive Taktflanke am STEP-PIN
    delayMicroseconds(2); //Kurze Pause für Stabilisierung der Pinspannung
    //Berechnung der Periodendauer für den nächsten Schritt
    this_move_period = this_move_period*(1.0-multiplier*(_accel/1E12)*this_move_period*this_move_period); 
    _current_position = _current_position + _dir;//Aktualisierung der Position

    digitalWrite(step_pin,LOW);//Negative Taktflanke am STEP-PIN

    last_move_time_US = current_time_US;//Aktualisierung der Variable für den Zeitpunkt des letzten Schrittes

    //Erreichen der Zielposition
    if(_current_position == absolute_position)
    {   
        return true;
    }
    return false;
}