import serial

# serial_port = 'COM3'
# baud_rate = 9600

<<<<<<< HEAD
# ser = serial.Serial(serial_port, baud_rate)

# message = 'test'

# message_bytes = message.encode('utf-8')

# ser.write(message_bytes)

# ser.close()

=======
ser = serial.Serial(serial_port, baud_rate, timeout=2)

while True:
  text = ser.readline().decode().strip()
  print(text)
>>>>>>> origin/main
