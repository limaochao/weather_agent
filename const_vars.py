# coding:utf-8


# -*- coding: UTF-8 -*-
# Filename: const.py
# 定义一个常量类实现常量的功能
#
# 该类定义了一个方法__setattr()__，和一个异常ConstError, ConstError类继承
# 自类TypeError. 通过调用类自带的字典__dict__, 判断定义的常量是否包含在字典
# 中。如果字典中包含此变量，将抛出异常，否则，给新创建的常量赋值。
class Const(object):
    class ConstError(PermissionError):
        pass

    def __setattr__(self, name, value):
        if name in self.__dict__.keys():
            raise self.ConstError("Can't rebind const(%s)" % name)
        self.__dict__[name] = value

    def __delattr__(self, name):
        if name in self.__dict__:
            raise self.ConstError("Can't unbind const(%s)" % name)
        raise NameError(name)


const = Const()
const.ERROR_CODE = 0
const.NORMAL_CODE = 1
const.UPDATE_CODE = 2
