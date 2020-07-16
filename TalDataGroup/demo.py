import time

date_time_now = time.strftime("%Y-%m-%d %H:%M", time.localtime())
import datetime




today = datetime.date.today()  # 今天
yesterday = datetime.date.strftime(today - datetime.timedelta(days=1), '%Y-%m-%d')

temp_date_min = date_time_now[11:]
temp_date_day = date_time_now[:10]

print(type(yesterday))
print(yesterday)
# temp_date_min >= "00:00" and temp_date_min <= "00:15" :
