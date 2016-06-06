# servo  - RasPi Python sample

Test for Continuous Rotation Servo <br/>
using RPi.GPIO on Rapberry Pi <br/>
<img src="https://github.com/FabLabKannai/RaspiStudy/blob/master/4_python/docs/raspi_servo.jpg" width="300" /> <br/>

## RPI Servo Duty
command specify duty cycle <br/>

**Usage**  <br/>
format : digits <br/>
example <br/>
- 5.0 : clockwide full speed <br/>
- 7.5 : stop <br/>
- 1.0 : anticlockwide full speed <br/>

**Contorl Signal**  <br/>
<img src="https://github.com/FabLabKannai/RaspiStudy/blob/master/4_python/docs/servo_control_signal.png" width="200" />

**Result**  <br/>
- cycle 20ms <br/>
<img src="https://github.com/FabLabKannai/RaspiStudy/blob/master/4_python/docs/rpi_pwm_cycle_20ms.png" width="200" />
- Servo did not stop in duty 7.5, and is rotating at a very slow. <br/>
Pulse width is about 1.6 msec, but expect value is 1.5 msec <br/>
<img src="https://github.com/FabLabKannai/RaspiStudy/blob/master/4_python/docs/rpi_pwm_duty_7_5.png" width="200" />
- Servo stop about duty 7.2. <br/>
But pulse has the jitter. <br/>
<img src="https://github.com/FabLabKannai/RaspiStudy/blob/master/4_python/docs/rpi_pwm_duty_7_2.png" width="200" />

**Blog (Japanese)**  <br/>
http://android.ohwada.jp/archives/6778

## RPI Servo Speed
command specify speed <br/>

**Usage**  <br/>
format : digits <br/>
example <br/>
- -100 : clockwide full speed <br/>
- 0 : stop <br/>
- 100 : anticlockwide full speed <br/>

**Blog (Japanese)**  <br/>
http://android.ohwada.jp/archives/6812

### Wiring
The servo has three lines. <br/>
Connect red line to Pin4 (+ 5v), black line to Pin6 (GND), and white line to Pin32 (GPIO12). <br/>
