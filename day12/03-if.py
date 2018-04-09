name = input('What is your name?')
if name.endswith('Gumby'):
 print('Hello, Mr. Gumby')
else:
 print('Hello, stranger')

# 三目运算符
status = "friend" if name.endswith("Gumby") else "stranger"
print(status)

score = input('Score: ')
grade = '不及格' if  int(score) < 60 else '及格'
print(grade)

# 关键字assert
age = 23
assert 0 < age < 100
# age=-12
# assert 0 < age < 100
# Traceback (most recent call last):
#   File "D:/python-learning-note/day12/03-if.py", line 19, in <module>
#     assert 0 < age < 100
# AssertionError
