#!/usr/bin/python
# Python Sample
#   play music when press the button
#   using mpg321
# 2016-06-01 K.OHWADA @ FabLab Kannai

import RPi.GPIO as GPIO
import time
import subprocess

PIN_LED = 17 # con-pin 11
PIN_BUTTON = 27 # con-pin 13
CMD_PLAY = "/usr/bin/mpg321"
CMD_KILL = "/bin/kill"
FILE = "/tmp/jazz.mp3"
g_process = None
g_is_playing = False

def my_callback(channel):
    global g_process, g_is_playing
    if channel == PIN_BUTTON:
        	# button is pushed
        if g_is_playing == False:
            # play music, when not playing
            print "Play music"
            g_is_playing = True
            GPIO.output(PIN_LED, GPIO.HIGH)
            args = [CMD_PLAY, FILE]
            g_process = subprocess.Popen(args)
        else:
            # stop music, when playing
            print "Stop music"
            g_is_playing = False
            GPIO.output(PIN_LED, GPIO.LOW)
            args = [CMD_KILL, str(g_process.pid)]
            subprocess.Popen(args)

# main
INTERVAL = 0.01 # 1 msec
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_LED, GPIO.OUT)
GPIO.output(PIN_LED, GPIO.LOW)
GPIO.setup(PIN_BUTTON, GPIO.IN)
GPIO.add_event_detect(PIN_BUTTON, GPIO.RISING, callback=my_callback, bouncetime=200)

try:
    	# endless loop
    while True:
        time.sleep(INTERVAL)
except KeyboardInterrupt:
    	# exit the loop, if key interrupt
    pass

GPIO.cleanup()
# main end
