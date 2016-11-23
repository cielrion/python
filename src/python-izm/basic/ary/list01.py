# -*- coding: utf-8 -*-
div="---------------------"
# リストの基本
print(div + 'list = []' + div)
list = ['h', 'e', 'l', 'l', 'o']
print(list)
for i in list:
    print(i)

# 要素を末尾に追加 append(value)
print(div+ 'append(value)' + div)
list2 = []
print(list2)
list2.append('w')
list2.append('o')
list2.append('r')
list2.append('l')
list2.append('d')
print(list2)

# インデックスを指定して追加 insert(index)
list3 = ['hello', 'world', '!']
print(list3)
print(div + 'insert(index)' + div)
list3.insert(1,'-')
list3.insert(3,'?')
print(list3)
list3.insert(0,'Hi, ')
print(list3)

# 最初に見つかった要素の削除 remove(value)
list4 = [1, 2, 3, 4, 5, 4, 3, 2, 1]
print(div + 'remove(value)' + div)
print(list4)
list4.remove(1)
print(list4)
list4.remove(1)
print(list4)

# 指定インデックスに存在する要素の削除 pop(index)
# 引数なしで、末尾削除 pop()
list5 = [1, 2, 3, 2, 1]
print(div + 'pop(index)' + div)
print(list5)
list5.pop(2)
print(list5)
print(list5.pop())
print(list5)

# 最初に見つかった要素のインデックスを取得 index(value)
list6 = [100, 200, 300, 200, 100]
print(div + 'index(value)' + div)
print(list6)
print(list6.index(200))

# リスト内での要素の格納数を取得 count(value)
print(div + 'count(value)' + div)
print(list6)
print(list6.count(200))
