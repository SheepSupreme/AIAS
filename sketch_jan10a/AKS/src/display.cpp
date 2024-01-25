
#include "display.h"

display::display() : display(128, 64, &Wire, -1) {

}

void display::begin()
{
  display.begin(SSD1306_SWITCHCAPVCC, 0x3C);
  display.display();
  delay(2000);
  display.clearDisplay();
}


void display::update_display(String input, uint8_t x, uint8_t y, uint8_t size)
{
  display.clearDisplay();
  display.setCursor(x,y);
  display.setFont();
  display.setTextSize(size);
  display.setTextColor(SSD1306_WHITE);
  display.print(input);
  display.display();
}

void display::status_errorRange()
{
  display.update_display("move not\n possible",15 ,10, 2);
  delay(2000);
  display.update_display("range\n violation",35 ,10, 2);
}

void display::status_position(int position)
{
  
}

void display::status_calibration()
{

}
