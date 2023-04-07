#!/usr/bin/python3
''' This module compresses files on web_static folder to .tgz archive'''
from fabric.api import local
from datetime import datetime
import os


def do_pack():
    ''' generates .tgz archive '''
    mydate = datetime.now()
    my_date2 = mydate.strftime("%Y%m%d%H%M%S")
    local("mkdir -p versions")
    path = "versions/web_static_{}.tgz".format(my_date2)
    local("tar -cvzf {} web_static".format(path))
    if os.path.exists(path):
        return path
    return None
