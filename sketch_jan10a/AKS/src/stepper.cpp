
#include "stepper.h"

Stepper::Stepper(){
    M0 = 5;
    M1 = 6;
    M2 = 7;
    nEnable_pin = 4;
    step_pin = 3;
    direction_pin = 2;
    _speed = 200;
    _accel = 200;
}

void Stepper::pin_init(byte step_pin, byte direction_pin){
    pinMode(step_pin,OUTPUT);
    digitalWrite(step_pin,LOW);
    pinMode(direction_pin,OUTPUT);
    digitalWrite(direction_pin,LOW);
}

void Stepper::change_microstep_resolution(short int _microstep_resolution)
{
    
}

