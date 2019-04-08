import logging
from lib.PowerShell import psexec
from pprint import pprint

def WindowsVersion():
    """
    :return: Windows Operating System Version
    """
    return( psexec("[environment]::OSVersion.Version")[0] )

def TotalMemory():
    """
    :return:
    Total memory in bytes
    """
    totalMemory = psexec( "(Get-CimInstance -ClassName 'Cim_PhysicalMemory' | Measure-Object -Property Capacity -Sum).Sum")[0]
    return("%s" % totalMemory)
    