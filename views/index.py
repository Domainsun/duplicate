from tornado.web import RequestHandler
import json, os
import config
import re
import docx

import random

login_user = ''


class IndexHandler(RequestHandler):
    def get(self, *args, **kwargs):
        # self.write("successful")
        self.render('index.html',error='')


class HomeHandler(RequestHandler):

    def get(self):
        self.write("weclome to home!")


class ParameterHandler(RequestHandler):

    def initialize(self, name, age):  # 获取传递过来的值，赋值给self对应的变量，之后就可以通过self调用
        self.name = name
        self.age = age

    def get(self):
        self.write("name:%s age: %s" % (self.name, self.age))


# 响应json数据
class JsonHandler(RequestHandler):

    def get(self):
        data = {
            "name": "domian",
            "age": 18,
            "sex": 1
        }
        self.write(data)


# 设置响应header
class HeaderHandler(RequestHandler):
    def set_default_headers(self):
        self.set_header("Content-Type", "text/html;chartset=utf-8")
        self.set_header("name", "domain")

    def get(self, *args, **kwargs):
        self.write("test for header")
        pass


# 设置响应状态码status
class StatusHandler1(RequestHandler):
    def get(self, *args, **kwargs):
        self.set_status(404)  # 只给状态码，用于已知状态


class StatusHandler2(RequestHandler):
    def get(self, *args, **kwargs):
        self.set_status(999, "未知原因")  # 给状态码和原因，用于未知状态
        self.write(111)


class RedirectHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.redirect('/')


class ErrorHandler(RequestHandler):

    def write_error(self, status_code, **kwargs):
        if status_code == 404:
            code = 404
            self.write("404 错误")
        elif status_code == 500:
            code = 500
            self.write("500 错误")

    def get(self, *args, **kwargs):
        flag = self.get_query_argument("flag")
        if flag == "0":  # flas参数为0，发送error，error code为404，send_error之后，下面的代码不执行，跳到write_error
            self.send_error(404)
        elif flag == "2":  # flas参数为2，发送error，error code为500
            self.send_error(500)
        self.write("you are right ")  # flas参数不为2和0，输出 "you are right"


class GetUriHandler(RequestHandler):
    def get(self, h1, h2, h3, *args, **kwargs):
        print(h1 + "-" + h2 + "-" + h3)
        self.write("get uri successful.")


class GetParameter(RequestHandler):

    def get(self, *args, **kwargs):
        # 通过self.get_query_argument获取url传递过来的参数，同名参数以最后一个为准
        parameter1 = self.get_query_argument(name="parameter1", default="defaultParamter",
                                             strip=True)  # name：key 名字、default：默认值、strip:值去除左右空格。不传递值和不设置默认值，抛出缺少参数异常
        parameter2 = self.get_query_argument(name="parameter2", default="defaultParamter", strip=True)
        parameter3 = self.get_query_argument(name="parameter3", default="defaultParamter", strip=True)
        # self.write("Get Parameter:parameter1 is %s parameter2 is %s parameter3 is %s"%(parameter1,parameter2,parameter3))

        # 通过self.get_query_arguments 获取多个同名参数
        parameters = self.get_query_arguments('name')
        print(parameters[0], parameters[1])
        self.write(parameters[0] + parameters[1])


# class LoginHandler(RequestHandler):
#
#     def get(self, *args, **kwargs):  # get 方式返回login 界面 html
#         self.render('login.html', num=100, list=["hello", "domain"])
#
#     def post(self, *args, **kwargs):  # post 方式处理登陆逻辑
#         user = self.get_body_argument("user", "", False)
#         password = self.get_body_argument("password", "", False)
#         hobbyList = self.get_body_arguments("hobby")
#
#         print(user, password, hobbyList)


class GetAndPostParameter(RequestHandler):

    def get(self, *args, **kwargs):
        name = self.get_argument("name")  # 在get请求中用self.get_argument("name") 获取传递过来的参数
        self.write("name in get:" + name)
        print("name in get:" + name)

    def post(self, *args, **kwargs):
        name = self.get_argument("name")  # 在post请求中用self.get_argument("name") 获取传递过来的参数
        print("name in post" + name)
        self.write("name in post" + name)


class RequestObjectHandler(RequestHandler):
    def get(self, *args, **kwargs):
        print(self.request.method)
        print(self.request.host)
        print(self.request.uri)
        print(self.request.query)
        print(self.request.version)
        print(self.request.headers)
        print(self.request.remote_ip)
        print(self.request.files)


list = ['', '']


class UpFileHandler(RequestHandler):

    def get(self, *args, **kwargs):
        # self.write("successful")
        self.render('upfile.html', user=login_user,error='')

    def post(self, *args, **kwargs):
        print('upfile post')
        fileDict = self.request.files
        # print(fileDict)

        for input_name in fileDict:
            file_list = fileDict[input_name]
            # for file_obj in file_list:
            for index, file_obj in enumerate(file_list):
                file_path = os.path.join(config.BASE_DIRS, "upfile/" + file_obj.filename)
                with open(file_path, "wb") as f:
                    f.write(file_obj.body)
                    list[index] = file_path
        language = self.get_body_argument("language", "", False)
        # if get_different(language):
        content, similarity_degree = get_different(language)
        if content:
            if similarity_degree > 100:
                similarity_degree == 87
            self.render('showdifferent.html', content=content, similarity_degree=similarity_degree, user=login_user)
        else:
            self.render('upfile.html', user=login_user,error='Please submit the correct language files!')
            # self.write('Please submit the correct language files!')


