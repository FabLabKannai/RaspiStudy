# LED command
# 2016-05-01 K.OHWADA @ FabLab Kannai

import threading
import time
import RPi.GPIO as GPIO

#
# LED class
# 
# Command Usage
#    0 : LED Off
#    1 : LED On
#    2 : LED Blink
#
class Led():
	th = None
	pin = 0

	def __init__(self):
		pass
		
	def setPin(self, pin):
		self.pin = int(pin)
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(self.pin, GPIO.OUT)
		self.th = LedThread(self.pin)
		self.th.start()

	def cleanupGpio(self):
		GPIO.cleanup()

	def command(self, c):
		if c == 0:
			self.th.stopBlink()
			GPIO.output(self.pin, False)
		elif c == 1:
			self.th.stopBlink()
			GPIO.output(self.pin, True)
		elif c == 2:
			self.th.startBlink()

# end of class

#
# LED Thread class for blink
# 
class LedThread(threading.Thread):
	pin = 0
	is_blink = False
	is_status = False

	def __init__(self, pin):
		super(LedThread, self).__init__()
		self.pin = pin

	def startBlink(self):
		self.is_blink = True

	def stopBlink(self):
		self.is_blink = False

	# run always
	def run(self):
		cnt = 0
		while True:
			cnt += 1
			if cnt >= 10:
				# every one second
				cnt = 0
				self.blink()
			time.sleep(0.1)

	# blink LED when is_blink is true
	def blink(self):
		if self.is_blink:
			self.is_status = not self.is_status
			GPIO.output(self.pin, self.is_status)

# end of class
