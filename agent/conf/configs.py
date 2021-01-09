#!/usr/bin/env python3
'''
Description: 
Author: limaochao
Date: 2020-12-26 12:29:13
LastEditTime: 2020-12-27 15:44:12
'''


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
            print(
                'Config file not exist, please make sure the path is correct!'
            )


config = Config().load_sets()
