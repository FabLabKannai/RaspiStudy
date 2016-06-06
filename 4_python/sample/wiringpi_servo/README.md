# WiringPi Servo  - RasPi Python sample

Test for Continuous Rotation Servo <br/>
using WiringPi on Rapberry Pi <br/>
<img src="https://github.com/FabLabKannai/RaspiStudy/blob/master/4_python/docs/raspi_servo.jpg" width="300" /> <br/>

## WiringPi Servo Pulse
Command specify pulse <br/>

**Usage**  <br/>
format : digits <br/>
example <br>
- 200 : clockwide full speed <br>
- 300 : stop <br>
- 400 : anticlockwide low speed <br>

## WiringPi Servo Speed
Command specify speed <br/>

**Usage**  <br/>
format : digits <br/>
example <br/>
- -100 : clockwide full speed <br/>
- 0 : stop <br/>
- 100 : anticlockwide full speed <br/>

### Install wiringpi
> $ sudo apt-get update <br/>
> $ sudo apt-get install python-dev <br/>
> $ sudo apt-get install wiringpi <br/>
> $ sudo pip install wiringpi2 <br/>

### Wiring
The servo has three lines. <br/>
Connect red line to Pin4 (+ 5v), black line to Pin6 (GND), and white line to Pin32 (GPIO12). <br/>

### Blog (Japanese)
http://android.ohwada.jp/archives/6921
