s='helloworld'
#in
print('e在helloworld里存在吗',('e'in s))
print('v在helloworld里存在吗',('v'in s))
#not in
print('e在helloworld里不存在吗',('e'not in s))
print('v在helloworld里不存在吗',('v'not in s))

#内置函数
print('len():',len(s))
print('max():',max(s))#按照ASCII
print('min():',min(s))#按照ASCII

#序列对象的方法，使用序列的名称，打点调用
print('s.index():',s.index("o"))
#print('s.index():',s.index('v'))#v在字符串中根本不存在，不存在所以找不到位置
print('s.count():',s.count("o"))