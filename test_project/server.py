from tornado.ioloop import IOLoop
from tornado.web import Application
from urls import *

import platform
if platform.system() == "Windows":
    import  asyncio
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())



class HttpServer(Application):
    def __init__(self,port):
        self.listen(port)
        Application.__init__(self,**settings)
    def start(self):
        IOLoop.instance().start()

if __name__ == '__main__':
    HttpServer().start()