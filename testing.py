import serial
import time

# Establish serial communication with Arduino
arduino_port = 'COM6'  # Replace with your Arduino port
baud_rate = 9600
ser = serial.Serial(arduino_port, baud_rate, timeout=1)

# Set the encoding to UTF-8
ser.encoding = 'utf-8'

# Function to set the angle of the servo motor connected to pin 9
def set_servo_angle(pin, angle):
    command = f'{pin}:{angle}\n'
    ser.write(command.encode())

# Test the servo motors by rotating them from 0 to 180 degrees
for angle in range(0, 181, 90):
    set_servo_angle(12, angle)
    set_servo_angle(10, angle)
    set_servo_angle(11, angle)
    time.sleep(1)  # Wait for 1 second

# Close the serial connection
ser.close()
