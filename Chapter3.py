if False:
    print("This is so true")
else:
    print("This is false")


# # * if -else 練習
# # & python 沒有 Switch 語法
# Age = 5
# if Age < 8:
#     print("This movie is free for you!")
# elif 8 <= age < 65:
#     print("You need to pay $300!")
# else:
#     print("You only pay for $150!")

# name = input("Enter your name:")
# money = input("Enter your cash amount: ")
# hungry = input("Are you hungry? (Y/N) ")

# if hungry == "Y":
#     if int(money) >= 30:
#         print(f"{name} he should go eat breakfast!")
#     else:
#         print(f"{name} is hungry but might not have enough money to buy breakfast!!")
# elif hungry == "N":
#     if int(money) >= 30:
#         print(f"{name} has budget but doesn't want to eat breakfast~")
#     else:
#         print(f"{name} has no money but {name} is not hungry~~")
# else:
#     print("Please make sure that you either Y or N!")

for letter in "Hello World":
    if (letter == letter.upper()):
        print(letter)
for a, b, c in [(1, 2, 5), (3, 5, 6), (5, 7, 8)]:
    print(a+b+c)
# 等同於 tuple[0]+tuple[1]

# * for in 迭代用法
myDictionary = {"name": "Danny", "age": 25}
for item in myDictionary.values():
    print(item)
for key in myDictionary.items():  # tuple輸出
    print(key)
for key in myDictionary.keys():
    print(key)

for key, value in myDictionary.items():
    print(f"The key is {key}")
    print(f"The value is {value}")

counter = 0
for i in "1234":
    for j in "abcdefg":
        print(i, j)
        counter += 1
    print(f"counter is now {counter}")
# & pyhton 的縮排很重要，在不同位置，輸出表現就不同。可以操作這個print來練習

# * 巢狀迴圈， Break使用練習 和 Continue使用練習

for i in "1234567":
    if i == "5":
        break
    for j in "abcdefg":

        if j == "c":
            break
        print(i, j)

# for i in "ABCDE":
#     print("Now the curreny i is " + i)
#     if i == "B":
#         continue
#     print(i)
# print("Here is the line after continue")
