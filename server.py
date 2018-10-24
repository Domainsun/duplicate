import os
import sys
import tornado.web

# import responseDemo.application
# import responseDemo.config

# relactive_path=__file__  #相对路径
# absolute_path=os.path.abspath(__file__)  #绝对路径
# dir1=os.path.dirname(absolute_path)           #返回当前文件所在目录
# PATH=os.path.dirname(dir1)          #返回当前文件所在目录的上级目录
# print(dir1)
# print(PATH)
# print("path:",sys.path)

#以上等于下面这句话
PATH=os.path.dirname(os.path.dirname(os.path.abspath(__file__) ))
sys.path.append(PATH)     #添加项目的环境变量 ，也就ATM的目录

import config
from application import Application
if __name__ == '__main__':
    app = Application()
    app.listen(config.options["port"])
    tornado.ioloop.IOLoop.current().start()  # IOLoop.current:返回当前线程的实例,IOLoop.start:启动IoLoop的I/O 循环，同时开启监听



