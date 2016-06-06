#!/usr/bin/python
# coding: utf-8
# Python Sample: calendar
# 2016-05-01 K.OHWADA @ FabLab Kannai
# http://ar.aichi-u.ac.jp/python/text.pdf
wday=("sun","mon","tue","wed","thu","fri","sat")
def cal0(n,m):
	# cal0(n,m) は 1 つの月のカレンダーを作成する。
	# n は月の開始日の曜日を表す数字 (0 から 6) であり、
	# 0 は日曜日を意味する。
	# m はその月の日数である。例えば 1 月は m=31 である。
	# 従って 2000 年 1 月のカレンダーは cal0(6,31) で表示される。
	for x in wday: print " ",x,
	print
	for x in range(0, n): print "  ---",
	for x in range(1, m+1):
		print "%5d"%x,
		if (x+n)%7==0 : print
	print
# main	
cal0(6,31)
