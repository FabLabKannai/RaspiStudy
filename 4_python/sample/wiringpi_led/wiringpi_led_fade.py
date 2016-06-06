#!/usr/bin/python
# Python Sample: LED fade
# 2016-06-01 K.OHWADA @ FabLab Kannai

import wiringpi as gpio
import time

# main
PIN = 18 # con-pin 12
INTERVAL = 0.05 # 0.05 sec
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
		bright = bright + amount
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
