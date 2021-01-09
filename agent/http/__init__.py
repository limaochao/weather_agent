#!/usr/bin/env python3
# coding: utf-8


from agent.common import gol, agent, constant
from agent.conf.configs import config
from agent.conf.config_read import ServerConf
from agent.conf.config_read import ConfigInit
from agent.http import url_access


def api_agent(http_dict, server_dict):
    # 读取HTTP部分字典

    metric = http_dict.get_http_metric()
    step = http_dict.get_interval()
    tags = http_dict.get_tags('http')

    # 读取SERVER部分字典
    endpoint = server_dict.get_endpoint()
    push_url = server_dict.get_push_url()

    # 调取配置文件URL访问相关部分
    url_info = http_dict.get_url_info()
    # print("url info = ", url_info)

    # 将URL地址以及回显缓存字典key移交URL处理，采集分析结果以及回显
    key = endpoint + metric + tags + "_access_cache"
    result = url_access.access(url_info, key)

    # 读取URL访问结果，并尝试推送
    value = result[0]
    sender = agent.Agent(endpoint, metric, step, value, "GAUGE", tags)
    # 数据有更新，尝试连续推送5次，其他情况只推送一次
    success_count = 0
    range_times = 1
    if value == constant.const.UPDATE_CODE:
        range_times += constant.const.UPDATE_PUSH_TIME
    for _ in range(range_times):
        if sender.push(push_url):
            success_count += 1
    if success_count == 0:
        raise RuntimeError("Failed to send report to Falcon!")


def main():
    gol.init()
    http_list = config.get('http')
    server_zone = config.get('server')
    if http_list is not None and server_zone is not None:
        server_dict = ServerConf(server_zone)
        for http_zone in http_list:
            http_dict = ConfigInit(http_zone)
            api_agent(http_dict, server_dict)


if __name__ == "__main__":
    main()
