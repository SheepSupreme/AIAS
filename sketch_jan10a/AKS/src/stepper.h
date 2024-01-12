#ifndef stepper_h
#define stepper_h

#include <Arduino.h>

class Stepper
{
    public:
        byte M0;
        byte M1;
        byte M2;
        byte nEnable_pin;
        byte step_pin;
        byte direction_pin;
        int stepper_speed;
        int stepper_period;
        Stepper(); //Constructor decleration
        void move(int steps_to_move, int stepper_speed);
        void pin_init(byte step_pin, byte direction_pin);
        int speed2time(int stepper_speed);
};

#endif