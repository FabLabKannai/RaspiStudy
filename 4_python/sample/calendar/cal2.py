#!/usr/bin/python
# Python Sample: calendar
# 2016-05-01 K.OHWADA @ FabLab Kannai
import datetime
import calendar
today = datetime.date.today()
print calendar.month(today.year, today.month)
