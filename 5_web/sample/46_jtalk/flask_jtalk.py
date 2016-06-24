#!/usr/bin/python
# Flask sample : Open JTalk
# 2016-06-01 K.OHWADA @ FabLab Kannai

from flask import Flask, render_template, request
import subprocess
import codecs
	
CMD_JTALK = "/usr/bin/open_jtalk"
CMD_APLAY = "/usr/bin/aplay"

FILE_TEXT = "/tmp/jtalk.txt"
FILE_WAVE = "/tmp/jtalk.wav"

OPT_M = "/usr/share/hts-voice/mei/mei_normal.htsvoice"
OPT_X = "/var/lib/mecab/dic/open-jtalk/naist-jdic"

# create & play voice file using jtalk
def jtalk(text):
	f = codecs.open(FILE_TEXT, "w", "utf-8")
	f.write(text)
	f.close()	
	jtalk_args = [CMD_JTALK, "-m", OPT_M, "-x", OPT_X, "-ow", FILE_WAVE, FILE_TEXT]
	subprocess.check_call(jtalk_args)
	aplay_args = [CMD_APLAY, "--quiet", FILE_WAVE]
	subprocess.check_call(aplay_args)

# jtalk end
 
# Flask start	
app = Flask(__name__)

# route index
@app.route('/')
def show_index():
	return render_template('index.html')

# route action with post
@app.route('/action', methods=['POST'])
def action():
	if request.method == 'POST':
		do_post()
	return ''

# do post method
def do_post():
	speech = request.form['speech']
	if speech:
		# jtalk if valid param
		jtalk(speech)

# Flask end

# main
if __name__ == '__main__':
    app.run(host="0.0.0.0")
