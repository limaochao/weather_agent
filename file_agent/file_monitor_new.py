# coding: utf-8

"""
@Time : 2020-01-02 17:39 
@Author : cuihaipeng
@File : file_monitor_new.py
@pyVersion: 3.6.8
@desc :
"""

import json
import threading

from common.constant import const
from conf.configs import config
from file_agent.agent_push import AgentPush, push
from file_agent.myenum.file_attr_enum import FileAttr
from file_agent.monitor.file_num_size import file_num_large_size
from file_agent.monitor.is_created import on_created, is_created
from file_agent.monitor.is_modify import on_modified, is_modify


def task(file_conf):
    """任务调度"""
    endpoint = config.get('server').get('ip')
    metric = metric_append(file_conf)
    tag = tag_append(file_conf)
    service_name = endpoint + metric + tag
    service_logic(file_conf, service_name)


def service_logic(file_conf, service_name):
    """业务逻辑判断"""
    # payload_list = []
    file_attr_list = file_conf.get('attr')
    result = []
    for file_attr in file_attr_list:
        key = file_attr.get('key')
        if key == FileAttr.IS_EXIST.value:
            pass
        if key == FileAttr.IS_CREATED.value:
            result.append(is_created(file_conf, service_name))
        if key == FileAttr.IS_DELETED.value:
            pass
        if key == FileAttr.IS_MOVED.value:
            pass
        if key == FileAttr.IS_MODIFIED.value:
            result.append(is_modify(file_conf, service_name))
        if key == FileAttr.FILE_SIZE.value:
            pass
        if key == FileAttr.FILE_NUM.value:
            pass
        if key == FileAttr.FILE_NUM_LARGE_SIZE.value:
            result.append(file_num_large_size(file_conf, file_attr))
        if key == FileAttr.IS_TIMEOUT.value:
            pass
    code = integration_result(result)
    payload_push = payload(file_conf, code)
    print(json.dumps(payload_push))
    # payload_list.extend(payload(file_conf, code))
    # print(json.dumps(payload_list))
    # TODO open falcon push
    push(config.get('server').get('push_url'), payload_push)


def init_watchdog(attr_list, path, service_name):
    """初始化watchdog"""
    for attr in attr_list:
        if attr.get('key') == FileAttr.IS_CREATED.value:
            '''created'''
            threading.Thread(target=on_created, args=(path, service_name), daemon=True).start()
        elif attr.get('key') == FileAttr.IS_DELETED.value:
            '''deleted'''
            pass
        elif attr.get('key') == FileAttr.IS_MOVED.value:
            '''moved'''
            pass
        elif attr.get('key') == FileAttr.IS_MODIFIED.value:
            '''modified'''
            threading.Thread(target=on_modified, args=(path, service_name), daemon=True).start()


def payload(file_conf, code):
    """
    拼接payload
    param:  file_conf 当前文件配置
            attr：文件属性，即校验规则
            code：检验结果
    """
    endpoint = config.get('server').get('ip')
    metric = metric_append(file_conf)
    step = int(file_conf['polling']['one']['interval'])
    tag = tag_append(file_conf)
    _push = AgentPush(endpoint, metric, step, code, 'GAUGE', tag)
    return _push.payload_push()


def metric_append(file_conf):
    attr_list = []
    for file_attr in file_conf.get('attr'):
        attr_list.append(file_attr.get('key'))
    return 'file-' + file_conf.get('dataType') + '-' + file_conf.get('subDataType') + '-' + '&'.join(attr_list)


def tag_append(file_conf):
    return 'department=' + file_conf['department'] + ',branch=' + file_conf['branch'] + ',type=file,dataType=' + \
           file_conf['dataType'] + ',id=' + file_conf['id'] + ',pid=' + file_conf['pid'] + ',is_finish=' + file_conf[
               'is_finish'] + ',leader=' + file_conf['leader'] + ',subDataType=' + file_conf[
               'subDataType'] + ',project=' + file_conf['project'] + ',deputy=' + file_conf['deputy'] + ',source=' + \
           file_conf['dir_path'] + file_conf['file_name']


def integration_result(result):
    """
    聚合校验结果list列表，返回唯一值
    result 校验结果list列表
    """
    for i in result:
        if i == const.ERROR_CODE:
            return const.ERROR_CODE
    return const.SUCCESS_CODE
