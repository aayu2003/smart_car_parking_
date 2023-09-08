import pyrebase
import qrcode
import random
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.scrollview import ScrollView
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.core.image import Image
from kivy.graphics import Color, Rectangle
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager , Screen
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
Window.size=(500,700)
class Booking(Screen):
    def on_enter(self):
        call1=db.child('parking').get()
        l=[]
        try:
            for i in call1.each():
                c=i.key()
                l.append(c)
                call12=db.child('parking').child(c).get()
                #layout = GridLayout(cols=2, rows=len(l))
                for j in call12.each():
                    if j.key()=="name":
                        c1=j.val()
                        button=Button(text=c1,size_hint_y=None,height=100,background_color =(215/255, 191/255, 224/255,0.5),font_size=22,bold=True)
                        button.bind(on_release=self.button_pressed)
                        button.bind(on_release=self.button_pressed_once)
                        self.ids.gd.add_widget(button)
        except:
            print("none")
    def search(self):
        try:
            if len(self.ids.booksearch.text)>0:
                grid_layout=self.ids.gd
                for child in grid_layout.children[:]:
                    if isinstance(child, Button):
                        grid_layout.remove_widget(child)
                a=self.ids.booksearch.text
                a.lower()
                c101=db.child("parking").child("101").child("area").get()
                c102=db.child("parking").child("102").child("area").get()
                c103=db.child("parking").child("103").child("area").get()
                c104=db.child("parking").child("104").child("area").get()
                print(c101.val())
                if c101.val()==a:
                    t1=db.child("parking").child("101").child("name").get()
                    button=Button(text=t1.val(),size_hint_y=None,height=100,background_color =(215/255, 191/255, 224/255,0.5),font_size=22,bold=True)
                    button.bind(on_release=self.button_pressed)
                    button.bind(on_release=self.button_pressed_once)
                    self.ids.gd.add_widget(button)
                if c102.val() == a:
                    t2 = db.child("parking").child("102").child("name").get()
                    button = Button(text=t2.val(), size_hint_y=None, height=100,background_color=(215 / 255, 191 / 255, 224 / 255, 0.5), font_size=22, bold=True)
                    button.bind(on_release=self.button_pressed)
                    button.bind(on_release=self.button_pressed_once)
                    self.ids.gd.add_widget(button)
                if c103.val() == a:
                    t3 = db.child("parking").child("103").child("name").get()
                    button = Button(text=t3.val(), size_hint_y=None, height=100,background_color=(215 / 255, 191 / 255, 224 / 255, 0.5), font_size=22, bold=True)
                    button.bind(on_release=self.button_pressed)
                    button.bind(on_release=self.button_pressed_once)
                    self.ids.gd.add_widget(button)

                if c104.val() == a:
                    t4 = db.child("parking").child("104").child("name").get()
                    button = Button(text=t4.val(), size_hint_y=None, height=100,background_color=(215 / 255, 191 / 255, 224 / 255, 0.5), font_size=22, bold=True)
                    button.bind(on_release=self.button_pressed)
                    button.bind(on_release=self.button_pressed_once)
                    self.ids.gd.add_widget(button)
        except:
            print("none")

    def button_pressed(self,button):
        o=open("id.txt",'w')
        o.write(button.text)
        o.close()
    def button_pressed_once(self,instance):
        app = App.get_running_app()
        app.root.current = "slot"



    pass
class Slot(Screen):
    def on_enter(self):
        parkid=""
        ope=open("id.txt",'r')
        a=ope.readlines()
        a1=a[0]
        call=db.child('parking').get()
        for i in call.each():
            key=i.key()
            call1=db.child('parking').child(key).get()
            for j in call1.each():
                if j.val()==a1:
                    parkid=parkid+i.key()
        call12=db.child('parking').child(parkid).child('available').get()
        ope.close()
        ope=open("id.txt",'w')
        ope.write(parkid)
        ope.close()
        l=[]
        lav=[]
        for k in call12.each():
            l.append(k.key()+" "+str(k.val()))
        for k1 in l:
            av=k1.split()
            if int(av[1])==1:
                lav.append(av[0])
        try:
            self.ids.availabletext.text=str(len(lav))
            for buto in lav:
                button1=Button(text=buto,size_hint_y=None,height=100,background_color =(215/255, 191/255, 224/255,0.5),font_size=22,bold=True)
                button1.bind(on_release=self.GenerateQR)
                button1.bind(on_release=self.GenerateQR1)
                self.ids.availablelist.add_widget(button1)
        except:
            self.ids.availabletext.text="0"


    def GenerateQR1(self,button1):
        op=open("id.txt",'r')
        op1=open("user.txt",'r')
        n=button1.text+" "+str(op.read())+" "+str(op1.read())+" "+str(0)
        op.close()
        op1.close()
        op12=open("QR.txt",'w')
        op12.write(n)
        op12.close()
        op123=open("id.txt",'r')
        db.child("parking").child(op123.read()).child("available").update({button1.text:0})
        img = qrcode.make(n)
        img.save("qr.png")

    def GenerateQR(self,instance):
        app = App.get_running_app()
        time.sleep(2)
        app.root.current = "qrgeneration"
        pass
class Login(Screen):
    def presslog(self):
        a=self.ids.lnuminp.text +" "+self.ids.lpassinp.text
        print(a)
        op=open("user.txt",'w')
        op.write(self.ids.lnuminp.text)
        op.close()
        self.ids.lnuminp.text=""
        self.ids.lpassinp.text=""
        db.child('user').push(a)

    pass
class QRgenerate(Screen):
    def on_enter(self):
        self.ids.img.source="qr.png"
        self.ids.pass_label.text="PASS TO ENTER"
    def generate(self):
        pass
    def generate1(self):
        o=open("QR.txt",'r')
        o1=o.read()
        o2=o1.split()
        if o2[3]=="1":
            self.ids.pass_label.text="PASS TO EXIT"
            img = qrcode.make(o2[0]+" "+o2[1]+" "+o2[2]+" "+o2[3])
            img.save("qr1.png")
            time.sleep(2)
            self.ids.img.source = "qr1.png"
            time.sleep(1)
        elif o2[3]=="3":
            l=['1','1.36','0.33']
            e=open("price.txt",'r')
            r=random.randint(0,2)
            self.ids.pass_label.text=l[r]
            self.ids.img.source="background.jpg"




    pass
class WindowManager(ScreenManager):
    pass
kv=Builder.load_file('smartcar.kv')

class SmartCarApp(App):
  def build(self):
    #Builder.load_file('smartcar.kv')
    Window.clearcolor=1,1,1,1
    return kv

if __name__=='__main__':
    SmartCarApp().run()
