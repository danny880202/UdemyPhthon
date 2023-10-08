

a = "Today is a good day"
print(a == a.lower())  # 判斷a 這句話，是不是全部小寫

a = 10
b = 5

print(a == b)
print(a != b)
print(a*b)

# * Truthy 和 Falsy value定義
print(bool(0.0))  # Falsy
print(bool("danny"))  # Truthy
print(bool([1, 2, 3, 5]))  # Truthy
print(bool(None))  # Falsy

# * Short-Circuit 練習
if 2 or (10/0):
    print("程式沒有錯誤")
if (10/0) or 2:
    print("程式有錯誤，因為先偵測到錯誤，short-circuit直接判定失誤，所以不用在計算後面[完整的]")
