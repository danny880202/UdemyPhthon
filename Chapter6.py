

# * Object-Oriented Programming(OOP) 語法練習

# #  OOP : A class is a code template for creating procject。
# #　在一個template裡面，加入properties，object。之後只要調用template，在更改那些properties，object的data就行了

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


# *  inheritance 與法練習

# #  尤其中一個class去繼承他想要的class。
class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sleep(self):
        print(f"{self.name}is sleeping...")

    def eat(self):
        print(f"{self.name} is eating food")


class Student(People):  # & (要繼承的對象Class名字) ，這樣就是繼承，並且可以使用parent class所有的attributes和methods
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        # #不用加self，這個用法就是專門用來存取parent class
        # & 等同於=>People.__init__(self, name, age)
        # #繼承People__init__()裡面的功能

        self.student_id = student_id

    def eat(self, food):  # ! 雖然從parent class那裏繼承，但是可以去覆寫他，程式碼也只會抓到覆寫的
        print(f"{self.name} is now eating {food}")


student_one = Student("Danny", 25, 100)
print(student_one.name, student_one.age, student_one.student_id)
student_one.sleep()
student_one.eat("beef")


# *  child  class 繼承多個parent class

class A:
    def do_stuff(self):
        print("hello form class A")


class B:
    def do_another_stuff(self):
        print("hello from class B")


class C(A, B):
    pass


a = C()
a.do_stuff()
a.do_another_stuff()


class E:
    pass


class F:
    def do_stuff(self):
        print("doing stuff from F")


class G:
    def do_stuff(self):
        print("doing stuff from G")


class H(E, F):
    pass


class I:
    def do_stuff(self):
        print("doing stuff from I")


class J:
    pass


class K(H, I, J):
    pass


print(K.mro())  # list 的形式輸出
print(K.__mro__)  # tuple 的形式輸出
# & methods resolution order

b = K()
b.do_stuff()

# *   Private Attributes and Methods


class Teacher:
    def __init__(self, name):
        self.name = name

        self.__age = 25  # & 加2條__ 就是 private property

    def __this_is_private(self):  # & private method
        print("hello from private method.")

    def greet(self):
        print("Hi, i am a teacher")
        self.__this_is_private()

    def age_setter(self, new_age):
        if new_age > 0 and new_age < 100:
            self.__age = new_age
        else:
            print("New age setting is invalid")

    def age_getter(self):
        print(self.__age)


my_Teacher = Teacher("Danny")
my_Teacher.greet()
my_Teacher.age_setter(-30)  # 因為是invalide，所以維持原本private data = 25
my_Teacher.age_getter()


# *  OOP style in Python

#! encapsulation 定義: 在做OOP 的設計的時候，最重要的就是要把information藏起來
# 要把information藏起來的方式就是設定private。 盡可能得讓attributes都是 private
# 可以使用 getter() 和 setter() 。這2個不常使用


# *  Property Decorator (虛擬Property) 語法練習
class Employee:
    def __init__(self):
        self.income = 0

    def earn_money(self, money):
        self.income += money

    @property  # #雖然我們定義的是一個function，但事實上會成為Employee的property
    def tax_amount(self):
        return self.income * 0.05

    @ tax_amount.setter  # #可以更改 虛擬property的值
    def tax_amount(self, tax_number):
        self.income = tax_number * 20


Danny = Employee()
Danny.earn_money(300)
print(Danny.tax_amount)
# tax_amount 不是一個真正的Employee 的property，是一個虛擬的property(藉由一個function來定義的)
# # tax_amount 虛擬property 是 read-only

Danny.tax_amount = 200
print(Danny.income)


# 不使用 @property的用法
class Employee_1:
    def __init__(self):
        self.income = 0
        self.__tax = 0

    def earn_money(self, money):
        self.income += money
        self.__tax = self.income * 0.05

    def get_tax(self):
        return self.__tax


Danny = Employee_1()
Danny.earn_money(300)
print(Danny.get_tax())

Danny.earn_money(500)
print(Danny.get_tax())
