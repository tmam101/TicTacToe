from Board import Board
import sys
trials1 = sys.argv[1]
trials2 = sys.argv[2]
trials3 = sys.argv[3]

board = Board()
print(board.toString())
print board.win()


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
