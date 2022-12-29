#!/user/bin/python3
"""
fabric script based on `2-do_deploy_web_Static.py` that creates an
achive to your web servesrs using the function `deploy`
"""

from fabric.api import *
from os import path
from datetime import datetime

env.hosts = ['54.236.25.236', '54.173.164.226']
env.user = "ubuntu"


def deploy():
    """deploy static files in web_static dir to webservers"""
    archive_path = do_pack()
    if archive_path is not None:
        return_val = do_deploy(archive_path)
        return return_val
    else:
        return False


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


def do_deploy(archive_path):
    """deploy achive files to web servers"""

    file_name = archive_path.split("/")[1]
    f_path = "/data/web_static/releases/"
    new_name = archive_path.split(".")[0].split("/")[1]
    new_name = "/data/web_static/releases/{}".format(new_name)

    if not path.exists(archive_path):
        return False

    try:
        put(archive_path, "/tmp/")
        run("tar -xzvf /tmp/{} -C {}".format(file_name, f_path))
        run("mv {}{} {}".format(f_path, "web_static", new_name))
        run("rm -rf /tmp/{}".format(file_name))
        run("rm -f /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(new_name))
        print("New version deployed")
        return True
    except Exception:
        return False
