# Python Sample: LED Blink
# 2016-05-01 K.OHWADA @ FabLab Kannai

import RPi.GPIO as GPIO
import time

# main
PIN = 11
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN, GPIO.OUT)

try:
	# endless loop
	while True:
		GPIO.output(PIN, False)
		time.sleep(1)
		GPIO.output(PIN, True)
		time.sleep(1)	
except KeyboardInterrupt:
	# exit the loop, if key interrupt
	pass

# cleanup GPIO
GPIO.cleanup()

# main end
