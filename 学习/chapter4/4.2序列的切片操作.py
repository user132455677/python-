s=('helloworld')
#切片
s1=s[0:5:2]#0开始5结束（不包含），步长为2
print(s1)
#省略开始，start默认零开始
print(s[:5:1])
#省略start 省略step
print(s[:5:])
#省略结束
print(s[0::1])#默认到最后一个元素（包含）

print(s[5::])
print(s[5:])

print(s[0:5:2])

print(s[::2])#02468
#步长为负数

print(s[::-1])
print(s[-1:-11:-1])