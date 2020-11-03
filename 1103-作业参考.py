#coding=utf-8
num=int(input('your num'))
ge=num%10
shi=num%100//10
bai=num//100
#print(ge,shi,bai)

if ge**3+shi**3+bai**3==num:
    print('水仙花数！')
else:
    print('不是水仙花！')
