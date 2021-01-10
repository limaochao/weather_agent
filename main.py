#!/usr/bin/env python3
'''
Description: 
Author: limaochao
Date: 2020-12-26 18:04:52
LastEditTime: 2021-01-16 16:12:09
'''


from agent.common.agentAlive import pushAgentAlive
from agent.conf.configs import config
from agent.conf import config_read
from agent.http import api_agent
from agent.scheduler.taskScheduler import AgentScheduler
from agent.common import globals
from agent.file import task, init_watchdog
import os

if __name__ == '__main__':
    globals.init()
    tasksc = AgentScheduler()
    server_dict = config_read.ServerConf(config['server'])
    file_list = config['file']
    http_list = config.get('http', {})
    endpoint = server_dict.get_endpoint()
    pushUrl = server_dict.get_push_url()
    # tasksc.add_job(
    #     func=pushAgentAlive, args=[endpoint, str(pushUrl)],
    #     id='agentAlive', trigger='interval',\
    #           seconds=30, replace_existing=True
    # )
    for file_conf in file_list:
        file_dict = config_read.ConfigInit(file_conf)
        filename = file_dict.get_file_path()
        path = file_dict.get("dir_path")
        metric = file_dict.get_file_metric()
        tag = file_dict.get_tags('file')
        attr_list = file_dict.get_attr()
        init_watchdog(
            # 文件或目录监控
            attr_list,
            path,
            endpoint + metric + tag,
            filename=filename
        )
        taskid = (endpoint + metric + tag).replace(',', '')
        interval = file_dict.get_interval() \
            if not file_dict.get_interval else 30
        tasksc.add_job(
            # 添加任务
            func=task,
            kwargs={
                'file_dict': file_dict,
                'server_dict': server_dict
            },
            id=taskid,
            trigger='interval',
            seconds=interval,
            replace_existing=True
        )
        if len(str.strip(file_dict.get_cron())) != 0:
            pass
        else:
            pass
    if http_list:
        for http_conf in http_list:
            http_dict = config_read.ConfigInit(http_conf)
            metric = http_dict.get_http_metric()
            tag = http_dict.get_tags('http')
            taskid = (endpoint + metric + tag).replace(',', '')
            tasksc.add_job(func=api_agent, kwargs={
                'http_dict': http_dict, 'server_dict': server_dict},
                id=taskid, trigger='interval', seconds=int(
                    http_dict.get_interval()
            ), replace_existing=True)
        # Daemonize(tasksc.start).start()
    os.system('echo {} > agent.pid'.format(os.getpid()))

    # print(tasksc.get_jobs())
    tasksc.start()
