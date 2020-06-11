import platform
if platform.system() == "Windows":
    import  asyncio
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

import tornado.web
import tornado.ioloop
import pymysql

class LoginHandler(tornado.web.RequestHandler):
    def initialize(self,conn):
        self.conn = conn
    def prepare(self):
        if self.request.method == 'POST':
            # 获取请求参数
            self.uname = self.get_argument('uname')
            self.pwd = self.get_argument('pwd')
    def get(self, *args, **kwargs):
        self.render('templates/login.html')
    def post(self, *args, **kwargs):
        1/0
        cursor = self.conn.cursor()
        cursor.execute('select * from t_auser where uname="%s" and pwd="%s"'%(self.uname,self.pwd))
        user = cursor.fetchone()
        if user:
            self.write("登录成功")
        else :
            self.write("登录失败")
    def write_error(self, status_code: int, **kwargs):
        self.render('templates/error.html')
    def set_default_headers(self):
        self.set_header('Server','YiminServer/1.0')

settings={'debug':True}
dbconfig={
    'host':'127.0.0.1',
    'user':'root',
    'passwd':'123456',
    'db':'tornado_test',
    'port':3306
}
if __name__ == '__main__':
    app = tornado.web.Application([
        (r'^/login/$',LoginHandler,{'conn':pymysql.connect(**dbconfig)}),
    ], **settings)
    app.listen(9997)
    tornado.ioloop.IOLoop.current().start()