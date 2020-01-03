# coding: utf-8

"""
@Time : 2019-12-30 9:42 
@Author : cuihaipeng
@File : is_modify.py
@pyVersion: 3.6.8
@desc : 是否更新
"""

import time
from common import gol
from watchdog.observers import Observer
from common.constant import const
from file_agent.funcs.watchdog_monitor import OnModified


def is_modify(file_conf, service_name):
    last_modify = gol.get_value("modified" + service_name)
    if last_modify is None:
        gol.set_value("modified" + service_name, time.time())
        code = const.SUCCESS_CODE
    elif (last_modify + int(file_conf['polling']['one']['data_update_interval'])) < time.time():
        code = const.ERROR_CODE
    else:
        code = const.SUCCESS_CODE
    return code


def on_modified(path, service_name):
    """watchdog监控文件是否修改"""
    observer = Observer()
    event_handler = OnModified("modified" + service_name)
    observer.schedule(event_handler, path, recursive=False)
    try:
        observer.start()
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

# def on_modify(file_conf):
#     """单位时间内是否有文件更新"""
#     path = file_conf['dir_path'] + file_conf['file_name']
#     service_name = "modify" + file_conf['server_name'] + file_conf['process_name'] + file_conf['app_name']
#     last_modify = gol.get_value(service_name)
#     if last_modify is None:
#         gol.set_value(service_name, os.path.getmtime(path))
#         code = const.SUCCESS_CODE
#     elif (last_modify + int(file_conf['polling']['one']['data_update_interval'])) < time.time():
#         code = const.ERROR_CODE
#     else:
#         code = const.SUCCESS_CODE
#     return code
