s="3.14+3"
print(s,type(s))
x=eval(s)#使用eval函数去掉s中左右的引号
print(x,type(x))

#eval函数经常与input一起使用，用来获取用户输入的数值
age=eval(input("请输入您的年龄："))#将字符串类型转换成int类型，相当于int（）
print(age,type(age))

height=eval(input("请输入您的身高："))
print(height,type(height))

hello="北京欢迎你"
print(hello)
print(eval(hello))#也能成功输出,因为输出的是hello，去掉的是变量hello的引号而非其赋的值
#print(eval("北京欢迎您"))#无法输出