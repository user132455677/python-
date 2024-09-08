row=eval(input("输入行数"))
while row%2==0:
    print("请重新输入")
    row=eval(input("请输入行数"))
top_row=(row+1)//2#上半部分行数
#上半部分
for i in range(1,top_row+1):
    #打印倒三角
    for j in range(1,top_row+1-i):
        print(" ",end="")
    for k in range(1,i*2):
        if k==1 or k==i*2-1:
            print("*",end="")
        else:
            print(" ",end="")
    print() #当两个并列的for 循环执行完毕后在换行

#下半部分
bottom_row=row//2
for i in range(1,bottom_row+1):
    #直角三角形
    for j in range(1,i+1):
        print(" ",end="")
    #倒三角
    for k in range(1,2*bottom_row-2*i+2):
        if k==1 or k==2*bottom_row-2*i+2-1:
            print("*",end="")
        else:
            print(" ",end="")

    print()