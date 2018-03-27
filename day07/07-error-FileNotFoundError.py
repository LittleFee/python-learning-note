file_name='FileNotFoundError.txt'
try:
    with open(file_name) as file_object:
        file=file_object.read()
except FileNotFoundError:
    print('Opps the file '+file_name+' doesn\'t exist!')
else:
    print(file)

# 方法split()以空格为分隔符将字符串分拆成多个部分，并将这些部分都存储到一个列表中。
def count_words(file_name):
    """统计文件中有多少个单词"""
    try:
        with open(file_name) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        print('Sorry,the file ' + file_name + '  doesn\'t exist!')
        # 失败时一声不吭
        # pass
        # Python有一个pass语句，可在代码块中使用它来让Python什么都不要做
    else:
        words = contents.split()
        num = len(words)
        print(file_name + ' has ' + str(num) + ' words.')

file_list=['guest.txt','null.txt','alice.txt']
for file in file_list:
    count_words(file)