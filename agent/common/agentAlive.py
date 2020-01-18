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
    data = {
        "metric": "agent.alive",
        "endpoint": str(endpoint),
        "timestamp": int(time.time()),
        "step": 30,
        "value": 1,
        "counterType": "GAUGE",
        "tags":''
    }
    requests.post(url,data = json.dumps(data))
