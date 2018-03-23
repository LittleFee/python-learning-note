# 8-6 城市名：编写一个名为city_country()的函数，它接受城市的名称及其所属的
# 国家。这个函数应返回一个格式类似于下面这样的字符串："Santiago, Chile"
# 至少使用三个城市国家对调用这个函数，并打印它返回的值。
def city_country(city,country):
    """创建城市国家字符串"""
    string=city.title()+','+country.title()
    return string

print(city_country('Nanchong','china'))
print(city_country(country='japan',city='tokoyo'))


# 8-7 专辑：编写一个名为make_album()的函数，它创建一个描述音乐专辑的字典。
# 这个函数应接受歌手的名字和专辑名，并返回一个包含这两项信息的字典。使用这个函
# 数创建三个表示不同专辑的字典，并打印每个返回的值，以核实字典正确地存储了专辑
# 的信息。
# 给函数make_album()添加一个可选形参，以便能够存储专辑包含的歌曲数。如果调
# 用这个函数时指定了歌曲数，就将这个值添加到表示专辑的字典中。调用这个函数，并
# 至少在一次调用中指定专辑包含的歌曲数。

def make_album(singer,name,num=0):
    """创建专辑信息"""
    album={}
    if num:
        album['singer']=singer
        album['name']=name
        album['number']=num
    else:
        album['singer'] = singer
        album['name'] = name

    return album

album=make_album('jaychou','qilixiang')
print(album)
album=make_album('xusong','youhebuke',1)
print(album)
album=make_album('xuwei','Blue Lotus')
print(album)


# 8-8 用户的专辑：在为完成练习8-7 编写的程序中，编写一个while 循环，让用户
# 输入一个专辑的歌手和名称。获取这些信息后，使用它们来调用函数make_album()，并
# 将创建的字典打印出来。在这个while 循环中，务必要提供退出途径。
def end():
    """结束前打印字符串"""
    print('Opps...Byebye')
    
while True:
    print('enter q to quit ')
    singer=input('Tell me name of singer: ')
    if singer.lower()=='q':
        end()
        break
    name=input('Tell me name of album: ')
    if name.lower()=='q':
        end()
        break
    num=input('Number? ')
    if num == 'q':
        end()
        break
    print(make_album(singer,name,num))
