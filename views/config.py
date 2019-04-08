from flask import jsonify
import lib.WindowsOS as WindowsOS
import lib.ADFS as ADFS
def env():
    return jsonify({
            "OSVersion": "%s" % WindowsOS.WindowsVersion(),
            "TotalMemory": "%s" % WindowsOS.TotalMemory()
        })