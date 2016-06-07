# Button - RasPi Python Sample

### RPI Button Read
read the status of the button <br/>

**Wiring** <br/>
put the Button  between pin 13 (GPIO 27) and pin 1 (3.3V) <br/>
and put 10 kilo ohm resistor between pin 13 (GPIO 27) and pin 9 (GND3) <br/>

### RPI Button LED
turns on the LED when press the button <br/>

**Wiring** <br/>
put the LED and 330 ohm resistor in series between pin 11 (GPIO 17) and pin 6 (GND) <br/>

### RPI Button Camera
take a picture when press the button with USB camera using fswebcam <br/>
USB camera [Buffalo BSW20KM15](http://buffalo.jp/product/multimedia/web-camera/bsw20km15/) needs to be specified resolution 1600x1200  <br/>

**Install fswebcam** <br/>
> $ sudo apt-get update <br/>
> $ sudo apt-get install fswebcam <br/>

**Prepare** <br/>
connect USB camera to USB port <br/>

### RPI Button Music
play music when press the button using mpg321 <br/>

**Install mpg321** <br/>
> $ sudo apt-get update <br/>
> $ sudo apt-get install mpg321 <br/>

**Prepare** <br/>
setup music file "jazz.mp3" in tmp directory <br/>
source [JWilborn - Smooth jazz music](https://soundcloud.com/jwilborn) <br/>

### RPI Button Poweroff
power off when press the button <br/>
