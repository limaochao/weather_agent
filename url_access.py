# coding:utf-8

import requests

import const_vars
import gol


def access(url_info, key):
    url = url_info[0]
    attrs = url_info[2]
    response_code = url_info[3]
    current_response = requests.get(url).text
    # current_time = int(time.time())
    # print(response_data)

    # 字典为{key: 回显}形式，在此提取上一次执行时的缓存
    previous_response = gol.get_value(key)
    # if previous_data is not None:
    #     previous_time = previous_data[0]
    #     previous_response = previous_data[1]

    # 这一次回显正常
    if response_code in current_response:

        # 上一次缓存为空，且这一次回显正常，写入缓存并设定返回值为“正常”
        if previous_response is None:
            gol.set_value(key, current_response)
            re_val = [const_vars.const.NORMAL_CODE, current_response]

        # 上一次缓存不为空，且这一次回显与上一次缓存内容相同，设定返回值为“正常”，隐含默认条件回显内容正常，缓存中只有正常回显或None
        elif previous_response is not None and previous_response == current_response:
            re_val = [const_vars.const.NORMAL_CODE, current_response]

        # 上一次缓存不为空，且这一次回显与上一次缓存内容相同，写入缓存并设定返回值为“有更新”
        elif previous_response is not None and previous_response != current_response:
            gol.set_value(key, current_response)
            re_val = [const_vars.const.UPDATE_CODE, current_response]

        # 其他情况，逻辑上实际不存在，不做任何操作
        else:
            pass

    # 这一次回显不正常，直接返回错误码，不写缓存
    else:
        re_val = [const_vars.const.ERROR_CODE, current_response]

    return re_val

    # if response_code in current_response:
    #     re_val = [const_vars.const.SUCCESS_CODE, current_response]
    # else:
    #     re_val = [const_vars.const.ERROR_CODE, current_response]

    # print("access result = ", re_val)
    # return re_val

    # github_url = "http://product.weather.com.cn/alarm/grepalarm_cn.php"
    # data = json.dumps({'name': 'test', 'description': 'some test repo'})
    # r = requests.post(github_url, data, auth=('user', '*****'))
    # print(r.json)
    # webdata = requests.get(github_url).text
    # print(webdata)
