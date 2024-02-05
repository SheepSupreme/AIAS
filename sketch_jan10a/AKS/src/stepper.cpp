
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

int Stepper::relative2absolute(int relative)
{
    double absolute = (_current_position + relative);
    return absolute;
}

int Stepper::absolute2relative(int absolute)
{
    double relative = (absolute - _current_position);
    return relative;
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

void Stepper::calibration_direction(int endstop_offset, int direction)
{   
    if(direction == -1){
        alt_pos = _current_position;
    }
    else{
        alt_pos = endstop_position;
    }
    
    setup_move(direction*alt_pos);
    digitalWrite(nEnable_pin,LOW);
    while(!move()){}
    Serial.println("move1 end");

    if(direction == -1){
        alt_pos = endstop_position;
    }
    else{
        alt_pos = _current_position;
    }

    setup_move(-direction*alt_pos);
    Serial.println(alt_pos);
    while(!move()){}
    Serial.println("move2 end");
    digitalWrite(nEnable_pin,HIGH);

    move_relative(-direction*endstop_offset);
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

    calibration_direction(endstop_offset/_microstep_resolution, -1);

    calibration_direction(endstop_offset/_microstep_resolution, 1);

    _speed = _speed_copy;
}


void Stepper::setup_move(double relative)
{
    _relative = relative;
    absolute_position = _current_position + _relative;
    Serial.println(absolute_position);

    //Test if target position is in calibrated range
    if(absolute_position < 0 || absolute_position > endstop_position+_current_position){
      out_ofRange();
    }
    
    this_move_period = 1000000.0/sqrt(2.0*_accel); // first period in US
    running_period_US = 1000000.0/_speed;
    deceleration_distance = (_speed*_speed)/(2.0*_accel);

    if (_relative < 0){
        _dir = -1;
    }
    else if(_relative > 0){
        _dir = 1;
    }

    if (abs(_relative)/2 < deceleration_distance){
        deceleration_distance = abs(_relative)/2;
    }
    new_move = true;
}

void Stepper::out_ofRange(){
    absolute_position = _current_position;
    Serial.println("Move not possible due to calibration range restrictions");
}

void Stepper::move_relative(double relative_steps)
{
  setup_move(relative_steps);
  digitalWrite(nEnable_pin,LOW);
  while(!move()){}
  digitalWrite(nEnable_pin,HIGH);
}

void Stepper::move_absolute(uint32_t position){
  setup_move(absolute2relative(position));
  digitalWrite(nEnable_pin,LOW);
  while(!move()){}
  digitalWrite(nEnable_pin,HIGH);
}

bool Stepper::buttonPressed(int btn_pin,bool &btn_state){
  bool* last_state = &btn_state;
  int endstop_pin = btn_pin;
  int endstop_State = digitalRead(endstop_pin);
  lastDebounceTime = millis();
  if(endstop_State != *last_state){
    while((millis() - lastDebounceTime) < DEBOUNCE_DELAY){
      int _read = digitalRead(endstop_pin);
      if(_read != *last_state){
        lastDebounceTime = millis();
        *last_state = _read;
      }
      *last_state = _read;
    }
    Serial.println("trigger");
    return true;
  }
  return false;
}

bool Stepper::move()
{
    unsigned int period_last_step;
    unsigned int current_time_US;
    int distance_2_target;

    if(_current_position == absolute_position)
    {   
        return true;
    }

    if(buttonPressed(endstop1_pin, endstop1_lastState))
    {   
        return true;
    }

    if(buttonPressed(endstop2_pin, endstop2_lastState))
    {   
        return true;
    }

    digitalWrite(direction_pin,abs(min(0,_dir)));

    if(new_move){
        multiplier = 1;
        last_move_time_US = micros();
        new_move = false;
    }
    current_time_US = micros();
    period_last_step = current_time_US - last_move_time_US;

    if(period_last_step < this_move_period){
        return false;
    }
    last_move_time_US = micros();

    distance_2_target = abs(absolute2relative(absolute_position));

    if(distance_2_target == deceleration_distance){
        multiplier = -1;
    }
    if(this_move_period < running_period_US){
        this_move_period = running_period_US;
        multiplier = 0;
    }

    
    digitalWrite(step_pin,HIGH);
    delayMicroseconds(2);
    this_move_period = this_move_period*(1.0-multiplier*(_accel/1E12)*this_move_period*this_move_period);
    _current_position = _current_position + _dir;

    digitalWrite(step_pin,LOW);

    last_move_time_US = current_time_US;

    if(_current_position == absolute_position)
    {   
        return true;
    }
    return false;
}