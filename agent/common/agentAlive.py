#!/usr/bin/env python3
'''
Description: 
Author: limaochao
Date: 2020-12-27 20:07:17
LastEditTime: 2020-12-27 20:07:35
'''
import requests
import json
import time


def pushAgentAlive(endpoint, url):
    payload = [
        {
            "metric": "agent.alive",
            "endpoint": str(endpoint),
            "timestamp": int(time.time()),
            "step": 30,
            "value": 1,
            "counterType": "GAUGE",
            "tags": ''
        }
    ]
    requests.post(url, data=json.dumps(payload))
