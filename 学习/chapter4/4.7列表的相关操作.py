lst=['hello','world','python']
print('原列表',lst,id(lst))
#增加元素的操作
lst.append('sql')
print('增加元素之后:',lst,id(lst))
#使用insert(index,x)在指定位置插入x
lst.insert(1,100)
print(lst)

#列表元素的删除操作
lst.remove('world')
print('删除元素后的列表',lst,id(lst) )

#使用pop（index）根据索引将元素取出，然后再删除
print(lst.pop(1))
print(lst)

#清楚所有元素
# lst.clear()
# print(lst,id(lst))
# #ctrl+?选中全注释

#列表的逆向输出
lst.reverse()#不会产生新的列表，在原列表基础上进行
print(lst)

#列表的拷贝，将产生一个新的列表对象
new_lst=lst.copy()
print(lst,id(lst))
print(new_lst,id(new_lst))

#列表元素的修改操作
lst[1]='mysql'
print(lst)



