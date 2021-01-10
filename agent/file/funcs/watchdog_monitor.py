#!/usr/bin/env python3
# coding = utf-8
'''
Description: 
Author: limaochao
Date: 2020-12-27 20:09:48
LastEditTime: 2021-01-10 11:55:36
'''


import time
from watchdog.events import FileSystemEventHandler
from agent.common import globals


class OnCreated(FileSystemEventHandler):
    """
    Called when a file or directory is created.
    param: service 具体业务名称，不能重复
    """

    def __init__(self, service=None):
        self.service = service

    def on_created(self, event):
        # super(OnCreated, self).on_created(event)
        print(event.src_path)
        globals.set_value(self.service, time.time())
        print(time.time())


class OnModified(FileSystemEventHandler):
    """Called when a file or directory is modified."""

    def __init__(self, service=None):
        self.service = service

    def on_modified(self, event):
        super(OnModified, self).on_modified(event)
        globals.set_value(self.service, time.time())


class OnDeleted(FileSystemEventHandler):
    """Called when a file or directory is deleted."""

    def __init__(self, service=None):
        self.service = service

    def on_deleted(self, event):
        super(OnDeleted, self).on_deleted(event)
        globals.set_value(self.service, time.time())


class OnMoved(FileSystemEventHandler):
    """Called when a file or a directory is moved or renamed."""

    def __init__(self, service=None):
        self.service = service

    def on_moved(self, event):
        super(OnMoved, self).on_moved(event)
        globals.set_value(self.service, time.time())
