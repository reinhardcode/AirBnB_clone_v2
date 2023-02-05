#!/usr/bin/python3
"""fabric script based on `1-pack_web_static.py` that distributes an archive
to your web servers using the function `do_deploy`
"""
from fabric.api import *
from os import path

env.hosts = ['100.25.110.75', '52.91.149.16']
env.user = "ubuntu"


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
