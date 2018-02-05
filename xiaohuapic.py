from urllib import request
import re
from bs4 import BeautifulSoup
#网页设置了防爬，需伪装浏览器
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/51.0.2704.63 Safari/537.36'}
req=request.Request('http://www.xiaohuar.com/hua/',headers=headers)
response=request.urlopen(req)
soup=BeautifulSoup(response,'html.parser',from_encoding='gbk')
imgs=soup.find_all('img',src=re.compile(r'/d/file/\d+/\w+\.jpg'))
print(imgs)
for img in imgs:
  img_req=request.Request(url='http://www.xiaohuar.com%s' % img['src'],headers=headers)
  data=request.urlopen(img_req).read()
 #写入文件
  with open('%s.jpg'%img['alt'],'wb') as f:
      f.write(data)
