# Flask sample : LED Ui
# 2016-05-01 K.OHWADA @ FabLab Kannai

from flask import Flask, render_template, request

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
# get parameter, and print
def do_post():
	c = int(request.form['led'])
	if c == 1:
		print 'LED On'
	else:	
		print 'LED Off'

# main
if __name__ == '__main__':
    app.run(host="0.0.0.0")
