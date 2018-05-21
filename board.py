import random,copy
CUTOFF = 3
class Board():

    def __init__(self):
        #set up the empty board
        self.__squares = []
        #Valid coordinates with their definitions in the array ie coordinate C3 is [2][2]
        self.__xCoor = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}
        self.__yCoor = {'1': 0, '2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6, '8': 7}
        self.__directions = [(1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1)]
        # each of these represent a direction in which a move will be made (SE,E,NE,N,NW,W,SW,S)

        for i in range(8):
            self.__squares.append([' '] * 8)


        #Reversi starts with 4 pieces in the center
        # 1 = Black, 2 = White
        self.__squares[3][4] = 'B'
        self.__squares[4][3] = 'B'
        self.__squares[3][3] = 'W'
        self.__squares[4][4] = 'W'

    def displayBoard(self):
        #display the current board

        HLINE = '  +---+---+---+---+---+---+---+---+'

        print('    A   B   C   D   E   F   G   H')
        print(HLINE)
        for y in range(8):
            print(y + 1, end=' ')
            for x in range(8):
                print('| %s' % (self.__squares[x][y]), end=' ')
            print('| %s' % (y+1))
            print(HLINE)
        print('    A   B   C   D   E   F   G   H\n\n')
        score = self.getScore()
        print('  ----------CURRENT SCORE---------')
        print('  BLACK:     %s       WHITE:     %s'%(score.get('B'), score.get('W')))


    #simple method to check if coordinate is between the 8x8 boundaries
    def existsOnBoard(self, x, y):
        return x >= 0 and x <= 7 and y >= 0 and y <= 7

    def translateXCoor(self,x):
        if x in self.__xCoor:
            return self.__xCoor[x]
        else:
            return None

    def translateYCoor(self,y):
        if y in self.__yCoor:
            return self.__yCoor[y]
        else:
            return None


    def checkIfValid(self,color, xini, yini):

        # if Square is occupied, not a valid move or if square doesn't exist

        if self.__squares[xini][yini] != ' ' or self.existsOnBoard(xini, yini) is False:

            return False

        if color == 'B':
            enemy = 'W'
        else:
            enemy = 'B'
        flip = []

        for xdir, ydir in self.__directions:
            x = xini
            y = yini
            x = xdir + x
            y = ydir + y
            if self.existsOnBoard(x, y) and self.__squares[x][y] == enemy:
                x += xdir
                y += ydir
                if not self.existsOnBoard(x, y):
                    continue
                while self.__squares[x][y] == enemy and self.existsOnBoard(x,y):
                    x += xdir
                    y += ydir
                    if not self.existsOnBoard(x, y):  # break out of while loop, then continue in for loop
                        break
                if not self.existsOnBoard(x, y):
                    continue
                if self.__squares[x][y] == color:
                    # There are pieces to flip over. Go in the reverse direction until we reach the original space, noting all the tiles along the way.
                    while True:
                        x -= xdir
                        y -= ydir
                        if x == xini and y == yini:
                            break
                        flip.append([x, y])
        self.__squares[xini][yini] = ' '  #put space back to emtpy, this is used to check all legal moves
        if len(flip) == 0:  #no tiles flipped, therefor not a valid move
            return False
        return flip

    def placeTile(self,color,x,y):
        flips = self.checkIfValid(color,x,y)
        if flips is False:
            return False #Not a valid move
        self.__squares[x][y] = color
        for x,y in flips:
            self.__squares[x][y]=color
        return True #valid move !

    def getLegalMoves(self, color):

        legalMoves = []

        for x in range(8):
            for y in range(8):
                if self.checkIfValid(color, x, y) is not False:
                    legalMoves.append([x, y])
        return legalMoves

    def getScore(self):
        bscore=0
        wscore = 0
        for x in range(8):
            for y in range(8):
                if self.__squares[x][y] == 'B':
                    bscore += 1
                if self.__squares[x][y] == 'W':
                    wscore += 1
        scores = {'B': bscore, 'W': wscore}
        return scores

    def getMove(self,color):
        cont = True
        print("A valid coordinate must be a combination of x and y, a letter and a number")
        print("Example: A1,B3,C9...etc....")
        while cont:
            move = input("Enter move or type exit to quit game:" )
            if move.lower() == "exit":
                cont = False
                return "exit"

            #check if it is a valid coordinate
            if move[0].upper() in self.__xCoor and move[1:2] in self.__yCoor:
                y = self.translateYCoor(move[1:2])
                x = self.translateXCoor(move[0].upper())
                #check if its an actual valid move
                if self.checkIfValid(color, x, y):

                    return [x, y]
                else: print("That is not a valid move.")
            else:
                print("\nThat is not a valid coordinate.\n"
                      "First type the column with a letter from A to H\n"
                      "then type the row with a number from 1 to 8\n")

    def getPlayerColor(self):
        choice = ''
        while choice.upper() != 'W' or choice.upper() != 'B':
            choice = input("Player 1 enter B for Black or W for White")
            if choice == 'W':
                return ['W','B']
            elif choice == 'B':
                return ['B','W']

    def giveTurn(self):
        flip = random.randint(0, 1)
        if flip == 0:
            return 1
        else:
            return 2

    def duplicateBoard(self,board):
        for x in range(8):
            for y in range(8):
                self.__squares[x][y] = board.__squares[x][y]










