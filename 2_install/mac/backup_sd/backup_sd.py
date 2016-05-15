#!/usr/bin/env python
# Backup SD card of Raspberry Pi
# 2016-04-10 K.OHWADA @ FabLab Kannai

# usage
# $ sudo python backup_sd.py

import subprocess
import re
import datetime

CMD_MOUNT = "/sbin/mount"
CMD_FDISK = "/usr/sbin/fdisk"
CMD_DD = "/bin/dd"
SPACE = " "

def find_dev():
	print CMD_MOUNT
	ret  =  subprocess.check_output( CMD_MOUNT )
	print ret
# /dev/disk1 on / (hfs, local, journaled)
# devfs on /dev (devfs, local, nobrowse)
# map -hosts on /net (autofs, nosuid, automounted, nobrowse)
# map auto_home on /home (autofs, automounted, nobrowse)
# localhost:/1b2R7FzHbKtDidk48ynnU3 on /Volumes/MobileBackups (mtmfs, nosuid, read-only, nobrowse)
# /dev/disk2s1 on /Volumes/boot (msdos, local, nodev, nosuid, noowners)

	line_dev = None
	lines = ret.split("\n")
	for line in lines:
		m = re.search("boot.*msdos", line)
		if m:
			line_dev = line
			break

	if line_dev is None:
		print "NOT find boot partition"
		exit()	

	m = re.search("/dev/(.*)s1 on", line_dev)
	if m is None:
		print "NOT find boot device"
		exit()

	disk = m.group(1).strip()
	dev = "/dev/" + disk
	print "Finded device " + dev
	print 
	return dev

def find_sector(dev):
	cmd = "%s %s" % (CMD_FDISK, dev)
	print cmd
	ret  =  subprocess.check_output( cmd.split(SPACE) )
	print ret
# Disk: /dev/disk2	geometry: 966/255/63 [15523840 sectors]
# Signature: 0xAA55
#         Starting       Ending
# #: id  cyl  hd sec -  cyl  hd sec [     start -       size]
# ------------------------------------------------------------------------
# 1: 0C    0 130   3 -    8  40  32 [      8192 -     122880] Win95 FAT32L
# 2: 83    0   0   1 -    0   0   1 [    131072 -   10485761] Linux files*
# 3: 00    0   0   0 -    0   0   0 [         0 -          0] unused      
# 4: 00    0   0   0 -    0   0   0 [         0 -          0] unused  

	line_linux = None
	lines = ret.split("\n")
	for line in lines:
		m = re.search("Linux", line)
		if m:
			line_linux = line
			break

	if line_linux is None:
		print "NOT find Linux partition"
		exit()	

	m = re.search("\[(.*)\-(.*)\]", line_linux)
	if m is None:
		print "NOT find start sector"
		exit()

	str_start = m.group(1).strip()
	str_size = m.group(2).strip()
	start = int(str_start)
	size = int(str_size)
	end = start + size
	msg = "Finded end sector: " + str(end) + " = " + str(start) + " + " + str(size)
	print msg
	print 
	return end

def save_sd(dev, end):
	today = datetime.datetime.today()
	date = today.strftime("%Y%m%d%H%M%S")
	of = date + ".img"
	cmd = "%s if=%s of=%s bs=512 count=%d" % (CMD_DD, dev, of, end)
	print cmd
	print "Please wait about 10 min"
	ret  =  subprocess.check_output( cmd.split(SPACE) )
	print ret
# 10616833+0 records in
# 10616833+0 records out
# 5435818496 bytes transferred in 670.993897 secs (8101144 bytes/sec)

#
# main
#
if __name__ == "__main__":	
	dev = find_dev()
	end = find_sector(dev)
	save_sd(dev, end)
