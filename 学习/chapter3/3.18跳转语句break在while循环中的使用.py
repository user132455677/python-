s=0 #存储累加和
i=1#初始化变量
while i<11:#条件判断
    #语句块
    s+=1
    if s>20:
        print("累加和大于20的当前数是：",i)
        break
    i+=1#改变变量

print('-'*11)
i=0#统计登录次数
while i<3:
    user_name=input("请输入用户名:")
    pwd=input("请输入密码：")
    if user_name=='ysj' and pwd=='88888':
        print("正在登陆")
        break
    else:
        if i<2:
            print('用户名不正确，您还有',2-i,"次机会")
    i+=1
else:
    print("三次均错误")
