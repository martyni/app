from flask import Flask
import os
application = Flask(__name__)


@application.route('/')
def index():
   return os.uname()[1]

@application.route('/info')
def info():
   return str(os.uname())



if __name__ == '__main__':
   
   applicationrun(host='0.0.0.0')
