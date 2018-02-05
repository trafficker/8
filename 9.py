import requests
import json
comments = requests.get('http://comment5.news.sina.com.cn/page/info?version=1&\
format=js&channel=gn&newsid=comos-fyihrwk1575695&group=&\
compress=0&ie=utf-8&oe=utf-8&page=1&\
page_size=20')

jd = json.loads(comments.text.strip('var data='))
print(jd['result']['count']['total'])
