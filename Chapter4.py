
# # x,y are the parameters
# def addition():
#     print(x+y)


# # 15,20 are the argument
# addition(15, 20)
# # 我們輸入的參數英文叫做 argument，自訂義function的參數叫做 parameter


# * Global 和 local variables練習

a = 5


def f1():
    x = 2  # f1 function's Local variables
    y = 3  # f1 function's Local variables
    print(x, y, a)


def f2():
    x = 10  # f2 function's Local variables
    y = 17  # f2 function's Local variables
    print(x, y)


f2()


a = 10
# 我們可以更改任何的 copy by valu global variables


def change(num):  # parameters(input values) are Local variables in the function
    global a    # 我們可以更改任何的 copy by value global variables
    a = 25


change(a)
print(a)


def myAddition(a, b):
    """This function does addition for inputs a and b"""
    # 使用help() functoin，可以讓人知道裡面的解釋是什麼?
    print(a+b)


help(myAddition)


# * return 練習
def myAddition(a, b):

    return a+b


result1 = myAddition(10, 18)
result2 = myAddition(26, 19)
result3 = myAddition(15, 17)

print(result1+result2+result3)


def myAddition1(a, b):
    for i in range(a):
        for j in range(b):
            if i == 3 and j == 4:
                return
            print(i, j)


print(myAddition1(10, 15))


# * Key words argument 練習
def exponent(a, b):
    return a**b


print(exponent(2, 3))  # 2**3=8 ，依照正確的順序進行輸出，便是positional argumnet
print(exponent(b=2, a=10))
myList = [4, 6, 3, 2, 1,]
print(sorted(myList, reverse=True))
# myList is positional argument ，所以要放在正確的順序
# reverse=True is keywords argument


# * Default argument 練習
def sum(n1=10, n2=3):  # default argument
    return n1+n2


print(sum(12))
print(sum(12, 25))
print(sum())
print(sum(n2=100, n1=50))  # keyword argument


def sum(*args):
    print(args)
    print(type(args))
    result = 0
    for number in range(0, len(args)):
        print(f"We are now at index {number} .")
        print(f"Also , args[number] is {args[number]} .")
        result += args[number]
        print(f"Now, the result is {result}")
    return result


print(sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


def myfunc(**kwargs):
    print("{} is now {} years old.".format(kwargs["name"], kwargs["age"]))


myfunc(name="Danny", age=25, address="Taiwan")

# # *args被用來輸入任意non-keywords數字，這些輸入在funciotn當中被包裝成tuples
# # **kwargs 被用來輸入任意 keywords數字，這些輸入再function當中被包裝成 Dictionary


def myfunc2(*args, **kwargs):  # (*,**)variable名稱可以更換，主要是*號判斷，但是約定俗成使用這些variable名稱
    print("I would like to eat {} {}".format(args[1], kwargs["food"]))


myfunc2(14, 17, 23, "hello", name="Danny", food="eggs")


# 1.normal argument (p1, p2)
# 2.default argument
# 3. *args
# 4. **kwargs
# #function input 必須按照順序排位，1. ~ 4.
def func(p1, p2, p3="three", *args, **kwargs):
    print("------------------")
    print(p1, p2, p3, args, kwargs)


func(1, 2, 3, 4, 5, x=1, y=3)
func(1, 2, 3, 4, x=4)
func(1, 2, 3, 4)
func(1, 2, 3)
func(1, 2)
# func(1)
# 會出現invalid syntax ，因為少了 p2存在

# * Higher-Order function 練習


def higherOrder(fn):
    fn()


def smallFunc():
    print("Hello from the smaller function.")


higherOrder(smallFunc)
# &  就是把其他funciotn拿來當argument使用，我們可以自訂義function


def square(num):
    return num**2


myList = [-10, 3, 9, 8, 10]
for value in map(square, myList):
    print(value)
# &  map(function , iterable )


def even(num):
    return num % 2 == 0
    # if num % 2 == 0:
    #     return True
    # else:
    #     return False


myList = [1251616512, 1516131317, 848452, 659494]
for value in filter(even, myList):
    print(value)
# &  filter(func,iterable)=>第一個參數function，如果回傳true，則iterable 元素，加入進去。若回傳false，不加入進去

# * lambda Expression練習
#  #使用lambda的時機，1.不需要名字的function，短期使用，2.使用在 Higher-order function，因為使用lambda會自動return，故不需要使用return 語法

result = (lambda x, y: (x+y, x-y))(15, 30)
# & Lambda input1,input2,...... : operation
print(result[0])
print(result[1])

for value in map(lambda x: x**2, [15, 10, 5, 20]):
    print(value)

for item in filter(lambda x: x % 2 == 0, [15, 10, 5, 20]):
    print(item)


print("你好大白癡")
