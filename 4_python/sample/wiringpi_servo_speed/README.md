# servo speed - RasPi Python sample

Test for Continuous Rotation Servo  <br/>
using WiringPi on Rapberry Pi <br/>
Command specify speed <br>
<img src="https://github.com/FabLabKannai/RaspiStudy/blob/master/4_python/docs/raspi_servo.jpg" width="300" /> <br/>

### Install
> $ sudo apt-get install python-dev <br/>
> $ sudo apt-get install wiringpi <br/>
> $ sudo pip install wiringpi2 <br/>

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
Connect red line to Pin4 (+ 5v), black line to Pin6 (GND), and white line to Pin12 (GPIO18). <br/>

### Servo Control Signal
Servo Control Signal <br/>
<img src="https://github.com/FabLabKannai/RaspiStudy/blob/master/4_python/docs/servo_control_signal.png" width="200" /> <br/>

PWM Cycle 20ms <br/>
<img src="https://github.com/FabLabKannai/RaspiStudy/blob/master/4_python/docs/wiringpi_pwm_cycle_20ms.png" width="200" /> <br/>

PWM Pluse Width 1.5ms <br/>
<img src="https://github.com/FabLabKannai/RaspiStudy/blob/master/4_python/docs/wiringpi_pwm_width_1_5ms.png" width="200" /> <br/>

### Blog (Japanese)
http://android.ohwada.jp/archives/6921