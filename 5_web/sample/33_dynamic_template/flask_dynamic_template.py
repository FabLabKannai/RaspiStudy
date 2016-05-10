# Flask sample : dynamic template
# 2016-05-01 K.OHWADA @ FabLab Kannai

from flask import Flask, render_template

# Flask start
app = Flask(__name__)

# route index
@app.route('/')
def show_index(name='World'):
	return render_template('index.html', name=name)

# route name
# get parameter from URL, and set variable in template 
@app.route('/<name>')
def show_name(name):
	return show_index(name)

# main
if __name__ == '__main__':
    app.run(host="0.0.0.0")
