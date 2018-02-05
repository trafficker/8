import urllib.request
from urllib import request
from bs4 import BeautifulSoup
import requests
import ssl
import json
from json import loads#为了将取得字符串类型的转化为json
ssl._create_default_https_context=ssl._create_unverified_context
def getList():
    html=urllib.request.urlopen('https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2017-08-12&leftTicketDTO.from_station=CSQ&leftTicketDTO.to_station=CDW&purpose_codes=0X00').read()
    dict =loads(html)
    #字典型
    return dict['data']['result']
a=0
while 1:

    for i in getList():
        tmp_list=i.split('|')
        if int(tmp_list[23])>0:
            print("有票")
            print('车次%s'%tmp_list[3])
            a=1
            break
  #  for n in tmp_list:
   #     print("[%s]%s"%(a,n))
    #    a+=1
    break
       #SSL出现证书验证没有通过error

html2 = urllib.request.urlopen('https://kyfw.12306.cn/otn/resources/js/framework/favorite_name.js').read()



#req=request.Request('https://kyfw.12306.cn/otn/resources/js/framework/favorite_name.js')
#response=request.urlopen(req)
soup=BeautifulSoup(html2,'html.parser',from_encoding='utf-8')

