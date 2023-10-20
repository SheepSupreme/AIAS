
// Stepper
#include "LukiStepper.h"

// SSD1306
#include <SPI.h>
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

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
const int CLK = 10;
const int DATA = 11;
const int SW = 12;

static int8_t c,val;
static uint8_t prevNextCode = 0;
static uint16_t store=0;

int pos_max;
int rotary_resolution;
int counter;


// OLED DISPLAY Constants
#define SCREEN_WIDTH 128 // OLED display width, in pixels
#define SCREEN_HEIGHT 64 // OLED display height, in pixels

#define OLED_RESET     -1 // Reset pin # (or -1 if sharing Arduino reset pin)
#define SCREEN_ADDRESS 0x3C ///< See datasheet for Address; 0x3D for 128x64, 0x3C for 128x32

Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);


//
// create the stepper motor object
//
LukiStepper stepper;

void setup() 
{

  // setup the LED pin and enable print statements
  pinMode(LED_PIN, OUTPUT); 

  // 1/4 Viertelstep-Betrieb
  pinMode(M0, OUTPUT); 
  pinMode(M1, OUTPUT);
  pinMode(M2, OUTPUT);
  digitalWrite(M0,LOW);
  digitalWrite(M1,LOW);
  digitalWrite(M2,LOW);

  // Rotary Encoder Pin dekleration
  pinMode(CLK, INPUT_PULLUP);
  pinMode(DATA, INPUT_PULLUP);
  pinMode(SW, INPUT_PULLUP);

  Serial.begin(9600);

  // Driver wird disabled
  digitalWrite(nEnable,HIGH);

  // connect and configure the stepper motor to its IO pins
  stepper.connectToPins(MOTOR_STEP_PIN, MOTOR_DIRECTION_PIN);

  if(!display.begin(SSD1306_SWITCHCAPVCC, SCREEN_ADDRESS)) {
    Serial.println(F("SSD1306 allocation failed"));
    for(;;); // Don't proceed, loop forever
  }
  display.clearDisplay();
  display.setTextColor(SSD1306_WHITE);
  display.setTextSize(2);
  display.setCursor(0, 10);
  
  

  // Standart Bewegungsprofil
  stepper.setSpeedInStepsPerSecond(16000);
  stepper.setAccelerationInStepsPerSecondPerSecond(250000);


  //Kalibrierung mit Microstepping
  digitalWrite(nEnable, LOW);
  digitalWrite(M0,HIGH);
  digitalWrite(M1,HIGH);
  digitalWrite(M2,HIGH);
  display.print("Calibration");
  display.display();
  Serial.println("start calibration"); // Waypoint
  stepper.calibration(-1, 16000, 200000, S1, true);
  stepper.calibration(1, 16000, 200000, S2, false);
  digitalWrite(nEnable, HIGH);

  //Umstellung auf 1/4 Step-Betrieb
  digitalWrite(M0,LOW);
  digitalWrite(M1,HIGH);
  digitalWrite(M2,LOW);
  stepper.setCurrentPositionInSteps(stepper.getCurrentPositionInSteps()/8);
  pos_max = stepper.getCurrentPositionInSteps();
  counter = pos_max;
  rotary_resolution = pos_max/20;
  Serial.print("end calibration"); // Waypoint
  Serial.println("start manual"); // Waypoint

  stepper.setSpeedInStepsPerSecond(16000);
  stepper.setAccelerationInStepsPerSecondPerSecond(250000);

  control();
}



void loop() {
  if(digitalRead(SW)==0){
    while(digitalRead(SW)==0){}
    Serial.println("pressed");
    return 0;
  }

  if(val = read_rotary() ) {
    Serial.println(val);
  }
}


bool control(){
  Serial.println("control start");
  manual_image();
  while(true){
    if(digitalRead(SW)==0){
      while(digitalRead(SW)==0){}
      digitalWrite(nEnable,LOW);
      Serial.println(counter - stepper.getCurrentPositionInSteps());
      stepper.moveRelativeInSteps(counter - stepper.getCurrentPositionInSteps(),S1,S2);
      digitalWrite(nEnable,HIGH);
      manual_image();
    }

    if(val = read_rotary() ) {
      Serial.println(counter);
      if (val > 0 && counter < pos_max){
        counter += rotary_resolution;
      }
      else if (val < 0 && counter > 0+rotary_resolution){
        counter += -rotary_resolution;
      }
      manual_image();
    }
  }
  Serial.println("control end");
}


void manual_image(){
  display.clearDisplay();
  display.drawRect(0, 0, display.width(), 20, 1);
  display.fillRect(0, 0,stepper.getCurrentPositionInSteps()/float (pos_max)*127, 20, 1);
  display.drawLine(float (counter)/float (pos_max)*127, 0,float (counter)/float (pos_max)*127, 25, 1);
  display.setTextColor(SSD1306_WHITE);
  display.setCursor(10,40);
  display.println(stepper.getCurrentPositionInSteps());
  display.display();
}


int8_t read_rotary() {
  static int8_t rot_enc_table[] = {0,1,1,0,1,0,0,1,1,0,0,1,0,1,1,0};
  
  prevNextCode <<= 2;
  if (digitalRead(DATA)) prevNextCode |= 0x02;
  if (digitalRead(CLK)) prevNextCode |= 0x01;
  prevNextCode &= 0x0f;

   // If valid then store as 16 bit data.
   if  (rot_enc_table[prevNextCode] ) {
      store <<= 4;
      store |= prevNextCode;
      //if (store==0xd42b) return 1;
      //if (store==0xe817) return -1;
      if ((store&0xff)==0x2b) return -1;
      if ((store&0xff)==0x17) return 1;
   }
   return 0;
}
