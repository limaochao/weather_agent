# coding: utf-8
'''
Description: 
Author: limaochao
Date: 2020-12-27 20:10:32
LastEditTime: 2020-12-27 20:10:33
'''


from enum import Enum, unique
@unique
class FileAttr(Enum):
    """
        IS_EXIST:文件是否存在,
        IS_CREATED:是否新建,
        IS_DELETED:是否删除,
        IS_MOVED:是否移动或改名,
        IS_MODIFIED:文件或文件夹是否更新,
        FILE_SIZE:文件大小是否正常(需填写文件大小),bytes
        FILE_NUM :文件数量是否正常(需填写文件数量),
        FILE_NUM_LARGE_SIZE:文件夹下文件大小大于n的文件数量是否正常,(需填写文件大小和文件数量)
        IS_TIMEOUT:文件是否超时,
    """
    IS_EXIST = '0'
    IS_CREATED = '1'
    IS_DELETED = '2'
    IS_MOVED = '3'
    IS_MODIFIED = '4'
    FILE_SIZE = '5'
    FILE_NUM = '6'
    FILE_NUM_LARGE_SIZE = '7'
    IS_TIMEOUT = '8'
