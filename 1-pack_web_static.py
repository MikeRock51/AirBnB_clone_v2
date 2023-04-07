#!/usr/bin/python3


from fabric.api import *


def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static
    """
    local("mkdir -p versions")
    path = "versions/web_static_$(date +'%Y%m%d%H%M%S').tgz"
    status = local("tar -cvzf {} ./web_static/".format(path))

    if status.succeeded:
        return path
    else:
        return None
