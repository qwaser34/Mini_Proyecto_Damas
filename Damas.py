class DamasChinas:
    def __init__(self,Board):
        self.Board = Board
        for i in range(9):
            self.Board.append(['']*9)

        for i in range(0,9):
            for j in range(0,9):

                if(i%2 == 0):
                    self.Board[i][j] = "⬜"
                    if(j%2 == 0):
                        self.Board[i][j] = "⬛"

                if(i%2 != 0):
                    self.Board[i][j] = "⬜"
                    if(j%2 != 0):
                        self.Board[i][j] = "⬛"

                if(i == 0 and j == 0):
                    self.Board[i][j] = "0"

                if(i == 0 and j == 1 or i == 1 and j == 0):
                    self.Board[i][j] = "1"

                if(i == 0 and j == 2 or i == 2 and j == 0):
                    self.Board[i][j] = "2"

                if(i == 0 and j == 3 or i == 3 and j == 0):
                    self.Board[i][j] = "3"

                if(i == 0 and j == 4 or i == 4 and j == 0):
                    self.Board[i][j] = "4"

                if(i == 0 and j == 5 or i == 5 and j == 0):
                    self.Board[i][j] = "5"

                if(i == 0 and j == 6 or i == 6 and j == 0):
                    self.Board[i][j] = "6"

                if(i == 0 and j == 7 or i == 7 and j == 0):
                    self.Board[i][j] = "7"

                if(i == 0 and j == 8 or i == 8 and j == 0):
                    self.Board[i][j] = "8"

    def state(self):
        for x in self.Board:
            print(x)



FirstBoard = DamasChinas([])
FirstBoard.state()