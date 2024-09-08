d={'hello':10,'world':20,'python':30}
#访问字典中的元素
#（1）使用d【key】
print(d['hello'])
#(2)d.get(key)
print(d.get('hello'))

#二者区别为key不存在，d【key】报错，d.get(key)可以指定默认值
print(d.get('java'))#NONE
#print(d['java'])#KeyError: 'java'
print(d.get('java','不存在'))


#字典的遍历
for item in d.items():
    print(item)#key=value组成一个元素

#在使用for循环遍历时，分别获取key和value
for key,value in d.items():
    print(key,'--->',value)
