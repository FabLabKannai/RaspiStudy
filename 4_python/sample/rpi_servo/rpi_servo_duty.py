#!/usr/bin/python
# Python Sample
#   Test for Continuous Rotation Servo
#   command specify duty : 5 - 7.5 - 10
# 2016-05-01 K.OHWADA @ FabLab Kannai

import RPi.GPIO as GPIO

#
# ServoDuty
#
# duty
#   5.0 : clockwide full speed
#   7.5 : stop
#   1.0 : anticlockwide low speed
#
class ServoDuty():
	servo = None

	def __init__(self, pin):
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(pin, GPIO.OUT)
		self.servo = GPIO.PWM(pin, 50) # 50 Hz (20 ms)
		self.servo.start(7.5)

	def stop(self):
		self.servo.stop()
		GPIO.cleanup()
		
	def change(self, duty):
		self.servo.ChangeDutyCycle(duty)

# end of class

# main
PIN = 12 # con-pin 32
servo = ServoDuty(PIN)

try:
	# endless loop
	while True:
		# wait to enter command
		duty = input('> ')
		servo.change(duty)
except KeyboardInterrupt:
	# exit the loop, if key Interrupt
	pass

servo.stop()	
# end of main
