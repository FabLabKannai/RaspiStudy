# Flask sample : JQuery
# 2016-05-01 K.OHWADA @ FabLab Kannai

from flask import Flask, render_template, request
import os
import json

# Flask start
app = Flask(__name__)

# route index
@app.route('/')
def show_index():
	return render_template('index.html')

# route action with get and post
@app.route('/action', methods=['GET', 'POST'])
def action():
    if request.method == 'POST':
        do_post()
        return ''
    else:
        return do_get()

# do get method
# read person.json, and return text
def do_get():
	json_data = read_file();
	encode_data = json.loads(json_data)
	data = 'My name is ' + encode_data['name'] + '.<br/>'
	data += 'I am ' + encode_data['age'] + '.<br/>'
	return data

# do post method
# get parameters, and write person.json
def do_post():
	dict = {}
	dict['name'] = request.form['name']
	dict['age'] = request.form['age']
	data = json.dumps(dict)
	wite_file(data)

# read_file
def read_file():
	f = open(get_filename(), 'r')
	data = f.read()
	f.close()
	print 'read: ' + data
	return data

# wite_file
def wite_file(data):
	print 'write: ' + data
	f = open(get_filename(), 'w')
	f.write(data)
	f.close()

# get_filename
def get_filename():
	name = os.path.join(os.path.dirname(__file__), 'data/person.json')
	return name

# main
if __name__ == '__main__':
    app.run(host="0.0.0.0")
