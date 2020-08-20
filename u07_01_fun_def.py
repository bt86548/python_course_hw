# def my_avg(a,b):
#     r = (a+b)/2
#     return r
#     print(r)
#
# my_avg(10,20)
# x = my_avg(1,2)
# print(x)

#函式定義方法
# def ret_test1(m,n):
#     a = m+n
#     return a
#
# def ret_test2(m,n):
#     a = m+n
#
# def ret_test3(m,n):
#     a = m+n
#     b = m-n
#     c = 'hello'
#     return a,b,c
#
# r = ret_test1(10,20)
# print(r)
#
# r = ret_test2(10,20)
# print(r)
#
# r1, r2,r3 = ret_test3(10,20)
# print(r1,r2,r3)

# def fun1(a,b):
#     print('進入fun1')
#     c = (a+b) *2
#     return  c
#
# def fun2(a,b):
#     print('進入fun2')
#     c = (a+b)*3
#     return c
#
# def main():
#     print('主程式開始')
#     r = fun1(10,20)
#     print('fun1 回傳:',r)
#     r = fun2(5,6)
#     print('fun2回傳:',r)
#     print('主程式結束')
#
# if __name__ == '__main__':
#     main()

#串列可更改原始物件
# def modify(L):
#     T = [5]
#     L += T
#
# def main():
#     L = [1,2,3,4]
#     modify(L)
#     print(L)
#
# if __name__ == "__main__":
#     main()

#tuple不能更改原始物件
# def modify(s):
#     s = s +"!"
# def modify_return(s):
#     s = s + "!"
#     return s
# def main():
#     s = 'hello python'
#     modify(s)
#     print(s)
#
#     s = modify_return(s)
#     print(s)
#
# if __name__ == "__main__":
#     main()

#傳入引數要符合參數宣告,錯誤訊息para_test() missing 1 required positional argument: 'c'

# def para_test(a,b,c):
#     print(a,b,c)
#
# def main():
#     para_test(10,20,30)
#     para_test(10,20)
#
# if __name__ == "__main__":
#      main()

#傳入引數可用參數名稱賦值
# def para_assign(a,b,c,):
#     print(a,b,c)
#
# def main():
#     para_assign(b=20,c=30,a=10) #引數順序可更動!!
#
# if __name__ == "__main__":
#      main()

#參數預設值(呼叫函式時沒有給引數,函式依然有預設值)
# def para_dft1(a=0,b=0,c=0):
#     print(a,b,c)
#
# def para_dft2(a,b,c=0): #無預設值須寫在前面,有預設值寫在後面
#     print(a,b,c)
#
# def main():
#     para_dft1()
#     para_dft1(b=20,c=30)
#     para_dft1(c=30,b=20,a=10)
#     para_dft2(10,20)
#
# if __name__ == "__main__":
#       main()

#*args可變量參數
# def para_tuple(p,*v):
#     print('p=',p)
#     print('v=',v)
#     return sum(v)-p
#
# def main():
#     r = para_tuple(10,20,30,40) #v以值組方式回傳 讀取print('p=')及print('v=')
#     print(r) #讀取return的回傳值
#     print() #換行用
#
#     t = (20, 30, 40, 50)
#     r = para_tuple(10,*t)
#     print(r)
#
# if __name__ == "__main__":
#       main()

#**kwargs可變數量參數(******傳入方式為dict******)
# def para_kw(p,**d):
#     print(p)
#     print(d)
#
# def para_tup_kw(p,*t,**d):
#     print(p)
#     print(t)
#     print(d)
#
# def main():
#     para_kw(10,i=20,j=30,k=40)
#
#     k = {'m':20,'n':33}
#     para_kw(11,**k)
#
#     para_tup_kw(5,'a','b','c',i=20,j=30,k=40) #自動抓取dict的key與value
#
# if __name__ == "__main__":
#       main()

#參數名稱為星號(*) 出現星號*後的參數必須用關鍵字引用傳入
# def para_star(a,*,b,c):
#     print(a,b,c,end=' ')
#     print(b,c,a)
#
# def main():
#     para_star(10,b=3,c='AAA')
#
# if __name__ == "__main__":
#     main()

#巢狀函式
# def func_outer():
#     print('執行外包函式')
#     a=10
#
#     def func_inner():
#             b = 20
#             print('執行內部函式')
#             print('func_inner()的外部變數 a=',a)
#             print('func_inner()的內部變數 b=',b)
#
#     func_inner()
#
# def main():
#     print('執行主函式')
#     func_outer()
#
# if __name__ == "__main__":
#    main()

