import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import PyQt4
import tkinter55555
#from dncrypte import *  #引入自己的方法
from tornado.options import define, options
define("port", default=8080, help="run on the given port", type=int)

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        result = ""
        Encrypted = ""
        self.render('test.html',**getlocals(locals()))
    def post(self):
        encry=self.get_argument('Encrypted', 'Hello')
        result = "kkkkk"
        self.render('test.html',**getlocals(locals()))
def getlocals(locals):
    tmpd={}
    for k,v in locals.iteritems():
        if k not in ['self']:
            tmpd[k] = v
    return tmpd
if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[(r"/", IndexHandler)])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()