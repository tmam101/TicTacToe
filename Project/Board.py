from random import randint
class Board:
    # TODO Refactor this to be a flat one dimensional array?
    # cells = [[["X", None, None, None], ["X", "X", None, None], [None, None, "X", None], [None, None, None, "X"]],
    #     [[None, None, None, None], [None, "X", "X", "X"], [None, None, None, "O"], [None, None, None, None]],
    #     [[None, None, None, None], ["X", None, None, "O"], [None, None, None, None], [None, None, None, None]],
    #     [[None, None, None, "O"], [None, None, None, None], [None, None, None, None], [None, None, None, None]]]

    cells = [[[None, None, None, None], [None, None, None, None], [None, None, None, None], [None, None, None, None]],
             [[None, None, None, None], [None, None, None, None], [None, None, None, None], [None, None, None, None]],
             [[None, None, None, None], [None, None, None, None], [None, None, None, None], [None, None, None, None]],
             [[None, None, None, None], [None, None, None, None], [None, None, None, None], [None, None, None, None]]]

    cellsRw = [[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
             [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
             [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
             [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]]
    player = "X"


# TODO ToString
    def toString(self):
        str = ""
        for x in range(4):
            for y in range(4):
                for z in range(4):
                    if self.cells[x][y][z] is None:
                        str += "- "
                    else:
                        str += self.cells[x][y][z] + " "

                str += "\n"
            str += "\n"
        return str


# TODO make win/lose/draw/incomplete function
    def win(self):
        cells = self.cells
        for a in range(4):
            for b in range(4):
                # Check horizontals and verticals
                if "X" == cells[a][b][0] == cells[a][b][1] == cells[a][b][2] == cells[a][b][3]: return 1
                if "O" == cells[a][b][0] == cells[a][b][1] == cells[a][b][2] == cells[a][b][3]: return -1
                if "X" == cells[a][0][b] == cells[a][1][b] == cells[a][2][b] == cells[a][3][b]: return 1
                if "O" == cells[a][0][b] == cells[a][1][b] == cells[a][2][b] == cells[a][3][b]: return -1
                if "X" == cells[0][a][b] == cells[1][a][b] == cells[2][a][b] == cells[3][a][b]: return 1
                if "O" == cells[0][a][b] == cells[1][a][b] == cells[2][a][b] == cells[3][a][b]: return -1


        # for a in range(4):
        #         # Check diagonals
        #         if "X" == cells[0][a][a] == cells[1][a][a] == cells[0][a][2] == cells[a][b][3]: return 1
        #         if "O" == cells[a][b][0] == cells[a][b][1] == cells[a][b][2] == cells[a][b][3]: return -1
        #         if "X" == cells[a][0][b] == cells[a][1][b] == cells[a][2][b] == cells[a][3][b]: return 1
        #         if "O" == cells[a][0][b] == cells[a][1][b] == cells[a][2][b] == cells[a][3][b]: return -1
        #         if "X" == cells[0][a][b] == cells[1][a][b] == cells[2][a][b] == cells[3][a][b]: return 1
        #         if "O" == cells[0][a][b] == cells[1][a][b] == cells[2][a][b] == cells[3][a][b]: return -1

        # Different planes
        if "X" == cells[0][0][0] == cells[1][1][1] == cells[2][2][2] == cells[3][3][3]: return 1
        if "X" == cells[0][3][0] == cells[1][2][1] == cells[2][1][2] == cells[3][0][3]: return 1
        if "X" == cells[0][0][3] == cells[1][1][2] == cells[2][2][1] == cells[3][3][0]: return 1
        if "X" == cells[0][3][3] == cells[1][2][2] == cells[2][1][1] == cells[3][0][0]: return 1
        if "O" == cells[0][0][0] == cells[1][1][1] == cells[2][2][2] == cells[3][3][3]: return -1
        if "O" == cells[0][3][0] == cells[1][2][1] == cells[2][1][2] == cells[3][0][3]: return -1
        if "O" == cells[0][0][3] == cells[1][1][2] == cells[2][2][1] == cells[3][3][0]: return -1
        if "O" == cells[0][3][3] == cells[1][2][2] == cells[2][1][1] == cells[3][0][0]: return -1



        # return 0 if not enough info/game still in progress
        # return -1 if draw?

    def playGame(self, isRandom):
        self.clearBoard()
        self.chooseMove(isRandom)
        self.reward()

    def clearBoard(self):
        self.cells = [
            [[None, None, None, None], [None, None, None, None], [None, None, None, None], [None, None, None, None]],
            [[None, None, None, None], [None, None, None, None], [None, None, None, None], [None, None, None, None]],
            [[None, None, None, None], [None, None, None, None], [None, None, None, None], [None, None, None, None]],
            [[None, None, None, None], [None, None, None, None], [None, None, None, None], [None, None, None, None]]]

    # Alternates between X and O
    def getPlayer(self):
        if self.player == "X":
            self.player = "O"
            return "X"
        else:
            self.player = "X"
            return "O"

    def chooseMove(self, rand):
        if rand:
            # While all cells have not been filled
            while self.toString().__contains__("-"):
                cellFull = True
                while cellFull:
                    r1 = randint(0,len(self.cells)-1)
                    r2 = randint(0,len(self.cells[0])-1)
                    r3 = randint(0,len(self.cells[0][0])-1)
                    if self.cells[r1][r2][r3] is None:
                        cellFull = False
                        # Assign the cell's X or O value
                        self.cells[r1][r2][r3] = self.getPlayer()
        else:
            # TODO
            x =2
        return

# reward with value of 1 if putting a move in that square leads to a win- keep running total, when we need
# the percentage of the time, divide by the iteration we're on
# should we reward any square that leads to a win for either x or o? the strategy will be the same
# average the value each iteration(trial)? is this the same as value iteration?

    # When a player wins, call this reward function.  It increases the reward of every cell that the winning player used to win.
    def reward(self):
        winner = self.win()
        for a in range(len(self.cells)):
            for b in range(len(self.cells[a])):
                for c in range(len(self.cells[a][b])):
                    if winner == 1:  # X
                        if self.cells[a][b][c] == "X":
                            self.cellsRw[a][b][c] += 1
                    else:
                        if self.cells[a][b][c] == "O":
                            self.cellsRw[a][b][c] += 1
