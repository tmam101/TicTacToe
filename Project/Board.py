from random import randint


class Board:
    cells = [[[None, None, None, None], [None, None, None, None], [None, None, None, None], [None, None, None, None]],
             [[None, None, None, None], [None, None, None, None], [None, None, None, None], [None, None, None, None]],
             [[None, None, None, None], [None, None, None, None], [None, None, None, None], [None, None, None, None]],
             [[None, None, None, None], [None, None, None, None], [None, None, None, None], [None, None, None, None]]]

    cellsRw = [[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
               [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
               [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
               [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]]
    player = "X"

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

    # print reward values
    def rewToString(self, iteration):
        string = ""
        currRewards = [[[0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0]],
                       [[0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0]],
                       [[0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0]],
                       [[0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0]]]
        # divide by current iteration to get % of the time square was used in win
        for a in range(len(self.cells)):
            for b in range(len(self.cells[a])):
                for c in range(len(self.cells[a][b])):
                    currRewards[a][b][c] = round(self.cellsRw[a][b][c] / (iteration + 1.0), 3)
                    string += str(currRewards[a][b][c]) + " "

                string += "\n"
            string += "\n"
        return string

    def win(self):
        cells = self.cells

        # On the 4x4x4 board, there are 76 winning lines. On each of the four 4x4 boards, or horizontal planes,
        # there are four columns, four rows, and two diagonals, accounting for 40 lines. There are 16 vertical
        # lines, each ascending from a cell on the bottom board through the corresponding cells on the other
        # boards. There are eight vertically-oriented planes parallel to the sides of the boards, each of
        # these adding two more diagonals (the horizontal and vertical lines of these planes have already
        # been counted). Finally, there are two vertically-oriented planes that include the diagonal lines of
        # the 4x4 boards, and each of these contributes two more diagonal lines- each of these including two
        # corners and two internal cells.                        https://en.wikipedia.org/wiki/3D_tic-tac-toe

        # 4 horizontal planes, 10 wins each:
        for z in range(4):
            # 4 rows
            for x in range(4):
                if "X" == cells[x][0][z] == cells[x][1][z] == cells[x][2][z] == cells[x][3][z]: return 1
                if "O" == cells[x][0][z] == cells[x][1][z] == cells[x][2][z] == cells[x][3][z]: return -1

            # 4 columns
            for y in range(4):
                if "X" == cells[0][y][z] == cells[1][y][z] == cells[2][y][z] == cells[3][y][z]: return 1
                if "O" == cells[0][y][z] == cells[1][y][z] == cells[2][y][z] == cells[3][y][z]: return -1

            # 2 diagonals
            if "X" == cells[0][0][z] == cells[1][1][z] == cells[2][2][z] == cells[3][3][z]: return 1
            if "O" == cells[0][0][z] == cells[1][1][z] == cells[2][2][z] == cells[3][3][z]: return -1
            if "X" == cells[3][0][z] == cells[2][1][z] == cells[1][2][z] == cells[0][3][z]: return 1
            if "O" == cells[3][0][z] == cells[2][1][z] == cells[1][2][z] == cells[0][3][z]: return -1

        # 16 vertically oriented lines
        for x in range(4):
            for y in range(4):
                if "X" == cells[x][y][0] == cells[x][y][1] == cells[x][y][2] == cells[x][y][3]: return 1
                if "O" == cells[x][y][0] == cells[x][y][1] == cells[x][y][2] == cells[x][y][3]: return -1

        # 4 vertical planes parallel to x, 2 diagonals each
        for y in range(4):
            if "X" == cells[0][y][0] == cells[1][y][1] == cells[2][y][2] == cells[3][y][3]: return 1
            if "O" == cells[0][y][0] == cells[1][y][1] == cells[2][y][2] == cells[3][y][3]: return -1
            if "X" == cells[3][y][0] == cells[2][y][1] == cells[1][y][2] == cells[0][y][3]: return 1
            if "O" == cells[3][y][0] == cells[2][y][1] == cells[1][y][2] == cells[0][y][3]: return -1

        # 4 vertical planes parallel to y, 2 diagonals each
        for x in range(4):
            if "X" == cells[x][0][0] == cells[x][1][1] == cells[x][2][2] == cells[x][3][3]: return 1
            if "O" == cells[x][0][0] == cells[x][1][1] == cells[x][2][2] == cells[x][3][3]: return -1
            if "X" == cells[x][3][0] == cells[x][2][1] == cells[x][1][2] == cells[x][0][3]: return 1
            if "O" == cells[x][3][0] == cells[x][2][1] == cells[x][1][2] == cells[x][0][3]: return -1

        # 4 long diagonals
        if "X" == cells[0][0][0] == cells[1][1][1] == cells[2][2][2] == cells[3][3][3]: return 1
        if "O" == cells[0][0][0] == cells[1][1][1] == cells[2][2][2] == cells[3][3][3]: return -1

        if "X" == cells[0][3][0] == cells[1][2][1] == cells[2][1][2] == cells[3][0][3]: return 1
        if "O" == cells[0][3][0] == cells[1][2][1] == cells[2][1][2] == cells[3][0][3]: return -1

        if "X" == cells[3][0][0] == cells[2][1][1] == cells[1][2][2] == cells[0][3][3]: return 1
        if "O" == cells[3][0][0] == cells[2][1][1] == cells[1][2][2] == cells[0][3][3]: return -1

        if "X" == cells[3][3][0] == cells[2][2][1] == cells[1][1][2] == cells[0][0][3]: return 1
        if "O" == cells[3][3][0] == cells[2][2][1] == cells[1][1][2] == cells[0][0][3]: return -1

        return 0

        # return 0 if not enough info/game still in progress

    def playGame(self, isRandom, trial):
        self.clearBoard()
        self.chooseMove(isRandom, trial)
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

    def chooseMove(self, rand, iteration):
        if rand:
            # While all cells have not been filled
            while self.toString().__contains__("-"):
                # check if someone has won- if so, exit
                if self.win() == 1 or self.win() == -1:
                    return
                findingEmptyCell = True
                while findingEmptyCell:
                    r1 = randint(0, len(self.cells) - 1)
                    r2 = randint(0, len(self.cells[0]) - 1)
                    r3 = randint(0, len(self.cells[0][0]) - 1)
                    if self.cells[r1][r2][r3] is None:
                        findingEmptyCell = False
                        # Assign the cell's X or O value
                        self.cells[r1][r2][r3] = self.getPlayer()
        else:
            # select square with top reward value. if full, choose cell with next highest value

            # set up array to hold reward values without messing with running list
            currRewards = [[[0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0]],
                           [[0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0]],
                           [[0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0]],
                           [[0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0]]]
            # divide by current iteration to get % of the time square was used in win
            for a in range(len(self.cells)):
                for b in range(len(self.cells[a])):
                    for c in range(len(self.cells[a][b])):
                        currRewards[a][b][c] = round(self.cellsRw[a][b][c] / (iteration + 1.0), 3)

            # choose moves until the board is full or someone has won
            while self.toString().__contains__("-"):
                if self.win() == 1 or self.win() == -1:
                    return

                # look for an empty cell to put a mark in
                currMax = 0
                maxIndex = (0, 0, 0)
                findingEmptyCell = True

                while findingEmptyCell:
                    for a in range(len(self.cells)):
                        for b in range(len(self.cells[a])):
                            for c in range(len(self.cells[a][b])):
                                if currRewards[a][b][c] > currMax:
                                    currMax = currRewards[a][b][c]
                                    maxIndex = (a, b, c)

                    if self.cells[maxIndex[0]][maxIndex[1]][maxIndex[2]] is None:
                        self.cells[maxIndex[0]][maxIndex[1]][maxIndex[2]] = self.getPlayer()
                        findingEmptyCell = False
                    if self.cells[maxIndex[0]][maxIndex[1]][maxIndex[2]] is not None:
                        currRewards[maxIndex[0]][maxIndex[1]][maxIndex[2]] = -1.0

        return

    # reward with value of 1 if putting a move in that square leads to a win- keep running total, when we need
    # the percentage of the time, divide by the iteration we're on

    # When a player wins, call this reward function.
    # It increases the reward of every cell that the winning player used to win.
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

    # need to get input that tells how many trials to run-three numbers
    # maybe make a train function that we can call with number of trials?
    # and the function can print out values once it finishes

    def train(self, trials1, trials2, trials3):
        rand = True
        for i in range(trials3):
            # passing in i so we can calculate average reward inside board
            self.playGame(rand, i)
            if i == trials3/3:
                rand = False
            if i in [trials1 - 1, trials2 - 1, trials3 - 1]:
                # print the current reward/utility values
                print('Utility values at iteration ' + str(i + 1))
                print(self.rewToString(i))

        return
