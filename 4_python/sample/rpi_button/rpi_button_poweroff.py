#!/usr/bin/python
# Python Sample
#   power off when press the button
# 2016-06-01 K.OHWADA @ FabLab Kannai

import RPi.GPIO as GPIO
import time
import subprocess

# main
PIN = 27 # con-pin 13
INTERVAL = 0.5 # 0.5 sec
CMD_SUDO = "/usr/bin/sudo"
CMD_POWEROFF = "/sbin/poweroff"
counter = 0 # count 2 seconds

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.IN)

try:
    	# endless loop
    while True:
        if GPIO.input(PIN) == GPIO.HIGH:
            # when button is pushed
            if counter >= 2:
                # shutdown, if over 2 sec
                print "Power off"
                counter = 0
                args = [CMD_SUDO, CMD_POWEROFF]
                subprocess.Popen(args)
            else:
                # counter up, when pushed
                counter += 1
        else:
            # reset counter, otherwise
            counter = 0
        time.sleep(INTERVAL)
except KeyboardInterrupt:
    	# exit the loop, if key interrupt
    pass

GPIO.cleanup()
# main end
