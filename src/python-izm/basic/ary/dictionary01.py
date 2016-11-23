# -*- coding: utf-8 -*-
div="---------------------"

# ディクショナリ
# key, valueのセット
print(div +'dictionary = {key:value}' + div)
dic = {1:100, 2:200, 3:300}
print(dic)
for i in dic:
    print('key = ' + str(i), end=', ')
    print('value = ' + str(dic[i]))
