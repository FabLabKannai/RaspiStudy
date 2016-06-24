# Flask - Web App sample

running on Raspberry Pi with Flask <br/>

## Open JTalk
Speech by the text input from the web form using [Open JTalk](http://open-jtalk.sp.nitech.ac.jp/). <br/>
<img src="https://github.com/FabLabKannai/RaspiStudy/blob/master/5_web/docs/46_jtalk.png" width="300" /> <br/>

### Install Open JTalk
> $ sudo apt-get install open-jtalk <br/>
> $ sudo apt-get install open-jtalk-mecab-naist-jdic  <br/>
> $ sudo apt-get install hts-voice-nitech-jp-atr503-m001 <br/>

> $ cd /tmp <br/>
> $ wget http://downloads.sourceforge.net/project/mmdagent/MMDAgent_Example/MMDAgent_Example-1.6/MMDAgent_Example-1.6.zip <br/>
> $ unzip MMDAgent_Example-1.6.zip <br/>
> $ sudo cp -R ./MMDAgent_Example-1.6/Voice/mei /usr/share/hts-voice/ <br/>

### Setup
transfer this directory "46_jtalk" under /tmp <br/>

### run
> $ python flask_jtalk.py <br/>

### web
http://raspberrypi.local:5000/ <br/>
