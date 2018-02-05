import os #Python的标准库中的os模块包含普遍的操作系统功能  
import re #引入正则表达式对象  
import urllib #用于对URL进行编解码  
from http.server import HTTPServer,BaseHTTPRequestHandler#导入HTTP处理相关的模块  

#自定义处理程序，用于处理HTTP请求  
class TestHTTPHandler(BaseHTTPRequestHandler):
#处理GET请求  
    def do_GET(self):
      #页面输出模板字符串  
      templateStr='''''   
      <html>   
      <head>   
      <title>QR Link Generator</title>   
      </head>   
      <body>   
      %s 
      <br>   
      <br>   
      <form action="/qr" name=f method="GET"><input maxLength=1024 size=70   
      name=s value="" title="Text to QR Encode"><input type=submit   
      value="Show QR" name=qr>   
      </form> 
      </body>   
      </html> '''
# 将正则表达式编译成Pattern对象  
      pattern=re.compile(r'/qr\?s=([^\&]+)\&qr=Show\+QR')
# 使用Pattern匹配文本，获得匹配结果，无法匹配时将返回None  
      match = pattern.match(self.path)
      qrImg =''
      if match:
#使用Match获得分组信息  
         qrImg='<img src="https://image.baidu.com/search/detail?ct=503316480&z=0&ipn=d&word=basehttpserver%20python3&step_word=&hs=0&pn=1&spn=0&di=26855617910&pi=0&rn=1&tn=baiduimagedetail&is=0%2C0&istype=0&ie=utf-8&oe=utf-8&in=&cl=2&lm=-1&st=undefined&cs=3088547305%2C1001927398&os=2865178039%2C4096231422&simid=3387693104%2C4292831062&adpicid=0&lpn=0&ln=1985&fr=&fmq=1508151217310_R&fm=&ic=undefined&s=undefined&se=&sme=&tab=0&width=undefined&height=undefined&face=undefined&ist=&jit=&cg=&bdtype=0&oriquery=&objurl=http%3A%2F%2Fimages2015.cnblogs.com%2Fblog%2F952570%2F201607%2F952570-20160709105009561-2122805786.png&fromurl=ippr_z2C%24qAzdH3FAzdH3Fooo_z%26e3Bvgks52f_z%26e3Bv54AzdH3Fziwg2h7tAzdH3FrAzdH3Fcmcc9db_z%26e3Bip4s&gsm=0&rpstart=0&rpnum=0'+match.group(1) + '" /><br />' + urllib.unquote(match.group(1))
      self.protocal_version = 'HTTP/1.1' #设置协议版本  
      self.send_response(200) #设置响应状态码  
      self.send_header("Welcome","Contect") #设置响应头  
      self.end_headers()
      self.wfile.write(templateStr%qrImg)#输出响应内容 
#启动服务函数  
def start_server(port):
    http_server = HTTPServer(('', int(port)), TestHTTPHandler)
    http_server.serve_forever() #设置一直监听并接收请求  

#os.chdir('static') #改变工作目录到 static 目录  
start_server(8000) #启动服务，监听8000端口 