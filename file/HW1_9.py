money = float(input('請輸入金額:'))
rate = float(input('請輸入年收益率:'))
month = int(input('請輸入經過月份:'))

# sum_money = 0 # 本金和
# for i in range(month+1):
#     sum_money += money
#
#     print('過了' , i ,'個月，存款會是:' , (sum_money + (sum_money*rate/1200)))

i = 0
sum_money = money # 本金和
while i < month:
        i += 1
        sum_money = (sum_money + (sum_money * rate / 1200))
        print('過了' , i ,'個月，存款會是:' ,'%.2f'%sum_money )