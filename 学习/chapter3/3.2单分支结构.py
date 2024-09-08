number=eval(input("请输入您的6位中奖号码："))
#if
if number==987654: #等值判断
    print("恭喜您中奖了！")


if number!=987654:
    print("您没中奖！")

n=98#赋值
if n%2: #98%2的余数是False 0的布尔值为False 非0的布尔值为True
    print(n,"是奇数") #由于98%2余数为零所以不执行

if not n%2: #98%2余数为零 0是False 取反为True
    print(n,"为偶数")

#如何判断一个字符串是否为空字符串
x=input("请输入一段话")
if x:#再py中一切都为对象，每个对象都有一个布尔值，而非空字符串的布尔值为True，空字符串的布尔值为False
    print("x是一个非空字符串")

if not x:
    print("x是一个空字符串")

#表达式也可以是个纯粹的布尔型变量
flag=eval(input("请输入一个布尔类型的值："))
if flag:
    print("flag的值为True")
if not flag:
    print("flag的值为False")

#使用if语句时如果语句中只有一句代码，可以直接将语句块写在冒号后面
a=10
b=5
if a>b:max=a#语句块就只有一句
print("a和b的最大值为：",max)
