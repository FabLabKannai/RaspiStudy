# Flask - Web App sample

running on Raspberry Pi with Flask <br/>

## LED Controller Daemon
Web app to control LED <br/>
<img src="https://github.com/FabLabKannai/RaspiStudy/blob/master/5_web/sample/docs/46_led_deamon.png" width="300" /> <br/>

### Requirements
- OS: Raspbian <br/>
- Python 2.7 <br/>
- python-dev <br/>
$ sudo apt-get install python-dev <br/>
- [Virtualenv](https://virtualenv.readthedocs.org/en/latest/) <br/>
$ sudo pip install virtualenv <br/>

### Install
$ cd /tmp<br/>
$ git clone https://github.com/FabLabKannai/RaspiStudy.git <br/>
$ mkdir ~/RaspiStudy/ <br/>
$ mv RaspiStudy/5_web/sample/46_daemon/LedSample/ ~/RaspiStudy/ <br/>

$ cd ~/RaspiStudy <br/>
$ virtualenv venv <br/>
( You do not need to excute this command more than once, if you excuted this at once. ) <br/>

$ source venv/bin/activate <br/>
(venv) $ cd LedSample <br/>
(venv) $ python setup.py install <br/>
$ deactivate <br/>

you can use service daemon <br/>
$ sudo sh init.sh <br/>

### Run
$ cd ~<br/>
$ sudo RaspiStudy/venv/bin/led_sample <br/>

or service daemon <br/>
$ sudo /etc/init.d/led-sample start <br/>

### Usage
http://rasoberrypi.local:5010/ <br/>
