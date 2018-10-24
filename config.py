import os

BASE_DIRS = os.path.dirname(__file__)
# print("BASE_DIRS:" + BASE_DIRS)
# options参数
options = {
    "port": 9002

}

# 配置
settings = {
    "static_path": os.path.join(BASE_DIRS, "statics"),  # 设置静态文件目录
    "template_path": os.path.join(BASE_DIRS, "templates"),  # 设置模板文件目录
    "debug": False,
    # true 表示调试模式：1.不用重启服务,即应用更新后的代码 autoreload=True  2.取消缓存编译的代码compiled_template_cache = false  3.取消缓存文件的静态值 static_hash_cache = false 4.提供追踪信息 。false 为生产模式：需要重启服务才能更新
    "autoreload": False,  # 热加载，不用重启服务 即应用后的更新代码，和上面debug = true 不同的是，debug = ture 时还启用了上面其他的一些功能
    "autoescape":None  #关闭自动转义，整个项目生效
    # 'template_path': os.path.join(os.path.dirname(__file__), "templates")
}
