#创建二维列表
lst=[
    ['城市','环比','同比'],
    ['北京',102,103],
    ['上海',104,504],
    ['深圳',100,59]
]
print(lst)

#遍历二位列表使用双层for 循环
for row in lst:#行
    for item in row:#列
        print(item,end='\t')
    print()

#列表生成4行5列的二位列表
lst2=[[j for j in range(5)]for i in range(4)]
print(lst2)