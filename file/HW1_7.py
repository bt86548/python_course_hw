a = int(input('請輸入您的分數:'))

if  100 >= a >=80 :
    print('A')
elif 79 >= a >= 70:
    print('B')
elif 69 >= a >= 60:
    print('C')
elif a < 1 or a > 100:
    print('輸入錯誤')
else:
    print('F')
