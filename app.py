from flask import Flask
import os
app = Flask(__name__)


@app.route('/')
def index():
   return os.uname()[1]

@app.route('/info')
def info():
   return str(os.uname())



if __name__ == '__main__':
   
   app.run(host='0.0.0.0')
