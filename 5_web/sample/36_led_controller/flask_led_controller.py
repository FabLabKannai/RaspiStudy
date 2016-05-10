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
    	c = int(request.form['led'])
    	led.command(c)

# Flask end

# main
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5010)
