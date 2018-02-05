import urllib
import urllib.request
import gzip
import http.cookiejar
import time

def getOpener(head):
    cj = http.cookiejar.CookieJar()
    pro = urllib.request.HTTPCookieProcessor(cj)
    opener = urllib.request.build_opener(pro)
    header = []
    for key,value in head.items():
        elem = (key,value)
        header.append(elem)
    opener.addheaders = header
    return opener

def ungzip(data):
    try:
        print("正在解压")
        data = gzip.decompress(data)
        print("解压完毕")
    except :
        print("未经压缩")
    return data

header = {
    'Connection': 'Keep-Alive',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
    'Accept-Encoding': 'gzip, deflate',
    'X-Requested-With': 'XMLHttpRequest',
    'Host': 'www.17sucai.com',
    }
url = "http://www.17sucai.com/auth"
opener = getOpener(header)

id = "gjhgg1997@163.com"
ps = "7c4a8d09ca3762af61e59520943dc26494f8941b"
post = {
    'email':id,
    'password':ps,
    'token':'cb3EAr1DiRNNtxDAKhBrMhE0hql1xauYBpdNmVhtKY4=',
    }
postData = urllib.parse.urlencode(post).encode()
op = opener.open(url,postData)
data = op.read()
data = ungzip(data)

print(data)

url = 'http://www.17sucai.com/member/signin'
op = opener.open(url)
data = op.read()
data = ungzip(data)

print(data)