
#include "display.h"
#include "stepper.h"

Stepper NEMA17(2,3,4,5,6,7,8,9);
display SSD1306;

void setup()
{
  pinMode(LED_BUILTIN, OUTPUT);

  Serial.begin(9600);
  Serial.setTimeout(10);
  pinMode(LED_BUILTIN,OUTPUT);
  NEMA17.change_microstep_resolution(1);
  NEMA17.change_profile(5000,30000);

  SSD1306.begin();
 
  // NEMA17.calibration(50);
  // NEMA17.move_absolute(0);

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

  //Calibrate + 4position movement
  // delay(1000);
  // NEMA17.move_absolute((2.0/3.0)*NEMA17.endstop_position);
  // delay(1000);
  // NEMA17.move_absolute((1.0/3.0)*NEMA17.endstop_position);
  // delay(1000);
  // NEMA17.move_absolute(0);

}

  Stepper Issue(10,11,12,13,14,15);

  Issue.move_relative(2000);
  Issue.move_relative(-2000);


void loop(){
  if(Serial.available() == 0){  //Informationen im Buffer erkannt
    String message = Serial.readString(); //Nachricht lesen
    message.trim(); //Verarbeitung der Nachricht
    if(message != 0){
      int separatorIndex = message.indexOf(' '); //Aufteilung
      String cmd = message.substring(0, separatorIndex);
      int value = message.substring(separatorIndex + 1).toInt();
      if(cmd == "blink"){
        digitalWrite(LED_BUILTIN,HIGH);
        delay(1000);
        digitalWrite(LED_BUILTIN,LOW);
        Serial.println("cmd_end");
      }
      if(cmd == "calibration"){
        NEMA17.calibration(value); 
        Serial.println("cmd_end");
      }
      if(cmd == "pos_1"){
        NEMA17.move_absolute(0);
        Serial.println("cmd_end");
      }
      if(cmd == "pos_2"){
        NEMA17.move_absolute((1.0/3.0)*NEMA17.endstop_position);
        Serial.println("cmd_end");
      }
      if(cmd == "pos_3"){
        NEMA17.move_absolute((2.0/3.0)*NEMA17.endstop_position);
        Serial.println("cmd_end");
      }
      if(cmd == "pos_4"){
        NEMA17.move_absolute(NEMA17.endstop_position);
        Serial.println("cmd_end");
      }
      if(cmd == "Issue"){
        NEMA17.move_absolute(value*(1.0/3.0)*NEMA17.endstop_position);
        Issue.move_relative(2000);
        Issue.move_relative(-2000);
        Serial.println("cmd_end");
      }
      else{
        Serial.println(cmd);
      }
    }
  }
}  