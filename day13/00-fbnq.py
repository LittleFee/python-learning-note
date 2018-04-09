# 斐波那契数（一种数列，其中每个数都是前两个数的和）
f=[0,1]
for i in range(0,100):
    f.append(f[-1]+f[-2])

print(f)