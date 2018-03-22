# 7-1 汽车租赁：编写一个程序，询问用户要租赁什么样的汽车，并打印一条消息，
# 如“Let me see if I can find you a Subaru”。
brand=input('哈啰，你想租个啥子车嘛？说哈嘛： ')
print('让我qio一眼，我能不能帮你找一过'+brand.title())

# 7-2 餐馆订位：编写一个程序，询问用户有多少人用餐。如果超过8 人，就打印一
# 条消息，指出没有空桌；否则指出有空桌。
number=int(input('先森，恰饭哇，几位吶？ '))
if number > 8:
    print('嗨呀，'+str(number)+'大'+str(number)+'过人，没得空桌子咯~')
else:
    print('阔以阔以，刚好有个八仙桌，够你几爷子坐的了~')

# 7-3 10 的整数倍：让用户输入一个数字，并指出这个数字是否是10 的整数倍。
number=int(input('来，说个数字，我看一哈是不是10的整数倍: '))
if number % 10 == 0:
    print('哈哈，就是10的倍数')
else:
    print('哦豁，不是的')