# Flask sample : LED Controller
# 2016-05-01 K.OHWADA @ FabLab Kannai

from flask import Flask, render_template, request
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

	def __init__(self, pin):
		self.pin = int(pin)
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(self.pin, GPIO.OUT)
		self.th = LedThread(self.pin)

	def finish(self):
		self.th.stopRun()
		GPIO.cleanup()

	def command(self, c):
		if c == '0':
			# LED Off
			self.th.stopBlink()
			GPIO.output(self.pin, GPIO.LOW)
		elif c == '1':			
			# LED On
			self.th.stopBlink()
			GPIO.output(self.pin, GPIO.HIGH)
		elif c == '2':
			# LED Blink
			self.th.startBlink()

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
			GPIO.output(self.pin, self.is_status)

# end of class

# constant
PIN = 11

# Flask start	
app = Flask(__name__)
led = Led(PIN)

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

# do post method
# get parameter, and control LED
def do_post():
    	c = str(request.form['led'])
    	led.command(c)

# Flask end

# main
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5010)
