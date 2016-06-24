#!/usr/bin/python
# Flask sample : Camera
# 2016-06-01 K.OHWADA @ FabLab Kannai

from flask import Flask, render_template, request, send_file
import subprocess
import socket
import datetime
import os

# BASIC Authentication for mjpg-streamer
USER = "pi"
PASSWD = "raspberry"

# wget command
CMD_WGET = "/usr/bin/wget"
DIR_TMP = "/tmp/"
OPT_USER = "--http-user=" + USER
OPT_PASSWD = "--http-passwd=" + PASSWD
PARAM_URL = "http://localhost:8080/?action=snapshot"

# get filename with timestamp
def get_name():
	d = datetime.datetime.today()
	name = "{0}{1:02d}{2:02d}{3:02d}{4:02d}{5:02d}.jpg".format(d.year, d.month, d.day, d.hour, d.minute, d.second)
	return name

# take a picture
def take_picture(name):
	path = DIR_TMP + name
	args = [CMD_WGET, "-O", path, OPT_USER, OPT_PASSWD, PARAM_URL]
	subprocess.check_call(args)

# get myself ip addr
def get_ip_addr():
	# http://qiita.com/kjunichi/items/8e4967d04c3a1f6af35e
	list = [] 
	for s in [socket.socket( socket.AF_INET, socket.SOCK_DGRAM )]:
		s.connect( ('8.8.8.8', 80 ))
		list.append( s.getsockname()[0] )
		s.close()	
	return list[0]

# def end
 
# Flask start	
app = Flask(__name__)
ip_addr = get_ip_addr()
		
# route index
@app.route('/')
def show_index():
	return render_template('index.html', ip_addr=ip_addr)

# route action
@app.route('/action', methods=['POST'])
def action():
	if request.method == 'POST':
		return do_action()
	return ''

# route image
@app.route('/image', methods=['GET'])
def image():
	if request.method == 'GET':
		return do_image()
	return ''

# route download
@app.route("/download", methods=['GET'])
def download():
	if request.method == 'GET':
		return do_download()
	return ''

# do action
def do_action():
	take = int(request.form['take'])
	if take == 1:
		# return json, if valid param
		name = get_name()
		take_picture(name)
		json = '{"name":"' + name + '"}'
		return json
	return ''

# do image
def do_image():	
	path = get_path()
	if path:
		# return image file, if path exists
		return send_file(path, mimetype='image/jpeg')
	return ''

# do download
def do_download():
	path = get_path()
	if path:
		# return download file, if path exists	
		return send_file(path, as_attachment=True)
	return ''

# get path
def get_path():
	name = request.args.get('name','')
	if name:
		# if valid param
		path = DIR_TMP + name
		if os.path.exists(path):
			# return path, if path exists	
			return path
	return ''

# Flask end

# main
if __name__ == '__main__':
    app.run(host="0.0.0.0")
