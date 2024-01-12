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

        int _speed;
        int _accel;
        bool _dir;
        short int _microstep_resolution;
        Stepper(); //Constructor decleration
        bool move();
        void pin_init(byte step_pin, byte direction_pin);
        void setup_move(int _speed, int _accel, bool _dir);
        void change_microstep_resolution(short int _microstep_resolution); //

    private:
        
        bool increment_table[8][3] = 
        {{0,0,0},   // Full-Step-Betrieb
        {1,0,0},    // Half-Step-Betrieb
        {0,1,0},    // 1/4-Step-Betrieb        
        {1,1,0},    // 1/8-Step-Betrieb
        {0,0,1},    // 1/16-Step-Betrieb
        {1,0,1},    // 1/32-Step-Betrieb
        {0,1,1},    // 1/32-Step-Betrieb
        {1,1,1}};   // 1/32-Step-Betrieb

};

#endif