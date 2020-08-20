# c = int(input("請輸入一個整數:"))
# if c %2 == 0:
#     print("進入if")
#     print(c,"是偶數")
# else:
#     print("進入else")
#     print(c,"是奇數")
# print("判斷結束")


A = int(input("請輸入您的成績:"))

if A >= 95 and A<= 100:
    print("A+")
elif A>= 85 and  A<95:
    print("A")
elif A>= 75 and A< 85:
    print("B")
elif A >= 60 and A < 75:
    print("C")
elif A >= 100 and A < 0:
    print("輸入錯誤")
else:
    print("請多努力")
