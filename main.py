# -*- coding: utf-8 -*-
"""
@Author : hejian
@File   : main.py
@Project: weather_agent
@Time   : 2020-01-03 11:08:08
@Desc   : The file is ...
@Version: v1.0
"""
from agent.conf import config_read
from agent.conf.configs import config
from agent.scheduler.taskScheduler import AgentScheduler
from agent.common import gol
from agent.file import task, init_watchdog

if __name__ == '__main__':
    gol.init()
    tasksc = AgentScheduler()
    file_list = config.get('file')
    endpoint = config.get('server').get('ip')
    for file_conf in file_list:
        file_dict = config_read.ConfigInit(file_conf)
        path = file_dict.get_file_path()
        metric = file_dict.get_file_metric()
        tag = file_dict.get_file_tag()
        init_watchdog(file_dict.get_attr(), path, endpoint + metric + tag)
        taskid = (endpoint + metric + tag).replace(',', '')
        if len(str.strip(file_dict.get_interval())) != 0:
            tasksc.add_job(func=task, kwargs={'file_conf': file_conf},
                           id=taskid, trigger='interval', seconds=int(file_dict.get_interval()), replace_existing=True)

        elif len(str.strip(file_dict.get_cron())) != 0:
            pass
        else:
            pass
    # Daemonize(tasksc.start).start()

    tasksc.start()
