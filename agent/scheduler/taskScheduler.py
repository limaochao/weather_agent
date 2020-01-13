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
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor


class AgentScheduler(BlockingScheduler):
    """
    scheduler = {
        'function':'',    函数名,不能重复
        'args':'',    参数
        'id':'',    任务ID,可以为空
        'replace_existing':'True', 如果任务ID重复是否替换
        'trigger':'date|interval|cron', 触发器方式
        'trigger_args':[],    触发器时间格式
    }

    cron 定时调度格式:
    (int|str) 表示参数既可以是int类型,也可以是str类型
    (datetime | str) 表示参数既可以是datetime类型,也可以是str类型
     year (int|str) – 4-digit year -（表示四位数的年份，如2008年）
    month (int|str) – month (1-12) -（表示取值范围为1-12月）
    day (int|str) – day of the (1-31) -（表示取值范围为1-31日）
    week (int|str) – ISO week (1-53) -（格里历2006年12月31日可以写成2006年-W52-7（扩展形式）或2006W527（紧凑形式））
    day_of_week (int|str) – number or name of weekday (0-6 or mon,tue,wed,thu,fri,sat,sun) - （表示一周中的第几天，既可以用0-6表示也可以用其英语缩写表示）
    hour (int|str) – hour (0-23) - （表示取值范围为0-23时）
    minute (int|str) – minute (0-59) - （表示取值范围为0-59分）
    second (int|str) – second (0-59) - （表示取值范围为0-59秒）
    start_date (datetime|str) – earliest possible date/time to trigger on (inclusive) - （表示开始时间）
    end_date (datetime|str) – latest possible date/time to trigger on (inclusive) - （表示结束时间）
    timezone (datetime.tzinfo|str) – time zone to use for the date/time calculations (defaults to scheduler timezone) -（表示时区取值）

    interval 间隔调度
    weeks (int) – number of weeks to wait
    days (int) – number of days to wait
    hours (int) – number of hours to wait
    minutes (int) – number of minutes to wait
    seconds (int) – number of seconds to wait
    start_date (datetime|str) – starting point for the interval calculation
    end_date (datetime|str) – latest possible date/time to trigger on
    timezone (datetime.tzinfo|str) – time zone to use for the date/time calculations

    date 时间调度
    date (datetime.date) – the date/time to run the job at
    """

    def __init__(self):
        super(AgentScheduler, self).__init__(jobstores={'default': MemoryJobStore(), },
                                             job_defaults={'coalesce': False, 'max_instances': 10},
                                             executors={'default': ThreadPoolExecutor(10),
                                                        'processpool': ProcessPoolExecutor(1),
                                                        }
                                             )
