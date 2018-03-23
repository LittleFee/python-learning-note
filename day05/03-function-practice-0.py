# 8-1 消息：编写一个名为display_message()的函数，它打印一个句子，指出你在本
# 章学的是什么。调用这个函数，确认显示的消息正确无误。
def dispaly_message():
    print('I learned function in this chapter')

dispaly_message()

# 8-2 喜欢的图书：编写一个名为favorite_book()的函数，其中包含一个名为title
# 的形参。这个函数打印一条消息，如One of my favorite books is Alice in Wonderland。
# 调用这个函数，并将一本图书的名称作为实参传递给它。
def favorite_book(title):
    print('One of my favorite book is '+title.title())

favorite_book('Three Body')