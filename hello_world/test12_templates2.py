
from tornado.template import Loader
import os

import platform
if platform.system() == "Windows":
    import  asyncio
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

if __name__ == '__main__':
   # 创建加载器对象
   loader = Loader(os.path.join(os.getcwd(),'templates'))
   # 获取一个模板对象
   t = loader.load('index.html')
   content = t.generate(uname=u'明天会更好')
   print(content)