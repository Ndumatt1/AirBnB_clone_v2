#!/usr/bin/python3
''' This fabric script distributes an archive on webservers'''
import os
from fabric.api import run, local, env, put, task
from datetime import datetime


env.hosts = ['54.144.156.217', '18.207.234.44']
env.user = 'ubuntu'


def do_deploy(archive_path):
    ''' Distributes an archive to webservers'''
    if not os.path.exists(archive_path):
        return False
    try:
        put(archive_path, "/tmp/")
        filename = archive_path.split("/")[-1]
        no_ext = filename.split(".")[0]
        run("mkdir -p /data/web_static/releases/{}/".format(no_ext))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
            .format(filename, no_ext))
        run("rm /tmp/{}".format(filename))
        run("mv /data/web_static/releases/{}/web_static/* \
            /data/web_static/releases/{}/".format(no_ext, no_ext))
        run("rm -rf /data/web_static/releases/{}/web_static".format(no_ext))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
            .format(no_ext))
        return True
    except Exception:
        return False
