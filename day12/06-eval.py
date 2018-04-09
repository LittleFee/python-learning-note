# eval
# eval是一个类似于exec的内置函数。exec执行一系列Python语句，而eval计算用字符串表示
# 的Python表达式的值，并返回结果（exec什么都不返回，因为它本身是条语句）。例如，你可使
# 用如下代码来创建一个Python计算器：
# >>> eval(input("Enter an arithmetic expression: "))
# Enter an arithmetic expression: 6 + 18 * 2
# 42

result=eval(input("Enter an arithmetic expression: "))
print(result)