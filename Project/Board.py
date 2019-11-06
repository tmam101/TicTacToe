class Board:
    cells = [[["X", None, None, None], ["X", "X", None, None], [None, None, "X", None], [None, None, None, "X"]],
        [[None, None, None, None], [None, "X", "X", "X"], [None, None, None, "O"], [None, None, None, None]],
        [[None, None, None, None], ["X", None, None, "O"], [None, None, None, None], [None, None, None, None]],
        [[None, None, None, "O"], [None, None, None, None], [None, None, None, None], [None, None, None, None]]]

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

# Model free active q learning?

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

# TODO make reward function
# reward with value of 1 if putting a move in that square leads to a win?
# average the value each iteration(trial)? is this the same as value iteration?

# TODO make choose move function
#