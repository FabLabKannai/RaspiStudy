#!/usr/bin/python
# Python Sample
#   Test for Continuous Rotation Servo
#   command specify speed : -100 - 0 - 100
# 2016-05-01 K.OHWADA @ FabLab Kannai

import RPi.GPIO as GPIO

#
# ServoSpeed
#
# spped
#   -100 : clockwide full speed
#   0 : stop
#   100 : anticlockwide full speed
#
class ServoSpeed():
	FREQ = 50 # 50 Hz (20 ms)
	DUTY_STOP = 7.5 # 1.5ms / 20ms
	COEF = 0.025 # 2.5 / 100
	MIN_SPEED = -100
	STOP_SPEED = 0
	MAX_SPEED = 100	
	servo = None
	pin = 0
	isDebugPrint = False
	dutyOffset = 0

	def __init__(self, pin):
		GPIO.setmode(GPIO.BCM)
		self.pin = int(pin)
		GPIO.setup(self.pin, GPIO.OUT)

	def setDebugPrint(self, debug):
		self.isDebugPrint = bool(debug)

	def setOffset(self, offset):
		self.dutyOffset = self.COEF * float(offset)
		if self.isDebugPrint: 
			print "offset; " + str(offset) + " -> " + str(self.dutyOffset)
 
	def start(self):
		self.servo = GPIO.PWM(self.pin, self.FREQ)
		duty = self.calcDuty(0)
		self.servo.start(duty)

	def stop(self):
		self.servo.stop()
		GPIO.cleanup()

	def change(self, speed):
		duty = self.calcDuty(speed)
		self.servo.ChangeDutyCycle(duty)

	def calcDuty(self, speed):
		# -100 -> 5.0
		# 0 -> 7.5
		# 100 -> 10.0
		speed = float(speed)
		if speed < self.MIN_SPEED: speed = self.MIN_SPEED
		if speed > self.MAX_SPEED: speed = self.MAX_SPEED
		duty = self.DUTY_STOP + self.dutyOffset + self.COEF * speed
		if self.isDebugPrint: 
			print str(speed) + " -> " + str(duty)
		return duty

# end of class

# main
print "start ServoSpeed"
PIN = 12 # con-pin 32
OFFSET = -18.0
DEBUG = False
servo = ServoSpeed(PIN)
servo.setDebugPrint(DEBUG)
servo.setOffset(OFFSET)
servo.start()

try:
	# endless loop
	while True:
		# wait to enter command
		speed = input('> ')
		servo.change(speed)
except KeyboardInterrupt:
	# exit the loop, if key Interrupt
	pass

servo.stop()
# end of main
