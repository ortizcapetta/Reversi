import board as b
import player


'''
board = b.Board()
board.displayBoard()
x = board.translateXCoor('D')
y = board.translateYCoor('3')
print(board.checkIfValid('B', x, y))
moves = board.getLegalMoves('B')
print(moves)
board.placeTile('B',2,3)
board.displayBoard()
moves = board.getLegalMoves('W')
print(moves)
board.placeTile('W',2,2)
board.displayBoard()
board.getMove('B')
'''

def getPlayerChoice():
    cont = True
    while cont:
        option = input("Options: \n"
                       "1. P v P\n"
                       "2. P v AI\n"
                       "Enter number of selection:")
        if option == '1' or option == '2':
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
            print(board.getLegalMoves(color))
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
            print("\n ----------PLAYER " + str(pColors.index('W')) + " WINS---------\n")
        elif scores.get('W') < scores.get('B'):
            print("\n ----------PLAYER " + str(pColors.index('B')) + " WINS---------\n")
        else:
            print("\n ---------- IT'S A TIE ---------\n")

        print("THANKS FOR PLAYING. STARTING OVER.")

def StartvsAI():
    '''
    board = b.Board()
    board.displayBoard()
    x = board.translateXCoor('D')
    y = board.translateYCoor('3')
    print(board.checkIfValid('B', x, y))
    moves = board.getLegalMoves('B')
    print(moves)
    board.placeTile('B', 2, 3)
    board.displayBoard()
    moves = board.getLegalMoves('W')
    print(moves)
    board.placeTile('W', 2, 2)
    board.displayBoard()
    v = player.miniMaxStart('B', board)
    print(v)'''

    cont1 = True

    while cont1:
        board = b.Board()
        pColors= board.getPlayerColor() # index0 = 1 , index1 = 2
        turn = board.giveTurn()
        print("Player" + str(turn) +" goes first\n")
        cont2 = True
        while board.getLegalMoves('B') != [] or board.getLegalMoves('W') != []:
            color = pColors[turn-1]
            print(board.getLegalMoves(color))
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
            print("\n ----------PLAYER " + str(pColors.index('W')) + " WINS---------\n")
        elif scores.get('W') < scores.get('B'):
            print("\n ----------PLAYER " + str(pColors.index('B')) + " WINS---------\n")
        else:
            print("\n ---------- IT'S A TIE ---------\n")

        print("THANKS FOR PLAYING. STARTING OVER.")


option = getPlayerChoice()
if option =='1':
    StartPvP()
else:
    StartvsAI()
