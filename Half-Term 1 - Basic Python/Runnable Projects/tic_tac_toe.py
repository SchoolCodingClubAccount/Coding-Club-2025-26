def createBoard(Array1, Array2, Array3, Array4, irrelevant):
    for aa in Array4:
        print(aa, end="|")
    print()
    for ab in Array3:
        print(ab, end="|")
    print()
    for ac in Array2:
        print(ac, end="|")
    print()
    for ad in Array1:
        print(ad, end="|")
    print()
    for ae in irrelevant:
        print(ae, end=" ")
    print()

def player1(Array1, Array2, Array3, Array4, irrelevant):
    player1Move = input("Please make your move: ")
    if player1Move == "A1":
        if Array1[1] != "⬜️":
            player1(Array1, Array2, Array3, Array4, irrelevant)
        else:
            Array1[1] = "🟢"
    elif player1Move == "B1":
        if Array1[2] != "⬜️":
            player1(Array1, Array2, Array3, Array4, irrelevant)
        else:
            Array1[2] = "🟢"
    elif player1Move == "C1":
        if Array1[3] != "⬜️":
            player1(Array1, Array2, Array3, Array4, irrelevant)
        else:
            Array1[3] = "🟢"
    elif player1Move == "A2":
        if Array2[1] != "⬜️":
            player1(Array1, Array2, Array3, Array4, irrelevant)
        else:
            Array2[1] = "🟢"
    elif player1Move == "B2":
        if Array2[2] != "⬜️":
            player1(Array1, Array2, Array3, Array4, irrelevant)
        else:
            Array2[2] = "🟢"
    elif player1Move == "C2":
        if Array2[3] != "⬜️":
            player1(Array1, Array2, Array3, Array4, irrelevant)
        else:
            Array2[3] = "🟢"
    elif player1Move == "A3":
        if Array3[1] != "⬜️":
            player1(Array1, Array2, Array3, Array4, irrelevant)
        else:
            Array3[1] = "🟢"
    elif player1Move == "B3":
        if Array3[2] != "⬜️":
            player1(Array1, Array2, Array3, Array4, irrelevant)
        else:
            Array3[2] = "🟢"
    elif player1Move == "C3":
        if Array3[3] != "⬜️":
            player1(Array1, Array2, Array3, Array4, irrelevant)
        else:
            Array3[3] = "🟢"
    else:
        player1(Array1, Array2, Array3, Array4, irrelevant)

def player2(Array1, Array2, Array3, Array4, irrelevant):
    player2Move = input("Please make your move: ")
    if player2Move == "A1":
        if Array1[1] != "⬜️":
            player1(Array1, Array2, Array3, Array4, irrelevant)
        else:
            Array1[1] = "❌"
    elif player2Move == "B1":
        if Array1[2] != "⬜️":
            player1(Array1, Array2, Array3, Array4, irrelevant)
        else:
            Array1[2] = "❌"
    elif player2Move == "C1":
        if Array1[3] != "⬜️":
            player1(Array1, Array2, Array3, Array4, irrelevant)
        else:
            Array1[3] = "❌"
    elif player2Move == "A2":
        if Array2[1] != "⬜️":
            player1(Array1, Array2, Array3, Array4, irrelevant)
        else:
            Array2[1] = "❌"
    elif player2Move == "B2":
        if Array2[2] != "⬜️":
            player1(Array1, Array2, Array3, Array4, irrelevant)
        else:
            Array2[2] = "❌"
    elif player2Move == "C2":
        if Array2[3] != "⬜️":
            player1(Array1, Array2, Array3, Array4, irrelevant)
        else:
            Array2[3] = "❌"
    elif player2Move == "A3":
        if Array3[1] != "⬜️":
            player1(Array1, Array2, Array3, Array4, irrelevant)
        else:
            Array3[1] = "❌"
    elif player2Move == "B3":
        if Array3[2] != "⬜️":
            player1(Array1, Array2, Array3, Array4, irrelevant)
        else:
            Array3[2] = "❌"
    elif player2Move == "C3":
        if Array3[3] != "⬜️":
            player1(Array1, Array2, Array3, Array4, irrelevant)
        else:
            Array3[3] = "❌"
    else:
        player2(Array1, Array2, Array3, Array4, irrelevant)


