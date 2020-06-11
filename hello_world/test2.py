#coding=utf-8
import tornado.web
import tornado.ioloop
import platform
if platform.system() == "Windows":
    import  asyncio
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

class IndexHandler(tornado.web.RequestHandler):
    def get(self,*args,**kwargs):
        self.render('templates/login.html')

class LoginHandler(tornado.web.RequestHandler):
    def get(self,*args,**kwargs):
        # uname = self.get_argument('uname')
        pwd = self.get_argument('pwd')
        uname = self.get_query_argument('uname')

        print(uname,pwd)
        self.write(uname + ',' + pwd)
    def post(self, *args, **kwargs):
        uname = self.get_body_argument('uname')
        print(uname)
        self.write(uname)

if __name__ == "__main__":
    app = tornado.web.Application([
        ('/',IndexHandler),
        ('/login/', LoginHandler)
    ])
    app.listen(8888)
    tornado.ioloop.IOLoop.instance().start()