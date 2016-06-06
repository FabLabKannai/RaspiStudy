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
	is_run = False
	is_blink = False
	is_status = False

	def __init__(self, pin):
		super(LedThread, self).__init__()
		self.pin = pin

	def startRun(self):
		self.is_run = True
		self.start()
	
	def stopRun(self):
		self.is_run = False
		
	def startBlink(self):
		self.is_blink = True

	def stopBlink(self):
		self.is_blink = False

	# run when is_run is true
	def run(self):
		cnt = 0
		while self.is_run:
			cnt += 1
			if cnt >= self.MAX_CNT:
				# every one second
				cnt = 0
				self.blink()
			time.sleep(self.TIME_SLEEP)

	# blink LED when is_blink is true
	def blink(self):
		if self.is_blink:
			self.is_status = not self.is_status
			wiringpi.digitalWrite(self.pin, self.is_status)

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
