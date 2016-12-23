# Pulsates an LED connected to GPIO pin 1 with a suitable resistor 4 times using softPwm
# softPwm uses a fixed frequency
import wiringpi

OUTPUT = 1

PWMA = 7
PWMB = 13
HIGH = 1 
LOW = 0

wiringpi.wiringPiSetup()
wiringpi.pinMode(PWMA,OUTPUT)
wiringpi.pinMode(PWMB,OUTPUT)

#for time in range(0,4):
#	for brightness in range(0,100): # Going from 0 to 100 will give us full off to full on
#		wiringpi.softPwmWrite(PIN_TO_PWM,brightness) # Change PWM duty cycle
#		wiringpi.delay(10) # Delay for 0.2 seconds
#	for brightness in reversed(range(0,100)):
#		wiringpi.softPwmWrite(PIN_TO_PWM,brightness)
#		wiringpi.delay(10)


pwmacount= int(raw_input("Enter number of PWM pulses for pin 7:\n"))




for pulses in range(0,pwmacount):

	wiringpi.digitalWrite(PWMA,HIGH)
	wiringpi.delayMicroseconds(500) #f = 900Hz (pulses per second). T = 1/f. Delay = T/2 = 555.56us> Modified based on scope
	wiringpi.digitalWrite(PWMA,LOW)
	wiringpi.delayMicroseconds(500)


