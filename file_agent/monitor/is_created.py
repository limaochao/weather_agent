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


def is_created_in_time(data_update_interval, service_name):
    """单位时间内是否有文件新建"""
    last_modify = gol.get_value("create" + service_name)
    if last_modify is None:
        gol.set_value("create" + service_name, time.time())
        code = const.SUCCESS_CODE
    elif (int(last_modify) + int(data_update_interval)) <= time.time():
        code = const.ERROR_CODE
    else:
        code = const.SUCCESS_CODE
    return code


def is_created(service_name):
    """预警是否新建"""
    last_modify = gol.get_value("create" + service_name)
    before_last_modify = gol.get_value("create_before" + service_name)
    now_time = time.time()
    if last_modify is None:
        gol.set_value("create" + service_name, now_time)
        last_modify = now_time
    if before_last_modify is None:
        gol.set_value("create_before" + service_name, gol.get_value("create" + service_name))
        before_last_modify = now_time
    if last_modify > before_last_modify:
        code = const.UPDATE_CODE
        gol.set_value("create_before" + service_name, gol.get_value("create" + service_name))
    else:
        code = const.SUCCESS_CODE
    return code


def on_created(path, service_name):
    """watchdog监控是否有文件新建"""
    observer = Observer()
    event_handler = OnCreated("create" + service_name)
    observer.schedule(event_handler, path, recursive=True)
    try:
        observer.start()
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
