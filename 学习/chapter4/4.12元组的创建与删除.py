#小括号创建
t=('hello',[10,20,30],'python','world')
print(t)

#tuple（）
t=tuple('helloworld')
print()

t=tuple([10,20,30,40])
print(t)

print('10再元组中是否存在？',(10 in t))
print('10在元组中是否不存在？',(10 not in t))
print('最大值',max(t))
print('最小值',min(t))
print('len:',len(t))
print('t.index',t.index(10))
print('t.count',t.count(10))

#只有一个元素
t=(10,)
print(t,type(t))
#如果只有一个元素，逗号不能省

#删除
del t
#print(t)