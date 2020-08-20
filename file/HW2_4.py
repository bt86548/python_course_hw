a  = str(input('請輸入一個字元:'))
x  = int(input('請輸入一個個數:'))
y  = int(input('請輸入一個列數:'))

def compute():
    for i in range(y):
        print(a*x + '\n' )
compute()