#字符串遍历
for a in "abc":
    print(a)

print('--------------------')
#集合遍历
classmates = ['Michael', 'Bob', 'Tracy']
for b in classmates:
    print(b)

print('--------------------')
#数字计算
sum = 0
for c in range(5):
    sum += c

print(sum)
print('--------------------')
#循环的另一种实现
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
    if n<50:
        print('break n:',n)
        break
    else :
        print('continue n:',n)
        continue
print(sum)