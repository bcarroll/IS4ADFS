import logging

# Import required .NET Assemblies
import clr
clr.AddReference('System.Security.Principal')
from System.Security.Principal import WindowsIdentity, WindowsPrincipal, WindowsBuiltInRole

from flask import request

def request_wants_json():
    best = request.accept_mimetypes \
        .best_match(['application/json', 'text/html'])
    return best == 'application/json' and \
        request.accept_mimetypes[best] > \
        request.accept_mimetypes['text/html']

def isAdmin():
    """ Determine if the user executing this script has Admin rights """
    wi = WindowsIdentity.GetCurrent()
    wp = WindowsPrincipal(wi)
    if wp.IsInRole(WindowsBuiltInRole.Administrator):
        logging.debug("isAdmin=True")
        return True
    else:
        return False
        logging.debug("isAdmin=False")

