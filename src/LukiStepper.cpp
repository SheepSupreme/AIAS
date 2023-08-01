
//      ******************************************************************
//      *                                                                *
//      *                   Speedy Stepper Motor Driver                  *
//      *                                                                *
//      *            Stan Reifel                     12/8/2014           *
//      *               Copyright (c) S. Reifel & Co, 2014               *
//      *                                                                *
//      ******************************************************************


#include <LukiStepper.h>


LukiStepper::LukiStepper()
{
  //
  // initialize constants
  //
  stepPin = 0;
  directionPin = 0;
  stepsPerMillimeter = 25.0;
  currentPosition_InSteps = 0;
  desiredSpeed_InStepsPerSecond = 16000;
  acceleration_InStepsPerSecondPerSecond = 250000;
  currentStepPeriod_InUS = 0.0;
}


void LukiStepper::connectToPins(byte stepPinNumber, byte directionPinNumber)
{
  stepPin = stepPinNumber;
  directionPin = directionPinNumber;
  
  pinMode(stepPin, OUTPUT);
  digitalWrite(stepPin, LOW);

  pinMode(directionPin, OUTPUT);
  digitalWrite(directionPin, LOW);
}


