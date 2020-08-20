x = int(input('請輸入一個正整數x:'))

if x%3 == 0:
    if x%5 == 0:
        print('x is a multiple of 3 and 5.')
    else:
        print('x is a multiple of 3.')
elif x%5 == 0:
    if x%3 == 0:
        print('x is a multiple of 3 and 5.')
    else:
        print('x is a multiple of 5.')
else:
    print('x is not a multiple of 3 or 5.')