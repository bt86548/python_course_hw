
i=0;a_sum=0;j=0
while i < 3:
    i += 1
    while j < 5:
        j+=1
        a = int(input("請輸入第{0}位學生第{1}筆成績:".format(i,j)))
        a_sum += a
    print('第{0}位學生的總分為:{1}總平均為:{2}'.format(i,a_sum,'%.2f'%(a_sum/5)))
    j=0

