# -*- coding: utf-8 -*-
"""
@Author : hejian
@File   : main.py
@Project: weather_agent
@Time   : 2020-01-03 11:08:08
@Desc   : The file is ...
@Version: v1.0
"""

from taskScheduler import agentScheduler
from common import gol
from conf.configs import config
from file_agent.file_monitor_new import task, init_watchdog, metric_append, tag_append
import random

from api_agent import interface_agent, jsonconf_read

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
        rule = file_conf.get('polling').get('one').get('interval')
        taskid = (endpoint + metric + tag).replace(',', '')
        print(taskid)
        if len(str.strip(file_conf.get('polling').get('one').get('interval'))) != 0:
            tasksc.add_job(func=task, kwargs={'file_conf': file_conf},
                           id=taskid, trigger='interval', seconds=int(rule), replace_existing=True)

        elif len(str.strip(file_conf['polling'].get('two').get('cron'))) != 0:
            pass
        else:
            pass

    http_list = config.get('http')
    server_dict = config.get('server')
    push_url = config.get('server').get('push_url')
    for http_dict in http_list:
        http_zone = jsonconf_read.HttpConf(http_dict)
        metric = http_zone.get_metric()
        tag = http_zone.get_tag()
        rule = http_zone.get_interval()
        taskid = (endpoint + metric + tag).replace(',', '')
        print(taskid)
        if len(str.strip(rule)) != 0:
            tasksc.add_job(func=interface_agent.api_agent(), kwargs={'http_dict': http_dict, 'server_dict': server_dict},
                           id=taskid, trigger='interval', seconds=int(rule), replace_existing=True)





    tasksc.start()
