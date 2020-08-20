s='商品數量: %d 重量: %.2f 品名 : %s'%(10,800.452,'牛奶')
print(s)

i = 99
print('%d' %i)
print('%  d' %i) #兩個空白字元
print('|%8d|' % i) #寬度8 靠右對齊
print('|%08d|'% i) #寬度8 補零 靠右對齊
print('|%-8d|'% i) #寬度8 靠左對齊
print('|%+8d|'% i) #寬度8 加正號 靠右對齊
print('|%-+8d|'% i) #寬度8 加正號 靠左對齊

i = 127
print('%o' % i) #八進位
print('%#o' % i) #八進位
print('%x' % i) #十六進位
print('%X' % i) #十六進位
print('%#x' % i) #十六進位
print('%#X' % i) #十六進位

n = 1.2345
print('|%f|'%n) #預設六位
print('|%.3f|'%n) #有三位 有三位小數
print('|%8.3f|'%n) #寬度為八 有三位小數
print('|%-8.3f|'%n) #靠左對齊 寬度八位 有三位小數
print('|%08.3f|'%n) #寬度八位 前面補零 有三位小數
print('|%+8.3f|'%n) #靠右對齊 寬度八位 有加號
print('|%*.3f|'%(8,n)) #*為用8替代 靠右對齊 有八位 有三位小數



# n=99
# m=100
# print('{:$>8} {:$<8}'.format(n,m))
#
# n = 10.54564
# m = '$'+str(n)
# print('{}'.format(m))
# print('{:s}'.format(m))
# print('{:@>20.4f}'.format(n))
#
# print('{2:*<10},{1:*^10},{0:*>10}'.format('a','b','c'))
#
# n,m = (1,2),(3,4)
# print('{0[0]},{0[1]},{1[0]},{1[1]}'.format(n,m))
#
# print(f"{100*2}")

#第六章練習

for i in range(2,6):
    for j in range(1,10):
        print('{0}{1}{2}{3}',)

