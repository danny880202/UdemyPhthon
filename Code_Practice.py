
# *輸出 1~100
def printMany():
    for i in range(1, 101):
        print(i)


printMany()


# *輸出 1,4,7,10,...88
def printEvery3():
    for i in range(1, 89, 3):
        print(i)


printEvery3()

# * 找出第一個大寫字母以及他的index


def position(string):
    for num, s in enumerate(string):
        if s == s.upper():
            print((s, num))
            return (s, num)
        


    print(-1)
    return -1
    # # 不能在 if 之後加入 else，因為會只跑1次迭代，就輸出了


position("abcd")
position("Abcd")
position("abCD")

# * 找出最後一個大寫字母以及他的index


def position_1(string):
    for index in range(len(string)-1, -3, -1):
        if string[index] == string[index].upper():
            return (string[index], index)
    return ("cant find it.")


print(position_1("Abccccc"))

# #先預設一個變數為-1，如果找到大寫，則取代，若沒有，則輸出預設值


def position(string):
    final_answer = -1
    for num, s in enumerate(string):
        if s == s.upper():
            final_answer = (s, num)
    return final_answer


print(position("aacacabCD"))


# * 輸入2個，並且找出lst當中，總共有幾個小於num的數字
def findSmallCount(lst, num):
    count = 0
    for element in lst:
        if element < num:
            count += 1
    return count


print(findSmallCount([1, 2, 3], 2))  # returns 1
print(findSmallCount([1, 2, 3, 4, 5], 0))  # returns 0
print(findSmallCount([1, 2, 3, 4, 5], 30))

# * 輸入2個，並且找出lst當中，小於num的數字，之後算出他們的加總


def findSmallTotal(lst, num):
    count = 0
    sum = 0
    for element in lst:
        if element < num:
            sum += element
    return sum


print(findSmallTotal([1, 2, 3], 3))  # returns 3
print(findSmallTotal([1, 2, 3], 1))  # returns 0
print(findSmallTotal([3, 2, 5, 8, 7], 999))  # returns 25
print(findSmallTotal([3, 2, 5, 8, 7], 0))  # returns 0


# *輸入2個，並且找出lst當中，小於num的數字，之後把他們集合再一起形成list輸出

def findAllSmall(lst, num):
    result = []  # empty list

    for element in lst:
        if element < num:
            result.append(element)

    return (result)


print(findAllSmall([1, 2, 3], 10))  # returns [1, 2, 3]
print(findAllSmall([1, 2, 3], 2))  # returns [1]
print(findAllSmall([1, 3, 5, 4, 2], 4))  # returns [1, 3, 2]


# *輸入lst，之後加總他們

def summ(lst):
    sum = 0
    for element in lst:
        sum += element

    return sum


print(summ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))  # returns 55
print(summ([]))  # return 0
print(summ([-10, -20, -30]))  # return -60


# * 輸入數字，輸出 * 金字塔排列

def stars(n)
    for i in range (1,n+1):
        print("*"* i)


stars(20)

# * 輸入數字，輸出 * 山波浪金字塔

def stars2(n):
    for i in range (1,n+1):
        print("*" * i)
    # 1,2,3,4,...,n
    
    for a in range(n-1,0,-1):
        print("*" * a)
    # n-1 , n-2 , ... ,1
    
stars2(3)

#*  輸入數字，輸出9*9乘法表

def table(n):
    for i in range(1,10):
        a=n*i
        print(f"{n} x {i} ={a}")
        
table(3)

#* 輸出 9*9* 乘法表

def table9to9():
    # # nest loop
    for i in range(1,10):
        for j in range(1,10):
            a=i*j
            print(f"{i} x {j} = {a}")

table9to9()


#* Swap  大寫變小寫。小寫便大寫

def swap(string):
    result = ""
    for letter in string:
        if letter == letter.upper():
            result += letter.lower()
        else:
            result += letter.upper()
            
    print(result)
    return  result
            
swap("Aloha")
swap("Love you.")
swap("Today IS a Good day")



#* 輸入list 找出最小值

# # 思路歷程

# # (1) 設定index 0 elemnt 當作min element
# # (2) for loop 在每個 iteration中
# # (3) 如果 element 是小於我現在目前的min element
# # (4) 如果是 yes的話， 則更改我的 min element



def findMin(lst):
    if len(lst)==0:
        print("undefined")
        return "undefined"
    min_element = lst[0]#(1)
    for element in lst:
        if element < min_element:
            min_element = element
    print(min_element)
    return min_element
    
findMin([1, 2, 5, 6, 99, 4, 5]); # returns 1
findMin([]); # returns "undefined"
findMin([1, 6, 0, 33, 44, 88, -10]); # returns -10    