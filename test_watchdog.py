# coding: utf-8

"""
@Time : 2020-01-07 9:42 
@Author : cuihaipeng
@File : test_watchdog.py
@pyVersion: 3.6.8
@desc :
"""
from common import gol
from conf.configs import config
from file_agent.file_monitor_new import init_watchdog, metric_append, tag_append
from taskScheduler import agentScheduler

if __name__ == '__main__':
    gol.init()
    tasksc = agentScheduler()
    file_list = config.get('file')
    endpoint = config.get('server').get('ip')
    for file_conf in file_list:
        path = file_conf.get('dir_path') + file_conf.get('file_name')
        metric = metric_append(file_conf)
        tag = tag_append(file_conf)
        init_watchdog(file_conf['attr'], path, endpoint + metric + tag)
