# -*- coding: utf-8 -*-
"""
@Author : hejian
@File   : agentAlive.py
@Project: weather_agent
@Time   : 2020-01-18 15:40:52
@Desc   : The file is ...
@Version: v1.0
"""
import requests
import json
import time

def pushAgentAlive(endpoint,url):
    payload = [
        {
        "metric": "agent.alive",
        "endpoint": str(endpoint),
        "timestamp": int(time.time()),
        "step": 30,
        "value": 1,
        "counterType": "GAUGE",
        "tags":''
    }
        ]
    requests.post(url,data = json.dumps(payload))


# pushAgentAlive(endpoint='220.243.129.4',url='http://220.243.129.168:1988/v1/push')