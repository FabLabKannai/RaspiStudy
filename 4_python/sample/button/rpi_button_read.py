#!/usr/bin/python
# Python Sample: Button read
# 2016-05-01 K.OHWADA @ FabLab Kannai

import RPi.GPIO as GPIO
import time

# main
PIN = 27 # con-pin 13
INTERVAL = 1 # 1 sec
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.IN)

try:
	# endless loop
	while True:
		value = GPIO.input(PIN)
  		print value
  		time.sleep(INTERVAL)
except KeyboardInterrupt:
	# exit the loop, if key interrupt
	pass

# cleanup GPIO

GPIO.cleanup()
# main end
