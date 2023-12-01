
//      ******************************************************************
//      *                                                                *
//      *                   Speedy Stepper Motor Driver                  *
//      *                                                                *
//      *            Stan Reifel                     12/8/2014           *
//      *               Copyright (c) S. Reifel & Co, 2014               *
//      *                                                                *
//      ******************************************************************


// MIT License
// 
// Copyright (c) 2014 Stanley Reifel & Co.
// 
// Permission is hereby granted, free of charge, to any person obtaining a copy
// of this software and associated documentation files (the "Software"), to deal
// in the Software without restriction, including without limitation the rights
// to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
// copies of the Software, and to permit persons to whom the Software is furnished
// to do so, subject to the following conditions:
// 
// The above copyright notice and this permission notice shall be included in all
// copies or substantial portions of the Software.
// 
// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
// IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
// FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
// AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
// LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
// OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
// SOFTWARE.


#include "LukiStepper.h"


LukiStepper::LukiStepper()
{
  //
  // initialize constants
  //
  M0 = 5;
  M1 = 6;
  M2 = 7;
  nEnable = 4;
  stepPin = 3;
  directionPin = 2;
  currentPosition_InSteps = 0;
  desiredSpeed_InStepsPerSecond = 16000;
  calibrationSpeed = 8000;
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

void LukiStepper::setCurrentPositionInSteps(long currentPositionInSteps)
{
  currentPosition_InSteps = currentPositionInSteps;
}



//
// get the current position of the motor in steps, this functions is updated
// while the motor moves
//  Exit:  a signed motor position in steps returned
//
long LukiStepper::getCurrentPositionInSteps()
{
  return(currentPosition_InSteps);
}


void LukiStepper::setSpeedInStepsPerSecond(float speedInStepsPerSecond)
{
  desiredSpeed_InStepsPerSecond = speedInStepsPerSecond;
}

void LukiStepper::setAccelerationInStepsPerSecondPerSecond(
                      float accelerationInStepsPerSecondPerSecond)
{
    acceleration_InStepsPerSecondPerSecond = accelerationInStepsPerSecondPerSecond;
}

//
// setup a move relative to the current position, units are in steps, no motion  
// occurs until processMove() is called.  Note: this can only be called when the 
// motor is stopped
//  Enter:  distanceToMoveInSteps = signed distance to move relative to the current  
//          position in steps
//
void LukiStepper::setupRelativeMoveInSteps(long distanceToMoveInSteps)
{
  setupMoveInSteps(currentPosition_InSteps + distanceToMoveInSteps);

}


void LukiStepper::moveRelativeInSteps(long distanceToMoveInSteps, int endstop_1 , int endstop_2)
{
  setupRelativeMoveInSteps(distanceToMoveInSteps);

  while(digitalRead(endstop_1)!=HIGH && digitalRead(endstop_2)!=HIGH){
    if(processMovement()){
      return 0;
    }
  }

}




//
// move to the given absolute position, units are in steps, this function does not 
// return until the move is complete
//  Enter:  absolutePositionToMoveToInSteps = signed absolute position to move to  
//            in units of steps
//
void LukiStepper::moveToPositionInSteps(long absolutePositionToMoveToInSteps)
{
  setupMoveInSteps(absolutePositionToMoveToInSteps);
  
  while(!processMovement())
    ;
}



//
// setup a move, units are in steps, no motion occurs until processMove() is called
// Note: this can only be called when the motor is stopped
//  Enter:  absolutePositionToMoveToInSteps = signed absolute position to move to in 
//          units of steps
//
void LukiStepper::setupMoveInSteps(long absolutePositionToMoveToInSteps)
{
  long distanceToTravel_InSteps;
  
  
  //
  // save the target location
  //
  targetPosition_InSteps = absolutePositionToMoveToInSteps;
  

  //
  // determine the period in US of the first step
  //
  ramp_InitialStepPeriod_InUS =  1000000.0 / sqrt(2.0 * 
                                    acceleration_InStepsPerSecondPerSecond);
    
    
  //
  // determine the period in US between steps when going at the desired velocity
  //
  desiredStepPeriod_InUS = 1000000.0 / desiredSpeed_InStepsPerSecond;


  //
  // determine the number of steps needed to go from the desired velocity down to a 
  // velocity of 0, Steps = Velocity^2 / (2 * Accelleration)
  //
  decelerationDistance_InSteps = (long) round((desiredSpeed_InStepsPerSecond * 
    desiredSpeed_InStepsPerSecond) / (2.0 * acceleration_InStepsPerSecondPerSecond));
  
  
  //
  // determine the distance and direction to travel
  //
  distanceToTravel_InSteps = targetPosition_InSteps - currentPosition_InSteps;
  if (distanceToTravel_InSteps < 0) 
  {
    distanceToTravel_InSteps = -distanceToTravel_InSteps;
    direction_Scaler = -1;
    digitalWrite(directionPin, HIGH);
  }
  else
  {
    direction_Scaler = 1;
    digitalWrite(directionPin, LOW);
  }


  //
  // check if travel distance is too short to accelerate up to the desired velocity
  //
  if (distanceToTravel_InSteps <= (decelerationDistance_InSteps * 2L))
    decelerationDistance_InSteps = (distanceToTravel_InSteps / 2L);


  //
  // start the acceleration ramp at the beginning
  //
  ramp_NextStepPeriod_InUS = ramp_InitialStepPeriod_InUS;
  acceleration_InStepsPerUSPerUS = acceleration_InStepsPerSecondPerSecond / 1E12;
  startNewMove = true;
}

bool LukiStepper::calibration(long directionTowardsendStop, float calibrationSpeed, long maxDistanceToMoveInSteps, int endstop, bool zero)
{


  //
  // if the endstop1 is not already set, move toward it
  //
  setSpeedInStepsPerSecond(calibrationSpeed);
  setupRelativeMoveInSteps(maxDistanceToMoveInSteps * directionTowardsendStop);
  
  while(digitalRead(endstop)!=HIGH){
    processMovement();
  }
  delay(10);
  
  setupRelativeMoveInSteps(maxDistanceToMoveInSteps * directionTowardsendStop*-1);
  while(digitalRead(endstop)==HIGH){
    processMovement();
  }
  delay(10);

  if (zero){
    setCurrentPositionInSteps(0L);    
  }

  //
  // restore original velocity
  //
  setSpeedInStepsPerSecond(desiredSpeed_InStepsPerSecond);
  return(true);
}


bool LukiStepper::processMovement(void)
{ 
  unsigned long currentTime_InUS;
  unsigned long periodSinceLastStep_InUS;
  long distanceToTarget_InSteps;


  //
  // check if already at the target position
  //
  if (currentPosition_InSteps == targetPosition_InSteps)
    return(true);

  //
  // check if this is the first call to start this new move
  //
  if (startNewMove)
  {    
    ramp_LastStepTime_InUS = micros();
    startNewMove = false;
  }

    
  //
  // determine how much time has elapsed since the last step (Note 1: this method   
  // works even if the time has wrapped. Note 2: all variables must be unsigned)
  //
  currentTime_InUS = micros();
  periodSinceLastStep_InUS = currentTime_InUS - ramp_LastStepTime_InUS;

  //
  // if it is not time for the next step, return
  //
  if (periodSinceLastStep_InUS < (unsigned long) ramp_NextStepPeriod_InUS)
    return(false);

  //
  // determine the distance from the current position to the target
  //
  distanceToTarget_InSteps = targetPosition_InSteps - currentPosition_InSteps;
  if (distanceToTarget_InSteps < 0) 
    distanceToTarget_InSteps = -distanceToTarget_InSteps;

  //
  // test if it is time to start decelerating, if so change from accelerating to 
  // decelerating
  //
  if (distanceToTarget_InSteps == decelerationDistance_InSteps)
    acceleration_InStepsPerUSPerUS = -acceleration_InStepsPerUSPerUS;
  
  //
  // execute the step on the rising edge
  //
  digitalWrite(stepPin, HIGH);
  
  //
  // delay set to almost nothing because there is so much code between rising and 
  // falling edges
  delayMicroseconds(2);        
  
  //
  // update the current position and speed
  //
  currentPosition_InSteps += direction_Scaler;
  currentStepPeriod_InUS = ramp_NextStepPeriod_InUS;


  //
  // compute the period for the next step
  // StepPeriodInUS = LastStepPeriodInUS * 
  //   (1 - AccelerationInStepsPerUSPerUS * LastStepPeriodInUS^2)
  //
  ramp_NextStepPeriod_InUS = ramp_NextStepPeriod_InUS * 
    (1.0 - acceleration_InStepsPerUSPerUS * ramp_NextStepPeriod_InUS * 
    ramp_NextStepPeriod_InUS);


  //
  // return the step line high
  //
  digitalWrite(stepPin, LOW);
 
 
  //
  // clip the speed so that it does not accelerate beyond the desired velocity
  //
  if (ramp_NextStepPeriod_InUS < desiredStepPeriod_InUS)
    ramp_NextStepPeriod_InUS = desiredStepPeriod_InUS;


  //
  // update the acceleration ramp
  //
  ramp_LastStepTime_InUS = currentTime_InUS;
 
 
  //
  // check if move has reached its final target position, return true if all done
  //
  if (currentPosition_InSteps == targetPosition_InSteps)
  {
    currentStepPeriod_InUS = 0.0;
    return(true);
  }
    
  return(false);
}


bool LukiStepper::motionComplete()
{
  if (currentPosition_InSteps == targetPosition_InSteps)
    return(true);
  else
    return(false);
}