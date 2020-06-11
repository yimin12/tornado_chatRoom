#coding-utf8
import tornado.web
import tornado.ioloop
import pymysql
import datetime
import platform
if platform.system() == "Windows":
    import  asyncio
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

# Connect to the database
def _getConn():
    return pymysql.connect(host='localhost',user='root',password='123456',db='tornado_test',charset="utf8")

class RegisterHandler(tornado.web.RequestHandler):
    def initialize(self,conn):
        self.conn = conn
    def get(self, *args, **kwargs):
        self.render('templates/register.html')
    def post(self, *args, **kwargs):
        # 获取请求参数
        uname = self.get_argument('uname')
        pwd =self.get_argument('pwd')

        # 将数据插入到数据库中
        try:
            dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with self.conn.cursor() as cursor:
                sql = "INSERT INTO t_auser(uname, pwd, created) values('%s','%s','%s')"
                data = (uname, pwd, dt)
                cursor.execute(sql%data)
            self.conn.commit()
            self.write('注册成功！')
        except:
            self.conn.rollback()
            self.redirect('/register/')

if __name__ == '__main__':
    app = tornado.web.Application([
        ('/register/',RegisterHandler,{'conn':_getConn()})
    ])
    app.listen(9999)
    tornado.ioloop.IOLoop.instance().start()