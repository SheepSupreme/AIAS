
#include "stepper.h"

volatile bool Stepper::_interrupt = false;

Stepper::Stepper(){
    M0 = 5;
    M1 = 6;
    M2 = 7;
    nEnable_pin = 4;
    step_pin = 3;
    direction_pin = 2;
    _speed = 200;
    _accel = 200;
    pinMode(endstop1_pin,INPUT_PULLUP);
    attachInterrupt(digitalPinToInterrupt(endstop1_pin),endstop_trigger,FALLING);
}

void Stepper::pin_init(byte nEnable_pin_nmbr, byte step_pin_nmbr, byte direction_pin_nmbr){
    step_pin = step_pin_nmbr;
    direction_pin = direction_pin_nmbr;
    nEnable_pin = nEnable_pin_nmbr;

    pinMode(step_pin,OUTPUT);
    digitalWrite(step_pin,LOW);
    pinMode(direction_pin,OUTPUT);
    digitalWrite(direction_pin,LOW);

    pinMode(nEnable_pin,OUTPUT);
    digitalWrite(nEnable_pin,HIGH);
}

void Stepper::change_microstep_resolution(short int _microstep_resolution)
{
    digitalWrite(M0, microstep_table[_microstep_resolution][0]);
    digitalWrite(M1, microstep_table[_microstep_resolution][1]);
    digitalWrite(M2, microstep_table[_microstep_resolution][2]);
}

void Stepper::setup_move(int absolute_pos)
{
    absolute_position = absolute_pos;
    multiplier = 1;
    // first period in US
    this_move_period = 1000000.0/sqrt(2.0*_accel);
    running_period_US = 1000000.0/_speed;
    deceleration_distance = (_speed*_speed)/(2.0*_accel);

    relative_distance = absolute_position - _current_position;
    if (relative_distance < 0){
        _dir = -1;
    }
    else if(relative_distance > 0){
        _dir = 1;
    }

    if (abs(relative_distance)/2 < deceleration_distance){
        deceleration_distance = abs(relative_distance)/2;
    }
    new_move = true;
}


bool Stepper::endstop_contact(unsigned int endstop_offset, int direction, bool home)
{   
    _dir = direction;
    if(digitalRead(endstop1_pin)&&digitalRead(endstop2_pin)){
        _dir = -_dir;
        int endstop_position = _current_position;
        while((digitalRead(endstop1_pin)&&digitalRead(endstop2_pin))&&_current_position*direction < (endstop_position*direction+endstop_offset)){
            move();
        }
        if (home){_current_position = 0;}
        return true;
    }
    return false;
}


void Stepper::calibration(unsigned int endstop_offset)
{   

    running_period_US = 1000000/_speed_calibration;

    while(!endstop_contact(endstop_offset, -1, true)){
        move();
    }

    while(!endstop_contact(endstop_offset, 1, false)){
        move();
    }

    _dir = -1;
    while(!(digitalRead(endstop1_pin)&&digitalRead(endstop2_pin))){
        move();
    }

}

void Stepper::change_profile(int speed, int accel)
{
    _speed = speed;
    _accel = accel;
    Serial.println(_speed);
    Serial.println(_accel);
}

void Stepper::relative_in_steps(int relative_steps)
{
    setup_move(_current_position + relative_steps);
    digitalWrite(nEnable_pin,LOW);
    while(!move()){
        // Serial.print(_current_position);
        // Serial.print("   ");
        // Serial.print(this_move_period);
        // Serial.print("   ");
        // Serial.println(deceleration_distance);
    }
    digitalWrite(nEnable_pin,HIGH);
}

void Stepper::endstop_trigger()
{
    if(digitalRead(endstop1_pin) == LOW){
        _interrupt = true;
    }
    else{
        _interrupt = false;
    }
}

bool Stepper::move()
{
    unsigned int period_last_step;
    unsigned int current_time_US;
    unsigned int distance_2_target;

    digitalWrite(direction_pin,max(0,_dir));

    if(_interrupt){
        return true;
    }

    if(new_move){
        last_move_time_US = micros();
        new_move = false;
    }
    current_time_US = micros();
    period_last_step = current_time_US - last_move_time_US;

    if(period_last_step < this_move_period){
        return false;
    }
    last_move_time_US = micros();

    distance_2_target = abs(absolute_position - _current_position);

    if(distance_2_target == deceleration_distance){
        multiplier = -1;
        Serial.println("stop");
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
