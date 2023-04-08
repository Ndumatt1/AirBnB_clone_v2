#!/usr/bin/python3
''' This module creates and distributes an archive to webservers'''
import os
from fabric.api import *
do_deploy = __import__('2-do_deploy_web_static').do_deploy
do_pack = __import__('1-pack_web_static').do_pack

env.hosts = ['18.207.234.44', '54.144.156.217']
env.user = 'ubuntu'


def deploy():
    ''' Creates and distributes an archive to webservers'''
    path = do_pack()
    if not os.path.exists(path):
        return False
    deploy = do_deploy(path)
    return deploy
