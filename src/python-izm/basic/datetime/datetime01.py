# -*- coding: utf-8 -*-
import datetime
today  = datetime.date.today()
todaydetail = datetime.datetime.today()

# 今日の日付
div = "----------------------------"
print(div)
print(today)
print(todaydetail)

# 今日に日付：それぞれの値
print(div)
print(today.year)
print(today.month)
print(today.day)
print(div)
print(todaydetail.year)
print(todaydetail.month)
print(todaydetail.day)
print(todaydetail.minute)
print(todaydetail.second)
print(todaydetail.microsecond)

#  日付のフォーマット
print(div)
print(today.isoformat())
print(todaydetail.strftime("%Y/%m/%d %H:%M:%S"))
