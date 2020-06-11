
from tornado.template import Template
import os

import platform
if platform.system() == "Windows":
    import  asyncio
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

if __name__ == '__main__':
    with open(os.path.join(os.getcwd(),'templates', 'index.html'),'rb') as fr:
        content = fr.read()
    t = Template(content)
    str = t.generate(uname='Yimin')
    print(str)