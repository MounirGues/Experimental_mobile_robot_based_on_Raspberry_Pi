import RPi.GPIO as GPIO
import pylirc, time


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(9, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)

GPIO.setup(2,GPIO.OUT)
GPIO.setup(3,GPIO.OUT)
GPIO.setup(4,GPIO.OUT)

P = GPIO.PWM(2,50)              
P.start(91)

p = GPIO.PWM(3,50)              
p.start(100)   
 

GPIO.output(18, GPIO.LOW)
GPIO.output(9, GPIO.LOW)
GPIO.output(11, GPIO.LOW)
GPIO.output(8, GPIO.LOW)
GPIO.output(7, GPIO.LOW)
GPIO.output(25, GPIO.LOW)

s = pylirc.init("myprogram")

while True :
   
   m = pylirc.nextcode()
   print m

   if (m == ['record']) :
      GPIO.output(25, GPIO.HIGH)

   if (m == ['cut']) :
      GPIO.output(25, GPIO.LOW)
   
   if (m == ['up']) :
      GPIO.output(9, GPIO.LOW)
      GPIO.output(11, GPIO.LOW)
      GPIO.output(8, GPIO.LOW)
      GPIO.output(7, GPIO.LOW)
      time.sleep(0.001)
      GPIO.output(9, GPIO.HIGH)
      GPIO.output(11, GPIO.LOW)
      GPIO.output(8, GPIO.HIGH)
      GPIO.output(7, GPIO.LOW)

   if (m == ['down']) :
      GPIO.output(9, GPIO.LOW)
      GPIO.output(11, GPIO.LOW)
      GPIO.output(8, GPIO.LOW)
      GPIO.output(7, GPIO.LOW)
      time.sleep(0.001)
      GPIO.output(9, GPIO.LOW)
      GPIO.output(11, GPIO.HIGH)
      GPIO.output(8, GPIO.LOW)
      GPIO.output(7, GPIO.HIGH)

   if (m == ['left']) :
      GPIO.output(9, GPIO.LOW)
      GPIO.output(11, GPIO.LOW)
      GPIO.output(8, GPIO.LOW)
      GPIO.output(7, GPIO.LOW)
      time.sleep(0.001)
      GPIO.output(9, GPIO.LOW)
      GPIO.output(11, GPIO.HIGH)
      GPIO.output(8, GPIO.HIGH)
      GPIO.output(7, GPIO.LOW)
      time.sleep(0.367)
      GPIO.output(11, GPIO.LOW)
      GPIO.output(8, GPIO.LOW)

   if (m == ['right']) :
      GPIO.output(9, GPIO.LOW)
      GPIO.output(11, GPIO.LOW)
      GPIO.output(8, GPIO.LOW)
      GPIO.output(7, GPIO.LOW)
      time.sleep(0.001)
      GPIO.output(9, GPIO.HIGH)
      GPIO.output(11, GPIO.LOW)
      GPIO.output(8, GPIO.LOW)
      GPIO.output(7, GPIO.HIGH)
      time.sleep(0.38)
      GPIO.output(9, GPIO.LOW)
      GPIO.output(7, GPIO.LOW)

   if (m == ['ok']) :
      GPIO.output(9, GPIO.LOW)
      GPIO.output(11, GPIO.LOW)
      GPIO.output(8, GPIO.LOW)
      GPIO.output(7, GPIO.LOW)
      

   if (m == ['l']) :
      GPIO.output(9, GPIO.LOW)
      GPIO.output(11, GPIO.LOW)
      GPIO.output(8, GPIO.LOW)
      GPIO.output(7, GPIO.LOW)
      time.sleep(0.001)
      GPIO.output(9, GPIO.LOW)
      GPIO.output(11, GPIO.HIGH)
      GPIO.output(8, GPIO.HIGH)
      GPIO.output(7, GPIO.LOW)

   if (m == ['r']) :
      GPIO.output(9, GPIO.LOW)
      GPIO.output(11, GPIO.LOW)
      GPIO.output(8, GPIO.LOW)
      GPIO.output(7, GPIO.LOW)
      time.sleep(0.001)
      GPIO.output(9, GPIO.HIGH)
      GPIO.output(11, GPIO.LOW)
      GPIO.output(8, GPIO.LOW)
      GPIO.output(7, GPIO.HIGH)

   if (m == ['volumeup']) :
      GPIO.output(9, GPIO.LOW)
      GPIO.output(11, GPIO.LOW)
      GPIO.output(8, GPIO.LOW)
      GPIO.output(7, GPIO.LOW)
      time.sleep(0.001)
      GPIO.output(9, GPIO.HIGH)
      GPIO.output(11, GPIO.LOW)
      GPIO.output(8, GPIO.LOW)
      GPIO.output(7, GPIO.HIGH)
      time.sleep(0.1)
      GPIO.output(9, GPIO.LOW)
      GPIO.output(7, GPIO.LOW)


   if (m == ['volumedown']) :
      GPIO.output(9, GPIO.LOW)
      GPIO.output(11, GPIO.LOW)
      GPIO.output(8, GPIO.LOW)
      GPIO.output(7, GPIO.LOW)
      time.sleep(0.001)
      GPIO.output(9, GPIO.LOW)
      GPIO.output(11, GPIO.HIGH)
      GPIO.output(8, GPIO.HIGH)
      GPIO.output(7, GPIO.LOW)
      time.sleep(0.1)
      GPIO.output(11, GPIO.LOW)
      GPIO.output(8, GPIO.LOW)


   if (m == ['exit']) :
      GPIO.output(9, GPIO.LOW)
      GPIO.output(11, GPIO.LOW)
      GPIO.output(8, GPIO.LOW)
      GPIO.output(7, GPIO.LOW)
      break
 
