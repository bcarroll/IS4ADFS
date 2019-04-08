import logging
logging.basicConfig(level=logging.DEBUG)

# Import required .NET Assemblies
import clr
clr.AddReference('System.Security.Principal')
from System.Security.Principal import WindowsIdentity, WindowsPrincipal, WindowsBuiltInRole


def isAdmin():
    """ Determine if the user executing this script has Admin rights """
    wi = WindowsIdentity.GetCurrent()
    wp = WindowsPrincipal(wi)
    if wp.IsInRole(WindowsBuiltInRole.Administrator):
        return True
    else:
        return False

print( isAdmin() )

