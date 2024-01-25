#ifndef display_h
#define display_h

#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>
#include <Wire.h>

class display{
    public:
        display();
        update_display(int input);
    private:
        uint8_t SCREEN_WIDTH = 128;
        uint8_t SCREEN_HEIGHT = 64;    
        int8_t OLED_RESET = -1;
        uint8_t SCREEN_ADDRESS = 0x3C;
}

#endif 