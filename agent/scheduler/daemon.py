#!/usr/bin/env python3
'''
Description: 
Author: limaochao
Date: 2020-12-27 10:41:28
LastEditTime: 2020-12-27 14:43:55
'''
import os
import sys


class Daemonize:
    def __init__(self, target=None, args=()):
        self.func = target
        self.args = args
        self.filepid = 'agent.pid'

    def start(self):
        try:
            pid = os.fork()
            if pid > 0:
                sys.exit(0)

        except OSError as e:
            sys.stderr.write(e)
            sys.exit(1)
        else:

            # 挂载需要访问的目录
            # os.chdir("/opt/script")
            os.getcwd()
            os.umask(0o022)
            os.setsid()

        try:
            pid = os.fork()
            if pid > 0:
                sys.exit(0)
        except OSError as e:
            sys.stderr.write(e)
            sys.exit(1)
        else:
            os.system('echo {} > {}'.format(os.getpid(), self.filepid))
            self.func(*self.args)
