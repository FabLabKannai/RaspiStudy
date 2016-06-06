#!/usr/bin/python
# Python Sample: LED Blink
# 2016-06-01 K.OHWADA @ FabLab Kannai

import wiringpi
import time

# main
PIN = 17 # con-pin 11
INTERVAL = 1 # 1 sec
wiringpi.wiringPiSetupGpio()
wiringpi.pinMode(PIN, wiringpi.OUTPUT)

try:
	# endless loop
	while True:
		# LED off
		print "LED Off"
		wiringpi.digitalWrite(PIN, wiringpi.LOW) 
		time.sleep(INTERVAL) 
		# LED on 
		print "LED On"
		wiringpi.digitalWrite(PIN, wiringpi.HIGH)                 
		time.sleep(INTERVAL)
except KeyboardInterrupt:
	# exit the loop, if key interrupt
	pass

wiringpi.digitalWrite(PIN, wiringpi.LOW) 
# main end
