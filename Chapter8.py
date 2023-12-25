
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
