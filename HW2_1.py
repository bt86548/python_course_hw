x = 0
y = 0
for i in range(10):
    c = int(input("請輸入一個整數:"))
    if c%2 == 0:
        x = x + 1
    else:
        y = y + 1
print("偶數個數為:",x)
print("奇數個數為:",y)