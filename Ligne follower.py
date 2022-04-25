import RPi.GPIO as GPIO
import time
import pylirc

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(13, GPIO.IN)
GPIO.setup(6, GPIO.IN)
GPIO.setup(5, GPIO.IN)

GPIO.setup(9, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(2,GPIO.OUT)
GPIO.setup(3,GPIO.OUT)

P = GPIO.PWM(2,50)              
P.start(77)

p = GPIO.PWM(3,50)              
p.start(70)

s = pylirc.init("myprogram")

GPIO.output(9, GPIO.LOW)
GPIO.output(11, GPIO.LOW)
GPIO.output(8, GPIO.LOW)
GPIO.output(7, GPIO.LOW)

from nanpy import Arduino
from nanpy import serial_manager
from time import sleep

Arduino.pinMode(13, Arduino.OUTPUT)
Arduino.pinMode(12, Arduino.INPUT)
Arduino.pinMode(11, Arduino.INPUT)
Arduino.pinMode(8, Arduino.INPUT)
d=0
g=0

while True :

   m = pylirc.nextcode()
   print m
   
   if (m == ['mode']) :
       while True:
              r=Arduino.digitalRead(8)
              c=Arduino.digitalRead(11)
              l=Arduino.digitalRead(12)

              m = pylirc.nextcode()

              if  (m == ['exit']):
                     print "EXIT STOP"
                     GPIO.output(9, GPIO.LOW)
                     GPIO.output(11, GPIO.LOW)
                     GPIO.output(8, GPIO.LOW)
                     GPIO.output(7, GPIO.LOW)
                     break

              if (m == ['up']):
                     GPIO.output(9, GPIO.HIGH)
                     GPIO.output(11, GPIO.LOW)
                     GPIO.output(8, GPIO.HIGH)
                     GPIO.output(7, GPIO.LOW)
                     time.sleep(0.2)
                     GPIO.output(9, GPIO.LOW)
                     GPIO.output(11, GPIO.LOW)
                     GPIO.output(8, GPIO.LOW)
                     GPIO.output(7, GPIO.LOW)
               
              if l==0:
                   g=0
              else:
                   g=1
                   print "g=",g
                   
              if r==0:
                   d=0
              else:     
                   d=1
                   print "d=",d
                  
              if  (g==1):
                      print "LEFT Black"
                      GPIO.output(9, GPIO.LOW)
                      GPIO.output(11, GPIO.LOW)
                      GPIO.output(8, GPIO.LOW)
                      GPIO.output(7, GPIO.LOW)
                      time.sleep(0.1)
                      GPIO.output(9, GPIO.LOW)
                      GPIO.output(11, GPIO.LOW)
                      GPIO.output(8, GPIO.HIGH)
                      GPIO.output(7, GPIO.LOW)
                      g=1
                      d=0      
              
              if (d==1):
                      print "RIGHT Black"
                      GPIO.output(9, GPIO.LOW)
                      GPIO.output(11, GPIO.LOW)
                      GPIO.output(8, GPIO.LOW)
                      GPIO.output(7, GPIO.LOW)
                      time.sleep(0.1)
                      GPIO.output(9, GPIO.HIGH)
                      GPIO.output(11, GPIO.LOW)
                      GPIO.output(8, GPIO.LOW)
                      GPIO.output(7, GPIO.LOW)
                      d=1
                      g=0

              if (c==1):
                 if (r==0):
                    if (l==0):
                          print "Middel Black"
                          GPIO.output(9, GPIO.HIGH)
                          GPIO.output(11, GPIO.LOW)
                          GPIO.output(8, GPIO.HIGH)
                          GPIO.output(7, GPIO.LOW)

              if (c==1):
                 if (r==1):
                    if (l==1):
                          print "ALL BLACK STOP"
                          GPIO.output(9, GPIO.LOW)
                          GPIO.output(11, GPIO.LOW)
                          GPIO.output(8, GPIO.LOW)
                          GPIO.output(7, GPIO.LOW)
                          break


