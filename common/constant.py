# coding: utf-8

"""
@Time : 2019-12-25 9:21 
@Author : cuihaipeng
@File : constant.py
@pyVersion: 3.6.8
@desc : 常量类
"""


class Const(object):
    class ConstError(TypeError):
        pass

    class ConstCaseError(ConstError):
        pass

    def __setattr__(self, name, value):
        if name in self.__dict__:  # 判断是否已经被赋值，如果是则报错
            raise self.ConstError("Can't change const.%s" % name)
        if not name.isupper():  # 判断所赋值名称是否是全部大写，用来做第一次赋值的格式判断，也可以根据需要改成其他判断条件
            raise self.ConstCaseError('const name "%s" is not all supercase' % name)

        self.__dict__[name] = value


const = Const()
'''异常状态码'''
const.ERROR_CODE = 0
'''正常状态码'''
const.SUCCESS_CODE = 1
'''更新状态码'''
const.UPDATE_CODE = 2
'''更新状态码push次数'''
const.UPDATE_PUSH_TIME = 5
'''更新状态码push间隔'''
const.UPDATE_PUSH_INTERVAL = 10
