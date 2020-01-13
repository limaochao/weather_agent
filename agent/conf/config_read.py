# coding:utf-8
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
        url_info = [self.config_dict['url'], self.config_dict['name'], self.config_dict['attr'],
                    self.config_dict['response_code']]
        return url_info

    def get_http_tag(self):
        """ 返回http推送报警报告所需部分信息 """
        return 'branch=' + self.config_dict['branch'] + ',dataType=' + self.config_dict['dataType'] \
               + ',department=' + self.config_dict['department'] + ',deputy=' + self.config_dict['deputy'] \
               + ',id=' + self.config_dict['id'] + ',is_begin=' + self.config_dict['is_begin'] \
               + ',is_finish=' + self.config_dict['is_finish'] + ',leader=' + self.config_dict['leader'] \
               + ',pid=' + self.config_dict['pid'] + ',project=' + self.config_dict['project'] \
               + ',source=' + self.config_dict['url'] + ',subDataType=' + self.config_dict['subDataType'] \
               + ',type=http'

    def get_file_tag(self):
        """ 返回file推送报警报告所需部分信息 """
        return 'branch=' + self.config_dict['branch'] + ',dataType=' + self.config_dict['dataType'] \
               + ',department=' + self.config_dict['department'] + ',deputy=' + self.config_dict['deputy'] \
               + ',id=' + self.config_dict['id'] + ',is_begin=' + self.config_dict['is_begin'] \
               + ',is_finish=' + self.config_dict['is_finish'] + ',leader=' + self.config_dict['leader'] \
               + ',pid=' + self.config_dict['pid'] + ',project=' + self.config_dict['project'] \
               + ',source=' + self.config_dict['dir_path'] + self.config_dict['file_name'] + ',subDataType=' + \
               self.config_dict['subDataType'] \
               + ',type=file'

    def get_http_metric(self, result=None):
        if result is None:
            return 'http-' + self.config_dict.get('dataType') + '-' + self.config_dict.get('subDataType')
        else:
            return 'http-' + self.config_dict.get('dataType') + '-' + self.config_dict.get('subDataType') + result

    def get_file_metric(self):
        attr_list = []
        for file_attr in self.config_dict.get('attr'):
            attr_list.append(file_attr.get('key'))
        return 'file-' + self.config_dict.get('dataType') + '-' + self.config_dict.get('subDataType') + '-' + '&'.join(
            attr_list)

    def get_attr(self):
        return self.config_dict.get('attr')

    def get_file_path(self):
        return self.config_dict.get('dir_path') + self.config_dict.get('file_name')

    def get_step(self):
        return self.config_dict.get('step')

    def get_interval(self):
        """ 返回定时调度所需部分信息 """
        return self.config_dict.get('polling').get('one').get('interval')

    def get_cron(self):
        """ 返回定时调度所需部分信息 """
        return self.config_dict.get('polling').get('two').get('cron')


class ServerConf:
    def __init__(self, input_dict):
        self.conf_dict = input_dict

    def get_endpoint(self):
        """ 返回服务器endpoint """
        return self.conf_dict.get('ip')

    def get_push_url(self):
        """ 返回push url """
        return self.conf_dict.get('push_url')
