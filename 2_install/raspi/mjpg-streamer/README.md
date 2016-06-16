# mjpg-streamer - raspi 
Script to start mjpg-streamer daemon <br/>

original https://github.com/meinside/rpi-mjpg-streamer <br/>

modified <br/>
add -y (YUYV format) for Buffalo BSW20KM15 <br/>

### Setup
Please modify the template file to suit your environment <br/>
And copy the modified file to under directory /etc/init.d/ <br/>

> $ sudo chmod 755 /etc/init.d/mjpg-streamer <br/>
> $ sudo insserv mjpg-streamer <br/>
