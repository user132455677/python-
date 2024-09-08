x=10
y=3
z=x/y#执行除法运算时，将运算结果赋值给z
print(z,type(z))


#float转成int，只保留整数部分
print("float转成int类型",int(3.14))
print("float转成int类型",int(3.9))
print("float转成int类型",int(-3.14))
print("float转成int类型",int(-3.9))

#int转成float类型
print("int转成float类型",float(10))
#str转成int类型
print(int("100")+int("200"))
#将字符串转换成int活float报错情况
#print(int("18a"))#a不是十进制的数
#print(int("3.14"))#3.14不是整数
#print(float("45a,987"))#a无法转

#chr()ord()一对
print(ord("杨"))#杨在Unicode表中对应的整数值
print(chr(26472))#26472整数在Unicode表中对应的字符

#进制之间的转换操作，十进制与其他进制之间的转换
print("十进制转成十六进制",hex(26472))
print("十进制转成八进制",oct(26472))
print("十进制转成二进制",bin(26472))#转换后为字符串类型（以上三个