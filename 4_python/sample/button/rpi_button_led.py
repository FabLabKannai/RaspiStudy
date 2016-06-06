#!/usr/bin/python
# Python Sample
#   turns on the LED when press the button
# 2016-05-01 K.OHWADA @ FabLab Kannai

import RPi.GPIO as GPIO
import time

# main
PIN_LED = 17 # con-pin 11
PIN_BUTTON = 27 # con-pin 13
INTERVAL = 0.1 # 0.1 sec
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_LED, GPIO.OUT)
GPIO.setup(PIN_BUTTON, GPIO.IN)

try:
	# endless loop
	while True:
		value = GPIO.input(PIN_BUTTON)
		if value == GPIO.HIGH:
			# LED On, if button is pushed
			print "LED On"
  			GPIO.output(PIN_LED, GPIO.HIGH)
		else:
			# LED Off, otherwise
			print "LED Off"
  			GPIO.output(PIN_LED, GPIO.LOW)
  		time.sleep(INTERVAL)
except KeyboardInterrupt:
	# exit the loop, if key interrupt
	pass

# cleanup GPIO

GPIO.cleanup()
# main end
