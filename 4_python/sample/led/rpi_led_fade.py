#!/usr/bin/python
# Python Sample
#   LED fade : brighter LED, and darker LED gradually
# 2016-05-01 K.OHWADA @ FabLab Kannai

import time
import RPi.GPIO as GPIO

# main
PIN = 17 # con-pin 11
INTERVAL = 0.1 # 0.1 sec
FREQ = 60 # 60Hz
MIN_DUTY = 0 # 0%
MAX_DUTY = 100 # 100%
DIV_DUTY = 5 # 5%

duty = MIN_DUTY
amount = DIV_DUTY

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.OUT)
led = GPIO.PWM(PIN, FREQ)
led.start(duty)

try:
	# endless loop
	while True:
		print duty
		led.ChangeDutyCycle(duty)
		duty = duty + amount
		if duty <= MIN_DUTY:
			# limit min, if under 
			duty = MIN_DUTY
			# set increment
			amount = DIV_DUTY
		elif duty >= MAX_DUTY:
			# limit max, if over  
			duty = MAX_DUTY
			# set decrement
			amount = -DIV_DUTY
		time.sleep(INTERVAL)
except KeyboardInterrupt:
	# exit the loop, if key interrupt
	pass

led.stop()
GPIO.cleanup()
# main end
