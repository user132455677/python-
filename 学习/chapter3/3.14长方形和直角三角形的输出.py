#三行四列
#for i in range(1,4):
#    print("*"*4 )

for i in range(1,4):
    for j in range(1,5):
        print("*",end="")
    print()
print("-"*15)

for i in range(1,6):
    for j in range(i):
        print("*",end="")
    print()#转行用