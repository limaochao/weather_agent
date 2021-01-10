# coding: utf-8
'''
Description: 
Author: limaochao
Date: 2020-12-27 20:09:15
LastEditTime: 2021-01-09 15:16:36
'''

import time

from agent.common import globals
from watchdog.observers import Observer

from agent.common.constant import const
from agent.file.funcs.watchdog_monitor import OnCreated


def is_created_in_time(data_update_interval, service_name):
    """单位时间内是否有文件新建"""
    last_modify = globals.get_value("create" + service_name)
    if last_modify is None:
        globals.set_value("create" + service_name, time.time())
        code = const.SUCCESS_CODE
    elif (int(last_modify) + int(data_update_interval)) <= time.time():
        code = const.ERROR_CODE
    else:
        code = const.SUCCESS_CODE
    return code


def is_created(service_name):
    """预警是否新建"""
    last_modify = globals.get_value("create" + service_name)
    before_last_modify = globals.get_value("create_before" + service_name)
    now_time = time.time()
    if last_modify is None:
        globals.set_value("create" + service_name, now_time)
        last_modify = now_time
    if before_last_modify is None:
        globals.set_value(
            "create_before" + service_name,
            globals.get_value("create" + service_name)
        )
        before_last_modify = now_time
    if last_modify > before_last_modify:
        code = const.UPDATE_CODE
        globals.set_value(
            "create_before" + service_name,
            globals.get_value("create" + service_name)
        )
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
