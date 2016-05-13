# Linux - Raspberry Pi Study

## WebSite (Japanese)
http://fabble.cc/fablabkannai/rapsberryxpixxxlinux <br/>

- What is Linux
- Shell command
- Controll GPIO by shell

## Docs
- History of Unix/Linux
- History of UNIX computer

## Sample

### LED On / Off
Connect LED to GPIO 17 <br/>
> $ sudo su - <br/>
\# echo "17" > /sys/class/gpio/export <br/>
\# echo "out" > /sys/class/gpio/gpio17/direction <br/>
\# echo "1" > /sys/class/gpio/gpio17/value <br/>
\# echo "0" > /sys/class/gpio/gpio17/value <br/>
\# exit
