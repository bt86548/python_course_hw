
x = int(input("請輸入年分(西元年):"))

while(x!=-9999):

    if x >=100:
        if x%400 == 0:
            print(("該年為閏年"))
            break
        elif x%4 == 0 and x%100!=0:
            print(("該年為閏年"))
            break
        elif x%100==0 and x%4!=0:
            print("該年為平年")
            break
        else:
            print("該年為平年")
            break
    else :
        if x%4 == 0:
            print("該年為閏年")
            break
        else:
            print("該年為平年")
            break
