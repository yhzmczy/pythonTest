#递归方式计算阶乘
def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)

print(fact(100))
#由于栈深度有限，fact(1000)就会报错
#这个时候需要用尾递归处理，也就是每次返回是函数本身,但是python编译器没有做相关优化，所以还是会有问题
def fact2(num,product):
    if num == 1:
        return product
    return fact2(num - 1, num * product)

def p(n):
    return fact2(n,1)

print(p(100))

#汉诺塔算法：
def move(n, a, b, c):
    if n ==1:
        print(a, '-->', c)
        return
    else:
        move(n-1, a, c, b)
        print(a, '-->', c) 
        move(n-1, b, a, c)

move(8,'A','B','C')