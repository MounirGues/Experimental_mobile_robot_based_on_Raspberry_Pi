# -*- coding: utf-8 -*-
# Import required Python libraries
import time
import RPi.GPIO as GPIO
import pylirc

# Use BCM GPIO references
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
# Define GPIO to use on Pi
TRIG = 27
ECHO = 22
# Set pins as output and input
GPIO.setup(TRIG,GPIO.OUT)     # Trig
GPIO.setup(ECHO,GPIO.IN)      # Echo
GPIO.setup(9, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)

GPIO.output(9, GPIO.LOW)
GPIO.output(11, GPIO.LOW)
GPIO.output(8, GPIO.LOW)
GPIO.output(7, GPIO.LOW)
#IR buttons configuration
s = pylirc.init("myprogram")
#Servo ready
GPIO.setup(18, GPIO.OUT)            
p = GPIO.PWM(18,50)              
p.start(6.2)
time.sleep(0.5)
p.ChangeDutyCycle(6.2)
time.sleep(1)
p = GPIO.PWM(18,1)

print "Ultrasonic Measurement"
#Set TRIG as LOW
GPIO.output(TRIG, False)                
print "Waitng For Sensor To Settle"
time.sleep(1)

while True:
	m = pylirc.nextcode()
	print m
	if (m == ['power']) :
		while True:
                        #Obstacle Test
			GPIO.output(TRIG, False)                   #Set TRIG as LOW
			print "Waitng For Sensor To Settle"
			time.sleep(0.1)                            #Delay of 2 seconds

			GPIO.output(TRIG, True)                    #Set TRIG as HIGH
			time.sleep(0.00001)                        #Delay of 0.00001 seconds
			GPIO.output(TRIG, False)                   #Set TRIG as LOW

			while GPIO.input(ECHO)==0:                 #Check whether the ECHO is LOW
				pulse_start = time.time()              #Saves the last known time of LOW pulse

			while GPIO.input(ECHO)==1:                 #Check whether the ECHO is HIGH
				pulse_end = time.time()                #Saves the last known time of HIGH pulse 

			pulse_duration = pulse_end - pulse_start   #Get pulse duration to a variable

			distance = pulse_duration * 17150          #Multiply pulse duration by 17150 to get distance
			distance = round(distance, 2)
			print "Distance:",distance - 0.5,"cm"

			if distance > 2 and distance < 400:        
			#Check whether the distance is within range
				print "Distance:",distance - 0.5,"cm"  
				#Print distance with - 0.5 cm for calibration
			else:
				print "Out Of Range"                   #display out of range
			#End Test
				
			n = pylirc.nextcode()
			print n

			if (n == ['record']) :
			      GPIO.output(25, GPIO.HIGH)

			if (n == ['cut']) :
			      GPIO.output(25, GPIO.LOW)

##			
			if (distance>30) :
				    GPIO.output(9, GPIO.HIGH)
				    GPIO.output(11, GPIO.LOW)
				    GPIO.output(8, GPIO.HIGH)
				    GPIO.output(7, GPIO.LOW)
##
			if (distance<30) :
				    GPIO.output(9, GPIO.LOW)
				    GPIO.output(11, GPIO.LOW)
				    GPIO.output(8, GPIO.LOW)
				    GPIO.output(7, GPIO.LOW)
				    time.sleep(1)

				    p = GPIO.PWM(18,50)
				    p.start(6.2)
				    time.sleep(0.1)
				    p.ChangeDutyCycle(2.6)                   
				    time.sleep(1)	
				    p = GPIO.PWM(18,1)
				    			 
