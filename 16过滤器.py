#过滤器与map比较像，也是可以接收函数和集合
def getNum(s):
    return s%2 == 0

print(list(filter(getNum,[1,2,3,4,5,6,7,8])))