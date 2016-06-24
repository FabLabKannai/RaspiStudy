# mjpg-streamer - raspi 
Script to start mjpg-streamer daemon <br/>

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
> $ mkdir builds
> $ cd builds
> $ svn co https://svn.code.sf.net/p/mjpg-streamer/code/ mjpg-streamer mjpg-streamer <br/>
> $ cd mjpg-streamer <br/>
> $ make <br/>

### Setup service daemon 
Please modify the template file to suit your environment <br/>
And copy the modified file to under directory /etc/init.d/ <br/>

> $ sudo chmod 755 /etc/init.d/mjpg-streamer <br/>
> $ sudo insserv mjpg-streamer <br/>
