import logging
from lib.PowerShell import psexec
from pprint import pprint

def WindowsVersion():
    return( psexec("[environment]::OSVersion.Version")[0] )

def TotalMemory(format='bytes'):
    totalMemory = psexec( "(Get-CimInstance -ClassName 'Cim_PhysicalMemory' | Measure-Object -Property Capacity -Sum).Sum")[0]
    if format == 'bytes':
        return("%s" % totalMemory)
    elif format == 'kbytes':
        return("%s KB" % totalMemory/1024)