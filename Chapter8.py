
# LBYL 方法

def safe_divide_1(x, y):
    if y == 0:
        print("Divide by 0 attempt dectected. ")
        return None
    else:
        return x/y


# EAFP (Easier to ask forgiveness than permission)
def safe_divide_2(x, y):
    try:
        return x/y
    except ZeroDivisionError:
        print("Divide by 0 attempt detected. ")
        return None


# LBYL
def save_a_file():
    result = save_prefs()
    if result == 'error':
        print("Performance not saved.")
        return
    result = save_text()
    if result == 'error':
        print("Not enough money.")
        return
    result = save_format()
    if result == 'error':
        print("Format not saved.")
        return


# EAFP

def save_a_file():
    try:
        save_prefs()
        save_text()
        save_format()
    except:
        print("Something went wrong ...")

# #  2者差異: LBYL是做一件事情，再去檢查，檢查完才去下一個事件。  EAFP是直接跑過事件，有問題再跳到except，沒問題就繼續跑下個事件


# * Exception範例

try:
    f = open("testfile.txt")
    f.write("Write a test line.")
except TypeError:
    print("There is a type error.")
except OSError:
    print("There is an os Error.")
except:  # 如果都沒有抓到其他except，就會跑到這裡
    print("If it didn't catch others error,it will down to here.")
finally:
    print("This section will run no mattter what.")


def ask_for_int():
    while True:
        try:
            result = int(input("Enter a number here: "))
        except ValueError as VE:
            print(VE)
            print("Invalid number. Please try again.")
        else:
            print("Good job!")
            return result


ask_for_int()

# * Exception 自製練習


class NegativeNumberException (RuntimeError):
    def __init__(self, age):
        super().__init__()
        self.age = age
        if (age < 0):
            print("This is not a valid age!!")


def enter_age(age):
    if age < 0:
        raise NegativeNumberException(age)
        # & raise 丟出 exception，讓 try 和 except去抓到

    if age % 2 == 0:
        print("Your age is an even number. ")

    else:
        print("Your age is odd .")


try:
    num = " i"
    enter_age(num)

except NegativeNumberException as Error:
    print(Error)

except:
    print("請輸入數字，否則會回報Error")

# * Guard Class and Exception Handling 練習


def divide(a, b):
    if type(a) != int or type(b) != int:
        raise ValueError("Not valid type given!!!")

    if b == 0:
        raise ZeroDivisionError("Second argument cannot be 0 ")

    return a/b


try:
    print(divide(10, "hello"))
    print(divide(10, 0))
    print(divide(6, 3))
except Exception as error:
    print(error)


# 等同於以下常規的 巢狀的 if寫法
# if type(a) == int and type(b) == int:
#         if b != 0:
#             return a/b
#         else:
#             return "The second argumnet cannt be 0."
#     else:
#         return "Invalid argument type!!"


# print(divide(10, "hello"))
# print(divide(10, 0))
# print(divide(6, 3))
