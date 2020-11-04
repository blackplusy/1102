#coding=utf-8
dic1={'admin':'123','user1':'456','user2':'123'}
while 1:
    name=input('请输入用户名：')
    if name in dic1.keys():
        print('用户名正确')
        while 1:
            passwd=input('请输入用户名对应的密码:')
            if dic1['admin']==passwd:
                print('登录成功')
                break
            else:
                print('密码有问题')
        break
            
    else:
        print('用户名有问题')

