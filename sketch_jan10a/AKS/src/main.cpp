
#include "stepper.h"
#include "display.h"

Stepper NEMA17(2,3,4,5,6,7,20,21);

void setup()
{

  pinMode(LED_BUILTIN, OUTPUT);

  Serial.begin(9600);
  NEMA17.change_microstep_resolution(1);
  NEMA17.change_profile(12000,30000);

  //Different Stepper-Modes
  // NEMA17.calibration(50);
  // delay(1000);
  // NEMA17.change_microstep_resolution(2);
  // NEMA17.move_relative(-800);
  // delay(1000);
  // NEMA17.change_microstep_resolution(1);
  // NEMA17.move_relative(-400);
  // delay(1000);
  // NEMA17.change_microstep_resolution(2);
  // NEMA17.move_absolute(NEMA17.endstop_position);

  //Calibrate + 4position movement
  // delay(1000);
  // NEMA17.move_absolute((2.0/3.0)*NEMA17.endstop_position);
  // delay(1000);
  // NEMA17.move_absolute((1.0/3.0)*NEMA17.endstop_position);
  // delay(1000);
  // NEMA17.move_absolute(0);

  Serial.print("endstop_position");
  Serial.println(NEMA17.endstop_position);
  Serial.print("current_position");
  Serial.println(NEMA17._current_position);

  Serial.print("Runtime:");
  Serial.print(millis());
}

void loop(){
  
}