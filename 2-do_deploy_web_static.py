#!/usr/bin/python3
"""fabric script based on `1-pack_web_static.py` that distributes an archive
to your web servers using the function `do_deploy`
"""
from fabric.api import *
from os import path, environ

env.hosts = ['54.236.25.236', '54.173.164.226']
env.user = "ubuntu"

def do_deploy(archive_path):
    """deploy achive files to web servers"""

    file_name = archive_path.split("/")[1]
    new_name = archive_path.split(".")[0].split("/")[1]

    if not path.exists(archive_path):
        return False

    try:
        put(archive_path, "/tmp/")
        run("tar -xzvf /tmp/{} -C /data/web_static/releases/".format(file_name))
        run("mv /data/web_static/releases/{} /data/web_static/releases/{}".format("web_static", new_name))
        run("rm -rf /tmp/{}".format(file_name))
        run("rm -f /data/web_static/current")
        run("ln -s /data/web_static/releases/{} /data/web_static/current".format(new_name))
        print("New version deployed")
        return True
    except Exception:
        return False
