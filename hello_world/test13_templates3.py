
from tornado.template import Loader
import os
import tornado.web
import tornado.ioloop

import platform
if platform.system() == "Windows":
    import  asyncio
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render('templates/index.html', uname='yimin huang', PWD='12312321')


if __name__ == '__main__':
    app = tornado.web.Application([
        (r"/", IndexHandler),
    ])
    app.listen(9999)
    tornado.ioloop.IOLoop.current().start()