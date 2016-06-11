# Button - RasPi Python Sample

### RPI Button Read
read the status of the button <br/>

**Wiring** <br/>
put the Button  between pin 13 (GPIO 27) and pin 1 (3.3V) <br/>
and put 10 kilo ohm resistor between pin 13 (GPIO 27) and pin 9 (GND) <br/>
<img src="https://github.com/FabLabKannai/RaspiStudy/blob/master/4_python/docs/button_circuit.png" width="300" /> <br/>

### RPI Button LED
turns on the LED, when press the button <br/>

**Wiring** <br/>
put the LED and 330 ohm resistor in series between pin 11 (GPIO 17) and pin 6 (GND) <br/>

### RPI Button Camera
take a picture using fswebcam with USB camera, when press the button  <br/>
USB camera [Buffalo BSW20KM15](http://buffalo.jp/product/multimedia/web-camera/bsw20km15/) needs to be specified resolution 1600x1200  <br/>

**Install fswebcam** <br/>
[Raspberry Pi - Using a Standard USB Webcam](https://www.raspberrypi.org/documentation/usage/webcams/) <br/>
> $ sudo apt-get update <br/>
> $ sudo apt-get install fswebcam <br/>

**Prepare** <br/>
connect USB camera to USB port <br/>

### RPI Button Music
play music using mpg321, when press the button <br/>

**Install mpg321** <br/>
[mpg321 - a simple and lightweight command line MP3 player](http://mpg321.sourceforge.net/) <br/>
> $ sudo apt-get update <br/>
> $ sudo apt-get install mpg321 <br/>

**Prepare** <br/>
setup music file "jazz.mp3" in tmp directory <br/>
source [JWilborn - Smooth jazz music](https://soundcloud.com/jwilborn) <br/>

### RPI Button Poweroff
power off, when press the button <br/>
