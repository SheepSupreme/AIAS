
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
  

  NEMA17.calibration();
  NEMA17.move_absolute(500);
  delay(1000);
  NEMA17.move_absolute(300);
  delay(1000);
  NEMA17.move_relative(-500);

  Serial.print("endstop_position");
  Serial.println(NEMA17.endstop_position);
  Serial.print("current_position");
  Serial.println(NEMA17._current_position);
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