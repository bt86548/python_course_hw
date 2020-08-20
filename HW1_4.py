a = int(input('請輸入第一個邊:'))
b = int(input('請輸入第二個邊:'))
c = int(input('請輸入第三個邊:'))

if  a+b > c and a+c > b and b+c > a:
    print(a+b+c)
else:
    print('Invalid')
