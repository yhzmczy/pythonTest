#可变参数的函数：给定一组数字a，b，c……，请计算a2 + b2 + c2 + ……。
#老思路是参数为一个集合
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

l=[1,2,3,4]
print(calc(l))
#新思路为可变参数
def calc2(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

print(calc2(1,2,3,4))
#如果参数是集合也可以调用
print(calc2(*l))

#关键字参数
#可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
#而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。
def person(name, age, **kw):
    if 'city' in kw:
        # 有city参数
        pass
    if 'job' in kw:
        # 有job参数
        pass
    print('name:', name, 'age:', age, 'other:', kw)

person('Michael', 30)
person('Bob', 35, city='Beijing')
person('Adam', 45, gender='M', job='Engineer')

#另一种玩法
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **extra)

#限制关键字参数的名字
def person2(name, age, *, city, job):
    print(name, age, city, job)

#调用方法
person2('Jack', 24, city='Beijing', job='Engineer')