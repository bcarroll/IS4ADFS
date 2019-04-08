import logging

from sys import path as sys_path, exit as sys_exit
sys_path.append(".")

from flask import Flask, jsonify

from lib.utils import isAdmin
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

##############################################################################
# /config/
@app.route('/config/env')
def env():
    return(config.env())

##############################################################################
# Main entry point
if __name__ == '__main__':
    if not isAdmin():
        errorMessage = "Privelege error: Administrative priveleges required to manage ADFS."
        logging.error(errorMessage)
        raise WindowsError(errorMessage)
        sys_exit(1)
    app.run(debug=True)
