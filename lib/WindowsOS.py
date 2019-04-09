import logging
from flask import jsonify
from lib.PowerShell import psexec
from pprint import pprint
import win32evtlog

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

def EventLog(server="localhost", logtype="System", eventtype=None, source=None):
    handle = win32evtlog.OpenEventLog(server, logtype)
    flags  = win32evtlog.EVENTLOG_BACKWARDS_READ|win32evtlog.EVENTLOG_SEQUENTIAL_READ
    total  = win32evtlog.GetNumberOfEventLogRecords(handle)
    events = win32evtlog.ReadEventLog(handle, flags,0)
    eventData = []
    def eventVar(event):
        return ({"Category": event.EventCategory,
                    "Timestamp": event.TimeGenerated,
                    "Source": event.SourceName,
                    "EventID": event.EventID,
                    "EventType": event.EventType,
                    "Data": event.StringInserts
                })
    if events:
        for event in events:
            if eventtype is not None and eventtype == event.EventType and source is not None and source == event.SourceName:
                eventData.append(eventVar(event))
            elif eventtype is not None and eventtype == event.EventType and source is None:
                eventData.append(eventVar(event))
            elif source is not None and source == event.SourceName:
                eventData.append(eventVar(event))
            elif eventtype is None:
                eventData.append(eventVar(event))
    return jsonify(eventData)
