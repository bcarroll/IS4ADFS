import logging
from lib.PowerShell import psexec
import clr
clr.AddReference('System')
from System import ArgumentOutOfRangeException

def ServiceStatus(name="adfssrv"):
    serviceInfo = "Not Found"
    try:
        serviceInfo = psexec("Get-Service -Name %s")[0] % name
    except ArgumentOutOfRangeException as e:
        logging.error("Service not found on system (%s)" % name)
    return (serviceInfo)