import platform
if platform.system() == "Windows":
    import  asyncio
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

from tornado.web import RequestHandler, Application
from tornado.ioloop import IOLoop
import os

class Person(object):
    def __init__(self, sname, spwd):
        self.sname = sname
        self.spwd = spwd

def reverse(obj):
    if isinstance(obj,list):
        obj.reverse()
    return obj

class IndexHandler(RequestHandler):
    def get(self, *args, **kwargs):
        person = Person('Yimin','123')
        clist = ['c1','c2','c3']
        mdict = {'k1':'v1','k2':'v2'}
        str = '<script>window.location.href="https://www.google.com";</script>'
        self.render('index01.html', uname = 'Yimin', person = person, clist = clist, mdict = mdict, r = reverse, str = str)

if __name__ == '__main__':
    app =Application([
        (r"/", IndexHandler),
    ], template_path = os.path.join(os.getcwd(), 'templates'))
    app.listen(9999)
    IOLoop.current().start()