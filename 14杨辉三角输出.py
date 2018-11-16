#练习
#杨辉三角定义如下：

#           1
#          / \
#         1   1
#        / \ / \
#       1   2   1
#      / \ / \ / \
#     1   3   3   1
#    / \ / \ / \ / \
#   1   4   6   4   1
#  / \ / \ / \ / \ / \
# 1   5   10  10  5   1
# 把每一行看做一个list，试写一个generator，不断输出下一行的list：
#算法如下，zip()方法是讲两个或者多个迭代器依次组成一个个元组对象，总个数以较短的为准
#当前方法是讲前一个对象右边和左边分别补0，这样就做到了左右相加为新数字方法
def yhtri():
    a=[1]
    while 1:
        yield a
        a = [x+y for x,y in zip(a+[0],[0]+a)]

o=yhtri()
for n in range(10):
    print(next(o))
# a = [1,2,1]
# b = zip(a+[0],[0]+a)
# for x,y in b:
#     print(x,"--------------",y)
    
# print(list(b))
# x = [x+y for x,y in zip(a+[0],[0]+a)]
# print(x)