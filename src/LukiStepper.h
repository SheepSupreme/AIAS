#ifndef LukiStepper_h // Schützt vor mehrfachem includen
#define LukiStepper_h

#include <Arduino.h>
#include <stdlib.h>


// LukiStepper class

class LukiStepper
{
private:
    /* data */
public:
    LukiStepper(); // Constructor declaration
    ~LukiStepper(); // Destructor declaration
    void connectToPins(byte stepPinNumber, byte directionPinNumber);

};





#endif