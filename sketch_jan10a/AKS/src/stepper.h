#ifndef stepper_h
#define stepper_h

#include <Arduino.h>

class Stepper
{
    public:
        Stepper(); //Constructor decleration

        byte M0;
        byte M1;
        byte M2;
        byte nEnable_pin;
        byte step_pin;
        byte direction_pin;

        signed long int _current_position;
        signed int absolute_position;
        float _speed;
        int _speed_calibration;
        int _accel;
        signed int relative_distance;
        double this_move_period;
        unsigned int last_move_time_US;
        int _dir;
        bool home;
        short int _microstep_resolution;
        bool move();
        void pin_init(byte nEnable_pin_nmbr, byte step_pin_nmbr, byte direction_pin_nmbr);
        void setup_move(int absolute_pos);
        void change_microstep_resolution(short int _microstep_resolution);
        bool endstop_contact(unsigned int endstop_offset, int direction, bool home);
        void calibration(unsigned int endstop_offset);
        void relative_in_steps(int relative_steps);
        void change_profile(int speed, int accel);
        static void endstop_trigger();

    private:

        static volatile bool _interrupt;
        static const int endstop1_pin = 20;
        static const int endstop2_pin = 21;
        float multiplier;
        unsigned int first_period_US;
        unsigned int deceleration_distance;
        unsigned int running_period_US;
        bool new_move;
        
        int microstep_table[8][3] = 
        {{0,0,0},   //0 = Full-Step-Betrieb
        {1,0,0},    //1 = Half-Step-Betrieb
        {0,1,0},    //2 = 1/4-Step-Betrieb        
        {1,1,0},    //3 = 1/8-Step-Betrieb
        {0,0,1},    //4 = 1/16-Step-Betrieb
        {1,0,1},    //5 = 1/32-Step-Betrieb
        {0,1,1},    //6 = 1/32-Step-Betrieb
        {1,1,1}};   //7 = 1/32-Step-Betrieb

};

#endif