import serial
import time

# Define serial port settings
serial_port = 'COM3'  # Change this to your serial port
baud_rate = 9600  # Change this to match your device's baud rate

# Initialize serial connection
ser = serial.Serial(serial_port, baud_rate)

try:
    while True:
        # Transmit data
        data = "blink\n"  # Data to be transmitted
        ser.write(data.encode())  # Convert string to bytes and transmit
        print("Data transmitted:", data.strip())
        time.sleep(5)  # Delay between transmissions

except KeyboardInterrupt:
    print("Exiting program")
    ser.close()  # Close serial connection when program terminates

