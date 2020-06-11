import platform
if platform.system() == "Windows":
    import  asyncio
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

from tornado.web import RequestHandler, Application
from tornado.ioloop import IOLoop
import os
from tornado.gen import coroutine
from tornado.concurrent import Future

class IndexHandler(RequestHandler):
    @coroutine
    def get(self,filename):
        print(filename)
        content = yield(self.readImg(filename))
        if not content:
            self.write_error(404)
        else :
            self.set_header('Content-Type','image/png')
            self.write(content)
    def readImg(self,filename):
        BaseDir = os.path.join(os.getcwd(),'static/image',filename)
        with open(BaseDir, 'rb') as fr:
            content = fr.read()
        future = Future()
        future.set_result(content)
        return future

if __name__ == '__main__':
    app =Application([
        (r"/static/(.*)$", IndexHandler),
    ])
    app.listen(8000)
    IOLoop.current().start()
