#tornado创建一个HTTP的固定写法
from tornado import web
from tornado import httpserver
from tornado import ioloop
#逻辑处理模块

class MainPageHandler(web.RequestHandler):
    def get(self, *args, **kwargs):
      self.write('hello world!')#返回字串
      self.render('index.html')# #返回页面
    def put(self, *args, **kwargs):
     pass

class LoginHandler(web.RequestHandler):
    def get(self, *args, **kwargs):
      self.render('login.html')  # #返回页面

#路由设置
application=web.Application([(r"/index",MainPageHandler),(r"/login",LoginHandler),])
if __name__=='main':
    httpserver=httpserver.HTTPServer(application)
    print("http//:127.0.0.1:8080")
    httpserver.listen(8080)
    ioloop.IOLoop.current().start()