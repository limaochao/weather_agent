# coding: utf-8

"""
@Time : 2019-12-27 10:44 
@Author : cuihaipeng
@File : file_num_size.py
@pyVersion: 3.6.8
@desc : 大于size的文件数量
"""

import os

from agent.common.constant import const
from agent.file.funcs.counter_incr import counter_


def file_num_large_size(file_conf, file_attr):
    """判断文件大于size的文件数量,忽略子目录"""
    path = file_conf['dir_path']
    file_list = os.listdir(path)  # 获取path目录下所有文件
    num = 0
    for file_name in file_list:
        path_tmp = os.path.join(path, file_name)  # 获取path与filename组合后的路径
        if os.path.isfile(path_tmp):  # 判断是否为文件
            file_size = os.path.getsize(path_tmp)  # 如果是文件，则获取相应文件的大小
            if file_size > int(file_attr['size']):
                num = counter_()
    if num > int(file_attr['num']):
        return const.SUCCESS_CODE
    else:
        return const.ERROR_CODE
