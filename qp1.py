from splinter.browser import Browser
b = Browser(driver_name="chrome")
url = "https://kyfw.12306.cn/otn/leftTicket/init"
b = Browser(driver_name="chrome")
b.visit(url)
b.find_by_text(u"登录").click()
b.fill("loginUserDTO.user_name","xxx")
b.fill("userDTO.password","xxx")

b.cookies.add({"_jc_save_fromStation":"%u4E0A%u6D77%2CSHH"})
b.cookies.add({"_jc_save_fromDate":"2016-01-20"})
b.cookies.add({u'_jc_save_toStation':'%u6C38%u5DDE%2CAOQ'})
b.cookies.add({u'_jc_save_toStation':'xxxxxx'})
b.reload()
b.find_by_text(u"查询").click()