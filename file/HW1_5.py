a = int(input('請輸入一整數num(0<=num<=15):'))

if a/10 < 1:
    print(a)
elif a % 10 == 1:
    print('B')
elif a % 10 == 2:
    print('C')
elif a % 10 == 3:
    print('D')
elif a % 10 == 4:
    print('E')
elif a % 10 == 5:
    print('F')
else:
    print('A')
