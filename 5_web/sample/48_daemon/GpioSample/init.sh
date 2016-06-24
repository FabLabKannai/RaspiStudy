#!/bin/bash
# GPIO init
# 2016-05-01 K.OHWADA @ FabLab Kannai

cp scripts/gpio-sample.init /etc/init.d/gpio-sample
chmod 755 /etc/init.d/gpio-sample
cp scripts/gpio-sample.default /etc/default/gpio-sample
chmod 644 /etc/default/gpio-sample
insserv gpio-sample
systemctl daemon-reload