# #非區域變數(nonlocal variable:會先從區域內往外來找,找最接近的)
# flag = 10
# def func_outer():
#     flag = 20
#
#     def set_flag():
#         nonlocal flag
#         flag = 30
#     set_flag()
#     print(flag)
# def main():
#     func_outer()
#     print(flag)
# if __name__ == "__main__":
#    main()


#匿名函式(lambda:不使用def宣告的函式,lamda的主體式一行表達式,擁有自己的命名空間,
#  不能訪問自己參數列表外或全域命名空間的其他變數)
# avg = lambda arg1,arg2: (arg1+arg2)/2
#
# def main():
#     print(avg(10,20))
# if __name__ == "__main__":
#    main()


# list_a = [lambda  a : a**3,lambda b : b**3]
# print(list_a[0])
# g = list_a[0]
# print(g(2))

#lambda搭配list用法
# def add_ten(x):
#     x += 10
# def add_ten_r(x):
#     return  x + 10
# def main():
#     L = [1,2,3,4,5,6]
#     M = map(lambda  x  : x*10,L)
#
#     print(M)
#     print(list(M))
#
#     N = list(map(add_ten,L))
#     print(N)
#     N = list(map(add_ten_r,L))
#     print(N)
#
# if __name__ == "__main__":
#    main()

#map用法
# def square(x):  # 计算平方数
#     return x**2
#
# map(square, [1, 2, 3, 4, 5])  # 计算列表各个元素的平方
# map(lambda x: x ** 2, [1, 2, 3, 4, 5])  # 使用 lambda 匿名函数
# # 提供了两个列表，对相同位置的列表数据进行相加
# map(lambda x, y: x + y, [1, 3, 5, 7, 9], [2, 4, 6, 8, 10])


#遞迴函式(函式進行自我呼叫,讓大問題變小問題,再各個擊破(Divide and Conquer)
# def factorial(n):
#     print(('f',n))
#     if n == 1:
#         return n
#     else :
#         return n * factorial(n-1)
#
# def main():
#     print(factorial(4))
#
# if __name__ == "__main__":
#    main()

#生成器函式(特徵為使用yield讓函式連續回傳值,可搭配next()函式控制回傳一個數值後中斷
#再執行會從中斷處繼續,透過yield與next搭配使用,可以觀察值的變化)
# def my_range(n):
#     x = 0
#     while True:
#         yield x
#         x += 1
#         if x == n:
#             break
# def main():
#     print(list(my_range(8))) #用list展開range(8)中的值
#     g = my_range(8)
#     print(type(g)) #顯示g的狀態為generator生成函式
#     next(g)#執行一次停一次1
#     next(g)#執行一次停一次2
#     next(g)#執行一次停一次3
#     next(g)#執行一次停一次4
#     next(g)#執行一次停一次5
#     next(g)#執行一次停一次6
#     next(g)#執行一次停一次7
#     print(next(g))
#
# if __name__ == "__main__":
#     main()

#語法糖
# def func_b():
#     print('執行func_b')
#
# def b_deco(f):
#     def wrapper_func(*argc):
#         func_b()
#         f(*argc) #執行原本的函式
#
#     return  wrapper_func
# @b_deco
# def func_a(s):
#     print(s)
# @b_deco
# def func_c(s):
#     print(s)
#
# def main():
#     func_a('執行func_a的功能')
#     func_c('執行func_c的功能')
#
# if __name__ == "__main__":
#     main()

#隨堂練習:內建函式eval()會試著將字串轉換成python的表達式
# def main():
#     x = 10
#     s1 = 'x+3'
#     s2 = 'pow(2,3)'
#     s3 = '1,2,3,4'
#
#     print(eval('3*x'))
#     print(eval('pow(2,2)'))
#     print(eval(s1))
#     print(eval(s2))
#     print(eval(s3))
#
# if __name__ == "__main__":
#     main()

#費式數列yield寫法
# def myfab(n):
#     i = 0;
#     a = 0;
#     b = 1
#
#     while True:
#         if i == n:
#             break
#
#         yield a
#
#         a, b, i = b, a + b, i + 1
#
#
# def main():
#     print(list(myfab(7)))
#
#
# if __name__ == "__main__":
#     main()

# 費式數列遞迴寫法
# def factorial(i):
#     if i <= 1:
#         return i
#     else:
#         return factorial(i-1) + factorial(i-2)
#
# n = eval(input())
#
# for x in range(n):
#     print(factorial(x), end=" ")




n = int(input('請輸入一個正整數'))


def factorial(n):
    sum = 1
    for x in range(n+1):
        sum = sum * x
    print('n階層後為:', sum)

factorial(n)

