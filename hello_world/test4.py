#coding=utf-8

import tornado.web
import tornado.ioloop
import platform
if platform.system() == "Windows":
    import  asyncio
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

class GetRequestInfo(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        print(self.request)
        print(self.request.protocol)
        print(self.request.host)
        print(type(self.request.headers))
        print(self.request.headers['User_Agent'])

ugs = ['Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36']

class StuHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        # 1: 获取请求头中的user—agent的值
        ua = self.request.headers['User-Agent']
        # 2: 判断
        if ua not in ugs:
            self.send_error(403)
        else :
            self.write('hello XXX')

if __name__ == '__main__':
    app = tornado.web.Application([
        ('',GetRequestInfo),
        ('stu/',StuHandler)
    ])
    app.listen(8888)
    tornado.ioloop.IOLoop.instance().start()