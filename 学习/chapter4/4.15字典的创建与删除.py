#(1)创建字典
d={10:'cat',20:'dog',30:'pet',20:'zoo'}#后面的会覆盖前面的
print(d)#key相同的，value进行覆盖

#（2）zip函数
lst1=[10,20,30,40]
lst2=['cat','dog','pet','zoo','car' ]
zipobj=zip(lst1,lst2)
print(zipobj)#<zip object at 0x0000027799E94580>
#print(list(zipobj))#[(10, 'cat'), (20, 'dog'), (30, 'pet'), (40, 'zoo')]
d=dict(zipobj)
print(d)#{10: 'cat', 20: 'dog', 30: 'pet', 40: 'zoo'}

#使用参数创建字典
d=dict(cat=10,dog=20)#左侧cat为key，右侧10是value
print(d)


t=(10,20,30)
print({t:10})#t是key，10是value，元组是可以作为字典中的key

#lst=[10,20,30]
#print({lst:10})#TypeError: unhashable type: 'list'

#字典属于序列
print('max:',max(d))
print("min:",min(d))
print('len:',len(d))
#字典的删除
del d
#字典中key是无序的，在python3.6后解释器进行处理，所以看到的输出顺序为一致

