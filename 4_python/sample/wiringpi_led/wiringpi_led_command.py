#!/usr/bin/python
# Python Sample
#   command specify LED on, off, blink
# 2016-06-01 K.OHWADA @ FabLab Kannai

import time
import threading
import wiringpi

#
# LedController
#
# Usage
#    w : wakeup
#    q : quit
#    0 : LED Off
#    1 : LED On
#    2 : LED Blink
#
class LedController():
	TIME_QUIT = 0.5  # 0.5 sec
	ledThread = None	
	pin = 0
	isRun = False
	isFirst = True

	def __init__(self, pin):
		self.pin = int(pin)

	def wakeup(self):
		if self.isFirst:
			# setup, if first
			self.isFirst = False
			wiringpi.wiringPiSetupGpio()
			wiringpi.pinMode(self.pin, wiringpi.OUTPUT)
		self.quit()
		self.ledThread = LedThread(self.pin)		
		self.ledThread.startRun()
		self.ledThread.startBlink()

	def quit(self):
		if self.ledThread:
			# remove LED Thread
			self.ledThread.stopBlink()
			self.ledThread.stopRun()
			time.sleep(self.TIME_QUIT)	
			self.ledThread = None
		wiringpi.digitalWrite(self.pin, wiringpi.LOW) 

	def command(self, c):
		if c == 'w':
			if not self.isRun: 
				# Wakeup, if not run
				print 'Wakeup'
				self.isRun = True
				self.wakeup()
		elif not self.isRun:
			# nothing to do, if not run
			return
		elif c == 'q':
			# Qiut
			print 'Qiut'
			self.isRun = False
			self.quit()
		elif c == '0':			
			# LED off
			print 'LED off'
			self.stopBlink()
			wiringpi.digitalWrite(self.pin, wiringpi.LOW) 
		elif c == '1':			
			# LED on
			print 'LED on'
			self.stopBlink()
			wiringpi.digitalWrite(self.pin, wiringpi.HIGH) 
		elif c == '2':
			# LED blink
			print 'LED blink'
			self.startBlink()

	def startBlink(self):
		if self.ledThread:
			self.ledThread.startBlink()

	def stopBlink(self):
		if self.ledThread:
			self.ledThread.stopBlink()
										
# end of class

#
# LED Thread class for blink
# 
class LedThread(threading.Thread):
	TIME_BLINK = 1  # 1 sec
	TIME_SLEEP = 0.1 # 0.1 sec
	MAX_CNT = int( TIME_BLINK / TIME_SLEEP )
	pin = 0
	isRun = False
	isBlink = False
	isStatus = False

	def __init__(self, pin):
		super(LedThread, self).__init__()
		self.pin = pin

	def startRun(self):
		self.isRun = True
		self.start()

	def stopRun(self):
		self.isRun = False

	def startBlink(self):
		self.isBlink = True

	def stopBlink(self):
		self.isBlink = False

	# run when isRun is true
	def run(self):
		cnt = 0
		while self.isRun:
			cnt += 1
			if cnt >= self.MAX_CNT:
				# every one second
				cnt = 0
				self.blink()
			time.sleep(self.TIME_SLEEP)

	# blink LED when isBlink is true
	def blink(self):
		if self.isBlink:
			self.isStatus = not self.isStatus
			wiringpi.digitalWrite(self.pin, self.isStatus)

# end of class

# main
PIN = 17 # con-pin 11

# start LED
led = LedController(PIN)

try:
	# endless loop
	while True:
		# wait to enter command
		c = raw_input('> ')
		led.command(c)
except KeyboardInterrupt:
	# exit the loop, if key interrupt
	pass

led.quit()
# main end
