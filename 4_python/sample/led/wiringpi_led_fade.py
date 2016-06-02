# Python Sample: LED fade
# 2016-05-30 K.OHWADA @ FabLab Kannai

# requirement
# sudo apt-get install wiringpi
# sudo pip install wiringpi2

import wiringpi as gpio
import time

# main
# pwm pin 12 or 18, and 13 or 19
PIN = 19
INTERVAL = 0.05
MIN_BRIGHTNESS = 0
MAX_BRIGHTNESS = 1023

bright = 0
amount = 16
gpio.wiringPiSetupGpio()
gpio.pinMode(PIN, gpio.PWM_OUTPUT)

try:
	# endless loop
	while True:
		print bright
		gpio.pwmWrite(PIN, bright)
		bright = bright + amount;
		if bright <= MIN_BRIGHTNESS:
			bright = MIN_BRIGHTNESS
			amount = -amount
		elif bright >= MAX_BRIGHTNESS:
			bright = MAX_BRIGHTNESS
			amount = -amount
		time.sleep(INTERVAL)
except KeyboardInterrupt:
	# exit the loop, if key interrupt
	pass

gpio.pwmWrite(PIN, MIN_BRIGHTNESS)
# main end