def checkWin(Array1, Array2, Array3):
    if ((Array1[1] == Array1[2] and Array1[2] == Array1[3]) and ((Array1[1] == "❌" or Array1[1] == "🟢"))):
        if (Array1[1] == "❌"):
            print("Player ❌ has won!")
            return True

        else:
            print("Player 🟢 has won!")
            return True
    elif ((Array2[1] == Array2[2] and Array2[2] == Array2[3]) and ((Array2[1] == "❌" or Array2[1] == "🟢"))):
        if (Array2[1] == "❌"):
            print("Player ❌ has won!")
            return True

        else:
            print("Player 🟢 has won!")
            return True

    elif ((Array3[1] == Array3[2] and Array3[2] == Array3[3]) and ((Array3[1] == "❌" or Array3[1] == "🟢"))):
        if (Array3[1] == "❌"):
            print("Player ❌ has won!")
            return True

        else:
            print("Player 🟢 has won!")
            return True
    elif ((Array1[1] == Array2[1] and Array2[1] == Array3[1]) and ((Array3[1] == "❌" or Array3[1] == "🟢"))):
        if (Array3[1] == "❌"):
            print("Player ❌ has won!")
            return True

        else:
            print("Player 🟢 has won!")
            return True
    elif ((Array1[2] == Array2[2] and Array2[2] == Array3[2]) and ((Array3[2] == "❌" or Array3[2] == "🟢"))):
        if (Array3[2] == "❌"):
            print("Player ❌ has won!")
            return True

        else:
            print("Player 🟢 has won!")
            return True
    elif ((Array1[3] == Array2[3] and Array2[3] == Array3[3]) and ((Array3[3] == "❌" or Array3[3] == "🟢"))):
        if (Array3[3] == "❌"):
            print("Player ❌ has won!")
            return True

        else:
            print("Player 🟢 has won!")
            return True
    elif ((Array1[1] == Array2[2] and Array2[2] == Array3[3]) and ((Array3[3] == "❌" or Array3[3] == "🟢"))):
        if (Array3[3] == "❌"):
            print("Player ❌ has won!")
            return True

        else:
            print("Player 🟢 has won!")
            return True
    elif ((Array1[3] == Array2[2] and Array2[2] == Array3[1]) and ((Array3[1] == "❌" or Array3[1] == "🟢"))):
        if (Array3[1] == "❌"):
            print("Player ❌ has won!")
            return True

        else:
            print("Player 🟢 has won!")
            return True

    elif ((Array1[1] != "⬜️") and (Array1[2] != "⬜️") and (Array1[3] != "⬜️") and (Array2[1] != "⬜️") and (Array2[2] != "⬜️") and (Array2[3] != "⬜️") and (Array3[1] != "⬜️") and (Array3[2] != "⬜️") and (Array3[3] != "⬜️")):
        print("IT IS A DRAW!")
        return True
    else:
        return False

print("Make sure you make your moves in chess notation!")
Array4 = ["⬛️", "⬛️", "⬛️", "⬛️"]
Array3 = ["❸", "⬜️", "⬜️", "⬜️"]
Array2 = ["❷", "⬜️", "⬜️", "⬜️"]
Array1 = ["❶", "⬜️", "⬜️", "⬜️"]
irrelevant = ["🅞", "🅰 ", "🅱 ", "🅲"]

checkWin(Array1, Array2, Array3)
moves = 0

while True:
    if checkWin(Array1,Array2,Array3) == False:
        createBoard(Array1, Array2, Array3, Array4, irrelevant)
        player1(Array1, Array2, Array3, Array4, irrelevant)
        checkWin(Array1, Array2, Array3)
        moves+=1
    if checkWin(Array1,Array2,Array3) == False:
        createBoard(Array1, Array2, Array3, Array4, irrelevant)
        player2(Array1, Array2, Array3, Array4, irrelevant)
        checkWin(Array1, Array2, Array3)
        moves += 1
    if checkWin(Array1,Array2,Array3) == True:
        if moves > 4:
            print("Thanks for playing!")
            break