# Python Sample: LED Blink
# 2016-05-30 K.OHWADA @ FabLab Kannai

# requirement
# sudo apt-get install wiringpi
# sudo pip install wiringpi2

import wiringpi
import time

# main
PIN = 17
INTERVAL = 1
wiringpi.wiringPiSetupGpio()
wiringpi.pinMode(PIN, wiringpi.OUTPUT)

try:
	# endless loop
	while True:
		print("LED On")
		wiringpi.digitalWrite(PIN, wiringpi.HIGH)                 
		time.sleep(INTERVAL)
		print("LED Off")
		wiringpi.digitalWrite(PIN, wiringpi.LOW)            
		time.sleep(INTERVAL)
except KeyboardInterrupt:
	# exit the loop, if key interrupt
	pass

wiringpi.digitalWrite(PIN, wiringpi.LOW) 
# main end
