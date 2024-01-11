#include "library.h"

stepper stepper;

void setup() {
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  char text = stepper.text_return();
  Serial.println(text);
}
