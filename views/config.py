from flask import jsonify
import lib.WindowsOS as WindowsOS

def env():
    return jsonify({
            "OSVersion": "%s" % WindowsOS.WindowsVersion(),
            "TotalMemory": "%s" % WindowsOS.TotalMemory()
        })