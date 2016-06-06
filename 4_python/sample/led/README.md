# LED - RasPi Python Sample

<img src="https://github.com/FabLabKannai/RaspiStudy/blob/master/4_python/docs/raspi_led.jpg" width="300" />

## RPI.GPIO
- RPI LED Bllnk <br>
turn LED on and LED off repeatedly <br>
http://android.ohwada.jp/archives/6838 <br>
- RPI LED Fade <br>
brighter LED, and darker LED gradually <br>
- RPI LED Command <br>
command specify LED on, off, blink <br>

### Wiring
Put the LED and resistor in series between pin 11 (GPIO 17)
and pin 6 (GND) <br/>

## Wiring Pi
- WiringPi LED Bllnk <br/>
http://android.ohwada.jp/archives/6906 <br/>
- WiringPi LED Fade <br/>
PWM pin are 12 (GPIO 18) or 32 (GPIO 12), and 33 ( GPIO 13) or 35 (GPIO 19) <br/>
http://android.ohwada.jp/archives/6917 <br/>

### Install wiringpi
> $ sudo apt-get install python-dev <br/>
> $ sudo apt-get install wiringpi <br/>
> $ sudo pip install wiringpi2 <br/>
