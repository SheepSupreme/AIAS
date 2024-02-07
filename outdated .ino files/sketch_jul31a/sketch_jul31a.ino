#include <SpeedyStepper.h>
SpeedyStepper speedy;

const int LED_PIN = 13;
const int MOTOR_STEP_PIN = 3;
const int MOTOR_DIRECTION_PIN = 2;
const int SW = 6;
const int nEnable = 9;

void setup() {
  speedy.connectToPins(MOTOR_STEP_PIN, MOTOR_DIRECTION_PIN);
  //OUTPUT_PULLUP kann hier nicht verwendet werden da dies nur bei INPUT möglich ist.
  pinMode(nEnable, OUTPUT);
  digitalWrite(nEnable, HIGH);

  // Setup Serial Monitor
  Serial.begin(9600);

  //speedy speed

  speed_test(16000, 250000);
}

//loop
void loop() {}


// functions
void homing_test() {
  data();
  digitalWrite(nEnable, LOW);
  speedy.moveToHomeInSteps(-1, 400, 100000, SW);
  digitalWrite(nEnable, HIGH);
  data();
}

void data() {
  Serial.print("Position:");
  Serial.println(speedy.getCurrentPositionInRevolutions());
  Serial.print("nEnable: ");
  Serial.println(nEnable);
}

void speed_test(float speed, float accel) {
  unsigned long startTime = millis();
  speedy.setSpeedInStepsPerSecond(speed);
  speedy.setAccelerationInStepsPerSecondPerSecond(accel);
  digitalWrite(nEnable, LOW);
  speedy.moveRelativeInSteps(4000);
  digitalWrite(nEnable, HIGH);

  unsigned long endTime = millis();                   // Record the ending time
  unsigned long executionTime = endTime - startTime;  // Calculate the execution time

  Serial.print("Execution Time  ");
  Serial.print(speed);
  Serial.print("(ms): ");
  Serial.println(executionTime);
  delay(500);
  return 0;
}
