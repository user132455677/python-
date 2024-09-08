fp=open("note.txt","w")#打开文件-->write
print("北京欢迎你",file=fp)#将北京欢迎你输出（写入）到note.txt
fp.close()#关闭文件