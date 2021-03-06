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
- 400 : anticlockwide full speed <br>

**Contorl Signal**  <br/>
<img src="https://github.com/FabLabKannai/RaspiStudy/blob/master/4_python/docs/servo_control_signal.png" width="200" />

**Result**  <br/>
- cycle 20ms <br/>
<img src="https://github.com/FabLabKannai/RaspiStudy/blob/master/4_python/docs/wiringpi_pwm_cycle_20ms.png" width="200" />
- Servo stop in pluse 300 <br/>
Pulse width is 1.5 msec <br/>
<img src="https://github.com/FabLabKannai/RaspiStudy/blob/master/4_python/docs/wiringpi_pwm_width_1_5ms.png" width="200" />

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

### Setting of WiringPi
- pinMode  <br/>
Set PWM_OUTPUT in pin mode  <br/>

- pwmSetMode  <br/>
Set mark-space in PWM mode  <br/>

- pwmSetClock  <br/>
Set the division ratio of the clock .  <br/>
PWM clock is 19.2 MHz.  <br/>
The pulse width 0.5ms, and the control step is 100 , the frequency division ratio is 96 .  <br/>
0.5ms / 100 = 5μs (200 KHz)  <br/>
19.2 MHz / 200 KHz = 96  <br/>

- pwmSetRange  <br/>
Set the number of clocks to be PWM cycle.  <br/>
the number is 400,  PWM cycle is 20ms .   <br/>
20ms / 5μs = 4000  <br/>

- pwmWrite  <br/>
Set the number of clocks to be a pulse width . <br/>
The number is 300, when pulse width is 1.5ms. <br/>
1.5ms / 5μs = 300 <br/>

### Wiring
The servo has three lines. <br/>
Connect red line to Pin4 (+ 5v), black line to Pin6 (GND), and white line to Pin32 (GPIO12). <br/>

### Blog (Japanese)
http://android.ohwada.jp/archives/6921
