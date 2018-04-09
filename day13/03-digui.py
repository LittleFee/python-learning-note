# 阶乘
def factorial(n):
    result = n
    for i in range(1,n):
        result *= i
    return result
print(factorial(3))

def digui_fac(n):
    if n == 1:
        return 1
    else:
        return n * digui_fac(n - 1)
print(digui_fac(3))

def pows(x,n):
    if n == 0:
        return 1
    else:
        return x * pows(x,n-1)

print(pows(123,0))
# 1
print(pows(2,3))
# 8

def test(n):
    return n * 23
lsi = [1,1,2,3,4]
d = map(test,lsi)
print(d)

seq = ['34','kiwi','kiwi123','###','@#$Y12']
re = filter(lambda x: x.isalnum(), seq)
for item in re:
    print(item)

