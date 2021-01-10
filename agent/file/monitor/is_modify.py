# coding: utf-8
'''
Description: 
Author: limaochao
Date: 2020-12-27 14:40:40
LastEditTime: 2021-01-09 15:10:36
'''

import time
from agent.common import globals
from watchdog.observers import Observer

from agent.common.constant import const
from agent.file.funcs.watchdog_monitor import OnModified


def is_modified_in_time(data_update_interval, service_name):
    """单位时间内是否有文件更新"""
    last_modify = globals.get_value("modified" + service_name)
    if last_modify is None:
        globals.set_value("modified" + service_name, time.time())
        code = const.SUCCESS_CODE
    elif (last_modify + int(data_update_interval)) < time.time():
        code = const.ERROR_CODE
    else:
        code = const.SUCCESS_CODE
    return code


def is_modified(service_name):
    """预警是否更新"""
    last_modify = globals.get_value("modified" + service_name)
    before_last_modify = globals.get_value(
        "modified_before" + service_name)
    now_time = time.time()
    if last_modify is None:
        globals.set_value("modified" + service_name, now_time)
        last_modify = now_time
    if before_last_modify is None:
        globals.set_value(
            "modified_before" + service_name,
            globals.get_value("modified" + service_name)
        )
        before_last_modify = now_time
    if last_modify > before_last_modify:
        code = const.UPDATE_CODE
        globals.set_value(
            "modified_before" + service_name,
            globals.get_value("modified" + service_name)
        )
    else:
        code = const.SUCCESS_CODE
    return code


def on_modified(path, service_name):
    """watchdog监控文件是否修改"""
    observer = Observer()
    event_handler = OnModified("modified" + service_name)
    observer.schedule(event_handler, path, recursive=True)
    try:
        observer.start()
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

