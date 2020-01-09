# coding:utf-8

import json


#
# def my_obj_pairs_hook(lst):
#     result = {}
#     count = {}
#     for key, val in lst:
#         if key in count:
#             count[key] = 1 + count[key]
#         else:
#             count[key] = 1
#         if key in result:
#             # result[key].append(val)
#             if count[key] > 2:
#                 result[key].append(val)
#             else:
#                 result[key] = [result[key], val]
#         else:
#             # result[key] = [val]
#             result[key] = val
#     return result

#
# class JsonConf:
#
#     def __init__(self, input_path):
#         self.file_path = input_path
#         self.file = open(self.file_path, "rb")
#         # self.conf_dict = json.loads(self.file.read(), object_pairs_hook=my_obj_pairs_hook)
#         self.conf_dict = json.loads(self.file.read())
#         self.file.close()
#         self.http_lists = self.conf_dict.get('http')
#         if isinstance(self.http_lists, list):
#             self.http_count = len(self.http_lists)
#         else:
#             raise TypeError("unexpected type of http list")

class HttpConf:

    def __init__(self, input_dict):
        self.http_dict = input_dict
        if isinstance(self.http_dict, dict):
            self.http_count = len(self.http_dict)
        else:
            raise TypeError("unexpected type of http dict")

    def get_count(self):
        return self.http_count

    '''
    返回url所需信息（数组），依次是url地址，name，attr（含id和pass的字典），response_code
    '''

    def get_url_info(self):
        url_info = [self.http_dict['url'], self.http_dict['name'], self.http_dict['attr'],
                    self.http_dict['response_code']]
        return url_info

    '''
    返回推送报警报告所需部分信息
    '''

    def get_tag(self):
        return 'department=' + self.http_dict['department'] + ',branch=' + self.http_dict['branch'] \
               + ',type=http,id=' + self.http_dict['id'] + ',pid=' + self.http_dict['pid'] \
               + ',is_finish=' + self.http_dict['is_finish'] + ',leader=' + self.http_dict['leader'] \
               + ',project=' + self.http_dict['project'] + ',deputy=' + self.http_dict['deputy'] \
               + ',url=' + self.http_dict['url'] + ',name=' + self.http_dict['name']

    def get_metric(self):
        return 'http-' + self.http_dict.get('dataType') + '-' + self.http_dict.get('subDataType')

    def get_step(self):
        return self.http_dict.get('step')

    '''
        返回定时调度所需部分信息
    '''

    def get_interval(self):
        return self.http_dict.get('polling').get('one').get('interval')


class ServerConf:
    def __init__(self, input_dict):
        self.conf_dict = input_dict

    def get_endpoint(self):
        return self.conf_dict.get('ip')

    def get_push_url(self):
        return self.conf_dict.get('push_url')
