import platform
if platform.system() == "Windows":
    import  asyncio
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

from tornado.web import RequestHandler,Application
from tornado.ioloop import IOLoop
import os

class IndexHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.render('csrf.html')
    def post(self, *args, **kwargs):
        uname = self.get_argument('uname')
        self.write(uname)
settings={
    'xsrf_cookies':True
}

if __name__ == '__main__':
    app =Application([
        (r"/", IndexHandler),
    ], template_path = os.path.join(os.getcwd(), 'templates'),**settings)
    app.listen(9999)
    IOLoop.current().start()