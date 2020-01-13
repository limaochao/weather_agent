# coding: utf-8

"""
@Time : 2019-12-27 11:43 
@Author : cuihaipeng
@File : counter_incr.py
@pyVersion: 3.6.8
@desc :
"""


def CounterIncr():
    def increase():  # 定义一个含有自然数算法的生成器,企图使用next来完成不断调用的递增
        n = 0
        while True:
            n = n + 1
            yield n

    it = increase()  # 一定要将生成器转给一个(生成器)对象,才可以完成

    def counter():  # 再定义一个内函数
        return next(it)  # 调用生成器的值,每次调用均自增

    return counter


counter_ = CounterIncr()
