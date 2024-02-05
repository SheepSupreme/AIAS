
#include "display.h"
#include "stepper.h"

Stepper NEMA17(2,3,4,5,6,7,8,9);
display SSD1306;

void setup()
{

  SSD1306.begin();
  pinMode(LED_BUILTIN, OUTPUT);

  Serial.begin(9600);
  NEMA17.change_profile(7000,30000);
  NEMA17.change_microstep_resolution(1);
 
  NEMA17.calibration(50);
  // NEMA17.move_relative(200);
  // Serial.println(NEMA17._current_position);

  //Different Stepper-Modes
  // SSD1306.status_calibration();
  // delay(1000);
  // NEMA17.change_microstep_resolution(2);
  // NEMA17.move_relative(-800);
  // delay(1000);
  // NEMA17.change_microstep_resolution(1);
  // NEMA17.move_relative(-400);
  // delay(1000);
  // NEMA17.change_microstep_resolution(2);
  // NEMA17.move_absolute(NEMA17.endstop_position);

  // Calibrate + 4position movement
  delay(1000);
  NEMA17.move_absolute((1.0/3.0)*NEMA17.endstop_position);
  NEMA17.move_absolute((2.0/3.0)*NEMA17.endstop_position);
  NEMA17.move_absolute(0);

  Serial.print("endstop_position");
  Serial.println(NEMA17.endstop_position);
  Serial.print("current_position");
  Serial.println(NEMA17._current_position);

  Serial.print("Runtime:");
  Serial.print(millis());
}

void loop(){
  
}