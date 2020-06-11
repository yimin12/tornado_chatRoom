import platform
if platform.system() == "Windows":
    import  asyncio
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

import tornado.web
import tornado.ioloop

class CookieHandler(tornado.web.RequestHandler):
    def get(self,*args,**kwargs):
        # self.set_cookie('uname','yimin',expires_days=3)
        self.set_secure_cookie('hello','TheShy')
        

class GetCookieHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        # uname = self.get_cookie('uname')
        uname = self.get_secure_cookie('uname')
        print(uname)
        self.write(uname)

settings={
    'cookie_secret':'ShyShy'
}

if __name__ == '__main__':
    app = tornado.web.Application([
        (r"/",CookieHandler),
        (r"/getCookie/",GetCookieHandler),
    ],**settings)
    app.listen(9999)
    tornado.ioloop.IOLoop.current().start()