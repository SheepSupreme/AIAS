
#include "display.h"
#include "stepper.h"

Stepper Issue(1,0,6,22,22,22,14,15);
Stepper NEMA17(3,2,7,22,22,22,14,15);
display SSD1306;

void setup()
{
  pinMode(LED_BUILTIN, OUTPUT);
  pinMode(14,INPUT);
  

  Serial.begin(9600);
  SSD1306.begin();
  Serial.setTimeout(10);
  NEMA17.change_microstep_resolution(1);
  NEMA17.change_profile(5000,30000);

  Issue.change_microstep_resolution(1);
  Issue.change_profile(1000,1000);



  // Serial.println("start");
  // SSD1306.update_display("Issue",15 ,10, 2);
  // Issue.move_relative(2000);
  // Serial.println("end");

 
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


void loop(){
  Serial.println(digitalRead(14));
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
        SSD1306.update_display("Issue",15 ,10, 2);
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