'''設計學生的年紀與學習狀況'''
# class student:
#     def __init__(self,name,age=20):
#         self.name = name
#         self.age = age
#     def study(self,course_name):
#         print('%s 正在學習 %s'% (self.name, course_name))
#     def watch_movie(self):
#         if self.age < 18 :
#             print('%s 只能觀看普通電影'%self.name)
#         else:
#             print('%s 能觀看所有電影'%self.name)
#
# def main():
#
#     stu1 = student('大名',35)
#     stu1.study('程式學習')
#     stu1.watch_movie()
#     stu2 = student('小名',12)
#     stu2.study('語言設計書')
#     stu2.watch_movie()
#
# if __name__ == '__main__':
#     main()

# class Test:
#     def __init__(self,foo):
#         self.__foo = foo
#     def __bar(self):
#         print(self.__foo)
#         print('__bar')
#
# def main():
#     test_y = Test('Hello')
#     test_y._Test__bar()
#     print(test_y._Test__foo)
#
# if __name__ == '__main__':
#     main()

'''定義一個class描述數字時鐘'''
# from time import sleep
#
# class Clock(object):
#     def __init__(self,hour = 0,minute = 0,second = 0):
#         self._hour = hour #時
#         self._minute = minute #分
#         self._second = second #秒
#     def run(self):
#         self._second += 1       #秒數 +1
#         if self._second == 60:  # 當秒數為60,分會+1,秒數變為0
#             self._second = 0
#             self._minute += 1
#             if self._minute == 60: 當分數為60,時數 +1 ,分數變為0
#                 self._minute = 0
#                 self._hour += 1
#                 if self._hour == 24: #當時數為24,時數變為0
#                     self._hour = 0
#     def show(self):    #顯示時間
#         return '%02d:%02d:%02d' %(self._hour,self._minute,self._second)
#
# def main():
#     clock = Clock(10,59,50)
#     while True:
#         print(clock.show())
#         sleep(1) #函數推遲程式運行,單位為secs秒數,此為推遲1秒
#         clock.run()
#
# if __name__ == '__main__':
#     main()

'''定義一個 class 描述平面上的點並提供移動點和計算到另一個點距離的方法。'''

# from math import sqrt
#
# class Point(object):
#     def __init__(self,x=0,y=0):
#         self.x = x
#         self.y = y
#     def move_to(self,x,y):
#         self.x = x
#         self.y = y
#     def move_by(self,dx,dy):
#         self.x += dx
#         self.y += dy
#     def distance_to(self,other):
#         dx = self.x - other.x
#         dy = self.y - other.y
#         return sqrt(dx ** 2 + dy ** 2)
#     def __str__(self):
#         return '(%s, %s)' % (str(self.x),str(self.y))
#
# def main():
#     p1 = Point(3,5)
#     p2 = Point()     #(0,0)
#     print(p1)
#     print(p2)
#     p1.move_to(-1,2)
#     p2.move_by(3,5)
#     print(p1)
#     print(p2)
#     print(p1.distance_to(p2))
#
# if __name__ == '__main__':
#      main()

'''定義圓面積'''

# class Circle:
#     PI = 3.14
#
#     def __init__(self,r=1):
#         self.radius = r
#     def gatArea(self):
#         return self.PI * self.radius * self.radius
#
# c1 = Circle()
# print('半徑為',c1.radius,'圓面積為',c1.gatArea())
# c2 = Circle()
# print('半徑為',c2.radius,'圓面積為',c2.gatArea())

'''定義圓面積(私有物件)'''
# class Circle:
#     PI = 3.14
#
#     def __init__(self,r=1):
#         self.__radius = r
#     def getRadius(self):
#         return self.__radius
#     def getArea(self):
#         return self.PI * self.__radius * self.__radius
#
# c1 = Circle(10)
# print('C1半徑為',c1.getRadius())
# print('C1的圓面積為',c1.getArea())

