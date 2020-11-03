#coding=utf-8
#1000以内水仙花数
for i in range(100,1000):
    if (i%10)**3+(i%100//10)**3+(i//100)**3==i:
        print('水仙花数为%d' % i)

#1000以内的奇数
'''
for i in range(1000):
    if i%2==1:
        print(i)
'''
#打印菱形
#提示，空格和*的规律
#方法1：
for i in range(-3,4):
    if i<0:
        a=-i
    else:
        a=i
    print(a*' '+'*'*(7-a*2))
#方法2:
'''
n=int(input('输入一个数'))
c=n//2
for i in range(-c,c+1):
    a=-i if i<0 else i
    print(a*' '+'*'*(n-a*2))
'''
#99乘法表
#end在格式化输出中表示不换行显示
for i in range(1,10):
    for j in range(1,i+1):
        print(str(i)+'*'+str(j)+'='+str(i*j),end=" ")
    print()
