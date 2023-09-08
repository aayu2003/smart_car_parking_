import serial
import time

# Connect to Arduino via serial port
ser = serial.Serial('COM6', 9600)  # Replace 'COM3' with your Arduino's serial port

# Wait for Arduino to initialize
time.sleep(2)

# Function to set servo position
def set_servo_position(angle):
    # Send the angle to Arduino

    ser.write(bytes(str(angle), 'utf-8'))
    print(f"Set servo position: {angle}")
    time.sleep(1)

# Example usage

servoPin1 = 10
servoPin2 = 11
servoPin3 = 12

for i in range(0,10):
    set_servo_position(-90)  # Set the servo to 90 degrees
    time.sleep(1)
    set_servo_position( 90)
    time.sleep(1)
    set_servo_position( -90)
    time.sleep(1)

# Close the serial connection
ser.close()
