# coding: utf-8

"""
@Time : 2020-01-13 17:38 
@Author : cuihaipeng
@File : __init__.py.py
@pyVersion: 3.6.8
@desc :
"""
import re


class NullValueError(Exception):
    """自定义异常类，继承Exception
        值不能为空
    """

    def __init__(self, key=''):
        self.key = key

    def __str__(self):
        """设置抛出异常的描述信息"""
        return f'{self.key}值不能为空'


class TooLongError(Exception):
    """自定义异常类，继承Exception
            值不能为空
        """

    def __init__(self, length, max_len, key=None):
        self.key = key
        self.length = length
        self.max_len = max_len

    def __str__(self):
        """设置抛出异常的描述信息"""
        return f'你输入的{self.key}长度是{self.length}, 不能超过{self.max_len}个字符'


class MixtureStrError(Exception):
    """自定义异常类，继承Exception
            值不能为空
        """

    def __init__(self, max_str_len, key=None):
        self.key = key
        self.max_str_len = max_str_len

    def __str__(self):
        """设置抛出异常的描述信息"""
        return f'请检查你输入的{self.key}是否正确，请输入{self.max_str_len}位汉字或{self.max_str_len * 2}位字母'


def dict_value_is_empty(_dict, key):
    if len(str(_dict.get(key)).strip()) == 0:
        raise NullValueError(key)
    else:
        return _dict.get(key)


def str_length_valid(value, max_len, key=None):
    if len(value) > max_len:
        raise TooLongError(len(str(value)), max_len, key)
    else:
        return value


# def mixture_length_valid(value, strLength, key=None):
#     pattern = "^[\u4e00-\u9fa5]{1," + str(strLength) + "}$|^[\dA-Za-z]{1," + str(strLength * 2) + "}$"
#     var = re.match(pattern, str(value))
#     if var is None:
#         print(1)
#         raise MixtureStrError(strLength, key)
