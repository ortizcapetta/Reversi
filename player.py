import board as b
import random

boardeval = [[10000, -3000, 1000, 800, 800, 1000, -3000, 10000],
             [-3000, -5000, -450, -500, -500, -450, -5000, -3000],
             [1000, -450, 30, 10, 10, 30, -450, 1000],
             [800, -500, 10, 50, 50, 10, -500, 800],
             [800, -500, 10, 50, 50, 10, -500, 800],
             [1000, -450, 30, 10, 10, 30, -450, 1000],
             [-3000, -5000, -450, -500, -500, -450, -5000, -3000],
             [10000, -3000, 1000, 800, 800, 1000, -3000, 10000]]


def miniMax(color, board, depth, maxPlayer):
    if depth == 0 or board.getLegalMoves(color) == []:
        return board.getScore().get(color)

    if maxPlayer:
        bestValue = -1
        for x in board.getLegalMoves(color):
            newBoard = b.Board()
            newBoard.duplicateBoard(board)
            newBoard.placeTile(color, x[0], x[1])
            v = miniMax(color,newBoard,depth - 1, False)
            bestValue = max(bestValue, v)
    else:
        bestValue = 10000000
        for x in board.getLegalMoves(color):
            newBoard = b.Board()
            newBoard.duplicateBoard(board)
            newBoard.placeTile(color, x[0], x[1])
            v = miniMax(color,newBoard,depth - 1, True)
            bestValue = min(bestValue, v)
    return bestValue

def miniMaxStart(color,board):
    depth = 3
    moves = board.getLegalMoves(color)
    biggest = -1000000000
    if moves == []:
        return None

    for x in moves:
        nbiggest = miniMax(color,board,depth,True) + boardeval[x[0]][x[1]]
        if nbiggest > biggest:
            biggest = nbiggest
            move = x
        elif nbiggest == biggest:
            rand = random.randint(0, 1)
            if rand == 0:
                biggest = nbiggest


    return move

