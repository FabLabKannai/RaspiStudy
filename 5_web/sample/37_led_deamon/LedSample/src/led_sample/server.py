# LED server with flask
# 2016-05-01 K.OHWADA @ FabLab Kannai

from flask import Flask, render_template, request
from led import Led

# constant
PIN = 11

# Flask start
app = Flask(__name__)
led = Led(PIN)

# server_run
def server_run(host, port):
	app.run(host=host, port=port)

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
