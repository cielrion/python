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

# valueの取得 get(value)
# get()を使うとkeyが存在しないときでもエラー終了しない
dic2 = {'yyyy' : 2016, 'mm': 11, 'dd': 23}
print(div + 'get(value)' + div)
print(dic2['yyyy'])
# print(dic2['yyyyy']) # KeyError(エラー終了)
print(div)
print(dic2.get('yyyy'))
print(dic2.get('yyyyy'))
print(div)
print(dic2.get('yyyy', 'Not Found'))
print(dic2.get('yyyyy', 'Not Found'))

# 要素の追加
dic3 = {}
print(div + 'add value' + div)
print(dic3)
dic3['yyyy'] = 'YEAR'
dic3['mm'] = 'MONTh'
dic3['dd'] = 'DAY'
print(dic3)

# 要素の削除 del(key)
print(div +'del dict[key]' + div)
dic4 = {1: 'hello', 2: 'world', 3:'!'}
print(dic4)
del dic4[2]
print(dic4)

# key/valueだけを取得 keys() values()
print(div + 'keys() / values()' + div)
dic5 = {1:10, 2:20, 3:30}
print(dic5)
print(dic5.keys())
print(dic5.values())

# keyとvalueを同時に取得 item()
print(div + 'items()' + div)
dic6 = {5:50, 6:60, 7:70}
print(dic6)
print(dic6.items())
for key, value in dic6.items():
    print(str(key) + ':' + str(value))

# keyの存在確認 key in dict
print(div + 'key in dict' + div)
dic7 = {'apple': 100, 'banana': 150, 'orange':200}
print('apple is dictionary? ' + str('apple' in dic7))
print('napple is dictionary? ' + str('napple' in dic7))
