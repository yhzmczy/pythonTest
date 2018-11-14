classmates = ['Michael', 'Bob', 'Tracy']
print(classmates)
print(classmates[0])
#获取最后一个元素,-2为倒数第二个，依次类推
print(classmates[-1])
#扩充
classmates.append('Adam')
print(classmates)
#插入到指定位置
classmates.insert(1, 'Jack')
print(classmates)
#删除末尾元素
classmates.pop()
print(classmates)
#直接替换
classmates[1] = 'Sarah'
print(classmates)
#混乱数组
L = ['Apple', 123, True]
#数组嵌套
s = ['python', 'java', ['asp', 'php'], 'scheme']
print(len(s))
