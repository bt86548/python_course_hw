#九九乘法表(依照格式)

#while寫法
i=2
j=1
while j < 10:
    print("{0:}x{1}={2:<3}{3}x{4}={5:<3}{6}x{7}={8:<3}{9}x{10}={11:<3}".format(i,j,i*j,i+1,j,(i+1)*j,i+2,j,(i+2)*j,i+3,j,(i+3)*j))
    j = j+1
    if j == 10:
        print("\n")
        i=6
        j=1
        while j < 10:
            print("{0:}x{1}={2:<3}{3}x{4}={5:<3}{6}x{7}={8:<3}{9}x{10}={11:<3}".format(i,j,i*j,i+1,j,(i+1)*j,i+2,j,(i+2)*j,i+3,j,(i+3)*j))
            j = j+1

#for寫法
for  y in range(1,10):
    for x in range(2,6):
        print("{0:<2}x{1:<2}={2:<2}".format(x,y,x*y),end='') #end換行符號取消,輸出一次迴圈不換行
    else :
        print("\n",end='')

print('')
for  y in range(1,10):
    for x in range(6,10):
        print("{0}x{1}={2}".format(x,y,x*y),end='')
    else :
        print("\n",end='')


#一次寫(重要)
for y in range(1,19):

    for x in range(2,6):
        if y < 10:
            print('{:<2}{:<2}{:<2}{:}{:<2}  '.format( x ,'×', y ,'= ', x*y ), end='')
        else:
            x1 = x + 4
            y1 = y - 9
            print('{:<2}{:<2}{:<2}{:}{:<2}  '.format(x1, '×', y1, '= ', x1 * y1), end='')
    else:
        print('')









