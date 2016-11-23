# -*- coding: utf-8 -*-
import datetime

# 日付の計算
today = datetime.datetime.today()

# 今日の日付
print(today)

# 明日の日付
print(today + datetime.timedelta(days=1))
newyear = datetime.datetime(2010,1,1)

# 2010/01/01の1週間後
print(newyear + datetime.timedelta(days=7))

# 2010/01/01から今日までの日数
calc= today- newyear
print(calc.days)
