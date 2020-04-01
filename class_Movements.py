import os
from Damas import DamasChinas
from class_kill_Pieces import kill_Pieces
from class_QUEEN_KILL import Queen_Killer
class PiesesWhiteBlack(DamasChinas):
    turn = False
    def movement_normal_pieses(self, Row_Postion_Initial,Column_Postion_Initial,Row_Postion_Final,Column_Postion_Final,turn):
        self.Row_Postion_Initial = Row_Postion_Initial
        self.Column_Postion_Initial = Column_Postion_Initial
        self.Row_Postion_Final = Row_Postion_Final
        self.Column_Postion_Final = Column_Postion_Final
        

        if(turn):#turn white
            if(self.Row_Postion_Final%2 != 0 and self.Column_Postion_Final%2 == 0 or self.Row_Postion_Final%2 == 0 and self.Column_Postion_Final%2 != 0):
                self.Board[Row_Postion_Initial][Column_Postion_Initial] = self.Pieses_White
                self.Board[Row_Postion_Final][Column_Postion_Final] = '◻'

            # elif(self.Row_Postion_Final%2 != 0 and self.Column_Postion_Final%2 == 0 or self.Row_Postion_Final%2 == 0 and self.Column_Postion_Final%2 != 0):
            #     self.Board[Row_Postion_Initial][Column_Postion_Initial] = self.Pieses_Queen_White
            #     self.Board[Row_Postion_Final][Column_Postion_Final] = '◻'

            else:
                self.Board[Row_Postion_Initial][Column_Postion_Initial] = '◼'
                self.Board[Row_Postion_Final][Column_Postion_Final] = self.Pieses_White

            #change to queen
            # if(self.Pieses_White == self.Board[8][Column_Postion_Final]):
            #     self.Pieses_White = self.Pieses_Queen_White                


        else: #turn black
            if(self.Row_Postion_Final%2 != 0 and self.Column_Postion_Final%2 == 0 or self.Row_Postion_Final%2 == 0 and self.Column_Postion_Final%2 != 0):
                self.Board[Row_Postion_Initial][Column_Postion_Initial] = self.Pieses_Black
                self.Board[Row_Postion_Final][Column_Postion_Final] = '◻'

            # elif(self.Row_Postion_Final%2 != 0 and self.Column_Postion_Final%2 == 0 or self.Row_Postion_Final%2 == 0 and self.Column_Postion_Final%2 != 0):
            #     self.Board[Row_Postion_Initial][Column_Postion_Initial] = self.Pieses_Queen_Black
            #     self.Board[Row_Postion_Final][Column_Postion_Final] = '◻'
            else:    
                self.Board[Row_Postion_Initial][Column_Postion_Initial] = '◼'
                self.Board[Row_Postion_Final][Column_Postion_Final] = self.Pieses_Black
                                #change to queen
            # if(self.Pieses_Black == self.Board[1][Column_Postion_Final]):
            #     self.Pieses_Black = self.Pieses_Queen_Black


    def change_queen(self):
        for i in range(0,9):
            for j in range(0,9):
                if (i == 8):
                    if(self.Board[i][j] == self.Pieses_White):
                        self.Board[i][j] = self.Pieses_Queen_White
               
                if(i == 1):
                    if(self.Board[i][j] == self.Pieses_Black):
                        self.Board[i][j] = self.Pieses_Queen_Black

        # if(self.Pieses_White == self.Board[8][Column_Postion_Final]):            
        #     self.Pieses_White = self.Pieses_Queen_White
    
    def movement_queen_pieses(self, Row_Postion_Initial,Column_Postion_Initial,Row_Postion_Final,Column_Postion_Final,turn):
        self.Row_Postion_Initial = Row_Postion_Initial
        self.Column_Postion_Initial = Column_Postion_Initial
        self.Row_Postion_Final = Row_Postion_Final
        self.Column_Postion_Final = Column_Postion_Final

        if(turn):#turn white
            # if(self.Row_Postion_Final%2 != 0 and self.Column_Postion_Final%2 == 0 or self.Row_Postion_Final%2 == 0 and self.Column_Postion_Final%2 != 0):
            if(self.Board[Row_Postion_Final][Column_Postion_Final] == '◼'):
                self.Board[Row_Postion_Initial][Column_Postion_Initial] = '◼'
                self.Board[Row_Postion_Final][Column_Postion_Final] = self.Pieses_Queen_White

            elif(self.Board[Row_Postion_Final][Column_Postion_Final] == self.Pieses_White):
                self.Board[Row_Postion_Initial][Column_Postion_Initial] = self.Pieses_Queen_White
                self.Board[Row_Postion_Final][Column_Postion_Final] = '◼'

            elif(self.Board[Row_Postion_Final][Column_Postion_Final] == '◻'):
                self.Board[Row_Postion_Initial][Column_Postion_Initial] = self.Pieses_Queen_White
                self.Board[Row_Postion_Final][Column_Postion_Final] = '◻'
                

        else: #turn Queen black
            # if(self.Row_Postion_Final%2 != 0 and self.Column_Postion_Final%2 == 0 or self.Row_Postion_Final%2 == 0 and self.Column_Postion_Final%2 != 0):
            if(self.Board[Row_Postion_Final][Column_Postion_Final] == '◻'):
                self.Board[Row_Postion_Initial][Column_Postion_Initial] = self.Pieses_Queen_Black
                self.Board[Row_Postion_Final][Column_Postion_Final] = '◻'

            elif(self.Board[Row_Postion_Final][Column_Postion_Final] == self.Pieses_Black):
                self.Board[Row_Postion_Initial][Column_Postion_Initial] = self.Pieses_Queen_Black
                self.Board[Row_Postion_Final][Column_Postion_Final] = '◼'

            else:    
                self.Board[Row_Postion_Initial][Column_Postion_Initial] = '◼'
                self.Board[Row_Postion_Final][Column_Postion_Final] = self.Pieses_Queen_Black


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
            if(Player.lower() == Players[0]):
                print("You play with White")
                PiesesWhiteBlack.turn = True
                return PiesesWhiteBlack.turn
                
            elif(Player.lower() == Players[1]):
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
            Row_Postion_Initial = letter_to_number[Row_Postion]
            Column_Postion = Row_current[1]
            Column_Postion_Initial = letter_to_number[Column_Postion]
            Row_Postion2 = Row_Late[0]
            Row_Postion_Final = letter_to_number[Row_Postion2]
            Column_Postion2 = Row_Late[1]
            Column_Postion_Final = letter_to_number[Column_Postion2]

            Value_Row_Pieses = (Row_Postion_Initial - Row_Postion_Final)
            Value_Col_Pieses = (Column_Postion_Initial - Column_Postion_Final)
       
            if(self.Board[Row_Postion_Initial][Column_Postion_Initial] == self.Pieses_White  and Value_Row_Pieses == -1):
                self.movement_normal_pieses(Row_Postion_Initial,Column_Postion_Initial,Row_Postion_Final,Column_Postion_Final,PiesesWhiteBlack.turn)
                self.Clear_changeturn()

            else:
                if(self.Board[Row_Postion_Initial][Column_Postion_Initial] == self.Pieses_White and Value_Row_Pieses == -2):
                    # comer
                    kill_Pieces.kill_pieses(self,Row_Postion_Initial,Column_Postion_Initial,Row_Postion_Final,Column_Postion_Final)
                    self.Clear_changeturn()


            if(self.Board[Row_Postion_Initial][Column_Postion_Initial] == self.Pieses_Black and PiesesWhiteBlack.turn == False and Value_Row_Pieses == 1):
                self.movement_normal_pieses(Row_Postion_Initial,Column_Postion_Initial,Row_Postion_Final,Column_Postion_Final,PiesesWhiteBlack.turn)
                self.Clear_changeturn()

            else:
                if(self.Board[Row_Postion_Initial][Column_Postion_Initial] == self.Pieses_Black and PiesesWhiteBlack.turn == False and Value_Row_Pieses == 2):
                    # comer
                    kill_Pieces.kill_pieses(self,Row_Postion_Initial,Column_Postion_Initial,Row_Postion_Final,Column_Postion_Final)
                    kill_Pieces.kill_function(self, Row_Postion_Initial,Column_Postion_Initial,Row_Postion_Final,Column_Postion_Final)
                    self.Clear_changeturn()
                        
                
            #Queen
            if(self.Board[Row_Postion_Initial][Column_Postion_Initial] == self.Pieses_Queen_White):
                self.movement_queen_pieses(Row_Postion_Initial,Column_Postion_Initial,Row_Postion_Final,Column_Postion_Final,PiesesWhiteBlack.turn)
                Value_row_int = int(Value_Row_Pieses/2)
                Value_col_int = int(Value_Col_Pieses/2)
                if(self.Board[Row_Postion_Final + Value_row_int][Column_Postion_Final + Value_col_int] == self.Pieses_Black or self.Board[Row_Postion_Final + Value_row_int][Column_Postion_Final + Value_col_int] == self.Pieses_Queen_Black):
                    Queen_Killer.Queen_Killer_W(self,Row_Postion_Initial,Column_Postion_Initial,Row_Postion_Final,Column_Postion_Final)
                    self.Clear_changeturn()

        else:
            print("Invalid Movement, try again")

    def presentation(self):
        super().state()

    def Clear_changeturn(self):
        if(PiesesWhiteBlack.turn == True):
            # os.system('clear')
            self.change_queen()
            self.presentation()
            PiesesWhiteBlack.turn = False
            print("shift change, black")
            self.see_winer()
        elif(PiesesWhiteBlack.turn == False):
            # os.system('clear')
            self.change_queen()
            self.presentation()
            PiesesWhiteBlack.turn = True
            print("shift change, white")
            self.see_winer()

LPiesesWB = PiesesWhiteBlack()
LPiesesWB.players()
LPiesesWB.movement_pieses()