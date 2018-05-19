import board as b
import copy

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
    depth = 4
    moves = board.getLegalMoves(color)
    biggest = -100000
    if moves == []:
        return None

    for x in moves:
        nbiggest = miniMax(color,board,depth,True)
        if nbiggest > biggest:
            biggest = nbiggest
            move = x

    return move

