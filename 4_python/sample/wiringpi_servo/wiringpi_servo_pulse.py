#! /usr/bin/env python
# Python Sample
#   Test for Continuous Rotation Servo
#   command specify pulse : 200 - 300 - 400
# 2016-05-30 K.OHWADA @ FabLab Kannai

import wiringpi

#
# ServoPulse
#
# spped
#   200 : clockwide full speed
#   300 : stop
#   400 : anticlockwide full speed
#
class ServoPulse():
	# PWM base clock 19.2 MHz
	# PWM clock 200 KHz
	CLOCK = 96 # 96 = 19.2 MHz / 200 KHz
	RANGE = 4000 # 20ms * 200 KHz
	PULSE_STOP = 300 # 1.5ms  * 200 KHz

	pin = 0

	def __init__(self, pin):
		self.pin = int(pin)

	def setupGpio(self):
		wiringpi.wiringPiSetupGpio()

	def setPinMode(self):
		wiringpi.pinMode(self.pin, wiringpi.PWM_OUTPUT)

	def setPwm(self):
		wiringpi.pwmSetMode(wiringpi.PWM_MODE_MS)
		wiringpi.pwmSetClock(self.CLOCK)
		wiringpi.pwmSetRange(self.RANGE)

	def quit(self):
		wiringpi.pwmWrite(self.pin, 0)

	def change(self, pulse):
		wiringpi.pwmWrite(self.pin, pulse)

# end of class

# main
print "start ServoPulse"
PIN = 12 # con-pin 32
servo = ServoPulse(PIN)
servo.setupGpio()
servo.setPinMode()
servo.setPwm()

try:
	# endless loop
	while True:
		# wait to enter command
		pulse = input('> ')
		servo.change(pulse)
except KeyboardInterrupt:
	# exit the loop, if key Interrupt
	pass

servo.quit()
# end of main
