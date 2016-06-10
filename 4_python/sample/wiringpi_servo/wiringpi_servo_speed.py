#! /usr/bin/env python
# Python Sample
#   Test for Continuous Rotation Servo
#   command specify speed : -100 - 0 - 100
# 2016-05-30 K.OHWADA @ FabLab Kannai

import wiringpi

#
# ServoSpeed
#
# spped
#   -100 : clockwide full speed
#   0 : stop
#   100 : anticlockwide full speed
#
class ServoSpeed():
	# PWM base clock 19.2 MHz
	# PWM clock 200 KHz
	CLOCK = 96 # 96 = 19.2 MHz / 200 KHz
	RANGE = 4000 # 20ms * 200 KHz
	PULSE_STOP = 300 # 1.5ms  * 200 KHz
	COEF = 1.0 # 0.5ms  * 200 KHz / 100
	MIN_SPEED = -100
	STOP_SPEED = 0
	MAX_SPEED = 100
	pin = 0
	isDebugPrint = False
	pulseOffset = 0

	def __init__(self, pin):
		self.pin = int(pin)

	def setDebugPrint(self, debug):
		self.isDebugPrint = bool(debug)

	def setOffset(self, offset):
		self.pulseOffset = self.COEF * float(offset)
		if self.isDebugPrint: 
			print "offset; " + str(offset) + " -> " + str(self.pulseOffset)

	def setupGpio(self):
		wiringpi.wiringPiSetupGpio()

	def setPinMode(self):
		wiringpi.pinMode(self.pin, wiringpi.PWM_OUTPUT)
	
	def setPwm(self):
		wiringpi.pwmSetMode(wiringpi.PWM_MODE_MS)
		wiringpi.pwmSetClock(self.CLOCK)
		wiringpi.pwmSetRange(self.RANGE)

	def stop(self):
		self.change(0) # stop
		
	def quit(self):
		wiringpi.pwmWrite(self.pin, 0) # no pluse

	def change(self, speed):
		pulse = self.calcPulse(speed)
		wiringpi.pwmWrite(self.pin, pulse)

	def calcPulse(self, speed):
		# -100 -> 200
		# 0 -> 300
		# 100 -> 400
		speed = float(speed)
		if speed < self.MIN_SPEED: speed = self.MIN_SPEED
		if speed > self.MAX_SPEED: speed = self.MAX_SPEED
		pulse = int( self.PULSE_STOP + self.pulseOffset + self.COEF * speed )
		if self.isDebugPrint: 
			print str(speed) + " -> " + str(pulse)
		return pulse

# end of class

# main
print "start ServoSpeed"
PIN = 12 # con-pin 32
DEBUG = False
servo = ServoSpeed(PIN)
servo.setDebugPrint(DEBUG)
servo.setupGpio()
servo.setPinMode()
servo.setPwm()
servo.stop()

try:
	# endless loop
	while True:
		# wait to enter command
		speed = input('> ')
		servo.change(speed)
except KeyboardInterrupt:
	# exit the loop, if key Interrupt
	pass

servo.quit()
# end of main
