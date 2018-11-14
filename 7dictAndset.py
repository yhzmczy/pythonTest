#类似java的map
d = {'Michael':95,'Bob':75,'Tracy': 85}
#插入数据
d['Jerry']=100
print(d)
#查询数据，如果key错误会有异常
print(d['Michael'])
#另外的查询方式,key错误返回None，也可以指定错误后的返回值
print(d.get('Mi'))
print(d.get('Mi',-1))
#删除key，和集合中方法一样，用pop
d.pop('Jerry')
print(d)
#set只有key没有value，但是可以去重
s = set([1, 1, 2, 2, 3, 3])
print(s)
#新增
s.add(4)
print(s)
#删除
s.remove(1)
print(s)
s2=set([5,1,2,7])
#运算
print(s&s2)
print(s|s2)