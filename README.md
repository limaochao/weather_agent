#天气网业务监控客户端

##文件监控配置文件定义
    '''
    {
      "server": {
        "ip": "ip",
        "push_url": "数据push url"
      },
      "file": [
        {
          "dir_path": "目录路径,以/结尾",
          "file_name": "文件名(支持正则)(没有不填写)"
          "attr": [//文件属性监控
            {
              "key": "监控标识",
              "size": "size",
              "num": "num"
            },
            {
              "key": "监控标识
              "size": "size",
              "num": "num"
            }
          ],
          "server_name": "业务名称",
          "server_level": "业务级别",
          "process_name": "流程名称",
          "app_name": "应用名称",
          "polling": {//轮询
            "one": {//时间间隔方式
              "interval": "轮询间隔，汇报周期",
              "data_update_interval": "数据更新间隔"
            },
            "two": {//cron表达式方式
              "cron": "cron表达式",
              "time_error": "允许时间误差"
            }
          },
          "dataType": "数据大类",
          "subDataType": "数据类细分",
          "id": "agent id",
          "pid": "父id",
          "is_finish": "是否结束",
          "department": "部门",
          "branch": "支部",
          "leader": "负责人",
          "project": "项目名称（可选）",
          "deputy": "第二负责人（可选）"
        }
      ]
    }
    
    file.attr.key说明：
        0:文件是否存在,
        1:是否新建,
        2:是否删除,
        3:是否移动或改名,
        4:文件或文件夹是否更新,
        5:文件大小是否正常(需填写文件大小),bytes
        6:文件数量是否正常(需填写文件数量),
        7:文件夹下文件大小大于n的文件数量是否正常,(需填写文件大小和文件数量)
        8:文件是否超时,
    '''