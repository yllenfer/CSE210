#Tic tac toe game built while taking programming with classes class. Refereces from other people's code were used.
#Author: Yllen Fernandez

# variable that stores the number chosen
choice = []

#looping to get numbers from 1 to 9 and convert them into string
for i in range(0, 9):
    choice.append(str(i + 1))



#function to create and print table
def board():
    print(choice[0] + "|" +  choice[1] + "|" +  choice[2])
    print("_" + "+" + "_" + "+" + "_")
    print(choice[3] + "|" + choice[4] + "|" + choice[5])
    print("_" + "+" + "_" + "+" + "_")
    print(choice[6] + "|" + choice[7] + "|" + choice[8] + "\n")


#Game
def game():
    #there's only one varible that stores the two players movements and it set to true
    firstPlayer = True
    #there's not winner yet so variable is set to be false
    winner = False
    #while there's no winner the game wull be ran
    while  not winner:
        board()
        #Printing which player should play
        if firstPlayer:
            print("x's turn to choose a square (1-9):")
        else:
            print("o's turn to choose a square (1-9):")
        try:
            #move should be an interger that will be tried, if it's not the case, the turn will be lost
            move = int(input("Move: "))
        except:
            print("... ")
            continue
        if choice[move -1] == "X" or choice[move -1 ] == "O":
            #Movement cannot be O or X
            print("Enter a valid move ")
            continue
       #Replacing number by either O or X
        if firstPlayer:
            choice[move -1] = "X"
        else:
            choice[move -1] = "O"

        firstPlayer = not  firstPlayer

#if a player completes three lines in the board, there will be a winner
        for i in range(0, 3):
            a = i * 3
            #if choice 1 + 2 and 3 are the choice, there will be a winner
            if choice[a] == choice[(a + 1)] and choice[a] == choice[(a + 2)]:
                winner == True
                board()

            if choice[i] == choice[(i + 3)] and choice[i] == choice[(a + 6)]:
                winner == True
                board()
        if ((choice[0] == choice[4] and choice[0] == choice[8]) or
            (choice[2] == choice[4] and choice[4] == choice[6])):
             winner = True
             board()
#game will be ended if there's a winner
    print("Good game. Thanks for playing!")






if __name__ == "__main__":
    game()

