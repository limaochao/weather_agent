# coding:utf-8
import json

import jsonconf_read
import url_access
import agent_push
import gol
import const_vars


def api_agent(http_dict, server_dict):
    # 读取HTTP部分字典
    http_zone = jsonconf_read.HttpConf(http_dict)
    metric = http_zone.get_metric()
    step = http_zone.get_step()
    tags = http_zone.get_tag()

    # 读取SERVER部分字典
    server_zone = jsonconf_read.ServerConf(server_dict)
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
    if value == const_vars.const.UPDATE_CODE:
        for _ in (4):
            sender.push(push_url)
    sender.push(push_url)


def main():
    gol.init()
    conf_file = open("./configs.json", "rb")
    conf_dict = json.loads(conf_file.read())
    conf_file.close()
    http_list = conf_dict.get('http')
    server_dict = conf_dict.get('server')
    for http_dict in http_list:
        api_agent(http_dict, server_dict)


if __name__ == "__main__":
    main()
