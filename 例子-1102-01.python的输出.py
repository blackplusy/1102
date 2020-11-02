#coding=utf-8
#设置字符集
#相当于翻译官
#中文字符集GBK2312
#1.直接输出
#数字   123
#字符 abc
print(1000)
print('哈勒少！！')

#2.变量输出
#python中所有的符号都一定是英文
#变量:可以变化的值，相当于一个容器
a='告诉你妈晚上你不回家,我给你看我写的代码！！！'
#a是变量的名字,等号后面是变量的值
#print()函数可以对数据和变量进行输出
print(a)
a=100
print(a)
#变量操作后输出
a=100
b=20
print(a+b)
a='HeyGor'
b='真帅！！！'
print(a+b)
#3.函数输出
#系统中会有很多自带函数，可以进行操作
#abs()    绝对值
#len()    长度
print(abs(-2))
print(len('kouniqiwa'))

#4.格式化输出
# %s 接受变量传回来的字符类型数据
# %d 接受变量传回来的数值类型数据
# 输出内容如果只有一个变量值不需要加括号，多个的话需要加括号
name='heygor'
num=1
print('%s is no.%d'%(name,num))

name='gaga'
print('your name is %s' % name)












