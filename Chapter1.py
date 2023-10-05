import math
print(min(3, 5, 6, 7, -10))
print(math.e)
print(math.pi)
print(math.floor(4.95661616))
print(math.ceil(4.1363625656))
print(math.sqrt(36))
print("Water"[3])  # 輸出index[3]的字母

# *反轉字串
myString = "hello"  # 0=>h ，-1=>o,-2=>l,-3=>l,-4=>e,-5=>h
print(myString[0])
print(myString[-1])  # reverse字串，起點為-1
print(myString[-2])
print(myString[-3])
print(myString[-4])
print(myString[-5])

x = "abcdefg"
print(x[2:6])
print(x[1:5:2])  # 第3欄位，是代表每一步 要走的大小，2為一次走2步的意思
print(x[::-1])  # reverse 字串。從頭寫到尾，在-1 reverse
print(x[::2])

# * 單引號 和 雙引號使用
print('I said "Good morning."')
print("I said 'Good evening.'")  # 單引號 和 雙引號可以互用

# * 字串 串接
myString1 = "hello"
myString2 = " I am Danny"
res = myString1 + myString2
print(res)
myNumber1 = 2
print(myString1+str(myNumber1))  # 透過str()能讓數字，串接到字串後面

# * String method 練習1
print(len("water"))
name = "DannyIssoGood"
name.upper()
print(name)  # 這裡使用的是原來name的字串，並非大寫。除非重新賦值，或者在print使用函數
print(name.upper())  # object-oriented programming
name2 = name.upper()
print(name2)
print(name.upper().isupper())
print(name.index("n"))  # 第一個遇到n的index是多少?
print(name.index("sso"))  # 第一個遇到sso，這sub-字串的index是多少

# * String method 練習2
sentence = "Good Morning Everyone"
print(sentence.split(" "))  # 如果要以空格去做字串切割。記得要打上空格
print(list(sentence))  # 切割字串，用每一個字母去做切割，空白字符也會獨立切割
print("I have a string{}".format(" apple"))
print("I have a string{}".format(["zxcv,asdfgewq"]))

print(" {1},  {0},  {3}".format(20, "type a string", 3.14159, 6666))
# &  "{index 隨機}, {index 隨機}"       .format(index 0,index 1,....)

print(" {name},  {age},  {address}".format(
    name="danny", address="taiwan", age=19))

myName = "Danny"
age = 25
print(f"hello, my name is {myName},I am {age} years old.")
# & fstring用法跟formate相同，只不過函數更簡潔，在字串""前面加入f 就行了，其餘大括號用法相同，不能隨意調用index

string3 = "Good is a good day"
print(string3.count("good"))  # 只抓到good，沒有抓到Good
print(string3.lower().count("good"))  # 先把字串全變小寫，在開始抓

# &與.index()功能相同，差別在於如果要抓的substring，不在字串裡面，index會報錯，find則不會
print(string3.find("good"))  # 輸出字串第一次出現的index位置

print(myName.startswith("d"))
print(myName.endswith("ny"))

# * List 練習
friendList = ["Number0", "Number1", "Number2"]
print(f"{friendList[0]},{friendList[1]},{friendList[2]} are my new friends")
print(len(friendList))
a = [1, 2, 1, 5, 1, 1, 1, 13, 6, 9]
b = [5, 61, 9, 8, 1, 2, 5, 3, 4,]
print(a.count(1))  # 計算1出現個數
a[1] = 10
a[2] = 10
print(a)  # & List可以重新賦值[新的值]，但string不行。List is mutable，string is immutable

s = ["第1名", "第2名", "第3名", "第4名", "第5名"]
s.insert(2, "第7名")
print(s)

s.remove("第4名")
print(s)

snumbers = [-1, -3, -5, 8, 9, 2, 0]
snumbers.sort()  # python本身有內建一個sort。其功能為小->大
print(snumbers)

s.reverse()  # 等同於 s=s[::-1] 。 Slicing的reverse效果
print(s)

s.append("第10名")
s.append("第12名")  # 在list中的後面，再加入的意思
s.append(15.0)  # 在python 中的 list型態，不在意資料型態
print(s)

my_lost_data = s.pop()  # pop最右邊的元素
print(s)
print(my_lost_data)  # 回傳被pop掉的元素


s.clear()  # 清空List所有的元素
print(s)

z = [1, 2, 3, 4, 5, 6]
b = z.copy()  # b=[1,2,3,4,5,6]
b[0] = 15  # [15,2,3,4,5,6]
print(z)     # [1,2,3,4,5,6]
print(b)  # [15,2,3,4,5,6]
# &因為使用copy，所以是指向不同的memory，不會更改ram中的元素

b = z  # b=[1,2,3,4,5,6]
b[0] = 15  # [15,2,3,4,5,6]
print(z)     # [15,2,3,4,5,6]
print(b)  # [15,2,3,4,5,6]
# &因為 call by reference

# * list中的list
x = [1, 2, [4, 5, 6], 2, 1, 5, 3, [4, 3, [-10, 4]]]
print(x[2])
print(x[7][2][0])
print(x[7][2])

# *  Dictionary練習
person = {"name": "Danny", "age": 25}
print(person["name"])
print(person["age"])

person = {"x": {"age": [10, 20, 40]}}  # Dictionary中的Dictionary，或者在之中加入list
# & 一個Dictionary(KEY欄位)，他的(value欄位)可以有很多的Dictionary，也可以有很多的List 。

print(person["x"]["age"][2])

x = {}  # 另一種Dictionary寫法。給他空白Dictionary，再給他加入資料
x["name"] = "Danny"
x["age"] = 28
x["name"] = "APPlE"  # Dictionary可以 mutable資料
print(x)
print(x.keys())
print(x.values())
print(x.items())  # 是 key 和 value一對，是一個 list of tuples

# * Tuples 練習
# Tuples 是一個有序 immutable 的sequence of objects ( LIST )
myTuple = (10, "100", "hello")
print(myTuple[0])
print(myTuple.count(10))  # 10出現幾次?

print(myTuple.index("hello"))  # hello在第幾個index

# * Tuple packing 和 Tuple unpacking

x = 10, 15, 17, 126  # 只要用 逗號 隔開，將會自動變成一個 tuple packing
print(x)
print(type(x))  # < class "tuple" >

x = ("Danny", 30)
name, age = x
print(name)
print(age)  # variable names have meanings

x = 67
y = 72

# temp = x
# x = y
# y =temp

x, y = y, x
# &  tuple unpacking =  tuple packing
print(x)
print(y)

a = ([1, 2, 3], "Danny")
a[0][1] = 100
print(a)

# * Sets 練習
# an unordered collection of unique objects

mylist = [5, 1, 4, 2, 3, 6, 1, 3, 5, 2, 4, 7, 6]
myset = set(mylist)
print(myset)

s = set()
s.add(1)
s.add(2)
print(s)
s.add(3)
s.discard(1)
print(s)

a = {1, 3, 4, 5}
b = {3, 4, 7, 8}
print(a.isdisjoint(b))  # A和B 是否互斥
print(a.issubset(b))  # A是否為B的子集
print(a.issuperset(b))  # A是否為B的母集合
print(a.difference(b))  # A-B
print(b.difference(a))  # B-A
print(a.intersection(b))
print(b.intersection(a))
print(a.union(b))
print(b.union(a))
