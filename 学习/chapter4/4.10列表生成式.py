import random
lst=[item for  item in range(1,11)]
print(lst)

lst=[item*item for item in range(1,11)]
print(lst)

lst=[random.randint(1,100) for _ in range(10)]#_为函数名，代替item
print(lst)

#从列表中选择符合条件的元素组合成新的列表
lst=[i for i in range(10) if i%2==0]
print(lst)