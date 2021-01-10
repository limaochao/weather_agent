# /usr/bin/env python3
'''
Description: 
Author: limaochao
Date: 2020-12-27 14:52:43
LastEditTime: 2021-01-10 11:20:27
'''

import os
from agent.common.exceptions import dict_value_is_empty, str_length_valid


class ConfigInit:

    def __init__(self, input_dict):
        self.config_dict = input_dict
        if isinstance(self.config_dict, dict):
            self.config_count = len(self.config_dict)
        else:
            raise TypeError("unexpected type of dict")

    def get_count(self):
        return self.config_count

    def get_url_info(self):
        """ 返回url所需信息（数组），依次是url地址，name，attr（含id和pass的字典），response_code """
        url_info = [
            dict_value_is_empty(self.config_dict, 'url'),
            dict_value_is_empty(self.config_dict, 'name'),
            dict_value_is_empty(self.config_dict, 'attr'),
            dict_value_is_empty(self.config_dict, 'response_code')
        ]
        return url_info

    def get_tags(self, _type, value=None):
        if value is None:
            return self.tags_common(_type)
        else:
            return self.tags_common(_type) + ',value=' + str(value)

    def tags_common(self, _type):
        """返回tag公共部分信息"""
        # return 'branch=' + dict_value_is_empty(self.config_dict, 'branch') \
        #        + ',dataType=' + dict_value_is_empty(
        #            self.config_dict, 'dataType') \
        #        + ',department=' + dict_value_is_empty(
        #            self.config_dict, 'department') \
        #        + ',deputy=' + self.config_dict.get('deputy') \
        #        + ',id=' + dict_value_is_empty(
        #            self.config_dict, 'id') \
        #        + ',is_begin=' + dict_value_is_empty(
        #            self.config_dict, 'is_begin') \
        #        + ',is_finish=' + dict_value_is_empty(
        #            self.config_dict, 'is_finish') \
        #        + ',leader=' + dict_value_is_empty(
        #            self.config_dict, 'leader') \
        #        + ',pid=' + self.__get_pid() \
        #        + ',project=' + str_length_valid(
        #            dict_value_is_empty(
        #                self.config_dict, 'project'), 20, 'project') \
        #        + ',app_name=' + dict_value_is_empty(
        #            self.config_dict, 'app_name') \
        #        + ',subDataType=' + self.config_dict.get('subDataType') \
        #        + ',action=' + str_length_valid(
        #            dict_value_is_empty(
        #                self.config_dict, 'action'), 10, 'action') \
        #        + ',flow=' + dict_value_is_empty(
        #            self.config_dict, 'flow') \
        #        + ',type=' + _type
        
        return dict_value_is_empty(self.config_dict, 'branch') \
               + '_' + dict_value_is_empty(
                   self.config_dict, 'dataType') \
               + '_' + dict_value_is_empty(
                   self.config_dict, 'department') \
               + '_' + self.config_dict.get('deputy') \
               + '_' + dict_value_is_empty(
                   self.config_dict, 'id') \
               + '_' + dict_value_is_empty(
                   self.config_dict, 'is_begin') \
               + '_' + dict_value_is_empty(
                   self.config_dict, 'is_finish') \
               + '_' + dict_value_is_empty(
                   self.config_dict, 'leader') \
               + '_' + self.__get_pid() \
               + '_' + str_length_valid(
                   dict_value_is_empty(
                       self.config_dict, 
                       'project'
                    ), 20, 'project') \
               + '_' + dict_value_is_empty(
                   self.config_dict, 'app_name') \
               + '_' + self.config_dict.get('subDataType') \
               + '_' + str_length_valid(
                   dict_value_is_empty(
                       self.config_dict, 'action'), 20, 'action') \
               + '_' + dict_value_is_empty(
                   self.config_dict, 'flow') \
               + '_' + _type

    def __get_pid(self):
        if dict_value_is_empty(self.config_dict, 'is_begin') == 'True':
            return ''
        elif dict_value_is_empty(self.config_dict, 'is_begin') == 'False':
            return dict_value_is_empty(self.config_dict, 'pid')
        else:
            pass

    def get_http_metric(self, result=None):
        if result is None:
            return 'http-' + dict_value_is_empty(
                self.config_dict, 'dataType') + '-' + self.config_dict.get(
                'subDataType')
        else:
            return 'http-' + dict_value_is_empty(
                self.config_dict, 'dataType') + '-' + self.config_dict.get(
                'subDataType') + result

    def get_file_metric(self):
        attr_list = []
        for file_attr in self.get_attr():
            attr_list.append(file_attr.get('key'))
        return 'file-' + dict_value_is_empty(
            self.config_dict, 'dataType') + '-' + self.config_dict.get(
            'subDataType') + '-' + '&'.join(attr_list)

    def get_attr(self):
        return dict_value_is_empty(self.config_dict, 'attr')

    def get_file_path(self):
        '''
        这里以后扩展try捕获错误
        '''
        
        filename = self.config_dict.get('file_name')
        if not filename:
            return dict_value_is_empty(
                self.config_dict, 'dir_path')
        else:
            return os.path.join(dict_value_is_empty(
                self.config_dict, 'dir_path'), filename)

    def get_interval(self):
        """ 返回定时调度所需部分信息 """
        return int(self.config_dict['polling']['one'].get('interval', 60))

    def get_cron(self):
        """ 返回定时调度所需部分信息 """
        return self.config_dict.get('polling').get('two').get('cron')

    def get_is_push_update_continue(self):
        return dict_value_is_empty(self.config_dict, 'is_push_update_continue')


class ServerConf:
    def __init__(self, input_dict):
        self.conf_dict = input_dict

    def get_endpoint(self):
        """ 返回服务器endpoint """
        return dict_value_is_empty(self.conf_dict, 'ip')

    def get_push_url(self):
        """ 返回push url """
        return dict_value_is_empty(self.conf_dict, 'push_url')
