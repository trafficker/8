from http.server import HTTPServer,BaseHTTPRequestHandler
import io,shutil
from django.http import HttpResponse
import urllib
class MyHttpHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        templateStr = '''''   
<html>   
<head>   
<title>QR Link Generator</title>   
</head>   
<body>   
%s 
<br>   
<br>   
<form action="/qr" name=f method="GET"><input maxLength=1024 size=70   
name=s value="" title="Text to QR Encode">
<input type=submit   
value="Show QR" name=qr>   
</form> 
</body>   
</html> '''
        qrImg ='<img src="http://pic.ibaotu.com/00/29/64/75j888piCA2d.jpg-0.jpg!ww700'+'"/><br/>'
        r_str="Hello World"
        enc="UTF-8"
        encoded = ''.join(r_str).encode(enc)
        f = io.BytesIO()
        f.write(encoded)
        f.seek(0)
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=%s" % enc)
        self.send_header("Content-Length", str(len(encoded)))
        self.end_headers()
        shutil.copyfileobj(f,self.wfile)
        self.wfile.write(templateStr % qrImg)
httpd=HTTPServer(('',8080),MyHttpHandler)
print("Server started on 127.0.0.1,port 8080.....")
httpd.serve_forever()