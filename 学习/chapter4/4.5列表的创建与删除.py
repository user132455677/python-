lst=['hello','world',98,100.5]
print(lst)

#lis()创建列表
lst2=list('helloworld')
lst3=list(range(1,10,2))#从一开始十结束步长为二不带十
print(lst2)
print(lst3)

#表示序列的一种，对序列的操作五，运算符，函数都可使用
print(lst+lst2+lst3)
print(lst*3)
print(len(lst))
print(max(lst3))
print(min(lst3))

print(lst2.count('o'))#计数
print(lst2.index('o'))#查找

#列表的删除操作
lst4=[10,20,30]
print(lst4)
#删除列表
del lst4
#print(lst4)