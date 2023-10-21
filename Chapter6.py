

# * Object-Oriented Programming(OOP) 語法練習

# #  OOP : A class is a code template for creating procject。
# #　在一個template裡面，加入propertives，object。之後只要調用template，在更改那些propertives，object的data就行了

#!  首字母 要大寫
class Robot:

    ingredient = "metal"  # class attribute

    # constructor
    def __init__(self, inputname, inputage):
        # & __init__ 等同於其他程式語言的constructor。
        # & 當class被created之後，每一次都會先呼叫出來，__init__() methods會設定(initialize) object 的 attributes 和ㄓ
        # ! 習慣而言，__init()__的第一個parameter都會用  self (翻譯:我自己)(在在其他語言中，這個代表 this)

        self.name = inputname  # inputname這個 argument會放到這個self.name的 variable
        self.age = inputage
        self.ingredient = " metal"

    def walk(self):
        print(f"{self.name} is walking ...")

    def sleep(self, hours):
        print(f"{self.name} is going to sleep for {hours} hours.")

    def greet(self):
        print(
            f"hi, my name is {self.name}, 還有我是{self.__class__.ingredient} 所做成的")
        # & self.__class__.attribute ，用在 method definition 裡面

    @staticmethod
    def hi():
        print("機器人在打招呼")


my_robot_1 = Robot("Danny", 25)
my_robot_2 = Robot("Alex", 10)

my_robot_2.walk()
my_robot_1.sleep(30)

# class attributes 是屬於class的，定義在constructor function外面，並不屬於某個特定的object。
# 其他constructor function 皆能使用
print(my_robot_1.ingredient)
print(my_robot_2.ingredient)

my_robot_1.greet()
my_robot_2.greet()
print(my_robot_1.ingredient)
# & objectname.attribute( 使用在 method definition 外面)

print(Robot.ingredient)
# & classname.attribute (唯一要記住的地方，是不能用在 method definition裡面)
# #盡量不使用這個

print(my_robot_1.__class__.ingredient)
#! 最正確的習慣用法，是使用這個，避免class 名字被更改，導致所有有用到的method都要去做更改


my_robot_1.__class__.hi()


# * static methods 和 static class 語法差別

class Circle:
    pi = 3.14159
    all_circles = []  # class attribute

    def __init__(self, radius):
        self.radius = radius
        self.__class__.all_circles.append(self)

    def area(self):
        return self.__class__.pi * (self.radius ** 2)

    @staticmethod  # & 這個method 是跟class 綁在一起的，屬於class，而不是 object
    def total_area():  # #static method的第一個parameter，不需要輸入self parameter
        total = 0
        for circle in Circle.all_circles:  # ! 因為使用的是class 名字，所以小心class名字更改之後，這咧也需要跟著改
            total += circle.area()
        return total

    @classmethod
    def total_area2(cls):  # ! 因為使用的是cls ，所以不用擔心class名字，若被更改，這裡也需要更改的狀態
        total = 0
        for circle in cls.all_circles:
            total += circle.area()
        return total
    # # cls( stands for class )，習慣上當作第一個parameter


c1 = Circle(10)
print(c1.__class__.total_area())
# 因為有append的關係
c2 = Circle(10)
print(c2.__class__.total_area2())

# *  inheritan ce
