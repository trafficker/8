from datetime import datetime
dt=datetime.strptime(timesource,'%Y年%m月%d日%H:%M')
#字串转时间
dt.strftime('%Y-%m-%d')