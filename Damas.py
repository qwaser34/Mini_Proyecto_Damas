class DamasChinas:
    def __init__(self):
        self.Pieses_White = "w"
        self.Pieses_Black = "b"
        self.Pieses_Queen_White = "W"
        self.Pieses_Queen_Black = "B"
        self.Board = []
        collumns = "x12345678"
        rows = "xABCDEFGH"
        for i in range(9):
            self.Board.append(['']*9)

        for i in range(0,9):
            for j in range(0,9):
                if((i+j)%2 == 0):
                    self.Board[i][j] = "⬛"
                    if (i > 0 and i < 4):
                        self.Board[i][j] = self.Pieses_White
                    if (i > 5):
                        self.Board[i][j] = self.Pieses_Black
                else:
                    self.Board[i][j] = "⬜"

                self.Board[0][i] = collumns[i]
                self.Board[j][0] = rows[j]

    def state(self):
        for x in self.Board:
            print(x)

class PiesesWhiteBlack(DamasChinas):
    def movement(self, Row_Postion_Current,Column_Postion_current,Row_Postion_Late,Column_Postion_Late,Player,turn):
        self.Row_Postion_Current = Row_Postion_Current
        self.Column_Postion_current = Column_Postion_current
        self.Row_Postion_Late = Row_Postion_Late
        self.Column_Postion_Late = Column_Postion_Late
        self.Player = Player


        #     if(Value_Abs_Col == 1 and Value_Abs_Row == 1):


        if(turn):#turn white
            if(self.Row_Postion_Late%2 != 0 and self.Column_Postion_Late%2 == 0 or self.Row_Postion_Late%2 == 0 and self.Column_Postion_Late%2 != 0):
                self.Board[Row_Postion_Current][Column_Postion_current] = self.Pieses_White
                self.Board[Row_Postion_Late][Column_Postion_Late] = '⬜'
            else:
                self.Board[Row_Postion_Current][Column_Postion_current] = '⬛'
                self.Board[Row_Postion_Late][Column_Postion_Late] = self.Pieses_White

                
                                #change to queen
            if(self.Pieses_White == self.Board[8][Column_Postion_Late]):
                self.Board[8][Column_Postion_Late] = self.Pieses_Queen_White

        else: #turn black
            if(self.Row_Postion_Late%2 != 0 and self.Column_Postion_Late%2 == 0 or self.Row_Postion_Late%2 == 0 and self.Column_Postion_Late%2 != 0):
                self.Board[Row_Postion_Current][Column_Postion_current] = self.Pieses_Black
                self.Board[Row_Postion_Late][Column_Postion_Late] = '⬜'
            else:    
                self.Board[Row_Postion_Current][Column_Postion_current] = '⬛'
                self.Board[Row_Postion_Late][Column_Postion_Late] = self.Pieses_Black
                                #change to queen
            if(self.Pieses_Black == self.Board[1][Column_Postion_Late]):
                self.Board[1][Column_Postion_Late] = self.Pieses_Queen_Black
    
    def play(self):
        
        self.state()
        turn = False
        while(True):
            Player = input("What player do you want to be? [White or Black]: ")
            if(Player == "White" or Player == "white"):
                print("You play with White")
                turn = True
                break
            elif(Player == "Black" or Player == "black"):
                print("You play with Black")
                turn = False
                break
            else:
                print("Error, Does not exist")

        i = 0
        if turn == False:
            i = 1
            
        letter_to_number = {
            "A": 1,"a": 1,"B": 2,"b": 2,"C": 3,"c": 3,"D": 4,"d": 4,"E": 5,"e": 5,"F": 6,"f": 6,"G": 7,"g": 7,"H": 8,"h": 8,}
        while(True):
    
            Row_current = input("Enter the row of the piece you want to move: ")
            Row_Postion_Current = letter_to_number[Row_current]
            Column_Postion_current = int(input("Enter the column of the piece you want to move: "))
            Row_Late = input("Enter the row of the piece where it will move: ")
            Row_Postion_Late = letter_to_number[Row_Late]
            Column_Postion_Late = int(input("Enter the colunm of the piece where it will move: "))

            Value_Abs_Row_White = abs(Row_Postion_Current - Row_Postion_Late)
            Value_Abs_Col_White = abs(Column_Postion_current - Column_Postion_Late)
            Value_Abs_Row_Black = Row_Postion_Current - Row_Postion_Late
            Value_Abs_Col_Black = Column_Postion_current - Column_Postion_Late

            if(self.Board[Row_Postion_Current][Column_Postion_current] == self.Pieses_White and turn and i%2 == 0 and Value_Abs_Row_White == 1 and Value_Abs_Col_White == 1):
                self.movement(Row_Postion_Current,Column_Postion_current,Row_Postion_Late,Column_Postion_Late,Player,turn)
                self.presentation()
                turn = False
                print("shift change, Black")
                i += 1

            else:
                print(self.Board[Row_Postion_Current][Column_Postion_current] == self.Pieses_Black)
                if(self.Board[Row_Postion_Current][Column_Postion_current] == self.Pieses_Black and turn == False and i%2 != 0 and Value_Abs_Row_Black == -1 and Value_Abs_Col_Black == -1):
                    self.movement(Row_Postion_Current,Column_Postion_current,Row_Postion_Late,Column_Postion_Late,Player,turn)
                    self.presentation()
                    turn = True
                    print("shift change, White")
                    i += 1
                else:
                    print("Invalid Movement, try again")

    def presentation(self):
        super().state()

LPiesesWB = PiesesWhiteBlack()
LPiesesWB.play()
