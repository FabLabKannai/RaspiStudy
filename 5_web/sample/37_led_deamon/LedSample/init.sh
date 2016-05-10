#!/bin/sh
# LED init
# 2016-05-01 K.OHWADA @ FabLab Kannai

cp scripts/led-sample.init /etc/init.d/led-sample
chmod 755 /etc/init.d/led-sample
cp scripts/led-sample.default /etc/default/led-sample
chmod 644 /etc/default/led-sample
insserv led-sample
