import pyrebase
import time
import cv2
from pyzbar.pyzbar import decode
import serial
from datetime import datetime
import math
cam = cv2.VideoCapture(0)
cam.set(5,640)
cam.set(6,400)

arduino_port = 'COM6'  # Replace with your Arduino port
baud_rate = 9600
ser = serial.Serial(arduino_port, baud_rate, timeout=1)

config = {
  'apiKey': "AIzaSyDR719PMnmn0S-elO9DQOxhyhp0oaeaK4U",
  'authDomain': "carparking-ec58a.firebaseapp.com",
    'databaseURL':'https://carparking-ec58a-default-rtdb.firebaseio.com',
  'projectId': "carparking-ec58a",
  'storageBucket': "carparking-ec58a.appspot.com",
  'messagingSenderId': "621177940695",
  'appId': "1:621177940695:web:427b3f29a9c58b164b1e92",
  'measurementId': "G-D9VEL93T2C"
}
firebase = pyrebase.initialize_app(config)
db = firebase.database()
ser.encoding = 'utf-8'
def time_to_second(time_str):
    hh,mm,ss=map(int,time_str.split(":"))
    return hh*3600 + mm*60 + ss


# Function to set the angle of the servo motor connected to pin 9
def set_servo_angle(pin, angle):
    command = f'{pin}:{angle}\n'
    ser.write(command.encode())

camera=True
#set_servo_position(0)
while camera==True:
    success , frame =cam.read()

    for i in decode(frame):
        print(i.type)
        current_time=""
        current_time_out=""
        a=i.data.decode('utf-8')
        b=a.split()
        print(b)
        if b[3]=='0':
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            c = ""
            b[3]=str(1)
            for i in b:
                c=c+i+" "
            print(c)
            o = open("QR.txt", 'w')
            o.write(c)
            o.close()
            time.sleep(1)
            if b[0]=="A1":
                set_servo_angle(10, 90)
                time.sleep(3)
                set_servo_angle(10,-90)
            elif b[0]=="A2":
                set_servo_angle(13, 90)
                time.sleep(3)
                set_servo_angle(13,-90)
            elif b[0]=="A3":
                set_servo_angle(11, 90)
                time.sleep(3)
                set_servo_angle(11,-90)




        elif b[3]=='1':
            #current_time_out= now.strftime("%H:%M:%S")
            db.child("parking").child(b[1]).child("available").update({b[0]:1})
            if b[0]=="A1":
                set_servo_angle(10, 90)
                time.sleep(3)
                set_servo_angle(10,-90)
            elif b[0]=="A2":
                set_servo_angle(13, 90)
                time.sleep(3)
                set_servo_angle(13,-90)
            elif b[0]=="A3":
                set_servo_angle(11, 90)
                time.sleep(3)
                set_servo_angle(11,-90)
            o=open("QR.txt",'r')
            o1=o.read()
            o12=o1.split()
            o12[3]="3"
            str1=""
            for i in o12:
                str1=str1+str(i)+" "
            o.close()
            o2=open("QR.txt",'w')
            o2.write(str1)
            o2.close()


        #cv2.imshow("QRscanner",frame)
        #cv2.waitkey(3)
ser.close()