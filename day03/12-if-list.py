# 制作一杯柠檬水，每添加一个材料打印一个成功，但是店里的糖用完了，要提示没有盐，然后打印完成
needs=['salt','water','sugar','lemon']
for need in needs:
    if need=='sugar':
        print("Don't have enough sugar!")
    else:
        print(need+' is done')

print('Done!\n')

# 确定列表不是空的
# needs=[]
if needs:
    for need in needs:
        if need == 'sugar':
            print("Don't have enough sugar!")
        else:
            print(need + ' is done')

    print('Done!')
else:
    print('List is empy !')

all_needs=['salt','water','sugar','watermelon','apple']
for need in needs:
    if need in all_needs:
        print('add '+need+' and done !')
    else:
        print(need+' is not available ')

print('everting is ok')