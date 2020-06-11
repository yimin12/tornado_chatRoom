import platform
if platform.system() == "Windows":
    import  asyncio
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

from tornado.httpclient import HTTPClient, HTTPRequest

# GET 请求
def getRequest(url):
    hc = HTTPClient()
    response = hc.fetch(url)
    return response.body

print(getRequest('http://www.bjxst.com'))

# POST 请求
def postRequest(request):
    hc = HTTPClient()
    response = hc.fetch(request)
    return response.body

HTTPRequest(url='http://www.bjsxt.com',method='POST',headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'},body='uname=zhangsan')
print(postRequest(req))