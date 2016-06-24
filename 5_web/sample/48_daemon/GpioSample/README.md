# Flask - Web App sample

running on Raspberry Pi with Flask <br/>

## GPIO Controller Daemon
Web app to control GPIO <br/>
<img src="https://github.com/FabLabKannai/RaspiStudy/blob/master/5_web/docs/48_daemon.png" width="300" /> <br/>

### Requirements
- OS: Raspbian <br/>
- Python 2.7 <br/>
- python-dev <br/>
$ sudo apt-get install python-dev <br/>
- [Virtualenv](https://virtualenv.readthedocs.org/en/latest/) <br/>
$ sudo pip install virtualenv <br/>

### Install
> $ cd /tmp<br/>
> $ git clone https://github.com/FabLabKannai/RaspiStudy.git <br/>
> $ mkdir ~/RaspiStudy/ <br/>
> $ mv RaspiStudy/5_web/sample/48_daemon/GpioSample/ ~/RaspiStudy/ <br/>

> $ cd ~/RaspiStudy <br/>
> $ virtualenv venv <br/>
( You do not need to excute this command more than once, if you excuted this at once. ) <br/>

> $ source venv/bin/activate <br/>
> (venv) $ cd GpioSample <br/>
> (venv) $ python setup.py install <br/>
> (venv) $ deactivate <br/>

you can use service daemon <br/>
> $ sudo sh init.sh <br/>

### Run
> $ cd ~<br/>
> $ sudo RaspiStudy/venv/bin/gpio_sample <br/>

or service daemon <br/>
> $ sudo /etc/init.d/gpio-sample start <br/>

### Usage
Access using web browser. <br/>
http://raspberrypi.local:5010/ <br/>
