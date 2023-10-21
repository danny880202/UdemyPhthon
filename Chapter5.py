
import shelve
import pickle
import random


# *  I/O with file 的訓練

file = open("myfile.txt", encoding="utf-8")
# & 打開files檔案 。然後看要開啟的檔案，如果出現亂碼，記得改編碼方式


print(file.readline())  # & 回傳一行line，目前我們所在的文字敘述
print("-----------------")
print(file.read(5))  # & 從file當中，return 輸入的數字(offset)，以bytes為單位計算
print("-----------------")
print(file.read(6))
print("-----------------")

file.seek(0)  # & 輸入數字(offset)，set到數字要的位置
print(file.read())
file.seek(0)
print(file.read())

print(type(file.read()))  # &  file.read() 一定會return string

print(file.readlines())
# # ['hello,how are you today?\n', "I'm fine! Thank you!\n", '\n']
# #  會在字串後面加上 \n
# 不建議把readlines 用在一堆text上面，ram會爆炸

for line in file.readlines():
    print(line)
# 會有換行 \n 的效果


while True:
    line = file.readline()
    if line == "":  # 或者改成這樣寫法=> if not line:
        break  # #如果是 "" empty string， 便是 Falsy value
    else:
        print(line)

file.close()  # & 關掉file檔案， 頭是open，尾巴是close

# *  With 檔案  語法練習

with open("myfile.txt", mode="a",  encoding="utf-8") as AnyFileName:
    AnyFileName.write("我不想延畢，我想準時畢業!!!")

# & 和open()  { 內容 }  close() 流程一樣，差別在於，這個語法會自動幫你close()檔案


# *  input 與法練習
user_input = input("How old are you?")
user_address = input("Where do you live?")
print("-----------------")
print(user_input)
print(type(user_input))

# *  codind practice 練習  給一個數字範圍，猜終極數字


# #首先  import random

secret = random.randint(1, 100)  # # 呼叫random function，輸出一個隨機數字 從1~100
min_value = 1
max_value = 100
print(f"scret number 是: {secret}")

while True:
    guess = input(f"猜一個數字在{min_value} and {max_value}: ")
    if int(guess) < min_value or int(guess) > max_value:
        print("你輸入的數字不在range範圍裡面!!!!")
        continue
        # # 這個時候加入 continue 是為了進入下一個iterable迭代
        # # 按照if 條件，如果條件 true，則會一直for 迴圈，一直continue。

    if int(guess) == secret:
        print(f"正確的 Secret 是 {secret}")
        break
    elif int(guess) < secret:
        min_value = int(guess)
        # #  如果guess小於secret，則guess會變成最小value，取代原本範圍的最小值

    elif int(guess) > secret:
        max_value = int(guess)
        # #  如果guess大於secret，則guess會變成最大value，取代原本範圍的最大值


# * serialization 和 deserialization 練習

# #舉例: Book ==>藉由 serialization==> Binary 檔案 ==>藉由 deserialization ==> book
# # 現實例子: database ， SQL
# & 要import pickle
# # in pickle ,被用來連結binary files


x = 10
y = 100
my_List = [1, 2, 3, 4, 5, 9]


def save_data():
    global x, y, my_List
    data = {"x": x, "y": y, "my_List": my_List}
    with open("my_pickle_file", mode="wb") as pfile:
        pickle.dump(data, pfile)  # & dump(我要存的object, 我要存的地方)


save_data()

x = None
y = None
my_List = None


def restore_data():
    global x, y, my_List

    with open("my_pickle_file", mode="rb") as pfile:
        data = pickle.load(pfile)  # & dump(我要存的object, 我要存的地方)
        x = data["x"]
        y = data["y"]
        my_List = data["my_List"]


restore_data()
print(x, y, my_List)


# * shelve 與法練習
# shelve是:在pickle這個module上再做一個module。在shelve當中得object，都已經pickle了
# shelve 是利用pickle 的serialization，把object存到 dictionary
# 藉由使用 shelve，我們只需要 拿出必要的data，而不用load全部的tuples in memmory
# & import shelve


intergers_1 = [1, 2, 3, 4, 5, 6]
intergers_2 = [6, 7, 8, 9, 10]
intergers_3 = [100, 101, 102, 103]
with shelve.open("shelf-example", "c") as shelve:
    shelve["ints_1"] = intergers_1  # 設定shelve的 dictionary的Key
    shelve["ints_2"] = intergers_2
    shelve["ints_3"] = intergers_3

with shelve.open("shelf-example", "r") as shelve:
    for key in shelve.keys():
        print(key)
    print(shelve["ints_2"])  # 輸出[6, 7, 8, 9, 10]
