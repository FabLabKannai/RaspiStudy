#!/usr/bin/python
# Flask sample : LED Controller
# 2016-05-01 K.OHWADA @ FabLab Kannai

from flask import Flask, render_template, request
import threading
import time
import wiringpi

#
# GpioController
#
# Usage
#    0 : LED Off
#    1 : LED On
#    2 : LED Blink
#
class GpioController():
	led_th = None	
	pin_led = 0
	pin_button = 0
		
	def __init__(self, pin_led, pin_button, pin_servo):
		self.pin_led = int(pin_led)
		self.pin_button = int(pin_button)
		self.led_th = LedThread(self.pin_led)
		self.servo = ServoSpeed(pin_servo)

	def setDebugPrint(self, flag):
		self.servo.setDebugPrint(flag)

	def start(self):
		wiringpi.wiringPiSetupGpio()
		wiringpi.pinMode(self.pin_led, wiringpi.OUTPUT)
		wiringpi.pinMode(self.pin_button, wiringpi.INPUT)
		self.led_th.startRun()
		self.servo.setPinMode()
		self.servo.setPwm()
		self.servo.stop()

	def stop(self):
		self.led_th.stopRun()
		self.servo.quit()

	def commandLed(self, c):
		if c == '0':
			# LED off
			print 'LED off'
			self.led_th.stopBlink()
			wiringpi.digitalWrite(self.pin_led, wiringpi.LOW) 
		elif c == '1':			
			# LED on
			print 'LED on'
			self.led_th.stopBlink()
			wiringpi.digitalWrite(self.pin_led, wiringpi.HIGH) 
		elif c == '2':
			# LED blink
			print 'LED blink'
			self.led_th.startBlink()

	def commandServo(self, speed):
		self.servo.change(speed)

	def getButtonStatus(self):
		val = wiringpi.digitalRead(self.pin_button)
		ret = 1 if val == wiringpi.HIGH else 0
		return ret		
							
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

# constant
PIN_LED = 17 # con-pin 11
PIN_BUTTON = 27 # con-pin 13
PIN_SERVO = 12 # con-pin 32
DEBUG = False

# Flask start	
app = Flask(__name__)
# start GPIO
gpio = GpioController(PIN_LED, PIN_BUTTON, PIN_SERVO)
gpio.start()

# route index
@app.route('/')
def show_index():
	return render_template('index.html')

# route action with post
@app.route('/action', methods=['POST'])
def action():
	if request.method == 'POST':
		do_post()
	return ''

# route status with get
@app.route('/status', methods=['GET'])
def status():
	ret = ''
	if request.method == 'GET':
		ret = do_get()
	return ret

# do post method
# get parameter, and control LED or Servo
def do_post():
	type = str(request.form['type'])
	val = str(request.form['value'])
    	if type == 'led':
    		gpio.commandLed(val)
	elif type == 'servo':
    		gpio.commandServo(val)

# do get method
# return button status
def do_get():
	status = gpio.getButtonStatus()
	json = "{\"status\":%d}" %(status)
	return json

# Flask end

# main
if __name__ == '__main__':
    app.run(host="0.0.0.0")
