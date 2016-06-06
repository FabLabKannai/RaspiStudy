#!/usr/bin/python
# Python Sample
#   take a picture when press the button
#   with USB camera using fswebcam
# 2016-06-01 K.OHWADA @ FabLab Kannai

import RPi.GPIO as GPIO
import time
import subprocess
import datetime

PIN = 27 # con-pin 13
CMD = "/usr/bin/fswebcam"
RESOLUTION = "1600x1200" # Buffalo BSW20KM15

def my_callback(channel):
    if channel == PIN:
        d = datetime.datetime.today()
        filename = "{0}{1:02d}{2:02d}{3:02d}{4:02d}{5:02d}.jpg".format(d.year, d.month, d.day, d.hour, d.minute, d.second)
        args = [CMD, '-r', RESOLUTION, filename]
        subprocess.Popen(args)

# main
INTERVAL = 0.01 # 10 msec
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.IN)
GPIO.add_event_detect(PIN, GPIO.RISING, callback=my_callback, bouncetime=200)

try:
    	# endless loop
    while True:
        time.sleep(INTERVAL)
except KeyboardInterrupt:
	# exit the loop, if key interrupt
    pass

GPIO.cleanup()
# main end
