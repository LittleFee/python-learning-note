while True:
    print('Give me 2 numbers I can divided them and \'q\' to quit')
    num_1 = input('Now first number plz:  ')
    if num_1.lower() == 'q':
        break
    num_2 = input('Now second number plz:  ')
    if num_2.lower() == 'q':
        break
    try:
        ans = int(num_1) / int(num_2)
    except ZeroDivisionError:
        print('You can\'t divide by 0!')
    else:
        print(ans)