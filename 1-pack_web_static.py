#!/usr/bin/python3
"""
fabric script that generates a .tgz achive from the contents of
the `web_static` folder of the AirBnB clone repo using the do_pack function
"""
from fabric.api import *
from datetime import datetime
from os import path


def do_pack():
    """
    generates achive from the web_static folder/dir
    """
    try:
        if not path.exists("versions"):
            local('mkdir versions')
        time_s = datetime.now().strftime("%Y%m%d%H%M%S")
        full_path = "versions/web_static_{}.tgz".format(time_s)
        local('tar -cvzf {} web_static'.format(full_path))
        return full_path
    except Exception:
        return None
