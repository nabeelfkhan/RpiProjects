#Code to interface with DRV8821 and two stepper motors

import wiringpi


#Pin number listing

PWMA = 7 #Uses actual pin numbers, not GPIO number
PWMB = 13
ABRST = 33
ABDIR = 35
CDRST = 37
CDDIR = 15

# Static Variables
OUTPUT = 1
HIGH = 1
LOW = 0

wiringpi.wiringPiSetup()
wiringpi.pinMode(PWMA,OUTPUT)
wiringpi.pinMode(PWMB,OUTPUT)
wiringpi.pinMode(ABRST,OUTPUT)
wiringpi.pinMode(ABDIR,OUTPUT)
wiringpi.pinMode(CDRST,OUTPUT)
wiringpi.pinMode(CDDIR,OUTPUT)

#for time in range(0,4):
#	for brightness in range(0,100): # Going from 0 to 100 will give us full off to full on
#		wiringpi.softPwmWrite(PIN_TO_PWM,brightness) # Change PWM duty cycle
#		wiringpi.delay(10) # Delay for 0.2 seconds
#	for brightness in reversed(range(0,100)):
#		wiringpi.softPwmWrite(PIN_TO_PWM,brightness)
#		wiringpi.delay(10)


pwmacount= int(raw_input("Enter number of PWM pulses for pin 7:\n"))

#Inputs for later
MotorABDir = 1
MotorCDDir = 0

wiringpi.digitalWrite(ABRST,HIGH) #Enable motor 1
wiringpi.digitalWrite(CDRST,HIGH) #Enable motor 2
wiringpi.digitalWrite(ABDIR,MotorABDir) #Enable motor 2
wiringpi.digitalWrite(CDDIR,MotorCDDir) #Enable motor 2



for pulses in range(0,pwmacount):

	wiringpi.digitalWrite(PWMA,HIGH)
	wiringpi.delayMicroseconds(500) #f = 900Hz (pulses per second). T = 1/f. Delay = T/2 = 555.56us> Modified based on scope
	wiringpi.digitalWrite(PWMA,LOW)
	wiringpi.delayMicroseconds(500)
	
	#wiringpi.digitalWrite(PWMB,HIGH)
	#wiringpi.delayMicroseconds(500) #f = 900Hz (pulses per second). T = 1/f. Delay = T/2 = 555.56us> Modified based on scope
	#wiringpi.digitalWrite(PWMB,LOW)
	#wiringpi.delayMicroseconds(500)

wiringpi.digitalWrite(ABRST,LOW) #Disable motor 1
wiringpi.digitalWrite(CDRST,LOW) #Disable motor 2
