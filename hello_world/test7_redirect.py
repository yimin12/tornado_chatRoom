import tornado.web
import tornado.ioloop
from tornado.web import RedirectHandler
from tornado.routing import URLSpec
import platform

if platform.system() == "Windows":
    import  asyncio
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

class IndexHandler(tornado.web.RequestHandler):
    def get(self,*args, **kwargs):
        # 默认302 的重定向
        # self.redirect('http://www.google.com')
        self.set_status(302)
        self.set_header('Location','https://www.pornhub.com')
        self.redirect(self.reverse_url('index'))

class ReverseHandler(tornado.web.RequestHandler):
    def get(self,*args,**kwargs):
        self.redirect(self.reverse_url('index'))
if __name__ == '__main__':
    app = tornado.web.Application([
        (r'^/$',IndexHandler),
        (r'^/red/$',RedirectHandler,{'url':'https://www.taobao.com'}),
        URLSpec(r'^/asdfasdfasdf$',IndexHandler, name='index'),
        (r'^/reverse/$',ReverseHandler)

    ])
    app.listen(9999)
    tornado.ioloop.IOLoop.current().start()