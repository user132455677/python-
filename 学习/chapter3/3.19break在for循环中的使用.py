for i in "hello":
    if i==="e":
        break
    print(i)

print('-'*15)

for i in range(3):
    user_name=input("输入用户名:")
    pwd = input('请输入密码：')
    if user_name == 'ysj' and pwd == '88888':
        print("系统正在登录")
        break
    else:
        if i < 2:
            print("不正确，您还有",2-i,"次机会")