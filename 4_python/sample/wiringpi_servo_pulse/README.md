# servo pulse - RasPi Python sample

Test for Continuous Rotation Servo <br/>
using WiringPi on Rapberry Pi <br/>
Command specify pulse <br>
<img src="https://github.com/FabLabKannai/RaspiStudy/blob/master/4_python/docs/raspi_servo.jpg" width="300" /> <br/>

### Install
> $ sudo apt-get install python-dev <br/>
> $ sudo apt-get install wiringpi <br/>
> $ sudo pip install wiringpi2 <br/>

### Usage
format : digits <br>
example <br>
- 200 : clockwide full speed <br>
- 300 : stop <br>
- 400 : anticlockwide low speed <br>

### Wiring
The servo has three lines. <br/>
Connect red line to Pin4 (+ 5v), black line to Pin6 (GND), and white line to Pin12 (GPIO18). <br/>

### Blog (Japanese)
http://android.ohwada.jp/archives/6921
