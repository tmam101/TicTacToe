from Board import Board
import sys
trials1 = sys.argv[1]
trials2 = sys.argv[2]
trials3 = sys.argv[3]

board = Board()
# This tests diagonals
# board.cells[0][0][0] = board.cells[1][1][1] = board.cells[2][2][2] = board.cells[3][3][3] = "X"
# board.cells[0][3][0] = board.cells[1][2][1] = board.cells[2][1][2] = board.cells[3][0][3] = "X"
# board.cells[0][0][3] = board.cells[1][1][2] = board.cells[2][2][1] = board.cells[3][3][0] = "X"
# board.cells[0][3][3] = board.cells[1][2][2] = board.cells[2][1][1] = board.cells[3][0][0] = "X"

print(board.toString())
print board.win()

# TODO have a small perecent be random even after initial phase
# TODO Find x highest reward squares and choose randomly from those?
for i in range(1000):
    board.playGame(True)
for i in range(100):
    board.playGame(False)


# need to get input that tells how many trials to run-three numbers
# maybe make a train function that we can call with number of trials?
# and the function can print out values once it finishes
def train(self, trials1, trials2, trials3, gameBoard):
    for i in range(trials3):
        # play game until win/lose/draw
        if i in [trials1, trials2, trials3]:
            print()
        # print the current reward/utility values

    return
