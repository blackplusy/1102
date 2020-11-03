#coding=utf-8
#1000以内水仙花数
for i in range(100,1000):
    if (i%10)**3+(i%100//10)**3+(i//100)**3==i:
        print('水仙花数为%d' % i)

#1000以内的奇数
for i in range(1000):
    if i%2==1:
        print(i)
    
#提示，空格和*的规律
        
