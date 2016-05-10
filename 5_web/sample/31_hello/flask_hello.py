# Flask sample : hello
# http://a2c.bitbucket.org/flask/quickstart.html#id2
# 2016-05-01 K.OHWADA @ FabLab Kannai

from flask import Flask

# Flask start
app = Flask(__name__)

# route index
@app.route('/')
def hello_world():
    return "Hello World!"

# main
if __name__ == '__main__':
    app.run(host="0.0.0.0")
