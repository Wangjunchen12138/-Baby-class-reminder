import time
import datetime

class Account_time:
    def account_week(self,start):
        start = time.strptime(start, "%Y%m%d")
        date2 = datetime.datetime.now().timetuple()
        start = datetime.datetime(start[0], start[1], start[2])
        date2 = datetime.datetime(date2[0], date2[1], date2[2])
        differ = date2 - start  # 返回两个变量相差的值，就是相差天数
        weekth = differ // datetime.timedelta(days=7) + 1
        return weekth

    def account_day(self):
        day = datetime.datetime.now()
        day = day.weekday() + 1
        return day

account_time = Account_time()

