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
                    self.Board[i][j] = "X"
                if(i == 0 and j == 1):
                    self.Board[i][j] = "1"
                if(i == 0 and j == 2):
                    self.Board[i][j] = "2"
                if(i == 0 and j == 3):
                    self.Board[i][j] = "3"
                if(i == 0 and j == 4):
                    self.Board[i][j] = "4"
                if(i == 0 and j == 5):
                    self.Board[i][j] = "5"
                if(i == 0 and j == 6):
                    self.Board[i][j] = "6"
                if(i == 0 and j == 7):
                    self.Board[i][j] = "7"
                if(i == 0 and j == 8):
                    self.Board[i][j] = "8"

                if(i == 1 and j == 0):
                    self.Board[i][j] = "A"
                if(i == 2 and j == 0):
                    self.Board[i][j] = "B"
                if(i == 3 and j == 0):
                    self.Board[i][j] = "C"
                if(i == 4 and j == 0):
                    self.Board[i][j] = "D"
                if(i == 5 and j == 0):
                    self.Board[i][j] = "E"
                if(i == 6 and j == 0):
                    self.Board[i][j] = "F"
                if(i == 7 and j == 0):
                    self.Board[i][j] = "G"
                if(i == 8 and j == 0):
                    self.Board[i][j] = "H"

    def state(self):
        for x in self.Board:
            print(x)

class PiesesWhiteBlack(DamasChinas):

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

    def movement(self, Raw_Postion_current,Column_Postion_current,Raw_Postion_Late,Column_Postion_Late,Player,turn):
        self.Raw_Postion_current = Raw_Postion_current
        self.Column_Postion_current = Column_Postion_current
        self.Raw_Postion_Late = Raw_Postion_Late
        self.Column_Postion_Late = Column_Postion_Late
        self.Player = Player
         
        if(turn):
            
            if(self.Raw_Postion_Late%2 != 0 and self.Column_Postion_Late%2 == 0 or self.Raw_Postion_Late%2 == 0 and self.Column_Postion_Late%2 != 0):
                self.Board[Raw_Postion_current][Column_Postion_current] = self.Pieses_White
                self.Board[Raw_Postion_Late][Column_Postion_Late] = '⬜'
            else:  
                if(self.Board[Raw_Postion_Late][Column_Postion_Late] != ' '):
                    self.Board[Raw_Postion_current][Column_Postion_current] = ' '
                    self.Board[Raw_Postion_Late][Column_Postion_Late] = self.Pieses_White
                else:
                    self.Board[Raw_Postion_current][Column_Postion_current] = self.Pieses_White

        else:
            if(self.Raw_Postion_Late%2 != 0 and self.Column_Postion_Late%2 == 0 or self.Raw_Postion_Late%2 == 0 and self.Column_Postion_Late%2 != 0):
                self.Board[Raw_Postion_current][Column_Postion_current] = self.Pieses_Black
                self.Board[Raw_Postion_Late][Column_Postion_Late] = '⬜'
            else:    
                if(self.Board[Raw_Postion_Late][Column_Postion_Late] != ' '):
                    self.Board[Raw_Postion_current][Column_Postion_current] = ' '
                    self.Board[Raw_Postion_Late][Column_Postion_Late] = self.Pieses_Black
                else:
                    self.Board[Raw_Postion_current][Column_Postion_current] = self.Pieses_Black
    
    def play(self):
        self.InitialPositionForPieses('W','B')
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
            
        while(True):

            Raw_Postion_current = int(input("Enter the row of the piece you want to move: "))
            Column_Postion_current = int(input("Enter the column of the piece you want to move: "))
            Raw_Postion_Late = int(input("Enter the row of the piece where it will move: "))
            Column_Postion_Late = int(input("Enter the colunm of the piece where it will move: "))
            
            if(self.Board[Raw_Postion_current][Column_Postion_current] == self.Pieses_White and turn and i%2 == 0):
                self.movement(Raw_Postion_current,Column_Postion_current,Raw_Postion_Late,Column_Postion_Late,Player,turn)
                self.pre()
                turn = False
                print("shift change")
                i += 1
            else:
                print(self.Board[Raw_Postion_current][Column_Postion_current] == self.Pieses_Black)
                if(self.Board[Raw_Postion_current][Column_Postion_current] == self.Pieses_Black and turn == False and i%2 != 0):
                    self.movement(Raw_Postion_current,Column_Postion_current,Raw_Postion_Late,Column_Postion_Late,Player,turn)
                    self.pre()
                    turn = True
                    print("shift change")
                    i += 1
                else:
                    print("Invalid Movement, try again")


    def pre(self):
        super().state()

LPiesesWB = PiesesWhiteBlack([])
LPiesesWB.play()
