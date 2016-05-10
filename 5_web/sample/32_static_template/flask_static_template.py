# Flask sample : static template
# 2016-05-01 K.OHWADA @ FabLab Kannai

from flask import Flask, render_template

# Flask start
app = Flask(__name__)

# route index
@app.route('/')
def show_index():
    return render_template('index.html')

# main
if __name__ == '__main__':
    app.run(host="0.0.0.0")
