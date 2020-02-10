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
<<<<<<< HEAD

    def InitialPositionForPieses(self,Pieses_White,Pieses_Black):
        self.Pieses_White = Pieses_White
        self.Pieses_Black = Pieses_Black
        for i in range(0,9):
            for j in range(0,9):
                if(i == 1 and j == 1):
                    self.Board[i][j] = self.Pieses_White
                if(i == 1 and j == 3):
                    self.Board[i][j] = self.Pieses_White
                if(i == 1 and j == 5):
                    self.Board[i][j] = self.Pieses_White
                if(i == 1 and j == 7):
                    self.Board[i][j] = self.Pieses_White

                if(i == 2 and j == 2):
                    self.Board[i][j] = self.Pieses_White
                if(i == 2 and j == 4):
                    self.Board[i][j] = self.Pieses_White
                if(i == 2 and j == 6):
                    self.Board[i][j] = self.Pieses_White
                if(i == 2 and j == 8):
                    self.Board[i][j] = self.Pieses_White

                if(i == 3 and j == 1):
                    self.Board[i][j] = self.Pieses_White
                if(i == 3 and j == 3):
                    self.Board[i][j] = self.Pieses_White
                if(i == 3 and j == 5):
                    self.Board[i][j] = self.Pieses_White
                if(i == 3 and j == 7):
                    self.Board[i][j] = self.Pieses_White

                if(i == 6 and j == 2):
                    self.Board[i][j] = self.Pieses_Black
                if(i == 6 and j == 4):
                    self.Board[i][j] = self.Pieses_Black
                if(i == 6 and j == 6):
                    self.Board[i][j] = self.Pieses_Black
                if(i == 6 and j == 8):
                    self.Board[i][j] = self.Pieses_Black

                if(i == 7 and j == 1):
                    self.Board[i][j] = self.Pieses_Black
                if(i == 7 and j == 3):
                    self.Board[i][j] = self.Pieses_Black
                if(i == 7 and j == 5):
                    self.Board[i][j] = self.Pieses_Black
                if(i == 7 and j == 7):
                    self.Board[i][j] = self.Pieses_Black

                if(i == 8 and j == 2):
                    self.Board[i][j] = self.Pieses_Black
                if(i == 8 and j == 4):
                    self.Board[i][j] = self.Pieses_Black
                if(i == 8 and j == 6):
                    self.Board[i][j] = self.Pieses_Black
                if(i == 8 and j == 8):
                    self.Board[i][j] = self.Pieses_Black

    def movement(self, Raw_Postion_Current,Column_Postion_current,Raw_Postion_Late,Column_Postion_Late,Player,turn):
        self.Raw_Postion_Current = Raw_Postion_Current
=======
    def movement(self, Row_Postion_Current,Column_Postion_current,Row_Postion_Late,Column_Postion_Late,Player,turn):
        self.Row_Postion_Current = Row_Postion_Current
>>>>>>> 0bdf50699833e7654c40f6c114c06ed9d60d3224
        self.Column_Postion_current = Column_Postion_current
        self.Row_Postion_Late = Row_Postion_Late
        self.Column_Postion_Late = Column_Postion_Late
        self.Player = Player
<<<<<<< HEAD
         
        if(turn):
            
            if(self.Raw_Postion_Late%2 != 0 and self.Column_Postion_Late%2 == 0 or self.Raw_Postion_Late%2 == 0 and self.Column_Postion_Late%2 != 0):
                self.Board[Raw_Postion_Current][Column_Postion_current] = self.Pieses_White
                self.Board[Raw_Postion_Late][Column_Postion_Late] = '⬜'
            else:  
                if(self.Board[Raw_Postion_Late][Column_Postion_Late] != ' '):
                    self.Board[Raw_Postion_Current][Column_Postion_current] = ' '
                    self.Board[Raw_Postion_Late][Column_Postion_Late] = self.Pieses_White
                else:
                    self.Board[Raw_Postion_Current][Column_Postion_current] = self.Pieses_White

        else:
            if(self.Raw_Postion_Late%2 != 0 and self.Column_Postion_Late%2 == 0 or self.Raw_Postion_Late%2 == 0 and self.Column_Postion_Late%2 != 0):
                self.Board[Raw_Postion_Current][Column_Postion_current] = self.Pieses_Black
                self.Board[Raw_Postion_Late][Column_Postion_Late] = '⬜'
            else:    
                if(self.Board[Raw_Postion_Late][Column_Postion_Late] != ' '):
                    self.Board[Raw_Postion_Current][Column_Postion_current] = ' '
                    self.Board[Raw_Postion_Late][Column_Postion_Late] = self.Pieses_Black
                else:
                    self.Board[Raw_Postion_Current][Column_Postion_current] = self.Pieses_Black
