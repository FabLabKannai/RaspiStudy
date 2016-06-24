# mjpg-streamer - raspi 
Script to start [mjpg-streamer](https://sourceforge.net/projects/mjpg-streamer/) daemon <br/>

### Change log
original https://github.com/meinside/rpi-mjpg-streamer <br/>

modified <br/>
add -y (YUYV format) for [Buffalo BSW20KM15](http://www.amazon.co.jp/gp/product/B00HRSQ6B0/ref=as_li_qf_sp_asin_tl?ie=UTF8&camp=247&creative=1211&creativeASIN=B00HRSQ6B0&linkCode=as2&tag=welovediving-22) <br/>

### Install mjpg-streamer
> $ sudo apt-get install subversion <br/>
> $ sudo apt-get install imagemagick <br/>
> $ sudo apt-get install libjpeg-dev <br/>
> $ sudo apt-get install libv4l-dev <br/>
> $ sudo apt-get install v4l-utils <br/>

> $ cd ~ <br/>
> $ mkdir builds <br/>
> $ cd builds <br/>
> $ svn co https://svn.code.sf.net/p/mjpg-streamer/code/mjpg-streamer mjpg-streamer <br/>
> $ cd mjpg-streamer <br/>
> $ make <br/>

### Setup service daemon 
Please modify the template file to suit your environment <br/>
And copy the modified file to under directory /etc/init.d/ <br/>

> $ cd /tmp <br/>
> $ git clone https://github.com/FabLabKannai/RaspiStudy.git <br/>
> $ cd RaspiStudy/2_install/raspi/mjpg-streamer/ <br/>
> $ sudo cp mjpg-streamer /etc/init.d/mjpg-streamer <br/>
> $ sudo chmod 755 /etc/init.d/mjpg-streamer <br/>
> $ sudo insserv mjpg-streamer<br/>
