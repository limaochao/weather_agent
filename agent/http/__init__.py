# coding: utf-8

"""
@Time : 2020-01-10 17:10 
@Author : cuihaipeng
@File : __init__.py.py
@pyVersion: 3.6.8
@desc :
"""

from agent.common import gol, agent_push, constant
from agent.conf.configs import config
from agent.conf import config_read
from agent.http import url_access


def api_agent(http_dict, server_dict):
    # 读取HTTP部分字典

    http_zone = config_read.ConfigInit(http_dict)
    metric = http_zone.get_http_metric()
    step = http_zone.get_step()
    tags = http_zone.get_http_tag()

    # 读取SERVER部分字典
    server_zone = config_read.ServerConf(server_dict)
    endpoint = server_zone.get_endpoint()
    push_url = server_zone.get_push_url()

    # 调取配置文件URL访问相关部分
    url_info = http_zone.get_url_info()
    # print("url info = ", url_info)

    # 将URL地址以及回显缓存字典key移交URL处理，采集分析结果以及回显
    key = endpoint + metric + tags + "_access_cache"
    result = url_access.access(url_info, key)

    # 读取URL访问结果，并尝试推送
    value = result[0]
    sender = agent_push.AgentPush(endpoint, metric, step, value, "GAUGE", tags)
    # 数据有更新，尝试连续推送5次，其他情况只推送一次
    if value == constant.const.UPDATE_CODE:
        for _ in constant.const.UPDATE_PUSH_TIME:
            sender.push(push_url)
    sender.push(push_url)


def main():
    gol.init()
    http_list = config.get('http')
    server_dict = config.get('server')
    for http_dict in http_list:
        api_agent(http_dict, server_dict)


if __name__ == "__main__":
    main()
