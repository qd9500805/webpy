#coing=utf-8
from flask import Flask
app =Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

#if __name__ == '__name__':
if True:
    app.run(host='0.0.0.0',port=9000)
