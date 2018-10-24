import tornado.web
from views import index
import config
import tornado.ioloop
import os


class Application(tornado.web.Application):
    def __init__(self):  # 写初始化方法
        handlers = [  # 写路由
            (r'/', index.IndexHandler),

            (r'/home', index.HomeHandler),

            # 传递参数给响应类 ParameterHandler
            (r'/parameter', index.ParameterHandler, {"name": "domain", "age": 18}),  # 第三个为参数,以字典方式传递一个参数过去

            # 响应json数据
            (r'/json', index.JsonHandler),

            # 设置响应头header
            (r'/header', index.HeaderHandler),

            # 设置响应状态码status
            (r'/status1', index.StatusHandler1),
            (r'/status2', index.StatusHandler2),

            # 设置重定向
            (r'/index', index.RedirectHandler),

            # 错误处理
            (r'/iserror', index.ErrorHandler),

            # 反向解析
            tornado.web.url(r'/home', index.IndexHandler, name="url"),

            # 获取uri特定部分
            (r'/getUri/(\w+)/(\w+)/(\w+)', index.GetUriHandler),

            # http get传递参数
            (r'/getParameter', index.GetParameter),

            # # http post 传递参数
            # (r'/login', index.LoginHandler),

            # 同时处理 get 和 post 参数
            (r'/getandpostparameter', index.GetAndPostParameter),

            # request 对象
            (r'/reqeuestobject', index.RequestObjectHandler),

            # 上传文件
            (r'/upfile', index.UpFileHandler),

            # 响应请求
            (r'/write', index.WriteHandler),

            # 请求调用顺序
            (r'/callorder', index.CallOrderHandler),

            # 模板语法
            (r'/templates', index.TemplatesHandler),

            # 函数
            (r'/function', index.FunctionHandler),

            # 转义
            (r'/trans', index.TransHandler),

            # 继承
            (r'/shopCart', index.shopCartHandler),




            # 注册API
            (r'/register', index.RegisterHandler),
            # 登陆API
            (r'/login', index.LoginHandler),


            # StaticFileHandler
            # (r'/(.*)$', tornado.web.StaticFileHandler,  # (.*)$  匹配所有字符 ,一定要放到最后面，匹配所有字符，不然会会先匹配这个正则
            #
            #  {"path": os.path.join(config.BASE_DIRS, "statics/html"),  # 指定statics/html 目录
            #
            #   "default_filename": "index.html"}  # 不指定文件名，则为index.html
            #  ),

        ]

        super(Application, self).__init__(handlers, **config.settings)  # 把参数传递给父类
