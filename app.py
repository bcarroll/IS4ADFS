from os.path import abspath as osPathAbspath, dirname as osPathDirname, join as osPathJoin
pwd = osPathAbspath(osPathDirname(__file__))

##############################################################################
# Logging
import logging
import logging.config
logging_config_file = osPathAbspath(osPathJoin(pwd, 'logging.ini'))
print(logging_config_file)
logging.config.fileConfig(fname=logging_config_file, disable_existing_loggers=False)
logger = logging.getLogger('is4adfs')
##############################################################################

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
        errorMessage = "Elevation required (Run as Administrator)"
        logging.error(errorMessage)
        raise WindowsError(errorMessage)
        sys_exit(1)
    app.run(debug=True)
