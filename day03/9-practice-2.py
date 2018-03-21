# 对于下面列出的各种测试，
# 至少编写一个结果为True 和False 的测试。
#  检查两个字符串相等和不等。
#  使用函数lower()的测试。
#  检查两个数字相等、不等、大于、小于、大于等于和小于等于。
#  使用关键字and 和or 的测试。
#  测试特定的值是否包含在列表中。
#  测试特定的值是否未包含在列表中。
baby='FYX'
if baby=='FYX' :
    print('True')
if baby=='QW' :
    print('True')
else:
    print('False')
if baby.lower()=='fyx':
    print('True')
baby='QW'
if baby.lower()!='qw':
    print('True')
else:
    print('False')
num_1=23
if num_1==23:
    print('=23')
if num_1 > 0:
    print('>0')
if num_1 < 24 :
    print('<24')
if num_1<=23 :
    print('<=23')
if num_1>=23:
    print('>=23')

if (num_1>1) and (num_1<24):
    print('1<num_1<24')
if (num_1>0) or (num_1<23):
    print('true')

lists=['baby','fyx','qw']
if 'fyx' in lists :
    print('in')
if 'pop' not in lists:
    print('not in')