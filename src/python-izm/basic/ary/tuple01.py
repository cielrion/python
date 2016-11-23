# -*- coding: utf-8 -*-
import datetime

# tupleの使い方
# 括弧()で囲む
# 要素の変更「不可」
# インデックスは0から開始

def get_today():
    today = datetime.datetime.today()
    value = (today.year, today.month, today.day)

    return value

test_tuple = get_today()
print(test_tuple)
print(test_tuple[0])
print(test_tuple[1])
print(test_tuple[2])
