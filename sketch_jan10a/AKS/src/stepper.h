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

        //positions
        signed long int _current_position;
        signed int absolute_position;
        signed int endstop_position;

        //methods
        //paramenter
        void pin_init(byte nEnable_pin_nmbr, byte step_pin_nmbr, byte direction_pin_nmbr);
        void change_profile(int speed, int accel);
        void change_microstep_resolution(short int resolution);
        //movement
        void calibration(unsigned int endstop_offset);
        void endstop_contact(unsigned int endstop_offset, int direction, bool home, double max_calibration_travel);
        void relative_in_steps(double relative_steps);
        void setup_move(int absolute_pos);
        bool move();
        //interrupt fn
        static void endstop_trigger();

    private:
        int _accel;
        double _speed;
        double _speed_calibration = 300;

        static volatile bool _interrupt;

        static const int endstop1_pin = 20;
        static const int endstop2_pin = 21;

        int multiplier; //acceleration or deceleration
        unsigned int deceleration_distance;
        signed int relative_distance;
        unsigned int first_period_US;
        double this_move_period;
        unsigned int running_period_US;
        unsigned int last_move_time_US;
        unsigned int _microstep_resolution;
        int _dir;
        bool new_move;
        
        int microstep_table[8][4] = 
        {{0,0,0,1},   //0 = Full-Step-Betrieb
        {1,0,0,2},    //1 = Half-Step-Betrieb
        {0,1,0,4},    //2 = 1/4-Step-Betrieb        
        {1,1,0,8},    //3 = 1/8-Step-Betrieb
        {0,0,1,16},    //4 = 1/16-Step-Betrieb
        {1,0,1,32},    //5 = 1/32-Step-Betrieb
        {0,1,1,32},    //6 = 1/32-Step-Betrieb
        {1,1,1,32}};   //7 = 1/32-Step-Betrieb

};

#endif