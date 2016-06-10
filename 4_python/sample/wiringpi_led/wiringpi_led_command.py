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
#    0 : LED Off
#    1 : LED On
#    2 : LED Blink
#
class LedController():
	led_th = None	
	pin = 0

	def __init__(self, pin):
		self.pin = int(pin)
		self.led_th = LedThread(self.pin)

	def start(self):
		wiringpi.wiringPiSetupGpio()
		wiringpi.pinMode(self.pin, wiringpi.OUTPUT)
		self.led_th.startRun()

	def stop(self):
		self.led_th.stopRun()

	def command(self, c):
		if c == '0':
			# LED off
			print 'LED off'
			self.led_th.stopBlink()
			wiringpi.digitalWrite(self.pin, wiringpi.LOW) 
		elif c == '1':			
			# LED on
			print 'LED on'
			self.led_th.stopBlink()
			wiringpi.digitalWrite(self.pin, wiringpi.HIGH) 
		elif c == '2':
			# LED blink
			print 'LED blink'
			self.led_th.startBlink()
								
# end of class

#
# LED Thread class for blink
# 
class LedThread(threading.Thread):
	TIME_BLINK = 1.0  # 1 sec
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
led.start()

try:
	# endless loop
	while True:
		# wait to enter command
		c = raw_input('> ')
		led.command(c)
except KeyboardInterrupt:
	# exit the loop, if key interrupt
	pass

led.stop()
# main end
