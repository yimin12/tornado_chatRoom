import platform
if platform.system() == "Windows":
    import  asyncio
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

from tornado.web import RequestHandler,Application
from tornado.ioloop import IOLoop
import os

class IndexHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.render('readImg.html')


if __name__ == '__main__':
    # 存储静态文件的路径和templates都在app中输入进去
    app =Application([
        (r"/", IndexHandler),
        # (r"/static/(.*)", StaticFileHandler, {"path": os.path.join(os.getcwd(),'static','images')}), 第二种静态文件的方式
    ], template_path = os.path.join(os.getcwd(), 'templates'), static_path=os.path.join(os.getcwd(),'static','image'))

    app.listen(9999)
    IOLoop.current().start()