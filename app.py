from sys import path as sys_path
sys_path.append(".")

from flask import Flask, jsonify

from lib.WindowsOS import WindowsVersion
from views import config

VERSION = '0.0.1'
app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({
            "name": "ADFS Integration Service", 
            "version": "%s" % (VERSION)
        })

@app.route('/config/env')
def env():
    #return jsonify({"OSVersion": "%s" % WindowsVersion()})
    return(config.env())

if __name__ == '__main__':
    app.run(debug=True)