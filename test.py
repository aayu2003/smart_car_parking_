import pyrebase
import time
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
i=1
while i==1:
    o=open("IOT_Lab.txt","r")
    f=o.readlines()
    f1=f[-1]
    f2=f1.split("|")
    db.child("parking").child("101").child("available").update({'A1':int(f2[0])})
    db.child("parking").child("101").child("available").update({'A2': int(f2[1])})
    db.child("parking").child("101").child("available").update({'A3': int(f2[2])})
    db.child("parking").child("101").child("available").update({'A4': int(f2[3])})
    time.sleep(0.5)
    o.close()
