# coding: utf-8

"""
@Time : 2019-12-20 11:19 
@Author : cuihaipeng
@File : agent_push.py
@pyVersion: 3.6.8
@desc : open faicon push
"""
import json
import time

import requests


class AgentPush:

    def __init__(self, endpoint, metric, step, value, counterType, tags):
        """
        endpoint: 标明Metric的主体(属主)，比如metric是cpu_idle，那么Endpoint就表示这是哪台机器的cpu_idle
        metric: 最核心的字段，代表这个采集项具体度量的是什么, 比如是cpu_idle呢，还是memory_free, 还是qps
            file-{dataType}-{subDataType}-{attr}
            file：表示文件类型监控
            dataType：同上
            subDataType：同上
            attr：文件相关属性，如文件是否存在（exist），大小（size），修改时间（mtime）
        timestamp: 表示汇报该数据时的unix时间戳，注意是整数，代表的是秒
        step: 表示该数据采集项的汇报周期，这对于后续的配置监控策略很重要，必须明确指定。
        value: 代表该metric在当前时间点的值，float64
        counterType: 只能是COUNTER或者GAUGE二选一，前者表示该数据采集项为计时器类型，后者表示其为原值 (注意大小写)
            GAUGE：即用户上传什么样的值，就原封不动的存储
            COUNTER：指标在存储和展现的时候，会被计算为speed，即（当前值 - 上次值）/ 时间间隔
        tags: 一组逗号分割的键值对, 对metric进一步描述和细化, 可以是空字符串. 比如idc=lg，比如service=xbox等，多个tag之间用逗号分割
            必须：
                department：部门
                branch：支部（组）
                type: { mongo, redis, mysql, interface, webpage, }
                DataType：数据类型
                leader：负责人
                id:唯一标识
                pid：父id
                is_finish:是否最后一步
                source:监控目标源（例：文件路径、url、数据库名称或表名称）
            可选：
                subDataType：子数据类型
                project：项目名称
                deputy：第二负责人
        说明：这7个字段都是必须指定
        """
        self.endpoint = endpoint
        self.metric = metric
        self.step = step
        self.value = value
        self.counterType = counterType
        self.tags = tags

    def payload_push(self):
        payload = [
            {
                "endpoint": self.endpoint,
                "metric": self.metric,
                "timestamp": int(time.time()),
                "step": self.step,
                "value": self.value,
                "counterType": self.counterType,
                "tags": self.tags,
            },
        ]
        return payload


def push(push_url, payload):
    requests.post(push_url, data=json.dumps(payload))
