import logging
from sys import path as sys_path
from os.path import join as path_join
from os.path import abspath as abs_path

# Add lib/ARCH to sys.path
extlibdir = abs_path(path_join(__file__, '..', 'ext'))
logging.debug("extlibdir = %s" % extlibdir)
sys_path.append(extlibdir)

# Import required .NET Assemblies
import clr
clr.AddReference('System.Collections')
from System.Collections import ObjectModel
clr.AddReference('System.Management.Automation')
from System.Management.Automation import PowerShell

ps = PowerShell.Create()
def psexec(command):
    return ps.AddScript(command).Invoke()

