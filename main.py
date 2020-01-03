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

# if __name__ == '__main__':
#     def job2(para1, para2, para3):
#         print("This is job2")
#         print("The para1 is " + str(para1))
#         print("The para2 is " + str(para2))
#         print("The para2 is " + str(para2))
#
#
#     _dict = {'para1': 3, 'para2': '2', 'para3': '1'}
#     task = agentScheduler()
#     task.add_job(job2,kwargs=_dict,id='taskff', trigger='interval',seconds=2, replace_existing=True)
#     task.start()



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
        print(file_conf)
        if len(str.strip(file_conf.get('polling').get('one').get('interval'))) != 0:
            tasksc.add_job(func = task,kwargs={'file_conf':file_conf},
                           id='taskff', trigger='interval',seconds=int(rule), replace_existing=True)
            
        elif len(str.strip(file_conf['polling'].get('two').get('cron'))) != 0:
            pass
        else:
            pass
    
    tasksc.start()


