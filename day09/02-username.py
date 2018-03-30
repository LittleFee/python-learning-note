database = [
 ['albert', '1234'],
 ['dilbert', '4242'],
 ['smith', '7524'],
 ['jones', '9843']
]
uname=input('Username: ')
pin=input('Pin: ')
if [uname,pin] in database:
    print('bingo')
else:
    print('Opps')
