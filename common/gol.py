# coding = utf-8

"""
@author: cuihaipeng
@file: gol.py
@time: 2019/12/19 10:55
@pyVersion: 3.6.8
@desc: 跨所有模块的全局变量字典方法
"""


# 初始化
def init():
    global _global_dict
    _global_dict = {}


def set_value(key, value):
    """ 定义一个全局变量 """
    _global_dict[key] = value


def get_value(key, defValue=None):
    """ 获得一个全局变量,不存在则返回默认值 """
    try:
        return _global_dict[key]
    except KeyError:
        return defValue
