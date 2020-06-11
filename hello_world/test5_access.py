import tornado.web
import tornado.ioloop
import platform
if platform.system() == "Windows":
    import  asyncio
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

uas = ['Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36']

# 通过User-Agent来弄反爬虫
class AccessHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        ua = self.request.headers['User-Agent']
        if ua not in uas:
            self.send_error(403)
        else :
            self.write("Hello Yimin")
ipcount={}
class LoginHandler(tornado.web.RequestHandler):
    def get(self,*args,**kwargs):
        ip = self.request.remote_ip
        num = ipcount.get(ip,0) + 1
        ipcount[ip] = num
        if ipcount[ip] > 10:
            self.send_error(403)
        else :
            self.write('正常访问')

if __name__ == '__main__':
    app = tornado.web.Application([
        (r'^/$',AccessHandler),
        (r'^/login/$',LoginHandler),
    ])
    app.listen(9888, "192.168.0.81")
    tornado.ioloop.IOLoop.current().start()