#生成器和列表生成器比较像，将规则确定好之后就可以输出，例子如下：
g = (x * x for x in range(10))
#和列表的区别在于把[]变成()，通过next()方法获取下一个值
# for a in range(10):
#     print(next(g))
#也可以通过迭代搞定
for n in g:
    print(n)

#打印斐波拉切函数，传统做法
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'

fib(5)
#转换为生成器，只需要在输出的地方改成yield，一个函数只要带这个关键字说明就是一个生成器
#generator和函数的执行流程不一样。函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
#变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
def gen(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

#解释yield的例子
# def odd():
#     print('step 1')
#     yield 1
#     print('step 2')
#     yield(3)
#     print('step 3')
#     yield(5)

# o=odd()
# for s in range(4):
#     next(o)

#拿返回值的方法，其实就是作为异常抛出来的
g = gen(6)
while True:
     try:
         x = next(g)
         print('g:', x)
     except StopIteration as e:
         print('Generator return value:', e.value)
         break