#初始化变量
i=0
#条件判断
while i<3:
    #语句块
    user_name=input("请输入用户名")
    pwd=input("请输入您的密码")
    if user_name=="wby" and pwd=="888888":
        print("系统正在登陆请稍后")
        #改变循环变量，目的退出循环
        i=8 #第三行判断后False退出循环
    else:
        if i<2:
            print("用户名或密码不正确，您还有",2-i,"次机会")
        i+=1#改变变量

#单分支判断
if i==3:#当用户名或密码输入三次不正确的时候，循环执行结束，i最大值为三
    print("对不起三次均输入错误")