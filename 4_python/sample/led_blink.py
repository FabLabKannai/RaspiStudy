# Python Sample: LED Blink
# 2016-05-01 K.OHWADA @ FabLab Kannai

import RPi.GPIO as GPIO
import time

# main
PIN = 11
INTERVAL = 1
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN, GPIO.OUT)

try:
	# endless loop
	while True:
		# LED off
		GPIO.output(PIN, GPIO.LOW)
		time.sleep(INTERVAL)
		# LED on
		GPIO.output(PIN, GPIO.HIGH)
		time.sleep(INTERVAL)	
except KeyboardInterrupt:
	# exit the loop, if key interrupt
	pass

# cleanup GPIO
GPIO.cleanup()

# main end
