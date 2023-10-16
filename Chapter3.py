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


# * For in range()練習使用
for i in range(0, 10, 1):
    # & range(start,stop,step)
    # & range(可填-預設是0，必填(excluded，不包括輸入的數字)，可填-預設是1)
    print(i)


# * enumerate() 和 zip() 練習使用
for counter, char in enumerate("How are you today?"):
    # & 把字串的元素加上index形成tuple
    # # 語法是: 增加counter( index ) 到iterable object，讓它們形成tuple of 2 elements

    if counter < 10:  # counter用來追蹤iterable objects發生幾次
        print(char)

# #等同於下面程式碼
# counter = 0
# for letter in "How are you today?":
#     if counter < 10:
#         print(letter)
#     counter += 1


x = [1, 2, 3]
y = ['A', 'B', 'c']
z = ['a', 'b', 'c', 'd', 'e']
for tuple in zip(x, y, z):  # & zip()視作tuple packing，然後會依據元素最少者，為標準
    print(tuple)
# # zip()function ，用來接收iterable objects並且merge成 tuples


# * comprehension語法 (list , set, dictionary)
# list練習
x = [1, 2, 3, 4]
# & if(condtion)這個條件，可寫可不寫
x_squared_list = [item ** 2 for item in x if item > 2]
# &  new_list = [operation for variable in original list (if )]
print(x_squared_list)
# x = [1, 2, 3, 4]
# squared_x = []
# for item in x:
#     squared_x.append(item ** 2)
#     print(squared_x)


# dictionary練習
x = [1, 2, 3, 4, 5]
x_squared_dict = {item: item**2 for item in x if item > 2}
print(x_squared_dict)

# set練習
x = [1, 2, 3, 4, 5]
x_squared_set = {item**2 for item in x if item > 2}
print(x_squared_set)

# generator練習

# 跟list很相像，差別在於generator的記憶體使用，相對有效率
x = [1, 2, 3, 4, 5]
x_squared_generator = (item ** 2 for item in x)
# & 用小括號，而不是大括號
print(x_squared_generator)
for i in x_squared_generator:
    print(i)
