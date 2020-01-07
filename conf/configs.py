# coding: utf-8

"""
@Time : 2019-12-25 10:58 
@Author : cuihaipeng
@File : configs.py
@pyVersion: 3.6.8
@desc : json配置文件初始化
"""

import json
import os


def find_file_path():
    return os.path.dirname(os.path.abspath(__file__))


class Config:
    def __init__(self, file_path=None):
        if file_path is None:
            self.file_path = os.path.join(find_file_path(), 'configs.json')
        else:
            self.file_path = file_path

    def load_sets(self):
        if os.path.isfile(self.file_path):
            with open(self.file_path, encoding='UTF-8') as config_file:
                _config = json.load(config_file)
                return _config
        else:
            print('Config file not exist, please make sure the path is correct!')


config = Config().load_sets()