import os
from Damas import DamasChinas
from class_kill_Pieces import kill_Pieces
from class_QUEEN_KILL import Queen_Killer
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
            # if(self.Pieses_White == self.Board[8][Column_Postion_Late]):
            #     self.Pieses_White = self.Pieses_Queen_White                


        else: #turn black
            if(self.Row_Postion_Late%2 != 0 and self.Column_Postion_Late%2 == 0 or self.Row_Postion_Late%2 == 0 and self.Column_Postion_Late%2 != 0):
                self.Board[Row_Postion_Current][Column_Postion_current] = self.Pieses_Black
                self.Board[Row_Postion_Late][Column_Postion_Late] = '⬜'
            else:    
                self.Board[Row_Postion_Current][Column_Postion_current] = '⬛'
                self.Board[Row_Postion_Late][Column_Postion_Late] = self.Pieses_Black
                                #change to queen
            # if(self.Pieses_Black == self.Board[1][Column_Postion_Late]):
            #     self.Pieses_Black = self.Pieses_Queen_Black


    def change_queen(self, Row_Postion_Current,Column_Postion_current,Row_Postion_Late,Column_Postion_Late,turn):
        self.Row_Postion_Current = Row_Postion_Current
        self.Column_Postion_current = Column_Postion_current
        self.Row_Postion_Late = Row_Postion_Late
        self.Column_Postion_Late = Column_Postion_Late

        for i in range(0,9):
            for j in range(0,9):
                if (i == 8):
                    if(self.Board[i][j] == self.Pieses_White):
                        self.Board[i][j] = self.Pieses_Queen_White
               

        # if(self.Pieses_White == self.Board[8][Column_Postion_Late]):            
        #     self.Pieses_White = self.Pieses_Queen_White

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

            Value_Row_White = (Row_Postion_Current - Row_Postion_Late)
            # Value_Col_White = (Column_Postion_current - Column_Postion_Late)
            Value_Row_Black = (Row_Postion_Current - Row_Postion_Late)
            # Value_Col_Black = (Column_Postion_current - Column_Postion_Late)
            
            if(self.Board[Row_Postion_Current][Column_Postion_current] == self.Pieses_White  and Value_Row_White == -1):
                self.movement_normal_pieses(Row_Postion_Current,Column_Postion_current,Row_Postion_Late,Column_Postion_Late,PiesesWhiteBlack.turn)
                os.system("cls")
                self.presentation()
                PiesesWhiteBlack.turn = False
                print("shift change, Black")

            else:
                if(self.Board[Row_Postion_Current][Column_Postion_current] == self.Pieses_White and Value_Row_White == -2):

                    # izquierda arriba a derecha abajo
                    if(self.Board[Row_Postion_Late - 1][Column_Postion_Late - 1] == self.Pieses_Black):
                        kill_Pieces.kill_pieses_W1(self,Row_Postion_Current,Column_Postion_current,Row_Postion_Late,Column_Postion_Late)
                        os.system("cls")
                        self.presentation()
                        PiesesWhiteBlack.turn = False
                        print("shift change, Black")

                    # derecha arriba a izquierda abajo 
                    elif(self.Board[Row_Postion_Late - 1][Column_Postion_Late + 1] == self.Pieses_Black):
                        kill_Pieces.kill_pieses_W2(self,Row_Postion_Current,Column_Postion_current,Row_Postion_Late,Column_Postion_Late)
                        os.system("cls")
                        self.presentation()
                        PiesesWhiteBlack.turn = False
                        print("shift change, Black")

                        

            
            if(self.Board[Row_Postion_Current][Column_Postion_current] == self.Pieses_Black and PiesesWhiteBlack.turn == False and Value_Row_Black == 1):

                self.movement_normal_pieses(Row_Postion_Current,Column_Postion_current,Row_Postion_Late,Column_Postion_Late,PiesesWhiteBlack.turn)
                os.system("cls")
                self.presentation()
                PiesesWhiteBlack.turn = True
                print("shift change, White")

            else:
                if(self.Board[Row_Postion_Current][Column_Postion_current] == self.Pieses_Black and PiesesWhiteBlack.turn == False and Value_Row_Black == 2):
                        # de derecha abajo a izquierda arriba
                    if(self.Board[Row_Postion_Late + 1][Column_Postion_Late + 1] == self.Pieses_White):
                        kill_Pieces.kill_pieses_B1(self,Row_Postion_Current,Column_Postion_current,Row_Postion_Late,Column_Postion_Late)
                        os.system("cls")
                        self.presentation()
                        PiesesWhiteBlack.turn = True
                        print("shift change, White")

                        # de izquierda abajo a derecha arriba
                    if(self.Board[Row_Postion_Late + 1][Column_Postion_Late - 1] == self.Pieses_White):
                        kill_Pieces.kill_pieses_B2(self,Row_Postion_Current,Column_Postion_current,Row_Postion_Late,Column_Postion_Late)
                        os.system("cls")
                        self.presentation()
                        PiesesWhiteBlack.turn = True
                        print("shift change, White")

            #Queen
            if(self.Board[Row_Postion_Current][Column_Postion_current] == self.Pieses_Queen_White):

                if(self.Board[Row_Postion_Late - 1][Column_Postion_Late - 1] == self.Pieses_Black or self.Board[Row_Postion_Late - 1][Column_Postion_Late - 1] == self.Pieses_Queen_Black):
                    Queen_Killer.Queen_Killer_WD1(self, Row_Postion_Current,Column_Postion_current,Row_Postion_Late,Column_Postion_Late)
                    os.system("cls")
                    self.presentation()
                    PiesesWhiteBlack.turn = False
                    print("shift change, Black")

                if(self.Board[Row_Postion_Late - 1][Column_Postion_Late + 1] == self.Pieses_Black or self.Board[Row_Postion_Late - 1][Column_Postion_Late + 1] == self.Pieses_Queen_Black):
                    Queen_Killer.Queen_Killer_WD2(self, Row_Postion_Current,Column_Postion_current,Row_Postion_Late,Column_Postion_Late)
                    os.system("cls")
                    self.presentation()
                    PiesesWhiteBlack.turn = False
                    print("shift change, Black")

                if(self.Board[Row_Postion_Late + 1][Column_Postion_Late + 1] == self.Pieses_Black or self.Board[Row_Postion_Late + 1][Column_Postion_Late + 1] == self.Pieses_Queen_Black):
                    Queen_Killer.Queen_Killer_WD3(self, Row_Postion_Current,Column_Postion_current,Row_Postion_Late,Column_Postion_Late)
                    os.system("cls")
                    self.presentation()
                    PiesesWhiteBlack.turn = False
                    print("shift change, Black")

                if(self.Board[Row_Postion_Late + 1][Column_Postion_Late - 1] == self.Pieses_Black or self.Board[Row_Postion_Late + 1][Column_Postion_Late - 1] == self.Pieses_Queen_Black):
                    Queen_Killer.Queen_Killer_WD4(self, Row_Postion_Current,Column_Postion_current,Row_Postion_Late,Column_Postion_Late)
                    os.system("cls")
                    self.presentation()
                    PiesesWhiteBlack.turn = False
                    print("shift change, Black")

            if(self.Board[Row_Postion_Current][Column_Postion_current] == self.Pieses_Queen_Black):

                if(self.Board[Row_Postion_Late - 1][Column_Postion_Late - 1] == self.Pieses_White or self.Board[Row_Postion_Late - 1][Column_Postion_Late - 1] == self.Pieses_Queen_White):
                    Queen_Killer.Queen_Killer_BD1(self, Row_Postion_Current,Column_Postion_current,Row_Postion_Late,Column_Postion_Late)
                    os.system("cls")
                    self.presentation()
                    PiesesWhiteBlack.turn = True
                    print("shift change, White")

                if(self.Board[Row_Postion_Late - 1][Column_Postion_Late + 1] == self.Pieses_White or self.Board[Row_Postion_Late - 1][Column_Postion_Late + 1] == self.Pieses_Queen_White):
                    Queen_Killer.Queen_Killer_BD2(self, Row_Postion_Current,Column_Postion_current,Row_Postion_Late,Column_Postion_Late)
                    os.system("cls")
                    self.presentation()
                    PiesesWhiteBlack.turn = True
                    print("shift change, White")


                if(self.Board[Row_Postion_Late + 1][Column_Postion_Late + 1] == self.Pieses_White or self.Board[Row_Postion_Late + 1][Column_Postion_Late + 1] == self.Pieses_Queen_White):
                    Queen_Killer.Queen_Killer_BD3(self, Row_Postion_Current,Column_Postion_current,Row_Postion_Late,Column_Postion_Late)
                    os.system("cls")
                    self.presentation()
                    PiesesWhiteBlack.turn = True
                    print("shift change, White")

                if(self.Board[Row_Postion_Late + 1][Column_Postion_Late - 1] == self.Pieses_White or self.Board[Row_Postion_Late + 1][Column_Postion_Late - 1] == self.Pieses_Queen_White):
                    Queen_Killer.Queen_Killer_BD4(self, Row_Postion_Current,Column_Postion_current,Row_Postion_Late,Column_Postion_Late)
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