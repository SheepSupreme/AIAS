import serial

serial_port = 'COM3'
baud_rate = 9600

ser = serial.Serial(serial_port, baud_rate, timeout=2)

while True:
  text = ser.readline().decode().strip()
  print(text)