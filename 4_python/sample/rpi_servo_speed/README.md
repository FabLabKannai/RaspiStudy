# servo speed - RasPi Python sample

Test for Continuous Rotation Servo <br/>
using RPi.GPIO on Rapberry Pi <br/>
Command specify speed <br>
<img src="https://github.com/FabLabKannai/RaspiStudy/blob/master/4_python/docs/raspi_servo.jpg" width="300" /> <br/>

### Install & Run
$ cd /tmp <br>
$ git clone https://github.com/FabLabKannai/RaspiStudy.git  <br>
$ cd RaspiStudy/4_python/sample/rpi_servo_speed/ <br>
$ sudo python rpi_servo_speed.py <br>

### Usage
format : digits <br>
example <br>
- -100 : clockwide full speed <br>
- -10 : clockwide low speed <br>
- 0 : stop <br>
- 10 : anticlockwide low speed <br>
- 100 : anticlockwide full speed <br>

### Wiring
The servo has three lines. <br/>
Connect red line to Pin4 (+ 5v), black line to Pin6 (GND), and white line to Pin15 (GPIO22). <br/>

### Blog (Japanese)
http://android.ohwada.jp/archives/6812
