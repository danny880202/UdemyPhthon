
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

# *  With 語法練習

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
