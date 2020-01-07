import sys
import os
import pyinotify
from taskScheduler import agentScheduler
from common import gol
from conf.configs import config
from file_agent.file_monitor_new import task, init_watchdog, metric_append, tag_append

WATCH_PATH = '/home/cuihaipeng/python'  # 监控目录
if not WATCH_PATH:
    print("The WATCH_PATH setting MUST be set.")
    sys.exit()
else:
    if os.path.exists(WATCH_PATH):
        print('Found watch path: path=%s.' % (WATCH_PATH))
    else:
        print('The watch path NOT exists, watching stop now: path=%s.' % (WATCH_PATH))
        sys.exit()


# 事件回调函数
class OnIOHandler(pyinotify.ProcessEvent):
    # 重写文件写入完成函数
    def process_IN_CLOSE_WRITE(self, event):
        # logging.info("create file: %s " % os.path.join(event.path, event.name))
        # 处理成小图片，然后发送给grpc服务器或者发给kafka
        file_path = os.path.join(event.path, event.name)
        print('文件完成写入', file_path)

    # 文件删除函数
    def process_IN_DELETE(self, event):
        print("文件删除: %s " % os.path.join(event.path, event.name))

    # 文件改变函数
    def process_IN_MODIFY(self, event):
        print("文件改变: %s " % os.path.join(event.path, event.name))

    # 文件创建函数
    def process_IN_CREATE(self, event):
        print("文件创建: %s " % os.path.join(event.path, event.name))


def auto_compile(path):
    wm = pyinotify.WatchManager()
    mask = pyinotify.IN_CREATE
    notifier = pyinotify.ThreadedNotifier(wm, OnIOHandler())  # 回调函数
    notifier.start()
    wm.add_watch(path, mask, rec=True, auto_add=True)
    wm.add_watch('/home/cuihaipeng/test/', pyinotify.IN_DELETE, rec=True)
    print('Start monitoring %s' % path)
    while True:
        try:
            notifier.process_events()
            if notifier.check_events():
                notifier.read_events()
        except KeyboardInterrupt:
            notifier.stop()
            break


if __name__ == "__main__":
    auto_compile(WATCH_PATH)
    print('monitor close')
    # gol.init()
    # tasksc = agentScheduler()
    # file_list = config.get('file')
    # endpoint = config.get('server').get('ip')
    # for file_conf in file_list:
    #     path = file_conf.get('dir_path') + file_conf.get('file_name')
    #     metric = metric_append(file_conf)
    #     tag = tag_append(file_conf)
    #     init_watchdog(file_conf['attr'], path, endpoint + metric + tag)
    #     rule = file_conf.get('polling').get('one').get('interval')
    #     taskid = (endpoint + metric + tag).replace(',', '')
    #     if len(str.strip(file_conf.get('polling').get('one').get('interval'))) != 0:
    #         tasksc.add_job(func=task, kwargs={'file_conf': file_conf},
    #                        id=taskid, trigger='interval', seconds=int(rule), replace_existing=True)
    #
    #     elif len(str.strip(file_conf['polling'].get('two').get('cron'))) != 0:
    #         pass
    #     else:
    #         pass
    #
    # tasksc.start()
