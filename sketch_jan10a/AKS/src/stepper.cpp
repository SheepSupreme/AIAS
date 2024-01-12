
#include "stepper.h"

Stepper::Stepper(){
    M0 = 5;
    M1 = 6;
    M2 = 7;
    nEnable_pin = 4;
    step_pin = 3;
    direction_pin = 2;
    stepper_speed = 100;
}

void Stepper::pin_init(byte step_pin, byte direction_pin){
    pinMode(step_pin,OUTPUT);
    digitalWrite(step_pin,LOW);
    pinMode(direction_pin,OUTPUT);
    digitalWrite(direction_pin,LOW);
}

int Stepper::speed2time(int stepper_speed)
{   
    return unsigned (1000/stepper_speed);
}

void Stepper::move(int steps_to_move, int stepper_speed)
{
    unsigned int update_time = millis();
    
    int counter = 0;
    while(counter <= steps_to_move){
        if(millis()>=update_time+speed2time(stepper_speed)){
            digitalWrite(step_pin,LOW);
            digitalWrite(step_pin,HIGH);
            update_time = millis();
            counter++;
        }
    }
}