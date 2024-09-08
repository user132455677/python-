print(True and True)
print(True and False)
print(False and False)
print(False and True)

print("-" * 40)
print(8>7 and 6>5)#T
print(8>7 and 6<5)#F
print(8<7 and 10/0)#False , 10/0并没有被运算，当第一个表达式结果为False，直接的结果

print("-" * 40)
print(True or True)
print(True or False)
print(False or False)#False
print(False or True)

print(8>7 or 10/0)#TRUE 左侧为T，右侧不执行运算

print("-" * 40)
print( not True)#False取反
print( not False)
print( not(8>7) )