#!/usr/bin/env python3
# coding: utf-8


class Const(object):
    class ConstTypeError(TypeError):
        pass

    class ConstError(PermissionError):
        pass

    class ConstCaseError(ConstTypeError):
        pass

    def __setattr__(self, name, value):
        if name in self.__dict__:  # 判断是否已经被赋值，如果是则报错
            raise self.ConstTypeError("Can't change const.%s" % name)
        if name in self.__dict__.keys():
            raise self.ConstError("Can't rebind const(%s)" % name)
        if not name.isupper():  # 判断所赋值名称是否是全部大写，用来做第一次赋值的格式判断，也可以根据需要改成其他判断条件
            raise self.ConstCaseError('const name "%s" is not all supercase' % name)

        self.__dict__[name] = value

    def __delattr__(self, name):
        if name in self.__dict__:
            raise self.ConstError("Can't unbind const(%s)" % name)
        raise NameError(name)


const = Const()
'''异常状态码'''
const.ERROR_CODE = 0
'''正常状态码'''
const.SUCCESS_CODE = 1
'''更新状态码'''
const.UPDATE_CODE = 2
'''更新状态码push次数'''
const.UPDATE_PUSH_TIME = 4
