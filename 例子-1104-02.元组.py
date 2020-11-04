#coding=utf-8
#元组定义
tup=(1)
print(tup)
print(type(tup))

tup=(2,)
print(type(tup))
#元组访问
a=(1,2,3)
print(a)

for i in a:
    print(i)

if 3 in a:
    print('here!!')

#元组删除
a=(1,2,3)
del a
#print(a)

#元组的切片和索引
tup=(1,2,3)
print(tup[0])
print(tup[-2])
print(tup[1:2])
print(tup[2:])

#补充
tup=(1,2,3,4,5,3,3,3,3)
print(len(tup))
print(max(tup))
print(min(tup))
print(tup.index(3))
print(tup.count(3))






