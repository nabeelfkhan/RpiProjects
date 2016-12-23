# Pulsates an LED connected to GPIO pin 1 with a suitable resistor 4 times using softPwm
# softPwm uses a fixed frequency
import wiringpi

OUTPUT = 1

PIN = 7

wiringpi.wiringPiSetup()
wiringpi.pinMode(PIN,OUTPUT)

for time in range(0,4):
	wiringpi.digitalWrite(PIN,1)
	wiringpi.delay(500)
	wiringpi.digitalWrite(PIN,0)
	wiringpi.delay(500)
