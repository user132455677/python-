x=20#直接赋值
y=10
x=x+y#将x加y的值赋给30
print(x)
x+=y
x-=y
x*=y
print(x)
x/=y
print(x)#发生了类型转换
x%=2
print(x)

z=3
y//=z
print(y)

y**=2

#链式赋值
a=b=c=200
print(a,b,c)

#系列解包赋值
a,b=10,20  #a=10,b=20

#交换变量
a,b=b,a