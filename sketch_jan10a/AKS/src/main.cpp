/**
 * Blink
 *
 * Turns on an LED on for one second,
 * then off for one second, repeatedly.
 */
#include "stepper.h"

// Set LED_BUILTIN if it is not defined by Arduino framework
// #define LED_BUILTIN 13

Stepper NEMA17(2,3,4,5,6,7);

void setup()
{

  pinMode(LED_BUILTIN, OUTPUT);

  Serial.begin(9600);
  NEMA17.change_microstep_resolution(2);
  NEMA17.change_profile(12000,30000);
  
  NEMA17.calibration(50);
  NEMA17.move_relative(800);
  NEMA17.move_relative(-800);

  Serial.print(NEMA17.endstop_position);
  Serial.print(NEMA17._current_position);

  Serial.print("Runtime:");
  Serial.print(millis());
}

void loop(){

}