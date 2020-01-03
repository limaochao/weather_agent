# coding = utf-8

"""
@author: cuihaipeng
@file: watchdog_monitor.py
@time: 2019/12/19 16:55
@pyVersion: 3.6.8
@desc: watchdog监控文件变化
"""
import time
from watchdog.events import FileSystemEventHandler

from common import gol


class OnCreated(FileSystemEventHandler):
    """
    Called when a file or directory is created.
    param: service 具体业务名称，不能重复
    """

    def __init__(self, service=None):
        self.service = service

    def on_created(self, event):
        super(OnCreated, self).on_created(event)
        gol.set_value(self.service, time.time())


class OnModified(FileSystemEventHandler):
    """Called when a file or directory is modified."""

    def __init__(self, service=None):
        self.service = service

    def on_modified(self, event):
        super(OnModified, self).on_modified(event)
        gol.set_value(self.service, time.time())


class OnDeleted(FileSystemEventHandler):
    """Called when a file or directory is deleted."""

    def __init__(self, service=None):
        self.service = service

    def on_deleted(self, event):
        super(OnDeleted, self).on_deleted(event)
        gol.set_value(self.service, time.time())


class OnMoved(FileSystemEventHandler):
    """Called when a file or a directory is moved or renamed."""

    def __init__(self, service=None):
        self.service = service

    def on_moved(self, event):
        super(OnMoved, self).on_moved(event)
        gol.set_value(self.service, time.time())
