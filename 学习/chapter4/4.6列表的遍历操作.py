lst=['hello','world','python','php']

for item in lst:
    print(item)

#使用for 循环，range（）函数，len（）函数，根据索引进行遍历
for i in range(0,len(lst)):
    print(i,"-->",lst[i])

#enumearte()函数   #枚举
for index,item in enumerate(lst):#index序号，item为内容
    print(index,item)

print('-'*15)

#手动设置序号起始值
for index,item in enumerate(lst,start=1):
    print(index,item)

print('-'*15)

for index,item in enumerate(lst,1):
    print(index,item)