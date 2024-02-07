#ifndef LukiStepper_h // Schützt vor mehrfachem includen
#define LukiStepper_h

#include <Arduino.h>
#include <stdlib.h>


// LukiStepper class

class LukiStepper
{
  public:
    //
    // public functions
    //
    LukiStepper();
    void connectToPins(byte stepPinNumber, byte directionPinNumber);

    void setCurrentPositionInSteps(long currentPositionInSteps);
    long getCurrentPositionInSteps();
    void setSpeedInStepsPerSecond(float speedInStepsPerSecond);
    void setAccelerationInStepsPerSecondPerSecond(float accelerationInStepsPerSecondPerSecond);
    bool calibration(long directionTowardsendStop, float calibrationSpeed, long maxDistanceToMoveInSteps, int endStop1, bool zero);
    void moveRelativeInSteps(long distanceToMoveInSteps, int endstop_1, int endstop_2);
    void moveToPositionInSteps(long absolutePositionToMoveToInSteps);
    void setupMoveInSteps(long absolutePositionToMoveToInSteps);
    void setupRelativeMoveInSteps(long distanceToMoveInSteps);
    bool motionComplete();
    float getCurrentVelocityInStepsPerSecond(); 
    bool processMovement(void);


  private:
    //
    // private member variables
    //
    byte nEnable;
    byte M0;
    byte M1;
    byte M2;
    byte stepPin;
    byte directionPin;
    float calibrationSpeed;
    float desiredSpeed_InStepsPerSecond;
    float acceleration_InStepsPerSecondPerSecond;
    long targetPosition_InSteps;
    bool startNewMove;
    int endstop_1;
    int endstop_2;
    float desiredStepPeriod_InUS;
    long decelerationDistance_InSteps;
    int direction_Scaler;
    float ramp_InitialStepPeriod_InUS;
    float ramp_NextStepPeriod_InUS;
    unsigned long ramp_LastStepTime_InUS;
    float acceleration_InStepsPerUSPerUS;
    float currentStepPeriod_InUS;
    long currentPosition_InSteps;
};




#endif