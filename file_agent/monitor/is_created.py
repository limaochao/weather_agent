# coding: utf-8

"""
@Time : 2019-12-26 17:51 
@Author : cuihaipeng
@File : is_created.py
@pyVersion: 3.6.8
@desc : 是否新建
"""
import time

from common import gol
from common.constant import const
from file_agent.funcs.watchdog_monitor import OnCreated
from watchdog.observers import Observer


def is_created(file_conf, service_name):
    """单位时间内是否有文件新建"""
    last_modify = gol.get_value("create" + service_name)
    if last_modify is None:
        gol.set_value("create" + service_name, time.time())
        code = const.SUCCESS_CODE
    elif (int(last_modify) + int(file_conf['polling']['one']['data_update_interval'])) < time.time():
        code = const.ERROR_CODE
    else:
        code = const.SUCCESS_CODE
    return code


def on_created(path, service_name):
    """watchdog监控是否有文件新建"""
    observer = Observer()
    event_handler = OnCreated("create" + service_name)
    observer.schedule(event_handler, path, recursive=False)
    try:
        observer.start()
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
