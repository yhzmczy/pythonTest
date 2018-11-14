#以做一个数的n次方的函数，参数有默认值
def power(i,n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * i
    return s

print(power(5))
print(power(5,3))
#定义默认参数要牢记一点：默认参数必须指向不变对象！否则失败的情况如下，默认值会变动：
#Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。
def add_end(L=[]):
    L.append('END')
    return L

print(add_end())
print(add_end())
print(add_end())
#较好的做法
def add_end2(L=None):
    if L is None:
        L = []
    L.append('END')
    return L

print(add_end2())
print(add_end2())
print(add_end2())
