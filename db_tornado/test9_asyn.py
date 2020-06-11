import platform
if platform.system() == "Windows":
    import  asyncio
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

'''在使用tornado6之后，默认不再使用asychronous，导入新的包为gen'''
from tornado.web import RequestHandler,Application,gen
from tornado.ioloop import IOLoop
import os

class IndexHandler(RequestHandler):
    @gen.coroutine
    def get(self, filename):
        print(filename)
        BaseDir = os.path.join(os.getcwd(),'static/image', filename)
        with open(BaseDir, 'rb') as fr:
            content = fr.read()
        if not content:
            self.write_error(404)
        else :
            self.set_header('Content-Type','image/png')
            self.write(content)
        # 手动结束此次响应
        self.finish()

if __name__ == '__main__':
    app =Application([
        (r"/static/(.*)$", IndexHandler),
    ])
    app.listen(9999)
    IOLoop.current().start()