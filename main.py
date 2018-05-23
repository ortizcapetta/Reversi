import board as b
import player


def getPlayerChoice():
    cont = True
    while cont:
        print("+-+-+-+-+-+-WELCOME TO REVERSI -+-+-+-+-+-+-+\n")
        option = input("------------------Options:------------------- \n"
                       "|\t\t\t\t1. P v P                     | \n"
                       "|\t\t\t\t2. P v AI                    |\n"
                       "|\t\t\t\t3. AI v AI                   |\n"
                       "|\t\t\tEnter number of selection        |\n"
        "--------------------------------------------- \n")
        if option == '1' or option == '2' or option == '3':
            return option
        else:
            print("Not a valid option. Try Again.")

def StartPvP():
    cont1 = True

    while cont1:
        board = b.Board()
        pColors= board.getPlayerColor() # index0 = 1 , index1 = 2
        turn = board.giveTurn()
        print("Player" + str(turn) +" goes first\n")
        cont2 = True
        while board.getLegalMoves('B') != [] or board.getLegalMoves('W') != []:
            color = pColors[turn-1]
            board.displayBoard()
            print("\n ----------PLAYER " + str(turn) + "'s TURN--------\n")
            move = board.getMove(color)
            #move = board.getLegalMoves(color)[0]
            if move == 'exit':
                print("Exiting Game")
                exit()
            else:
                board.placeTile(color, move[0], move[1])

            if turn == 1:
                nturn = 2
            else:
                nturn = 1

            if board.getLegalMoves(pColors[nturn - 1]) != []:
                turn = nturn

        board.displayBoard()
        scores = board.getScore()
        if scores.get('W')>scores.get('B'):
            print("\n ----------PLAYER " + str(pColors.index('W')+1) + " WINS---------\n")
        elif scores.get('W') < scores.get('B'):
            print("\n ----------PLAYER " + str(pColors.index('B')+1) + " WINS---------\n")
        else:
            print("\n ---------- IT'S A TIE ---------\n")

        print("THANKS FOR PLAYING. STARTING OVER.")

def StartvsAI():


    cont1 = True

    while cont1:
        board = b.Board()
        pColors= board.getPlayerColor() # index0 = 1 , index1 = 2
        turn = board.giveTurn()
        print("Player" + str(turn) +" goes first\n")
        cont2 = True
        while board.getLegalMoves('B') != [] or board.getLegalMoves('W') != []:
            color = pColors[turn-1]

            board.displayBoard()
            print("\n ----------PLAYER " + str(turn) + "'s TURN--------\n")
            #move = board.getMove(color)
            #move = board.getLegalMoves(color)[0]

            if turn == 2:
                move = player.miniMaxStart(color, board)
                if move != None:
                    board.placeTile(color, move[0], move[1])
            else:
                move = board.getMove(color)
                #move = board.getLegalMoves(color)[0]
                if move == 'exit':
                    print("Exiting Game. Thanks for playing :)")
                    exit()
                else:
                    board.placeTile(color, move[0], move[1])

            if turn == 1:
                nturn = 2
            else:
                nturn = 1

            if board.getLegalMoves(pColors[nturn - 1]) != []:
                turn = nturn



        board.displayBoard()
        scores = board.getScore()
        if scores.get('W')>scores.get('B'):
            print("\n ----------PLAYER " + str(pColors.index('W')+1) + " WINS---------\n")
        elif scores.get('W') < scores.get('B'):
            print("\n ----------PLAYER " + str(pColors.index('B')+1) + " WINS---------\n")
        else:
            print("\n ---------- IT'S A TIE ---------\n")

        print("THANKS FOR PLAYING")


def AIvsAI():

    cont1 = True

    while cont1:
        board = b.Board()
        if board.giveTurn == 1:
            pColors = ['W', 'B']
        else:
            pColors = ['B', 'W']
        turn = board.giveTurn()
        print("Player" + str(turn) + " goes first\n")
        cont2 = True
        while board.getLegalMoves('B') != [] or board.getLegalMoves('W') != []:
            color = pColors[turn - 1]

            board.displayBoard()
            print("\n ----------PLAYER " + str(turn) + "'s TURN--------\n")
            # move = board.getMove(color)
            # move = board.getLegalMoves(color)[0]

            move = player.miniMaxStart(color, board)
            if move != None:
                board.placeTile(color, move[0], move[1])

            if turn == 1:
                nturn = 2
            else:
                nturn = 1

            if board.getLegalMoves(pColors[nturn - 1]) != []:
                turn = nturn

        board.displayBoard()
        scores = board.getScore()
        if scores.get('W')>scores.get('B'):
            print("\n ----------PLAYER " + str(pColors.index('W')+1) + " WINS---------\n")
        elif scores.get('W') < scores.get('B'):
            print("\n ----------PLAYER " + str(pColors.index('B')+1) + " WINS---------\n")
        else:
            print("\n ---------- IT'S A TIE ---------\n")

        print("THANKS FOR WATCHING")


option = getPlayerChoice()
if option =='1':
    StartPvP()
elif option == '2':
    StartvsAI()
else:
    AIvsAI()
