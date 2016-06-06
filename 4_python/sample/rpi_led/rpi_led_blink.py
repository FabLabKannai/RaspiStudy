#!/usr/bin/python
# Python Sample
#   LED Blink : turn LED on and LED off repeatedly 
# 2016-05-01 K.OHWADA @ FabLab Kannai

import RPi.GPIO as GPIO
import time

# main
PIN = 17 # con-pin 11
INTERVAL = 1 # 1 sec
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.OUT)

try:
	# endless loop
	while True:
		# LED off
		print "LED Off"
		GPIO.output(PIN, GPIO.LOW)
		time.sleep(INTERVAL)
		# LED on
		print "LED On"
		GPIO.output(PIN, GPIO.HIGH)
		time.sleep(INTERVAL)	
except KeyboardInterrupt:
	# exit the loop, if key interrupt
	pass

# cleanup GPIO
GPIO.cleanup()

# main end
