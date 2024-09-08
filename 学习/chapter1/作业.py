fp=open("note.txt","w")
print('人生苦短我用python',file=fp)
fp.close()


a=input('请输入您的姓名：')
b=input('请输入您的年龄：')
c=input('请输入您的座右铭：')
print("------自我介绍-------")
print('姓名：'+a)
print('年龄：'+b)
print('座右铭：'+c)