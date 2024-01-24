/**
 * Blink
 *
 * Turns on an LED on for one second,
 * then off for one second, repeatedly.
 */
#include "stepper.h"

// Set LED_BUILTIN if it is not defined by Arduino framework
// #define LED_BUILTIN 13

Stepper NEMA17;

void setup()
{
  // initialize LED digital pin as an output.
  pinMode(LED_BUILTIN, OUTPUT);

  Serial.begin(9600);
  NEMA17.change_microstep_resolution(2);
  NEMA17.change_profile(10000,30000);
  
  NEMA17.move_relative(600);
  NEMA17.calibration(50);

  Serial.print("Runtime:");
  Serial.print(millis());
}

void loop(){

}