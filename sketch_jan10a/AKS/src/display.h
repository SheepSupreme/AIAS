#ifndef display_h
#define display_h

#include <Adafruit_SSD1306.h>
#include <Adafruit_GFX.h>
#include <Wire.h>
#include <SPI.h>
#include <Fonts/Picopixel.h>
#include <string>

#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 64
#define OLED_RESET     -1 
#define SCREEN_ADDRESS 0x3C

class display{
  public:
    display();
    void update_display(String input, uint8_t x, uint8_t y, uint8_t size);
    void status_calibration();
    void status_position(int position);
    void begin();
  private:
    Adafruit_SSD1306 display;
};

#endif