def is_Chinese(word):
    for ch in word:
        if '\u4e00' <= ch <= '\u9fff':
            return "Chinese"
    return "English"


a = ''
j_str = ''
tmp = []


def not_empty(s):
    return s and s.strip()


def get_different(language):
    file1 = docx.Document(list[0])
    global a
    global j_str
    global tmp
    a = ''
    j_str = ''
    tmp = []
    # # 输出每一段的内容
    for para in file1.paragraphs:
        a = a + para.text

    print(a)
    print("language:", language, "ischinese", is_Chinese(a))
    if language == is_Chinese(a):
        a_list = re.split('[,.，。、]', a)
        print(a_list)
        if len(a_list) > 5:
            same_count = random.randint(3, len(a_list) - 5)
        else:
            same_count = 0
        tmp.clear()
        del tmp[:]
        for i in range(same_count):
            index = random.randint(0, len(a_list))
            print(index, 'alistlenth:', len(a_list))
            if index < len(a_list):
                tmp.append(a_list[index])

        print("tmp:", tmp)
        # tmp = filter(not_empty, tmp)
        for join_str in tmp:
            if not join_str == '':
                a = a.replace(join_str, (' <a style="background-color: #CCCCCC">%s</a>' % join_str))

                print("a---", a)
                j_str = j_str + join_str

        return a, int((len(j_str) / len(a)) * 100)
    else:
        return None, None


# self.write响应请求
class WriteHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.write("hello")
        self.write("domain")
        self.write("world")
        # 刷新当前缓冲区，关闭单次请求通道，finish之后的write无效
        self.finish()


class CallOrderHandler(RequestHandler):
    def set_default_headers(self):
        print("set default headers")

    def initialize(self):
        print("initialize")

    def prepare(self):
        print("prepare")

    def get(self, *args, **kwargs):
        print("get")

    def write_error(self, status_code, **kwargs):
        print("write error")

    def on_finish(self):
        print("on finish")


class TemplatesHandler(RequestHandler):
    def get(self, *args, **kwargs):  # get 方式返回界面 html,并向html 传递变量 列表 字典
        num = 100
        list = ["hello", "domain"]
        dic = {
            "name": "domain",
            "age": 18,
            "sex": "男"
        }
        self.render('templatesDemo.html', num=num, list=list, dic=dic)


class FunctionHandler(RequestHandler):
    def get(self, *args, **kwargs):  # get 方式返回界面 html,并向html 传递变量 列表 字典
        def func(n):
            n = n + 100
            return n

        self.render('function.html', func=func)


class TransHandler(RequestHandler):
    def get(self, *args, **kwargs):  # get 方式返回界面 html,并向html 传递变量 str
        str1 = "<h1>hello</h1>"
        self.render('trans.html', str1=str1)


class shopCartHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.render('shopCart.html')


class studentsHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.render('students.html')


dic = {}


class RegisterHandler(RequestHandler):

    def get(self, *args, **kwargs):
        self.render('register.html',error='')

    def post(self, *args, **kwargs):  # post 方式处理登陆逻辑
        user = self.get_body_argument("user", "", False)
        password = self.get_body_argument("password", "", False)
        verifypassword = self.get_body_argument("verifypassword", "", False)

        if user and password and verifypassword:
            # phone_pat = re.compile('^[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}$')
            # res = re.search(phone_pat, user)
            if user.__len__() > 3:
                if password == verifypassword:
                    if user not in dic.keys():
                        dic[user] = password
                        self.render('index.html',error='')
                    else:
                        # self.write('Already registered!')
                        self.render('register.html', error='Already registered!')
                else:
                    # self.write('The two password is inconsistent!')
                    self.render('register.html', error='The two password is inconsistent!')
            else:
                # self.write('The user name needs more than 3 characters!')
                self.render('register.html', error='The user name needs more than 3 characters!')
        else:
            # self.write('The username or password can not be empty!')
            self.render('register.html', error='The username or password can not be empty!')


class LoginHandler(RequestHandler):

    def post(self, *args, **kwargs):  # post 方式处理登陆逻辑
        user = self.get_body_argument("user", "", False)
        password = self.get_body_argument("password", "", False)

        if user and password:
            # phone_pat = re.compile('^[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}$')
            # res = re.search(phone_pat, user)
            if user.__len__() > 3:
                if user in dic.keys():
                    if dic[user] == password:
                        global login_user
                        login_user = user
                        self.render('upfile.html', user=user,error='')
                    else:
                        self.render('index.html', error=' Account or password error!')
                else:
                    self.render('index.html', error='Please register first!')
            else:
                self.render('index.html', error='The user name needs more than 3 characters!')
        else:
            self.render('index.html', error='The username or password can not be empty!')
