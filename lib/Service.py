# Based example code from: https://www.thepythoncorner.com/2018/08/how-to-create-a-windows-service-in-python/
import socket
import win32serviceutil
import servicemanager
import win32event
import win32service
import logging
import threading

class WindowsService(win32serviceutil.ServiceFramework):
    """Base class"""
    _svc_name_ = 'is4adfs'
    _svc_display_name_ = 'Integration Service for Microsoft AD FS'
    _svc_description_ = 'Microsoft AD FS Management Interface'

    @classmethod
    def parse_command_line(cls):
        """ Parse command line """
        win32serviceutil.HandleCommandLine(cls)

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
        socket.setdefaulttimeout(60)

    def SvcStop(self):
        """ Service stop requested """
        logging.info('%s service stop requested' % self._svc_display_name_)
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)

    def SvcDoRun(self):
        """ Service start requested """
        logging.info('%s service start requested' % self._svc_display_name_)
        servicemanager.LogMsg(servicemanager.EVENTLOG_INFORMATION_TYPE, servicemanager.PYS_SERVICE_STARTED, (self._svc_name_, ''))
        self.main()

    def main(self):
        """ Service runtime """
        logging.info('Starting HTTP server')
        pass

if __name__ == '__main__':
    WindowsService.parse_command_line()