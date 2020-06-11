import tornado.web
import tornado.ioloop
import platform
if platform.system() == "Windows":
    import  asyncio
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

class UploadHandler(tornado.web.RequestHandler):
    def get(self,*args,**kwargs):
        self.render('templates/upload.html')
    def post(self,*args,**kwargs):
        # 获取请求参数
        # 对于传入的img，格式是[{'body': '\0\x00IEND\xaeB`\x82', 'content_type': u'image/png', 'filename': u'1.png'}]
        img1 = self.request.files['img1']
        # 遍历img1
        for img in img1:
            body = img.get('body','')
            content_type = img.get('content_type','')
            filename = img.get('filename','')

        # 将图片存放至files目录中
        import os
        dir = os.path.join(os.getcwd(),'file',filename)
        with open(dir,'wb') as fw:
            fw.write(body)
        # 将图片显示到浏览器页面中
        # 设置响应头的信息
        self.set_header('Content-type',content_type)
        self.write(body)

if __name__ == '__main__':
    app = tornado.web.Application([
        ('/upload/',UploadHandler)
    ])
    app.listen(8888)
    tornado.ioloop.IOLoop.instance().start()