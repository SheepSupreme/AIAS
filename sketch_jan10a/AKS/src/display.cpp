#include "display.h"


display::display()
{
    Adafruit_SSD1306::Adafruit_SSD1306(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);
}

display::update_display(int input)
{
    Adafruit_SSD1306::clearDisplay();
    Adafruit_SSD1306::setCursor(10,10);
    // Adafruit_SSD1306::setFont(NULL);         TODO Font
    Adafruit_SSD1306::setTextSize(3);
    Adafruit_SSD1306::write(input);
}