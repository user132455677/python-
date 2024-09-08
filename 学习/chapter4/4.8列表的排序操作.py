lst=[4,56,3,78,40,56,89]
print('原列表：',lst)

#排序，默认是升序
lst.sort()#排序是在原列表基础上进行,不会产生新的列表对象
print('升序：',lst)

#排序降序
lst.sort(reverse=True)
print('降序',lst)

print("-"*15)
lst2=['banana','apple','Cat','Orange']
print('原列表：',lst2)

#升序
lst2.sort()
print("升序：",lst2)#按ASCII 大写字母比小写字母小32，所以先大写

#降序，小排小写后大写
lst2.sort(reverse=True)
print('降序：',lst2)

#忽略大小写比较
lst2.sort(key=str.lower)#lower此处为参数，参数不加括号,调用加括号,都转成小写
print('降序：',lst2)
