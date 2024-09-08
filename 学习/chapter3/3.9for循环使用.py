#遍历字符串
for i in "hello":
    print(i)
#range()函数，python中的内置函数，产生一个[n,m)的整数序列，包含n但不包含m
for i in range(1,11):
    if i%2==0:
        print(i,"是偶数")
#计算1~10的累加和
s=0 #用于存储累加和
for i in range(1,11):
    s+=i

print("累加和为",s)
#100到999的水仙花数

for i in range(100,1000):
    sd=i%10
    tens=i//10%10
    huns=i//100%10
    if sd**3 + tens**3 + huns **3 == i:
        print(i,"是水仙花数")