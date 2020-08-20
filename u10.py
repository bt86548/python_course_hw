# class Car():
#     #屬性
#     year = 2019 #車子年分
#     mpg = 30 #mileage
#     speed= 0 #現在速度
#     def __init__(self,speed):
#         self.speed = speed
#     def accelerate(self):
#         self.speed +=20
#     def brake(self):
#         self.speed -=10
#
# def main():
#         car1 = Car(15)
#         print('car1 speed',car1.speed)


# def main():
#     car1 = Car()
#     print('speed',car1.speed)
#     car1.accelerate()
#     car1.accelerate()
#     print('speed',car1.speed)
#     car1.brake()
#     print('speed',car1.speed)
#
# if __name__ == "__main__":
#     main()

#
# def main():
#     car1 = Car()
#     car2 = Car()
#     car1.accelerate()
#     car1.accelerate()
#     print('speed', car1.speed)
#     print('speed', car2.speed)


# if __name__ == "__main__":
# #     main()

class A :
    count = 1
    def __init__ (self):
        self.count += 1
    @classmethod
    def get_cls_count(cls):
        print(cls.count)
    @staticmethod
    def usage():
        print('Usage: This is class A')
    def get_self_count(self):
        print(self.count)

def main():
    A.get_cls_count()

    a = A()
    a.get_self_count()

    A.get_cls_count()

    a.usage()
    A.usage()

if __name__ == "__main__":
    main()

# class Car :
#
#     def __init__(self,speed):
#         self.speed = speed
#     def accelerate(self):
#         self.speed += 20
#     def brake(self):
#         self.speed -= 10
# def main():
#     Car.color = 'black'
#     Car.brand = 'benz'
#     car1 = Car(15)
#     car1.type = 'SUV'
#
#     car2 =Car(20)
#     print('car1 speed', car1.speed)
#     print('car1 color', car1.color)
#     print('car1 brand', car1.brand)
#     print('car1 type', car1.type)
#
#     print('car2 speed', car2.speed)
#     print('car2 color', car2.color)
#     print('car2 brand', car2.brand)
#     print('car2 type', car2.type)

#
# class Book():
#     def __init__(self, name = ' ', author = ' ' , price =0):
#         self.name = name
#         self.author = author
#         self.__price = price
#     def info(self):
#         print("Book info:",self.name,self.author,self.__price)
#     @property
#     def price(self):
#         return self.__price
#     @price.setter
#     def price(self,value):
#         if value < 250 :
#             self.__price =250
#         else:
#             self.__price = value
#
# def main():
#     book1 = Book('哈利波的神秘的魔法石','JK羅琳',120) #受保護所以350讀不到
#     book1.info()
#     # print('書名:',book1.name)
#     # print('作者:',book1.author)
#     # book1.price = 120
#     print('售價:',book1.price,'$NTD')
#
# if __name__ == "__main__":
#     main()

# class Book():
#     def __init__(self, name = ' ', author = ' ' , price =0):
#         self.name = name
#         self.author = author
#         self.__price = price
#     def __str__(self):
#         return 'name,'+self.name+\
#                 ',author,'+self.author+','\
#                 'price,'+str(self.__price)
#     def __del__(self):
#         print(self.name+"已移除")
#     def __call__(self, name = '', author = '', price=0):
#         if len(name.strip()) > 0:
#             self.name = name
#         if len(author.strip()) > 0:
#             self.author = author
#         if price>= 0:
#             self.__price = price
#
# def main():
#     book1 = Book('哈利波特的神秘魔法石','JK羅琳',350)
#     book1('哈利波特消失的密室','',320)
#     print(book1)
#
# if __name__ == "__main__":
#     main()

# class Car:
#     year = 1990 ; mpg = 30000; speed = 0
#     def __init__(self,year,mpg ,speed):
#         self.year = year
#         self.mpg = mpg
#         self.speed = speed
#     def accelerate(self):
#         self.speed += 20
#         print('speed up:',self.speed)
#     def brake(self):
#         self.speed -=10
#         print('speed down:',self.speed)
#
# class RaceCar(Car):
#     def __init__(self,color='',make = '',engine='',year='',mpg =0,speed=0):
#         self.color = color
#         self.make = make
#         self.engine = engine
#         super(RaceCar,self).__init__(year,mpg,speed)
#     def turbo_start(self):
#         self.speed += 100
#         print('Turbo Mode Start Speed:',self.speed)
#     def brake(self):
#         print('ABS mode start')
#         super().brake()
#
# def main():
#     my_car = RaceCar('White','Nissan GTR','V6','2007',3000,0)
#     print(my_car.color,my_car.make)
#     my_car.accelerate()
#     my_car.turbo_start()
#     my_car.accelerate()
#     my_car.brake()
#
# if __name__ == "__main__":
#    main()


# class juicer:
#     def open(self):
#         print('開啟果汁機電源')
#
#     def run(self):
#         print('開始打果汁')
#
#
# class Washer:
#     def open(self):
#         print('開始洗衣機電源')
#
#     def run(self):
#         print('開始洗衣服')
#
#
# def auto_run(thing):
#     thing.open()
#     thing.run()
#
#
# def main():
#     machine = juicer()
#     auto_run(machine)
#
#     machine = Washer()
#     auto_run(machine)
# if __name__ == "__main__":
#    main()

# class Vector3D:
#     def __init__(self,x,y,z):
#         self.x = x
#         self.y = y
#         self.z = z
#     def __add__(self, other):
#         v = Vector3D(self.x+other.x,self.y+other.y,self.z+other.z)
#         return v
#     def __sub__(self,other):
#         v = Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)
#         return v
#     def __str__(self):
#         s ='('+ str(self.x) + ',' + str(self.y) + ',' +str(self.z)+')'
#         return s
#
# def main():
#     v1 = Vector3D(1,2,3)
#     v2 = Vector3D(1,1,0)
#
#     print(v1-v2)
#     print(v1+v2)
#
#
# if __name__ == "__main__":
#     main()



# class Box():
# #     def __init__(self, L=1, W=1, H=1):
# #         self.L = L
# #         self.W = W
# #         self.H = H
# #
# #     def info(self):
# #         print(self.L, self.W, self.H)
# #
# #     def is_cube(self):
# #         if self.L == self.H == self.W:
# #             return True
# #         else:
# #             return False
# #
# #     def volume(self):
# #         return self.L * self.H * self.W
# #
# # def main():
# #     #Box.get_volume()
# #     #Box.is_cube()
# #
# #     b1 = Box(3, 4, 5)
# #     b1.info()
# #     print(b1.volume())
# #
# #     b2 = Box(3, 3, 3)
# #     print(b2.volume())
# #
# #     a = b1.is_cube()
# #     print(a)
# #
# # if __name__ == "__main__":
# #     main()

n = 3.1415926
print('|{:<20.4f}|'.format(n))