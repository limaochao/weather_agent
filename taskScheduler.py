# -*- coding: utf-8 -*-
"""
@Author : hejian
@File   : taskScheduler.py
@Project: agent
@Time   : 2019-12-27 14:37:43
@Desc   : Agent task scheduler
@Version: v1.0
"""

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.jobstores.memory import MemoryJobStore
from apscheduler.executors.pool import ThreadPoolExecutor,ProcessPoolExecutor


class agentScheduler(BlockingScheduler):
    def __init__(self):
        super(agentScheduler,self).__init__(jobstores = {'default': MemoryJobStore(),},
                                            job_defaults = {'coalesce': False,'max_instances': 10},
                                            executors={'default': ThreadPoolExecutor(10),
                                                       'processpool': ProcessPoolExecutor(1),
                                            }
                                            )
