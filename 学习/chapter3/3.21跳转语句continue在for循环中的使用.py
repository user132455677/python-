s=0
for i in range(1,101):
    if i%2==1:
        continue
    s+=i
print("1-100偶数和为",s)