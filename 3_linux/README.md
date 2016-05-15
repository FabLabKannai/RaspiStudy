# Linux - Raspberry Pi Study

## WebSite (Japanese)
http://fabble.cc/fablabkannai/rapsberryxpixxxlinux <br/>

- What is Linux
- Linux command
- Controll GPIO by shell

## Docs
- History of Unix/Linux
- History of UNIX computer

## Sample

### LED On / Off
Put LED and 1kΩ resistance in series, between P11(GPIO17) and P6 (GND) <br/>
<img src="https://github.com/FabLabKannai/RaspiStudy/blob/master/3_linux/raspi_led.jpg" width="300"> <br/>
> $ sudo su - <br/>
\# echo "17" > /sys/class/gpio/export <br/>
\# echo "out" > /sys/class/gpio/gpio17/direction <br/>
\# echo "1" > /sys/class/gpio/gpio17/value <br/>
\# echo "0" > /sys/class/gpio/gpio17/value <br/>
\# exit
