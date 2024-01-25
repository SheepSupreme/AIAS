
#include "display.h"

display::display() : OLED(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET) {

}

void display::begin()
{
  OLED.begin(SSD1306_SWITCHCAPVCC, SCREEN_ADDRESS);
  OLED.display();
  OLED.clearDisplay();
}


void display::update_display(String input, uint8_t x, uint8_t y, uint8_t size)
{
  OLED.clearDisplay();
  OLED.setCursor(x,y);
  OLED.setFont();
  OLED.setTextSize(size);
  OLED.setTextColor(SSD1306_WHITE);
  OLED.print(input);
  OLED.display();
}

void display::status_errorRange()
{
  update_display("move not\n possible",15 ,10, 2);
  delay(2000);
  update_display("range\n violation",35 ,10, 2);
}

void display::status_position(int position)
{
  update_display(String(position),40 ,25, 2);
}

void display::status_calibration()
{
    update_display("Aligning",20 ,10, 2);
}
