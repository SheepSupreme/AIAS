
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
  calibrationSpeed = 2000;
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


bool LukiStepper::processMovement(void)
{
  unsigned long currentTime;
  unsigned long timeSinceLastStep;
  unsigned long distanceToTarget;

  if (currentPosition_InSteps == targetPosition_InSteps){
    return(true);
  }

  if (startNewMove)
  {    
    ramp_LastStepTime_InUS = micros();
    startNewMove = false;
  }

}


bool SpeedyStepper::calibration(long directionTowardsendStop, 
  float calibrationSpeed, long maxDistanceToMoveInSteps, int endStop, bool zero)
{

  bool limitSwitchFlag;
  
  
  //
  // setup the home switch input pin
  //
  pinMode(endStop, INPUT_PULLUP);            //move this out of the function
 
 
  //
  // if the endStop is not already set, move toward it
  //
  if (digitalRead(endStop) == HIGH)
  {
    //
    // move toward the home switch
    //
    setSpeedInStepsPerSecond(calibrationSpeed);
    setupRelativeMoveInSteps(maxDistanceToMoveInSteps * directionTowardsendStop);
    limitSwitchFlag = false;
    while(!processMovement())
    {
      if (digitalRead(endStop) == LOW)
      {
        limitSwitchFlag = true;
        break;
      }
    }
    
    //
    // check if switch never detected
    //
    if (limitSwitchFlag == false)
      return(false);
  }
  delay(25);


  //
  // the switch has been detected, now move away from the switch
  //
  setupRelativeMoveInSteps(maxDistanceToMoveInSteps * directionTowardsendStop * -1);
  limitSwitchFlag = false;
  while(!processMovement())
  {
    if (digitalRead(endStop) == HIGH)
    {
      limitSwitchFlag = true;
      break;
    }
  }
  delay(25);
  
  //
  // check if switch never detected
  //
  if (limitSwitchFlag == false)
    return(false);


  //
  // have now moved off the switch, move toward it again but slower
  //
  setSpeedInStepsPerSecond(speedInStepsPerSecond/8);
  setupRelativeMoveInSteps(maxDistanceToMoveInSteps * directionTowardsendStop);
  limitSwitchFlag = false;
  while(!processMovement())
  {
    if (digitalRead(endStop) == LOW)
    {
      limitSwitchFlag = true;
      break;
    }
  }
  delay(25);
  
  //
  // check if switch never detected
  //
  if (limitSwitchFlag == false)
    return(false);


  //
  // successfully homed, set the current position to 0
  //
  if (zero){
  setCurrentPositionInSteps(0L);    
  }

  //
  // restore original velocity
  //
  setSpeedInStepsPerSecond(desiredSpeed_InStepsPerSecond);
  return(true);
}