##
				    #Obstacle Test
				    GPIO.output(TRIG, False)                 #Set TRIG as LOW
				    print "Waitng For Sensor To Settle"
				    time.sleep(0.1)                          #Delay of 2 seconds

				    GPIO.output(TRIG, True)                  #Set TRIG as HIGH
				    time.sleep(0.00001)                      #Delay of 0.00001 seconds
				    GPIO.output(TRIG, False)                 #Set TRIG as LOW

				    while GPIO.input(ECHO)==0:               #Check whether the ECHO is LOW
					    pulse_start = time.time()            #Saves the last known time of LOW pulse

				    while GPIO.input(ECHO)==1:               #Check whether the ECHO is HIGH
					    pulse_end = time.time()              #Saves the last known time of HIGH pulse 

				    pulse_duration = pulse_end - pulse_start #Get pulse duration to a variable

				    distance = pulse_duration * 17150        #Multiply pulse duration by 17150 to get distance
				    distance = round(distance, 2)
				    print "Distance:",distance - 0.5,"cm"

				    if distance > 2 and distance < 400:
					#Check whether the distance is within range
    					print "Distance:",distance - 0.5,"cm"  
						#Print distance with - 0.5 cm for calibration
				    else:
					    print "Out Of Range"                       #display out of range
				    #End Test

				    if (distance<30) :
					    oright=1
				    else:
					    oright=0

				    print 'oright=',oright

				    p = GPIO.PWM(18,50)              
				    p.start(2.8)
				    time.sleep(0.1)
				    p.ChangeDutyCycle(10.3)                   
				    time.sleep(1)	
				    p = GPIO.PWM(18,1)

				    #Obstacle Test
				    GPIO.output(TRIG, False)                 #Set TRIG as LOW
				    print "Waitng For Sensor To Settle"
				    time.sleep(0.1)                            #Delay of 2 seconds

				    GPIO.output(TRIG, True)                  #Set TRIG as HIGH
				    time.sleep(0.00001)                      #Delay of 0.00001 seconds
				    GPIO.output(TRIG, False)                 #Set TRIG as LOW

				    while GPIO.input(ECHO)==0:               #Check whether the ECHO is LOW
					    pulse_start = time.time()              #Saves the last known time of LOW pulse

				    while GPIO.input(ECHO)==1:               #Check whether the ECHO is HIGH
					    pulse_end = time.time()                #Saves the last known time of HIGH pulse 

				    pulse_duration = pulse_end - pulse_start #Get pulse duration to a variable

				    distance = pulse_duration * 17150        #Multiply pulse duration by 17150 to get distance
				    distance = round(distance, 2)            #Round to two decimal points

				    if distance > 2 and distance < 400:      
					#Check whether the distance is within range
					    print "Distance:",distance - 0.5,"cm"  
						#Print distance with - 0.5 cm for calibration
				    else:
					    print "Out Of Range"                   #display out of range
				    #End Test
				    
				    if (distance<30) :
					    oleft=1
				    else:
					    oleft=0

				    print 'oleft=',oleft
				    
				    p = GPIO.PWM(18,50)              
				    p.start(10)                             
				    time.sleep(0.1)
				    p.ChangeDutyCycle(6.2)                   
				    time.sleep(1)	
				    p = GPIO.PWM(18,1)
				    
				    if oright==0 :
					    if oleft==1:
						    GPIO.output(9, GPIO.HIGH)
						    GPIO.output(11, GPIO.LOW)
						    GPIO.output(8, GPIO.LOW)
						    GPIO.output(7, GPIO.HIGH)
						    time.sleep(0.38)
						    GPIO.output(9, GPIO.LOW)
						    GPIO.output(11, GPIO.LOW)
						    GPIO.output(8, GPIO.LOW)
						    GPIO.output(7, GPIO.LOW)
						    time.sleep(1)

				    if oleft==0:
					    if oright==1:
						    GPIO.output(9, GPIO.LOW)
						    GPIO.output(11, GPIO.HIGH)
						    GPIO.output(8, GPIO.HIGH)
						    GPIO.output(7, GPIO.LOW)
						    time.sleep(0.367)
						    GPIO.output(9, GPIO.LOW)
						    GPIO.output(11, GPIO.LOW)
						    GPIO.output(8, GPIO.LOW)
						    GPIO.output(7, GPIO.LOW)
						    time.sleep(1)
						    
				    if oright==1:
					    if oleft==1:
						     GPIO.output(9, GPIO.LOW)
						     GPIO.output(11, GPIO.HIGH)
						     GPIO.output(8, GPIO.LOW)
						     GPIO.output(7, GPIO.HIGH)
						     time.sleep(1.5)
						     GPIO.output(9, GPIO.LOW)
						     GPIO.output(11, GPIO.LOW)
						     GPIO.output(8, GPIO.LOW)
						     GPIO.output(7, GPIO.LOW)
						     time.sleep(1)
						     GPIO.output(9, GPIO.HIGH)
						     GPIO.output(11, GPIO.LOW)
						     GPIO.output(8, GPIO.LOW)
						     GPIO.output(7, GPIO.HIGH)
						     time.sleep(0.70)
						     GPIO.output(9, GPIO.LOW)
						     GPIO.output(11, GPIO.LOW)
						     GPIO.output(8, GPIO.LOW)
						     GPIO.output(7, GPIO.LOW)
						     time.sleep(1)
				    
			if (n == ['exit']) :
				GPIO.output(9, GPIO.LOW)
				GPIO.output(11, GPIO.LOW)
				GPIO.output(8, GPIO.LOW)
				GPIO.output(7, GPIO.LOW)
				break



