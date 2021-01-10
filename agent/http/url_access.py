# coding:utf-8
'''
Description: 
Author: limaochao
Date: 2021-01-09 15:13:47
LastEditTime: 2021-01-09 15:13:47
'''

import requests
from requests import RequestException

from agent.common import globals, constant


def access(url_info, key):
    url = url_info[0]
    attrs = url_info[2]
    response_code = url_info[3]

    try:
        current_response = requests.get(url).text

        # 字典为{key: 回显}形式，在此提取上一次执行时的缓存
        previous_response = global_dict.get_value(key)

        # 这一次回显正常
        if response_code in current_response:

            # 上一次缓存为空，且这一次回显正常，写入缓存并设定返回值为“正常”
            if previous_response is None:
                global_dict.set_value(key, current_response)
                re_val = [constant.const.SUCCESS_CODE, current_response]

            # 上一次缓存不为空，且这一次回显与上一次缓存内容相同，设定返回值为“正常”，隐含默认条件回显内容正常，缓存中只有正常回显或None
            elif previous_response is not None and previous_response == current_response:
                re_val = [constant.const.SUCCESS_CODE, current_response]

            # 上一次缓存不为空，且这一次回显与上一次缓存内容相同，写入缓存并设定返回值为“有更新”
            elif previous_response is not None and previous_response != current_response:
                global_dict.set_value(key, current_response)
                re_val = [constant.const.UPDATE_CODE, current_response]

            # 其他情况，逻辑上实际不存在，不做任何操作
            else:
                pass

        # 这一次回显不正常，直接返回错误码，不写缓存
        else:
            re_val = [constant.const.ERROR_CODE, current_response]

        return re_val

    except RequestException:
        re_val = [constant.const.ERROR_CODE, ""]
        return re_val


