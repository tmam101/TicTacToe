from Board import Board
import sys

# trials1 = int(sys.argv[1])
# trials2 = int(sys.argv[2])
# trials3 = int(sys.argv[3])

trials1 = 100
trials2 = 500
trials3 = 2000


board = Board()
board.train(trials1, trials2, trials3)


# This tests diagonals
# board.cells[0][0][0] = board.cells[1][1][1] = board.cells[2][2][2] = board.cells[3][3][3] = "X"
# board.cells[0][3][0] = board.cells[1][2][1] = board.cells[2][1][2] = board.cells[3][0][3] = "X"
# board.cells[0][0][3] = board.cells[1][1][2] = board.cells[2][2][1] = board.cells[3][3][0] = "X"
# board.cells[0][3][3] = board.cells[1][2][2] = board.cells[2][1][1] = board.cells[3][0][0] = "X"

# print(board.toString())
# print board.win()


# for i in range(10):
#     board.playGame(True, i)
#     if i in [9]:
#         print(board.rewToString(i))
# for i in range(100):
#     board.playGame(False, i)
#     if i in [25, 50, 75, 100]:
#         print(board.rewToString(i))



