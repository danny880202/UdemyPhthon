
# *   9宮格(Tic Tac Toe game) 圈圈叉叉

counter = 0

row1 = [' ', ' ', ' ']  # 使用者輸入 7,8,9, 對應 row1 的  index_0 index_1 index_2
row2 = [' ', ' ', ' ']  # 使用者輸入 4,5,6  對應 row2 的  index_0 index_1 index_2
row3 = [' ', ' ', ' ']  # 使用者輸入 1,2,3  對應 row1 的  index_0 index_1 index_2


def display(row1, row2, row3):
    print(row1)
    print(row2)
    print(row3)


def user_choice():
    choice = input("請輸入一個數字 (1~9) : ")
    while not choice.isdigit() or (int(choice) not in range(1, 10)):
        if not choice.isdigit():
            print("抱歉，你輸入的型態並不符合我們的要求")
            choice = input("請輸入一個數字 (1~9) : ")
        else:
            print("你輸入的數字不在1~9的範圍內 ")
            choice = input("請輸入一個數字 (1~9) : ")
    return int(choice)


# user_1 輸入 O
# user_2 輸入 X
# user_1 輸入 O

def getCurrenttSymbol():
    global counter
    symbol_list = ["X", "O"]
    counter += 1
    return symbol_list[counter % 2]


# & 輸入數字，並且把 getCurrenttSymbol() 指定給row[]，所以數字是index
def update_table(value):
    global row1, row2, row3
    if value in range(7, 10):
        if row1[value % 3 - 1] == " ":
            row1[value % 3 - 1] = getCurrenttSymbol()
            return True  # !  如果是空字串，則把"O" "X" 給指定進去，並且回傳True。如果不為空，則回傳False
        else:
            return False
    elif value in range(4, 7):
        if row2[value % 3 - 1] == " ":
            row2[value % 3 - 1] = getCurrenttSymbol()
            return True
        else:
            return False
    else:
        if row3[value % 3 - 1] == " ":
            row3[value % 3 - 1] = getCurrenttSymbol()
            return True
        else:
            return False


def check_winning():
    player_1_wins = False
    player_2_wins = False

    # &  橫線判斷，總共有 3 條橫線
    if (row1[0] == row1[1] and row1[1] == row1[2] and (" " not in row1)):
        if (row1[0] == "O"):
            player_1_wins = True
        else:
            player_2_wins = True

    elif (row2[0] == row2[1] and row2[1] == row2[2] and (" " not in row2)):
        if (row2[0] == "O"):
            player_1_wins = True
        else:
            player_2_wins = True

    elif (row3[0] == row3[1] and row3[1] == row3[2] and (" " not in row3)):
        if (row3[0] == "O"):
            player_1_wins = True
        else:
            player_2_wins = True

    # &  直線判斷， 總共有 3 條線
    elif (row1[0] == row2[0] and row2[0] == row3[0] and (row1[0] != " " and row2[0] != " " and row3[0] != " ")):
        if (row1[0] == "O"):
            player_1_wins = True
        else:
            player_2_wins = True

    elif (row1[1] == row2[1] and row2[1] == row3[1] and (row1[1] != " " and row2[1] != " " and row3[1] != " ")):
        if (row1[1] == "O"):
            player_1_wins = True
        else:
            player_2_wins = True

    elif (row1[2] == row2[2] and row2[2] == row3[2] and (row1[2] != " " and row2[2] != " " and row3[2] != " ")):
        if (row1[2] == "O"):
            player_1_wins = True
        else:
            player_2_wins = True

    # & 斜線判斷， 總共有2條斜線
    elif (row1[0] == row2[1] and row2[1] == row3[2] and (row1[0] != " " and row2[1] != " " and row3[2] != " ")):
        if (row1[0] == "O"):
            player_1_wins = True
        else:
            player_2_wins = True

    elif (row1[2] == row2[1] and row2[1] == row3[0] and (row1[2] != " " and row2[1] != " " and row3[0] != " ")):
        if (row1[2] == "O"):
            player_1_wins = True
        else:
            player_2_wins = True

    # # 如果 if True ，則回傳string
    if player_1_wins:
        return "player_1 wins the game"  # ! 我在這裡卡了25分鐘，只因為 在字串" " 雙引號中間，多加了一個 空格!!!!!
    elif player_2_wins:
        return "player_2 wins the game"  # !記住" " 字串雙引號，空格也是很重要的判斷依據!!!!
    else:
        return "no one wins"  # & else條件符合會發生2種情況，第1種:平手。第2種:遊戲還在繼續進行中
    #!所以當前2個條件都不符合。While true 有可能會一直卡在" on one wins " 這個else 條件"


def start_game():
    while True:
        display(row1, row2, row3)
        while True:
            choice = user_choice()
            if update_table(choice):
                break  # ! 如果update_table()回傳True，則 if ture便成立，進入statement，也就是break
            else:
                print("這個位置已經有人輸入過了，請換別的位置")
                # !  表示update_table()回傳False，進入到else的statement

        # & 看check_winning回傳哪個string
        result = check_winning()
        if result == "player_1 wins the game":
            display(row1, row2, row3)
            print("玩家1號獲勝 || 恭喜!! ")
            return
        elif result == "player_2 wins the game":
            display(row1, row2, row3)
            print("玩家2號獲勝 || 恭喜!! ")
            return

        elif result == "no one wins" and counter == 9:
            display(row1, row2, row3)
            print(" 平手!!!")
            return
        # & counter起始值為0，在getCurrenttSymbol()裡面，每次輸出[O][X]，則counter+1。剛好代表一個回合經過，以此來判定是否走完所有回合

        # # 不需要return "沒有人勝利!" 是因為While true會一直執行，然後一直要求user輸入，之後update table，不斷地重啟遊戲


start_game()


#  #判斷平手的方法，有2種 。
#  # 第1種:藉由row1,row2,row3的list，去檢查裡面的index[0~2]，是不是都是空字串?  如果都不是，而且 也 return "no one wins"，則可以輸出平手
#  # 第2種:藉由目前程式碼的counter去做判斷
