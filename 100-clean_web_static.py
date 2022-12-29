#!/usr/bin/python3
"""
fabric script based on `3-deploy_web_static.py` that deletes
out of date achive using the `do_clean`
"""
from fabric.api import *
from os import listdir

env.hosts = ['54.236.25.236', '54.173.164.226']
env.user = "ubuntu"

def do_clean(number=0):
    """delete out of date achive"""


    versions = listdir("versions")
    ver = []
    for i in versions:
        ver.append(int(i.split("_")[2].split(".")[0]))
    ver.sort(reverse=True)

    print(ver)
    
    if number == 0 or number == 1:
        del ver[0]
    else:
        for i in range(int(number)):
            del ver[0]
    for i in ver:
        file_loc = "versions/web_static_{}.tgz".format(i)
        file_rem = "/data/web_static/releases/web_satic_{}".format(i)
        local("rm -f {}".format(file_loc))
        run("rm -f {}".format(file_rem))

