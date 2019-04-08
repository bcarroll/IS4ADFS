import logging
from lib.PowerShell import psexec
import clr
clr.AddReference('System')
from System import ArgumentOutOfRangeException
from psutil import win_service_get

def ServiceStatus(name="adfssrv"):
    serviceInfo = "Not Found"
    try:
        serviceInfo = win_service_get(name)
        serviceInfo = serviceInfo.as_dict()
    except Exception as e:
        logging.error("Service not found (%s)" % str(name))
    return (serviceInfo)