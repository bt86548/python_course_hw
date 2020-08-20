# L = ['AA','BB','CC','DD','EE','FF']
#
# for item in L:
#     print(item,L.index(item))
# else:
#     print('結束for')
#
# L = ['AA','BB','CC','DD','EE','FF']
#
# print('索引1到索引4')
# for i in range(1,4):
#     print(L[i])
# print('偶數索引')
# for i in range(0,6,2):
#     print(L[i])
# print('奇數索引')
# for i in range(1,6,2):
#     print(L[i])

# L=[0,1,2,3,4,5,6,7,8,9,10]
#
# print('使用continue')
# for item in L:
#     if item == 7:
#         continue
#     print(item)

# L=[0,1,2,3,4,5,6,7,8,9,10]
#
# print('使用break')
# for item in L:
#     if item == 7:
#         break
#     print(item)

# L=[0,1,2,3,4,5,6,7,8,9,10]
#
# print('使用pass')
# for item in L:
#     if item == 7:
#         pass
#     print(item)
#
# L = [1,2,3,4]
# for x in L:
#     print(x)


#2直接碰到空值,4直接被整除就break
# for n in range(2,7):
#     for x in range(2,n):
#         if n % x ==0:
#             print(n,'被',x,'整除')
#             break
#     else:
#             print(n,'是整數')

# for x in range(4):
#     for y in range(3):
#         for z in range(2):
#             print(x,y,z)

#串列生成器
# print([x for x in range(10)])
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# print([x * 2 + 10 for x in range(10)])
# [10, 12, 14, 16, 18, 20, 22, 24, 26, 28]

# print([x for x in range(10) if x %3==0])
# [0, 3, 6, 9]

#計算長度輸出
# L = ['a','b','c','d','e','f']
#
# i = 0
# while i < len(L):
#     print(L[i])
#     i+=1

#while(1加到100)
# sum = 0
# i = 1
#
# while i <= 100:
#         sum += i
#         i +=1
# else :
#     print('從1加到100:',sum)

#while true

# while True:
#     n = input('請輸入一個數字:')
#     if n == 'q':
#         print('離開程式...')
#         break
#     elif int(n) % 2 ==0 and int(n) >=0 :
#         print(n,'是整數')
#     elif int(n) % 2 !=0 and int(n) >=0:
#         print(n,'是奇數')
#     elif int(n) <0 :
#         print('輸入錯誤')
#         break

#單元練習1:輸出一個0-20之間的串列
#print([x for x in range(0,21) if x % 2 == 0])
print(list(range(0,21,2)))

#單元練習2: L=[[1,2,3],[4,5,6],[7,8,9]] 請雙層迴圈逐一列印L最內層的每一個元素,例如L[1[]1]為5,遇到7請跳過
#****寫法1****
# L=[[1,2,3],[4,5,6],[7,8,9]]
#
# for i in range(0,3):
#     for j in range(0,3):
#         if L[i][j] == 7:
#             continue寫法2****
#         print(L[i][j])

#****寫# for x in L:
#     for y in x:
#         if y == 7:
#             continue
#         print(y)





