from tornado.web import  RequestHandler,Application
from models import User
from utils.sessions import SessionManager

class BaseHandler(RequestHandler):
    def prepare(self):
        # 从cookie中获取sessionid
        c_sessionid = self.get_cookie('sessionid','')
        # 根据sessionid在redis获取获取session对象
        sessionobj = SessionManager.getSessionObjBySid(c_sessionid)
        # 判断是否需要充值cookie中的sessionid
        if sessionobj.sessionid != c_sessionid:
            self.set_cookie('sessionid',sessionobj.sessionid,expires_days=14)
        self.session = sessionobj

    # 将session部分通过cookie存入redis中
    def on_finish(self):
        SessionManager.cache2reids(self.session)

class LoginHandler(BaseHandler):
    def get(self, *args, **kwargs):
        self.render('login.html')
    def post(self,*args, **kwargs):
        uname = self.get_argument('uname')
        pwd = self.get_argument('pwd')

        # 判断是否登录成功
        if uname == 'Theshy' and pwd == '123':
            user = User(uname, pwd)
            self.session.set('user',user)
            self.redirect('/center/')

class CenterHandler(BaseHandler):
    def get(self, *args, **kwargs):
        user = self.session.get('user')
        self.write(u'欢迎%s登录成功'%user.uname)