#coding=utf-8
#直接访问
l1=['李元芳','李白','钟馗']
print(l1)
#遍历访问
for i in l1:
    print(i)
#成员访问
if '张小敬' in l1:
    print('长安')
else:
    print('not here!')

#列表索引和切片
l1=['马超','赵云','黄忠','张飞','关羽']
print(l1[0])
print(l1[-2])
#print(l1[5])
#列表的拼接
l1=[1,2,3]
l2=[4,5]
print(l1+l2)
#列表更新
l=[1,2,3,4,5]
print(l)
l[2]='simida'
print(l)
l[-2]='kouniqiwa'
print(l)
#列表的删除
l=[1,2,3]
print(l)
del l[2]
print(l)
del l
#print(l)







