
# while寫法
a  = int(input('請輸入一個正整數a:'))

x = 0
i = 0
while i <= a:

        i += 1
        if i%5 == 0 and i >= 5:
            x += i
        else:
            continue

print("總和為:", x)

#for寫法

# a = eval(input('請輸入一個正整數:'))
# c= 0
# for i in range(1,a+1):
#     if i%5==0:
#         c+=i
# print(c)



