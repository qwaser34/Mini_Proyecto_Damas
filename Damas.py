class Damas:
    def __init__(self):# lo que siemre aparecera
        # definicion de piezas
        self.pieses_white = "♟"
        self.pieses_black = "♙"
        self.pieses_queen_white = "♚"
        self.pieses_queen_black = "♔"
        self.board = []
        collumns = "x12345678"
        rows = "xABCDEFGH"
        # creacion de tablero
        for i in range(9):
            self.board.append(['']*9)
        # colocacion de fichas, cuadros negros y blancos
        for i in range(0,9):
            for j in range(0,9):
                if((i+j)%2 == 0):
                    self.board[i][j] = '◼'
                    if (i > 0 and i < 4):
                        
                        self.board[i][j] = self.pieses_white
                    if (i > 5):
                        self.board[i][j] = self.pieses_black
                else:
                    self.board[i][j] = '◻'

                self.board[0][i] = collumns[i]
                self.board[j][0] = rows[j]


    def state(self):#recorrer el tablero y mostrar todo
        for x in self.board:
            print(x)


# LPiesesWB = DamasChinas()
# LPiesesWB.state()

# ⬛
# ⬜
