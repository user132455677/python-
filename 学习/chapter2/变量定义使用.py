luck_num=8 # 创建一个整数变量，并为其赋值为8


my_name = "一二三" #字符串类型变量

print("luck_num的数据类型是：",type(luck_num))#int
print(my_name,"的幸运数字是",luck_num)

#python动态修改变量的数据类型，通过不同类型的复制就可以修改
luck_num="北京欢迎你"
print("luck_num的数据类型是",type(luck_num))#str

#在python中允许多个变量指向同一个值
no=number=1024
print(no,number)
print(id(no))#id()查看对象的内存地址
print(id(number))