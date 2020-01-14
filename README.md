{
  "server": {全局配置
    "ip": "ip",
    "push_url": "数据push url"
  },
  "file": [
    {
      "dir_path": "目录路径,以/结尾",
      "file_name": "文件名(支持正则)(没有不填写)"
      "is_push_update_continue": "是是否连续push(默认5次)",
      "attr": [//文件属性监控
        {
          "key": "0",文件是否存在
          "size": "",
          "num": ""
        },
        {
          "key": "1",是否新建
          "size": "",
          "num": ""
        },
        {
          "key": "2",是否删除
          "size": "",
          "num": ""
        },
        {
          "key": "3",是否移动或改名
          "size": "",
          "num": ""
        },
        {
          "key": "4",文件或文件夹是否更新
          "size": "",
          "num": ""
        },
        {
          "key": "5",文件大小是否正常(需填写文件大小),bytes
          "size": "size",
          "num": ""
        },
        {
          "key": "6",文件数量是否正常(需填写文件数量)
          "size": "",
          "num": "num"
        },
        {
          "key": "7",文件夹下文件大小大于n的文件数量是否正常,(需填写文件大小和文件数量)
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
      "action": "从父节点到本节点的link描述(不超过10个字符)",
      "is_begin": "是否开始节点",
      "is_finish": "是否结束节点",
      "department": "部门",
      "branch": "支部",
      "leader": "负责人",
      "project": "项目名称（可选）",
      "deputy": "第二负责人（可选）"
    }
  ],
  "http": [
    {
      "id": "",
      "pid": "",
      "action": "",
      "is_begin": "",
      "is_finish": "",
      "url": "http://product.weather.com.cn/alarm/grepalarm_cn.php",
      "name": "预警数据接口总表查询",
      "attr": {
          "id": "",
          "pass": ""
        },
      "response_code": "var alarminfo=",
      "server_name": "预警业务",
      "server_level": "1",
      "process_name": "预警数据接口总表查询",
      "app_name": "预警数据接口探针",
      "polling": {
        "one": {
          "interval": "30",
          "data_update_interval": "30"
        },
        "two": {
          "cron": "",
          "time_error": ""
        }
      },
      "dataType": "预警",
      "subDataType": "json",
      "department": "department",
      "branch": "branch",
      "leader": "leader",
      "project": "project",
      "deputy": "deputy"
    }
    ]
}

