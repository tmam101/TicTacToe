from Board import Board
import sys

trials1 = int(sys.argv[1])
trials2 = int(sys.argv[2])
trials3 = int(sys.argv[3])

board = Board()
board.train(trials1, trials2, trials3)