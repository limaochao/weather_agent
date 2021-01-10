#!/usr/bin/env python3
'''
Description: 
Author: limaochao
Date: 2020-12-27 14:42:25
LastEditTime: 2021-01-09 16:48:25
'''


import threading
from agent.common import globals, agent
from agent.common.constant import const
from agent.file.monitor.file_num_size import file_num_large_size
from agent.file.monitor.is_created import is_created, on_created
from agent.file.monitor.is_modify import on_modified, is_modified
from agent.common.enums.file_attr_enum import FileAttr


def task(file_dict, server_dict):
    """任务调度"""
    endpoint = server_dict.get_endpoint()
    # push_url = server_dict.get_push_url()
    metric = file_dict.get_file_metric()
    step = file_dict.get_interval()
    tag = file_dict.get_tags('file')
    service_name = endpoint + metric + tag
    update_time_info = globals.get_value("update_times" + service_name)
    is_push_update_continue = file_dict.get_is_push_update_continue()
    if update_time_info is not None and update_time_info != 0:
        code = const.UPDATE_CODE
        globals.set_value("update_times" + service_name, update_time_info - 1)
    else:
        """业务逻辑判断"""
        file_attr_list = file_dict.get_attr()
        result = []
        for file_attr in file_attr_list:
            key = file_attr.get('key')
            if key == FileAttr.IS_EXIST.value:
                pass
            if key == FileAttr.IS_CREATED.value:
                result.append(is_created(service_name))
            if key == FileAttr.IS_DELETED.value:
                pass
            if key == FileAttr.IS_MOVED.value:
                pass
            if key == FileAttr.IS_MODIFIED.value:
                result.append(is_modified(service_name))
            if key == FileAttr.FILE_SIZE.value:
                pass
            if key == FileAttr.FILE_NUM.value:
                pass
            if key == FileAttr.FILE_NUM_LARGE_SIZE.value:
                result.append(file_num_large_size(
                    file_dict.get_file_path(), file_attr))
            if key == FileAttr.IS_TIMEOUT.value:
                pass
        code = integration_result(result)
        if code == const.UPDATE_CODE and is_push_update_continue == 'True':
            globals.set_value(
                "update_times" + service_name, const.UPDATE_PUSH_TIME)
    # agent.Agent(
    #     endpoint, metric, step, code, "GAUGE", tag).push(push_url)
    producer = agent.Producer(endpoint, metric, step, code, "GAUGE", tag)
    producer.produce()


def init_watchdog(attr_list, path, service_name):
    """初始化watchdog"""
    for attr in attr_list:
        if attr.get('key') == FileAttr.IS_CREATED.value:
            '''created'''
            threading.Thread(target=on_created, args=(
                path, service_name), daemon=True).start()
        elif attr.get('key') == FileAttr.IS_DELETED.value:
            '''deleted'''
            pass
        elif attr.get('key') == FileAttr.IS_MOVED.value:
            '''moved'''
            pass
        elif attr.get('key') == FileAttr.IS_MODIFIED.value:
            '''modified'''
            threading.Thread(target=on_modified, args=(
                path, service_name), daemon=True).start()


def integration_result(result):
    """
    聚合校验结果list列表，返回唯一值
    result 校验结果list列表
    """
    if const.ERROR_CODE in result:
        return const.ERROR_CODE
    elif const.UPDATE_CODE in result:
        return const.UPDATE_CODE
    else:
        return const.SUCCESS_CODE
