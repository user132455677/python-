#倒三角
for i in range(1,6):
    for j in range(6-i):
        print("*",end="")
    print()

print("-"*15)

#等腰三角形
#x=4
#for i in range(1,6):
#    print(" "*x,end="")
#    for j in range(i*2-1):
#       print("*",end="")
#    x-=1
#   print()

for i in range(1,6):
    #打印倒三角
    for j in range(1,6-i):
        print(" ",end="")
    for k in range(1,i*2):
        print("*",end="")
    print() #当两个并列的for 循环执行完毕后在换行
