# 任何集合都可以迭代，比如dict
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)

for value in d.values():
    print(value)

for k,v in d.items():
    print(k,v)

#如果要对list实现类似Java那样的下标循环怎么办？
#Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身：
for i, value in enumerate(['A', 'B', 'C']):
    print(i,value)

