#ifndef stepper_h
#define stepper_h

#include <Arduino.h>

class Stepper
{
    public:
        Stepper(int pin_dir, int pin_step, int pin_nEnable, int pin_M0, int pin_M1, int pin_M2, int es1_pin, int es2_pin); //Constructor decleration

        byte M0;
        byte M1;
        byte M2;
        byte nEnable_pin;
        byte step_pin;
        byte direction_pin;

        //positions

        double _current_position = 1E5;
        double absolute_position;
        double endstop_position =1E6;

        //methods
        //paramenter
        void change_profile(int speed, int accel);
        void change_microstep_resolution(short int resolution);
        //movement

        void calibration(unsigned int endstop_offset);
        void calibration_direction(int endstop_offset, int direction, double max_calibration_travel);
        void move_relative(double relative_steps);
        void move_absolute(uint32_t position);
        void setup_move(double absolute_pos);
        void out_ofRange();
        bool buttonPressed(int btn_pin,bool &btn_state);

        bool move();

    private:
        uint32_t DEBOUNCE_DELAY = 100;
        int _accel;
        double _speed;
        double _speed_calibration = 400;

        unsigned int lastDebounceTime = 0;

        bool endstop1_lastState = HIGH;
        bool endstop2_lastState = HIGH;
        int endstop1_pin;
        int endstop2_pin;

        int multiplier; //acceleration or deceleration
        int deceleration_distance;
        double relative_distance;
        unsigned int first_period_US;
        double this_move_period;
        unsigned int running_period_US;
        unsigned int last_move_time_US;
        float _microstep_resolution = 1.0f;
        int _dir;
        bool new_move;
        
        float microstep_table[8][4] = 
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