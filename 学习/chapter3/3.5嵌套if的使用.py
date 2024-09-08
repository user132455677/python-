answer=input("请问您喝酒了吗？")
if answer=="y":#answer 为 y表示喝酒了
    proof=eval(input("请输入酒精含量："))
    if proof<20:
        print("不构成酒驾")
    elif proof<80:
        print("已构成酒驾标准")
    else:
        print("已达到醉驾标准")
else:
    print("你走吧")