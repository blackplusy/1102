#coding=utf-8
#读文件
#定义一个变量接受open函数打开文件后的内容
file=open('D:\\test.txt','r',encoding='utf8')
print(file)
for i in file:
    print(i)
file.close()


#写文件
str1='oh my dear baby!'
file=open('D:\\test1.txt','w')
file.write(str1)
file.close()
print('OK了')


#追加文件
file=open('D:\\test.txt','a')
file.write('sailanggei\n')
file.close()
print('OK了')
