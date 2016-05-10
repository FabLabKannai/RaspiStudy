#!/usr/bin/env python
# LED run
# 2016-05-01 K.OHWADA @ FabLab Kannai

import os
import sys

basedir = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.join(basedir))

import led-sample
led-sample.main()
