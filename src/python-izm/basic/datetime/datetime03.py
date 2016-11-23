# -*- coding: utf-8 -*-
import calendar

# うるう年の判定
print("うるう年の判定".encode(encoding='utf_8'))
print(calendar.isleap(2015))
print(calendar.isleap(2016))
print(calendar.isleap(2017))

# うるう年が何回あるかの判定
print(calendar.leapdays(2010,2020))
