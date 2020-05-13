import os
from Damas import DamasChinas
from class_kill_Pieces import kill_Pieces
from class_QUEEN_KILL import Queen_Killer

class PiesesWhiteBlack(DamasChinas): #clase
    turn = False
    #  movimiento de piezas normales
    def movement_normal_pieses(self, Row_Postion_Initial,Column_Postion_Initial,Row_Postion_Final,Column_Postion_Final,turn):
        self.Row_Postion_Initial = Row_Postion_Initial
        self.Column_Postion_Initial = Column_Postion_Initial
        self.Row_Postion_Final = Row_Postion_Final
        self.Column_Postion_Final = Column_Postion_Final

        if(turn):#turn white
            # chequea si no donde se movera es una diagonal
            if(self.Row_Postion_Final%2 != 0 and self.Column_Postion_Final%2 == 0 or self.Row_Postion_Final%2 == 0 and self.Column_Postion_Final%2 != 0):
                self.Board[Row_Postion_Initial][Column_Postion_Initial] = self.Pieses_White
                self.Board[Row_Postion_Final][Column_Postion_Final] = self.Board[Row_Postion_Final][Column_Postion_Final]

            # si lo es pasa esto
            else:
                self.Board[Row_Postion_Initial][Column_Postion_Initial] = '◼'
                self.Board[Row_Postion_Final][Column_Postion_Final] = self.Pieses_White

        else: #turn black
            if(self.Row_Postion_Final%2 != 0 and self.Column_Postion_Final%2 == 0 or self.Row_Postion_Final%2 == 0 and self.Column_Postion_Final%2 != 0 or self.Board[Row_Postion_Final][Column_Postion_Final] == self.Pieses_White or self.Board[Row_Postion_Final][Column_Postion_Final] == self.Pieses_Queen_White):
                self.Board[Row_Postion_Initial][Column_Postion_Initial] = self.Pieses_Black
                self.Board[Row_Postion_Final][Column_Postion_Final] = self.Board[Row_Postion_Final][Column_Postion_Final]

            # lo mismo de las blancas
            else:
                self.Board[Row_Postion_Initial][Column_Postion_Initial] = '◼'
                self.Board[Row_Postion_Final][Column_Postion_Final] = self.Pieses_Black

        # cambia las piesas a reinas
    def change_queen(self):
        for i in range(0,9):
            for j in range(0,9):
                if (i == 8):
                    if(self.Board[i][j] == self.Pieses_White):
                        self.Board[i][j] = self.Pieses_Queen_White

                if(i == 1):
                    if(self.Board[i][j] == self.Pieses_Black):
                        self.Board[i][j] = self.Pieses_Queen_Black

    # queens movement
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

    #comienza el juego con las blancas
    def players(self):
        self.state()
        while(True):

            print("White Beginds")
            PiesesWhiteBlack.turn =False
            return PiesesWhiteBlack.turn

    # pregunta para donde quieres mover una pieza
    def movement_pieses(self):
        while(True):

            if(self.winner()==False):
                break
            elif(self.winner()==True):
                Row_Initial = input("Enter the piece you want to move: ")
                self.movement_pieses2(Row_Initial)

    def movement_pieses2(self, Row_Initial):

        if(self.winner()==False):
            print("Fin del juego")

        else:
            letter_to_number = {
                "A": 1,"a": 1,"B": 2,"b": 2,"C": 3,"c": 3,"D": 4,"d": 4,"E": 5,"e": 5,"F": 6,"f": 6,"G": 7,"g": 7,"H": 8,"h": 8,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8}

            #cual pueza quieres mover
            Row_Final = input("Enter where it will move: ")

            Row_Postion = Row_Initial[0]
            Row_Postion_Initial = letter_to_number[Row_Postion]
            Column_Postion = Row_Initial[1]
            Column_Postion_Initial = letter_to_number[Column_Postion]
            Row_Postion2 = Row_Final[0]
            Row_Postion_Final = letter_to_number[Row_Postion2]
            Column_Postion2 = Row_Final[1]
            Column_Postion_Final = letter_to_number[Column_Postion2]

            #calcula el valor para ver donde te mueves
            Value_Row_Pieses = (Row_Postion_Initial - Row_Postion_Final)
            Value_Col_Pieses = (Column_Postion_Initial - Column_Postion_Final)

            Value_row_int = int(Value_Row_Pieses/2)
            Value_col_int = int(Value_Col_Pieses/2)

            #White----------------
            if(self.Board[Row_Postion_Initial][Column_Postion_Initial] == self.Pieses_White  and Value_Row_Pieses == -1):# moverse de uno en uno
                self.movement_normal_pieses(Row_Postion_Initial,Column_Postion_Initial,Row_Postion_Final,Column_Postion_Final,PiesesWhiteBlack.turn)
                self.clear_changeturn()

            elif(self.Board[Row_Postion_Initial][Column_Postion_Initial] == self.Pieses_White and Value_Row_Pieses == -2): #detecta si puede comer
                
                # comer
                kill_Pieces.kill_pieses(self,Row_Postion_Initial,Column_Postion_Initial,Row_Postion_Final,Column_Postion_Final)# funcion que permite que se coma la contraria
                self.presentation()
                #limitar los bordes para que no se salga del rango
                if(Row_Postion_Final+2 <= 8 and Column_Postion_Final+2 <=8 and Row_Postion_Final-2 >= 0 and Column_Postion_Final-2 >= 0 ):
                    #para comer las normales
                    if(self.Board[Row_Postion_Final + 1][Column_Postion_Final + 1] == self.Pieses_Black and
                    self.Board[Row_Postion_Final + 2][Column_Postion_Final + 2] == '◼' or
                    self.Board[Row_Postion_Final + 1][Column_Postion_Final - 1] == self.Pieses_Black and
                    self.Board[Row_Postion_Final + 2][Column_Postion_Final - 2] == '◼' or
                    #para comer tambien lar reinas comtrarias
                    self.Board[Row_Postion_Final - 1][Column_Postion_Final - 1] == self.Pieses_Queen_Black and
                    self.Board[Row_Postion_Final - 2][Column_Postion_Final - 2] == '◼' or
                    self.Board[Row_Postion_Final - 1][Column_Postion_Final + 1] == self.Pieses_Queen_Black and
                    self.Board[Row_Postion_Final - 2][Column_Postion_Final + 2] == '◼'):

                        self.presentation()
                        #cuando se encuentra una contraria y puede seguir comiendo (Turn = True son para Blancas)
                        PiesesWhiteBlack.turn = True
                        self.movement_pieses2(Row_Final)
                
                elif(self.winner()==False):
                    print("Fin del juego")
                    
                #para cambiar de turno
                else:
                    PiesesWhiteBlack.turn = False

            #black------------------
            elif(self.Board[Row_Postion_Initial][Column_Postion_Initial] == self.Pieses_Black and PiesesWhiteBlack.turn == False and Value_Row_Pieses == 1):
                self.movement_normal_pieses(Row_Postion_Initial,Column_Postion_Initial,Row_Postion_Final,Column_Postion_Final,PiesesWhiteBlack.turn)

                self.clear_changeturn()

            elif(self.Board[Row_Postion_Initial][Column_Postion_Initial] == self.Pieses_Black and PiesesWhiteBlack.turn == False and Value_Row_Pieses == 2):

                # comer
                kill_Pieces.kill_pieses(self,Row_Postion_Initial,Column_Postion_Initial,Row_Postion_Final,Column_Postion_Final)
                self.presentation()
                #limitar los bordes para que no se salga del rango
                if(Row_Postion_Final+2 <= 8 and Column_Postion_Final+2 <=8 and Row_Postion_Final-2 >= 0 and Column_Postion_Final-2 >= 0 ):
                    #para comer las normales
                    if(self.Board[Row_Postion_Final - 1][Column_Postion_Final - 1] == self.Pieses_White and
                    self.Board[Row_Postion_Final - 2][Column_Postion_Final - 2] == '◼' or
                    self.Board[Row_Postion_Final - 1][Column_Postion_Final + 1] == self.Pieses_White and
                    self.Board[Row_Postion_Final - 2][Column_Postion_Final + 2] == '◼' or
                    #para comer tambien lar reinas comtrarias
                    self.Board[Row_Postion_Final - 1][Column_Postion_Final - 1] == self.Pieses_Queen_White and
                    self.Board[Row_Postion_Final - 2][Column_Postion_Final - 2] == '◼' or
                    self.Board[Row_Postion_Final - 1][Column_Postion_Final + 1] == self.Pieses_Queen_White and
                    self.Board[Row_Postion_Final - 2][Column_Postion_Final + 2] == '◼'):

                        self.presentation()
                        #cuando se encuentra una contraria y puede seguir comiendo (Turn = False son para Negras)
                        PiesesWhiteBlack.turn = False
                        self.movement_pieses2(Row_Final)

                elif(self.winner()==False):
                    print("Fin del juego")

                else:
                    PiesesWhiteBlack.turn = False

            #Queen_white-----------------
            elif(self.Board[Row_Postion_Initial][Column_Postion_Initial] == self.Pieses_Queen_White):
                self.movement_queen_pieses(Row_Postion_Initial,Column_Postion_Initial,Row_Postion_Final,Column_Postion_Final,PiesesWhiteBlack.turn)

                if(self.Board[Row_Postion_Final + Value_row_int][Column_Postion_Final + Value_col_int] == self.Pieses_Black or self.Board[Row_Postion_Final + Value_row_int][Column_Postion_Final + Value_col_int] == self.Pieses_Queen_Black):
                    Queen_Killer.queen_killer_w(self,Row_Postion_Initial,Column_Postion_Initial,Row_Postion_Final,Column_Postion_Final)
                    self.presentation()
                    if(Row_Postion_Final+2 <= 8 and Column_Postion_Final+2 <=8 and Row_Postion_Final-2 >= 0 and Column_Postion_Final-2 >= 0 ):
                        if(self.Board[Row_Postion_Final - 1][Column_Postion_Final - 1] == self.Pieses_Black and
                        self.Board[Row_Postion_Final - 2][Column_Postion_Final - 2] == '◼' or
                        self.Board[Row_Postion_Final - 1][Column_Postion_Final + 1] == self.Pieses_Black and
                        self.Board[Row_Postion_Final - 2][Column_Postion_Final + 2] == '◼' or
                        self.Board[Row_Postion_Final + 1][Column_Postion_Final + 1] == self.Pieses_Black and
                        self.Board[Row_Postion_Final + 2][Column_Postion_Final + 2] == '◼' or
                        self.Board[Row_Postion_Final + 1][Column_Postion_Final - 1] == self.Pieses_Black and
                        self.Board[Row_Postion_Final + 2][Column_Postion_Final - 2] == '◼' or
                        
                        self.Board[Row_Postion_Final - 1][Column_Postion_Final - 1] == self.Pieses_Queen_Black and
                        self.Board[Row_Postion_Final - 2][Column_Postion_Final - 2] == '◼' or
                        self.Board[Row_Postion_Final - 1][Column_Postion_Final + 1] == self.Pieses_Queen_Black and
                        self.Board[Row_Postion_Final - 2][Column_Postion_Final + 2] == '◼' or
                        self.Board[Row_Postion_Final + 1][Column_Postion_Final + 1] == self.Pieses_Queen_Black and
                        self.Board[Row_Postion_Final + 2][Column_Postion_Final + 2] == '◼' or
                        self.Board[Row_Postion_Final + 1][Column_Postion_Final - 1] == self.Pieses_Queen_Black and
                        self.Board[Row_Postion_Final + 2][Column_Postion_Final - 2] == '◼'):

                            self.presentation()
                            PiesesWhiteBlack.turn = True
                            self.movement_pieses2(Row_Final)

                    elif(self.winner()==False):
                        print("Fin del juego")

                    else:
                        PiesesWhiteBlack.turn = False

            #Queen_black
            elif(self.Board[Row_Postion_Initial][Column_Postion_Initial] == self.Pieses_Queen_Black):
                self.movement_queen_pieses(Row_Postion_Initial,Column_Postion_Initial,Row_Postion_Final,Column_Postion_Final,PiesesWhiteBlack.turn)
                #para comer
                if(self.Board[Row_Postion_Final + Value_row_int][Column_Postion_Final + Value_col_int] == self.Pieses_White or self.Board[Row_Postion_Final + Value_row_int][Column_Postion_Final + Value_col_int] == self.Pieses_Queen_White):
                    Queen_Killer.queen_killer_b(self,Row_Postion_Initial,Column_Postion_Initial,Row_Postion_Final,Column_Postion_Final)
                    self.presentation()
                    if(Row_Postion_Final+2 <= 8 and Column_Postion_Final+2 <=8 and Row_Postion_Final-2 >= 0 and Column_Postion_Final-2 >= 0 ):
                        if(self.Board[Row_Postion_Final - 1][Column_Postion_Final - 1] == self.Pieses_White and
                        self.Board[Row_Postion_Final - 2][Column_Postion_Final - 2] == '◼' or
                        self.Board[Row_Postion_Final - 1][Column_Postion_Final + 1] == self.Pieses_White and
                        self.Board[Row_Postion_Final - 2][Column_Postion_Final + 2] == '◼' or
                        self.Board[Row_Postion_Final + 1][Column_Postion_Final + 1] == self.Pieses_White and
                        self.Board[Row_Postion_Final + 2][Column_Postion_Final + 2] == '◼' or
                        self.Board[Row_Postion_Final + 1][Column_Postion_Final - 1] == self.Pieses_White and
                        self.Board[Row_Postion_Final + 2][Column_Postion_Final - 2] == '◼' or
                        
                        self.Board[Row_Postion_Final - 1][Column_Postion_Final - 1] == self.Pieses_Queen_White and
                        self.Board[Row_Postion_Final - 2][Column_Postion_Final - 2] == '◼' or
                        self.Board[Row_Postion_Final - 1][Column_Postion_Final + 1] == self.Pieses_Queen_White and
                        self.Board[Row_Postion_Final - 2][Column_Postion_Final + 2] == '◼' or
                        self.Board[Row_Postion_Final + 1][Column_Postion_Final + 1] == self.Pieses_Queen_White and
                        self.Board[Row_Postion_Final + 2][Column_Postion_Final + 2] == '◼' or
                        self.Board[Row_Postion_Final + 1][Column_Postion_Final - 1] == self.Pieses_Queen_White and
                        self.Board[Row_Postion_Final + 2][Column_Postion_Final - 2] == '◼'):

                            self.presentation()
                            PiesesWhiteBlack.turn = False
                            self.movement_pieses2(Row_Final)

                    elif(self.winner()==False):
                        print("Fin del juego")

                    else:
                        PiesesWhiteBlack.turn = True
            else:
                print("Invalid Movement, try again")


    def presentation(self):
        os.system('clear')
        super().state()


    def clear_changeturn(self):
        if(PiesesWhiteBlack.turn == True):
            self.change_queen()
            self.presentation()
            PiesesWhiteBlack.turn = False
            print("shift change, black")

        elif(PiesesWhiteBlack.turn == False):
            self.change_queen()
            self.presentation()
            PiesesWhiteBlack.turn = True
            print("shift change, white")

    def detect(self):# encontrar piezas
        pieseswhite = [self.Pieses_White,self.Pieses_Queen_White]
        piesesblack = [self.Pieses_Black, self.Pieses_Queen_Black]
        white_pieces = False
        black_pieces = False
        for i in range (1,9):
            for j in range(1,9):
                
                if(self.Board[i][j] in pieseswhite):
                    white_pieces = True
                elif(self.Board[i][j] in piesesblack):
                    black_pieces = True

        if(white_pieces and black_pieces): return None
        elif(white_pieces): return True
        elif(black_pieces): return False
        return "ERROR"

    def winner(self):#detectar quien gana

        if(self.detect() == True):
            print("White win")
            return False

        elif(self.detect() == False):
            print("Black win")
            return False

        elif(self.detect() == None):
            return True

LPiesesWB = PiesesWhiteBlack()
LPiesesWB.players()
LPiesesWB.movement_pieses()