#有时候，执行操作前必须检查列表是否包含特定的值 可以用 in
# 检查不包含的话用not in
things=['ball','tool','car','GF']
if 'GF' in things :
    print('Ha? you have a GF?')
if 'BF' not in things :
    print('Ha! you dont have a BF!')