'''完成以下的物件
一個成績 Score 的物件 
 ▸有國文 Chinese, 英⽂ English, 數學 Math 的成績屬性 
 ▸初始化時沒提供的成績資料設定為 None，有提供則改為那個數字 
 ▸計算出不為 None 的平均成績的方法 
 
一個學⽣ Student 物件 
 ▸有名字 name，身分證 id，成績 score 屬性 
 ▸其中 id 要是私有的 
 ▸初始化輸入名字，身分證，選擇性輸入國⽂英文數學的成績'''

# class Score:
#     def __init__(self,chinese = None, english = None , math = None ):
#         self.chinese = chinese
#         self.english = english
#         self.math = math
#     def calscore(self):
#         count = 0
#         sum = 0
#         if self.chinese != None:
#             count += 1
#             sum += self.chinese
#         if self.english != None:
#             count += 1
#             sum += self.english
#         if self.math != None:
#             count += 1
#             sum += self.math
#         if count != 0:
#             return sum/count
#         else:
#             return None
#
# class Student:
#     def __init__(self,name,id,chinese = None, english = None , math = None ):
#         self.name = name
#         self.__id = id
#         self.score = Score(chinese,english,math) #Score把科目都包起來
#     def getId(self):
#         return self.__id
#     def getAverage(self):
#         avg = self.score.calscore()
#         if avg != None:
#             return avg
#         else:
#             return 'No score.'
#
# StudA =  Student(name = 'hi',id = 123, chinese = 60 ,math = 100)
# StudB =  Student(name = 'bye',id = -1,chinese = 100 , english=0)
# print(StudA.name,StudA.getId(),StudA.getAverage())
# print(StudB.name,StudB.getId(),StudB.getAverage())

'''Articles繼承Ironmen類別'''
# class Ironmen:
#     def __init__(self,group,participants):
#         self.group = group
#         self.participants = participants
#     def print_info(self):
#         print(self.group, '組有', self.participants  ,"位鐵人參賽")
#
# class Articles(Ironmen):
#     def print_articles(self):
#         print(self.group, '組預計會有',self.participants*30,'篇文章')
# modern_web = Articles('Modern Web', 54)
# modern_web.print_articles()
# modern_web.print_info()

'''繼承時使用super可以根據原本的屬性或方法之上建立新的屬性或方法。'''

# class OnlyGroup:
#     def __init__(self,group):
#         self.group = group
# class Ironmen(OnlyGroup):
#     def __init__(self,group,participants):
#         super().__init__(group)
#         self.participants =participants
# modern_web = ('Modern Web', 54)
# modern_web.print_arts()
# modern_web.print_info()

'''例如我們設計一個模擬租借腳踏車的系統，租腳踏車的是人，利用電子錢包扣款租借，因此「人」、「電子錢包」、「腳踏車」在這個系統中都會是獨立的物件 (object) 。'''

# class Person:
#     name = ""
#     wallet = None
#     bike = None
#     def __init__(self,name):
#         self.name = name
#         m = "A person "
#         m += self.name
#         m += " is here."
#         print(m)
#
#
#     def setWallet(self,wallet):
#         self.wallet = wallet
#         m = self.name
#         m += "has the new wallet."
#         print(m)
#     def rentBike(self,bike):
#         self.wallet.balance -= 50
#         self.bike = bike
#         m = self.name
#         m += "'s wallet now has  "
#         m += str(self.wallet.balance)
#         m += " dollars."
#         print(m)
#
# class ElectronWallet:
#     balance = 0
#     person = None
#
#     def __init__(self,person,balance):
#         self.person = person
#         self.balance = balance
#         m = "A new wallet has "
#         m += str(self.balance)
#         m += " dollars."
#         print(m)
#
# class RenterBike:
#     person = None
#
#     def __init__(self,person):
#         self.person = person
#         m = "A bike is rented by "
#         m += self.person.name
#         m += "."
#         print(m)
#
# someone = Person("John")
# newWallet = ElectronWallet(someone, 1000)
# someone.setWallet((newWallet))
# newBike = RenterBike(someone)
# someone.rentBike(newBike)



