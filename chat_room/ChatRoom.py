import platform
if platform.system() == "Windows":
    import  asyncio
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

from tornado.web import RequestHandler,Application
from tornado.websocket import WebSocketHandler
from tornado.ioloop import IOLoop
import os
import datetime

class IndexHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.render('chat.html')

# 记录正在聊天的人的信息
userList = set()

class ChatHandler(WebSocketHandler):
    def open(self,*args,**kwargs):
        userList.add(self)
        # 给每个客户端发送一遍消息
        [user.write_message(
            u'%s-%s:上线了~' % (self.request.remote_ip, datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))) for user in
         userList]

    def on_message(self, message):
        [user.write_message(
            u'%s-%s说:%s' % (self.request.remote_ip, datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), message))
         for user in userList]

    def on_close(self):
        userList.remove(self)
        [user.write_message(
            u'%s-%s:下线了~' % (self.request.remote_ip, datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))) for
            user in userList]

if __name__ =='__main__':
    app = Application([
        (r'^/$', IndexHandler),
        (r'^/chat/$', ChatHandler),
    ],template_path=os.path.join(os.getcwd(),'templates'))
    app.listen(8000,'192.168.0.81')
    IOLoop.instance().start()