=======


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
>>>>>>> 0bdf50699833e7654c40f6c114c06ed9d60d3224
    
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
<<<<<<< HEAD

            Raw_current = input("Enter the row of the piece you want to move: ")
            if(Raw_current== 'A' or Raw_current== 'a'):
                Raw_Postion_Current = 1
            if(Raw_current== 'B' or Raw_current== 'b'):
                Raw_Postion_Current = 2
            if(Raw_current== 'C' or Raw_current== 'c'):
                Raw_Postion_Current = 3
            if(Raw_current== 'D' or Raw_current== 'd'):
                Raw_Postion_Current = 4
            if(Raw_current== 'E' or Raw_current== 'e'):
                Raw_Postion_Current = 5
            if(Raw_current== 'F' or Raw_current== 'f'):
                Raw_Postion_Current = 6
            if(Raw_current== 'G' or Raw_current== 'g'):
                Raw_Postion_Current = 7
            if(Raw_current== 'H' or Raw_current== 'h'):
                Raw_Postion_Current = 8

            Column_Postion_current = int(input("Enter the column of the piece you want to move: "))
            Raw_Late = input("Enter the row of the piece where it will move: ")
            if(Raw_Late== 'A' or Raw_Late== 'a'):
                Raw_Postion_Late = 1
            if(Raw_Late== 'B' or Raw_Late== 'b'):
                Raw_Postion_Late = 2
            if(Raw_Late== 'C' or Raw_Late== 'c'):
                Raw_Postion_Late = 3
            if(Raw_Late== 'D' or Raw_Late== 'd'):
                Raw_Postion_Late = 4
            if(Raw_Late== 'E' or Raw_Late== 'e'):
                Raw_Postion_Late = 5
            if(Raw_Late== 'F' or Raw_Late== 'f'):
                Raw_Postion_Late = 6
            if(Raw_Late== 'G' or Raw_Late== 'g'):
                Raw_Postion_Late = 7
            if(Raw_Late== 'H' or Raw_Late== 'h'):
                Raw_Postion_Late = 8
            Column_Postion_Late = int(input("Enter the colunm of the piece where it will move: "))
            
            if(self.Board[Raw_Postion_Current][Column_Postion_current] == self.Pieses_White and turn and i%2 == 0):
                self.movement(Raw_Postion_Current,Column_Postion_current,Raw_Postion_Late,Column_Postion_Late,Player,turn)
                self.pre()
=======
    
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
>>>>>>> 0bdf50699833e7654c40f6c114c06ed9d60d3224
                turn = False
                print("shift change, Black")
                i += 1

            else:
<<<<<<< HEAD
                print(self.Board[Raw_Postion_Current][Column_Postion_current] == self.Pieses_Black)
                if(self.Board[Raw_Postion_Current][Column_Postion_current] == self.Pieses_Black and turn == False and i%2 != 0):
                    self.movement(Raw_Postion_Current,Column_Postion_current,Raw_Postion_Late,Column_Postion_Late,Player,turn)
                    self.pre()
=======
                print(self.Board[Row_Postion_Current][Column_Postion_current] == self.Pieses_Black)
                if(self.Board[Row_Postion_Current][Column_Postion_current] == self.Pieses_Black and turn == False and i%2 != 0 and Value_Abs_Row_Black == -1 and Value_Abs_Col_Black == -1):
                    self.movement(Row_Postion_Current,Column_Postion_current,Row_Postion_Late,Column_Postion_Late,Player,turn)
                    self.presentation()
>>>>>>> 0bdf50699833e7654c40f6c114c06ed9d60d3224
                    turn = True
                    print("shift change, White")
                    i += 1
                else:
                    print("Invalid Movement, try again")

    def presentation(self):
        super().state()

LPiesesWB = PiesesWhiteBlack()
LPiesesWB.play()
