#生成[1*1,2*2,3*3...]的列表
L = [x*x for x in range(100)]
print(L)

#还可以加上条件
L2 = [x*x for x in range(100) if x%2==0]
print(L2)

#还可以使用两层循环，可以生成全排列：
L3 = [m + n for m in 'ABC' for n in 'XYZ']
print(L3)