# 10-3 访客：编写一个程序，提示用户输入其名字；用户作出响应后，将其名字写
# 入到文件guest.txt 中。
file_name='guest.txt'
name=input('What\' your name? ')
with open(file_name,'w') as file_object:
    file_object.write(name)

# 10-4 访客名单：编写一个while 循环，提示用户输入其名字。用户输入其名字后，
# 在屏幕上打印一句问候语，并将一条访问记录添加到文件guest_book.txt 中。确保这个
# 文件中的每条记录都独占一行。
file_name='guest_book.txt'
with open(file_name,'a') as file_object:
    while True:
        name=input('Your name plz(no or quiz): ')
        if name.lower() == 'no':
            break
        else:
            print('Welcome '+name)
            file_object.write(name+'\n')

# 10-5 关于编程的调查：编写一个while 循环，询问用户为何喜欢编程。每当用户输
# 入一个原因后，都将其添加到一个存储所有原因的文件中。
file_name='reasons.txt'
with open(file_name,'a') as file_object:
    while True:
        reason=input('why you love coding?(no for quit) ')
        if reason.lower() == 'no':
            break
        else:
            file_object.write(reason+'\n')
