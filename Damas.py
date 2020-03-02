import os
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
    turn = False
    def movement_normal_pieses(self, Row_Postion_Current,Column_Postion_current,Row_Postion_Late,Column_Postion_Late,turn):
        self.Row_Postion_Current = Row_Postion_Current
        self.Column_Postion_current = Column_Postion_current
        self.Row_Postion_Late = Row_Postion_Late
        self.Column_Postion_Late = Column_Postion_Late
        

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
    
    def movement_queen_pieses(self, Row_Postion_Current,Column_Postion_current,Row_Postion_Late,Column_Postion_Late,turn):
        self.Row_Postion_Current = Row_Postion_Current
        self.Column_Postion_current = Column_Postion_current
        self.Row_Postion_Late = Row_Postion_Late
        self.Column_Postion_Late = Column_Postion_Late

        if(turn):#turn Queen white
            if(self.Row_Postion_Late%2 != 0 and self.Column_Postion_Late%2 == 0 or self.Row_Postion_Late%2 == 0 and self.Column_Postion_Late%2 != 0):
                self.Board[Row_Postion_Current][Column_Postion_current] = self.Pieses_Queen_White
                self.Board[Row_Postion_Late][Column_Postion_Late] = '⬜'
            else:
                self.Board[Row_Postion_Current][Column_Postion_current] = '⬛'
                self.Board[Row_Postion_Late][Column_Postion_Late] = self.Pieses_Queen_White

        else: #turn Queen black
            if(self.Row_Postion_Late%2 != 0 and self.Column_Postion_Late%2 == 0 or self.Row_Postion_Late%2 == 0 and self.Column_Postion_Late%2 != 0):
                self.Board[Row_Postion_Current][Column_Postion_current] = self.Pieses_Queen_Black
                self.Board[Row_Postion_Late][Column_Postion_Late] = '⬜'
            else:    
                self.Board[Row_Postion_Current][Column_Postion_current] = '⬛'
                self.Board[Row_Postion_Late][Column_Postion_Late] = self.Pieses_Queen_Black


    def detect(self):# encontrar piesa
        pieseswhite = [self.Pieses_White,self.Pieses_Queen_White]
        piesesblack = [self.Pieses_Black, self.Pieses_Queen_Black]
        for i in range (0,9):
            for j in range(0,9):
                if(self.Board[i][j] in pieseswhite):
                    return pieseswhite
                else:
                    return piesesblack

    def see_winer(self):
        for i in range (0,9):
            for j in range(0,9):
                if(self.Board[i][j] not in self.detect()):
                    self.movement_pieses()
        else:
            print("End")
            

    def players(self):
        self.state()
        while(True):
            Players = ["white", "black"]
            Player = input("What player do you want to be? [white or black]: ")
            if(Player == Players[0]):
                print("You play with White")
                PiesesWhiteBlack.turn = True
                return PiesesWhiteBlack.turn
                
            elif(Player == Players[1]):
                print("You play with Black")
                PiesesWhiteBlack.turn = False
                return PiesesWhiteBlack.turn
                
            elif(Player not in Players):
                print("Error, Does not exist")



    def movement_pieses(self):
        letter_to_number = {
            "A": 1,"a": 1,"B": 2,"b": 2,"C": 3,"c": 3,"D": 4,"d": 4,"E": 5,"e": 5,"F": 6,"f": 6,"G": 7,"g": 7,"H": 8,"h": 8,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8}
        # i= self.players() if 0 else 1

        while(True):
            
            Row_current = input("Enter the piece you want to move: ")
            Row_Late = input("Enter where it will move: ")
            Row_Postion = Row_current[0]
            Row_Postion_Current = letter_to_number[Row_Postion]
            Column_Postion = Row_current[1]
            Column_Postion_current = letter_to_number[Column_Postion]
            Row_Postion2 = Row_Late[0]
            Row_Postion_Late = letter_to_number[Row_Postion2]
            Column_Postion2 = Row_Late[1]
            Column_Postion_Late = letter_to_number[Column_Postion2]

            if(self.Board[Row_Postion_Current][Column_Postion_current] == self.Pieses_White):

                    # de izquierda arriba a derecha abajo 
                if(self.Board[Row_Postion_Late - 1][Column_Postion_Late - 1] == self.Pieses_Black):
                    self.Board[Row_Postion_Late - 1][Column_Postion_Late - 1] = '⬛'
                    self.Board[Row_Postion_Late][Column_Postion_Late] = self.Pieses_White
                    self.Board[Row_Postion_Current][Column_Postion_current] = '⬛'
                
                    # de derecha arriba a izquierda abajo
                if(self.Board[Row_Postion_Late - 1][Column_Postion_Late + 1] == self.Pieses_Black):
                    self.Board[Row_Postion_Late - 1][Column_Postion_Late + 1] = '⬛'
                    self.Board[Row_Postion_Late][Column_Postion_Late] = self.Pieses_White
                    self.Board[Row_Postion_Current][Column_Postion_current] = '⬛'

                    os.system("cls")
                    self.presentation()
                    PiesesWhiteBlack.turn = False
                    print("shift change, Black")

                else:
                    self.movement_normal_pieses(Row_Postion_Current,Column_Postion_current,Row_Postion_Late,Column_Postion_Late,PiesesWhiteBlack.turn)
                    os.system("cls")
                    self.presentation()
                    PiesesWhiteBlack.turn = False
                    print("shift change, Black")

            else:
                if(self.Board[Row_Postion_Current][Column_Postion_current] == self.Pieses_Black and PiesesWhiteBlack.turn == False):

                        # de derecha abajo a izquierda arriba
                    if(self.Board[Row_Postion_Late + 1][Column_Postion_Late + 1] == self.Pieses_White):
                        self.Board[Row_Postion_Late + 1][Column_Postion_Late + 1] = '⬛'
                        self.Board[Row_Postion_Late][Column_Postion_Late] = self.Pieses_Black
                        self.Board[Row_Postion_Current][Column_Postion_current] = '⬛'
                    
                        # de izquierda abajo a derecha arriba
                    if(self.Board[Row_Postion_Late + 1][Column_Postion_Late - 1] == self.Pieses_White):
                        self.Board[Row_Postion_Late + 1][Column_Postion_Late - 1] = '⬛'
                        self.Board[Row_Postion_Late][Column_Postion_Late] = self.Pieses_Black
                        self.Board[Row_Postion_Current][Column_Postion_current] = '⬛'

                        os.system("cls")
                        self.presentation()
                        PiesesWhiteBlack.turn = True
                        print("shift change, White")

                    else:
                        self.movement_normal_pieses(Row_Postion_Current,Column_Postion_current,Row_Postion_Late,Column_Postion_Late,PiesesWhiteBlack.turn)
                        os.system("cls")
                        self.presentation()
                        PiesesWhiteBlack.turn = True
                        print("shift change, White")
                        
                else:
                    print("Invalid Movement, try again")
            

    def presentation(self):
        super().state()

LPiesesWB = PiesesWhiteBlack()
LPiesesWB.players()
LPiesesWB.movement_pieses()
