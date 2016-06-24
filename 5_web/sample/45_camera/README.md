# Flask - Web App sample

running on Raspberry Pi with Flask <br/>

## Camera
Motion JPEG streaming using [mjpg-streamer](https://sourceforge.net/projects/mjpg-streamer/) with USB camera. <br/>
And you can take a picture. <br/>
<img src="https://github.com/FabLabKannai/RaspiStudy/blob/master/5_web/docs/45_camera.png" width="300" /> <br/>

### Install mjpg-streamer
See https://github.com/FabLabKannai/RaspiStudy/tree/master/2_install/raspi/mjpg-streamer

### Setup
transfer this directory "45_camara" under /tmp <br/>

### run
$ sudo /etc/init.d/mjpg-streamer start <br/>
$ python flask_camera.py <br/>

### web
http://raspberrypi.local:5000/ <br/>
