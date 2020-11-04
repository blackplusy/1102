#coding=utf-8
dic={'name':'8jie','age':18}
dic1={'name':'o8ma'}
#直接访问
print(dic)
#数据筛选
print(dic['name'])
print(dic['age'])
#删除字典
dic={'name':'8jie','age':18}

print(dic)

del dic['name']
print(dic)

del dic
#print(dic)
#clear 清空字典
dic={'name':'8jie','age':18}
print(dic)
dic.clear()
print(dic)

#字典的修改
dic={'name':'8jie','age':18}
print(dic)
dic['name']='tangsir'
print(dic)
#keys
dic={'name':'8jie','age':18}
print(dic.keys())
for i in dic.keys():
    print(i)
#values
dic={'name':'8jie','age':18}
print(dic.values())
for i in dic.values():
    print(i)

#items
dic={'name':'8jie','age':18}
print(dic.items())

for key,value in dic.items():
    print(str(key)+':'+str(value))















