

#include "LukiStepper.h"


//
// pin assignments
//
const int LED_PIN = 13;
const int MOTOR_STEP_PIN = 3;
const int MOTOR_DIRECTION_PIN = 2;
const int nEnable = 4;
const int M0 = 5;
const int M1 = 6;
const int M2 = 7;
const int S1 = 8;
const int S2 = 9;


//
// create the stepper motor object
//
LukiStepper stepper;

void setup() 
{
  //
  // setup the LED pin and enable print statements
  //

  pinMode(LED_PIN, OUTPUT); 
  pinMode(M0, OUTPUT); 
  pinMode(M1, OUTPUT);
  pinMode(M2, OUTPUT);
  digitalWrite(M0,LOW);
  digitalWrite(M1,HIGH);
  digitalWrite(M2,LOW);

  Serial.begin(9600);

  digitalWrite(nEnable,HIGH);

  //
  // connect and configure the stepper motor to its IO pins
  //

  stepper.connectToPins(MOTOR_STEP_PIN, MOTOR_DIRECTION_PIN);
  stepper.setSpeedInStepsPerSecond(10000);
  stepper.setAccelerationInStepsPerSecondPerSecond(250000);
  digitalWrite(nEnable, HIGH);
  stepper.calibration(1, 1000, 200000, S1, false);
  stepper.calibration(-1, 1000, 200000, S1, true);
  digitalWrite(nEnable, HIGH);
  Serial.println(digitalRead(nEnable));

}



void loop() 
{

}


