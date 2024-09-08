for i in range(1,10):
    for j in range(1,i+1):
        print(str(j)+'*'+str(i)+'='+str(i*j),end="\t")#字符串连接用+，其余用，\t为制表符为一个tab
    print()