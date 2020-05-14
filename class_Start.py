import os
from Damas import Damas
from class_kill_Pieces import killPieces
from class_QUEEN_KILL import QueenKiller

class Start(Damas): #clase
    turn = False
    #  movimiento de piezas normales
    def movement_normal_pieses(self, row_postion_initial, column_postion_initial, row_postion_final, column_postion_final,turn):
        self.row_postion_initial = row_postion_initial
        self.column_postion_initial = column_postion_initial
        self.row_postion_final = row_postion_final
        self.column_postion_final = column_postion_final

        if(turn):#turn white
            # chequea si no donde se movera es una diagonal
            if((self.row_postion_final%2 != 0 and self.column_postion_final%2 == 0) or (self.row_postion_final%2 == 0 and self.column_postion_final%2 != 0) or 
            (self.board[row_postion_final][column_postion_final] == self.pieses_black) or (self.board[row_postion_final][column_postion_final] == self.pieses_queen_black)):

                self.board[row_postion_initial][column_postion_initial] = self.pieses_white
                self.board[row_postion_final][column_postion_final] = self.board[row_postion_final][column_postion_final]

            # si lo es pasa esto
            else:
                self.board[row_postion_initial][column_postion_initial] = '◼'
                self.board[row_postion_final][column_postion_final] = self.pieses_white

        else: #turn black
            if((self.row_postion_final%2 != 0 and self.column_postion_final%2 == 0) or (self.row_postion_final%2 == 0 and self.column_postion_final%2 != 0) or 
            (self.board[row_postion_final][column_postion_final] == self.pieses_white) or (self.board[row_postion_final][column_postion_final] == self.pieses_queen_white)):

                self.board[row_postion_initial][column_postion_initial] = self.pieses_black
                self.board[row_postion_final][column_postion_final] = self.board[row_postion_final][column_postion_final]

            # lo mismo de las blancas
            else:
                self.board[row_postion_initial][column_postion_initial] = '◼'
                self.board[row_postion_final][column_postion_final] = self.pieses_black

        # cambia las piesas a reinas
    def change_queen(self):
        for i in range(0,9):
            for j in range(0,9):
                if (i == 8):
                    if(self.board[i][j] == self.pieses_white):
                        self.board[i][j] = self.pieses_queen_white

                if(i == 1):
                    if(self.board[i][j] == self.pieses_black):
                        self.board[i][j] = self.pieses_queen_black

    # queens movement
    def movement_queen_pieses(self, row_postion_initial, column_postion_initial, row_postion_final, column_postion_final,turn):
        self.row_postion_initial = row_postion_initial
        self.column_postion_initial = column_postion_initial
        self.row_postion_final = row_postion_final
        self.column_postion_final = column_postion_final

        if(turn):#turn white
            # if(self.row_postion_final%2 != 0 and self.column_postion_final%2 == 0 or self.row_postion_final%2 == 0 and self.column_postion_final%2 != 0):
            if(self.board[row_postion_final][column_postion_final] == '◼'):
                self.board[row_postion_initial][column_postion_initial] = '◼'
                self.board[row_postion_final][column_postion_final] = self.pieses_queen_white

            elif(self.board[row_postion_final][column_postion_final] == self.pieses_white):
                self.board[row_postion_initial][column_postion_initial] = self.pieses_queen_white
                self.board[row_postion_final][column_postion_final] = '◼'

            elif(self.board[row_postion_final][column_postion_final] == '◻'):
                self.board[row_postion_initial][column_postion_initial] = self.pieses_queen_white
                self.board[row_postion_final][column_postion_final] = '◻'

        else: #turn Queen black
            # if(self.row_postion_final%2 != 0 and self.column_postion_final%2 == 0 or self.row_postion_final%2 == 0 and self.column_postion_final%2 != 0):
            if(self.board[row_postion_final][column_postion_final] == '◻'):
                self.board[row_postion_initial][column_postion_initial] = self.pieses_queen_black
                self.board[row_postion_final][column_postion_final] = '◻'

            elif(self.board[row_postion_final][column_postion_final] == self.pieses_black):
                self.board[row_postion_initial][column_postion_initial] = self.pieses_queen_black
                self.board[row_postion_final][column_postion_final] = '◼'

            else:
                self.board[row_postion_initial][column_postion_initial] = '◼'
                self.board[row_postion_final][column_postion_final] = self.pieses_queen_black

    #comienza el juego con las blancas
    def players(self):
        self.state()
        while(True):

            print("White Begins")
            Start.turn =False
            return Start.turn

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
            row_postion_initial = letter_to_number[Row_Postion]
            Column_Postion = Row_Initial[1]
            column_postion_initial = letter_to_number[Column_Postion]
            Row_Postion2 = Row_Final[0]
            row_postion_final = letter_to_number[Row_Postion2]
            Column_Postion2 = Row_Final[1]
            column_postion_final = letter_to_number[Column_Postion2]

            #calcula el valor para ver donde te mueves
            Value_Row_Pieses = (row_postion_initial - row_postion_final)
            Value_Col_Pieses = (column_postion_initial - column_postion_final)

            Value_row_int = int(Value_Row_Pieses/2)
            Value_col_int = int(Value_Col_Pieses/2)

            postion_final_row_int = row_postion_final + Value_row_int
            postion_final_col_int = column_postion_final + Value_col_int


            #White----------------
            if(self.board[row_postion_initial][column_postion_initial] == self.pieses_white  and Value_Row_Pieses == -1):# moverse de uno en uno
                self.movement_normal_pieses(row_postion_initial, column_postion_initial, row_postion_final, column_postion_final, Start.turn)
                self.clear_changeturn()

            elif(self.board[row_postion_initial][column_postion_initial] == self.pieses_white and Value_Row_Pieses == -2): #detecta si puede comer
                
                # comer
                killPieces.kill_pieses(self,row_postion_initial, column_postion_initial, row_postion_final, column_postion_final)# funcion que permite que se coma la contraria
                self.presentation()
                #limitar los bordes para que no se salga del rango
                if((row_postion_final+2 <= 8) and (column_postion_final+2 <=8) and (row_postion_final-2 >= 0) and (column_postion_final-2 >= 0)):
                    #para comer las normales
                    if(self.board[row_postion_final + 1][column_postion_final + 1] == self.pieses_black and
                    self.board[row_postion_final + 2][column_postion_final + 2] == '◼' or
                    self.board[row_postion_final + 1][column_postion_final - 1] == self.pieses_black and
                    self.board[row_postion_final + 2][column_postion_final - 2] == '◼' or
                    #para comer tambien lar reinas comtrarias
                    self.board[row_postion_final - 1][column_postion_final - 1] == self.pieses_queen_black and
                    self.board[row_postion_final - 2][column_postion_final - 2] == '◼' or
                    self.board[row_postion_final - 1][column_postion_final + 1] == self.pieses_queen_black and
                    self.board[row_postion_final - 2][column_postion_final + 2] == '◼'):

                        self.presentation()
                        #cuando se encuentra una contraria y puede seguir comiendo (Turn = True son para Blancas)
                        Start.turn = True
                        self.movement_pieses2(Row_Final)
                
                elif(self.winner()==False):
                    print("Game Over")
                    
                #para cambiar de turno
                else:
                    Start.turn = False

            #black------------------
            elif(self.board[row_postion_initial][column_postion_initial] == self.pieses_black and Start.turn == False and Value_Row_Pieses == 1):
                self.movement_normal_pieses(row_postion_initial, column_postion_initial, row_postion_final, column_postion_final, Start.turn)

                self.clear_changeturn()

            elif(self.board[row_postion_initial][column_postion_initial] == self.pieses_black and Start.turn == False and Value_Row_Pieses == 2):

                # comer
                killPieces.kill_pieses(self, row_postion_initial, column_postion_initial, row_postion_final, column_postion_final)
                self.presentation()
                #limitar los bordes para que no se salga del rango
                if((row_postion_final+2 <= 8) and (column_postion_final+2 <=8) and (row_postion_final-2 >= 0) and (column_postion_final-2 >= 0)):
                    #para comer las normales
                    if(self.board[row_postion_final - 1][column_postion_final - 1] == self.pieses_white and
                    self.board[row_postion_final - 2][column_postion_final - 2] == '◼' or
                    self.board[row_postion_final - 1][column_postion_final + 1] == self.pieses_white and
                    self.board[row_postion_final - 2][column_postion_final + 2] == '◼' or
                    #para comer tambien lar reinas comtrarias
                    self.board[row_postion_final - 1][column_postion_final - 1] == self.pieses_queen_white and
                    self.board[row_postion_final - 2][column_postion_final - 2] == '◼' or
                    self.board[row_postion_final - 1][column_postion_final + 1] == self.pieses_queen_white and
                    self.board[row_postion_final - 2][column_postion_final + 2] == '◼'):

                        self.presentation()
                        #cuando se encuentra una contraria y puede seguir comiendo (Turn = False son para Negras)
                        Start.turn = False
                        self.movement_pieses2(Row_Final)

                elif(self.winner()==False):
                    print("Game Over")

                else:
                    Start.turn = False

            #Queen_white-----------------
            elif(self.board[row_postion_initial][column_postion_initial] == self.pieses_queen_white):
                self.movement_queen_pieses(row_postion_initial, column_postion_initial, row_postion_final, column_postion_final, Start.turn)

                if(self.board[postion_final_row_int][postion_final_col_int] == self.pieses_black or self.board[postion_final_row_int][postion_final_col_int] == self.pieses_queen_black):
                    QueenKiller.queen_killer_w(self, row_postion_initial, column_postion_initial, row_postion_final, column_postion_final)
                    self.presentation()

                    if((row_postion_final+2 <= 8) and (column_postion_final+2 <=8) and (row_postion_final-2 >= 0) and (column_postion_final-2 >= 0)):
                        if(self.board[row_postion_final - 1][column_postion_final - 1] == self.pieses_black and
                        self.board[row_postion_final - 2][column_postion_final - 2] == '◼' or
                        self.board[row_postion_final - 1][column_postion_final + 1] == self.pieses_black and
                        self.board[row_postion_final - 2][column_postion_final + 2] == '◼' or
                        self.board[row_postion_final + 1][column_postion_final + 1] == self.pieses_black and
                        self.board[row_postion_final + 2][column_postion_final + 2] == '◼' or
                        self.board[row_postion_final + 1][column_postion_final - 1] == self.pieses_black and
                        self.board[row_postion_final + 2][column_postion_final - 2] == '◼' or
                        
                        self.board[row_postion_final - 1][column_postion_final - 1] == self.pieses_queen_black and
                        self.board[row_postion_final - 2][column_postion_final - 2] == '◼' or
                        self.board[row_postion_final - 1][column_postion_final + 1] == self.pieses_queen_black and
                        self.board[row_postion_final - 2][column_postion_final + 2] == '◼' or
                        self.board[row_postion_final + 1][column_postion_final + 1] == self.pieses_queen_black and
                        self.board[row_postion_final + 2][column_postion_final + 2] == '◼' or
                        self.board[row_postion_final + 1][column_postion_final - 1] == self.pieses_queen_black and
                        self.board[row_postion_final + 2][column_postion_final - 2] == '◼'):

                            self.presentation()
                            Start.turn = True
                            self.movement_pieses2(Row_Final)

                    elif(self.winner()==False):
                        print("Game Over")

                    else:
                        Start.turn = False

            #Queen_black
            elif(self.board[row_postion_initial][column_postion_initial] == self.pieses_queen_black):
                self.movement_queen_pieses(row_postion_initial, column_postion_initial, row_postion_final, column_postion_final, Start.turn)

                #para comer
                if(self.board[postion_final_row_int][postion_final_col_int] == self.pieses_white or self.board[postion_final_row_int][postion_final_col_int] == self.pieses_queen_white):
                    QueenKiller.queen_killer_b(self, row_postion_initial, column_postion_initial, row_postion_final, column_postion_final)
                    self.presentation()

                    if((row_postion_final+2 <= 8) and (column_postion_final+2 <=8) and (row_postion_final-2 >= 0) and (column_postion_final-2 >= 0) ):
                        if(self.board[row_postion_final - 1][column_postion_final - 1] == self.pieses_white and
                        self.board[row_postion_final - 2][column_postion_final - 2] == '◼' or
                        self.board[row_postion_final - 1][column_postion_final + 1] == self.pieses_white and
                        self.board[row_postion_final - 2][column_postion_final + 2] == '◼' or
                        self.board[row_postion_final + 1][column_postion_final + 1] == self.pieses_white and
                        self.board[row_postion_final + 2][column_postion_final + 2] == '◼' or
                        self.board[row_postion_final + 1][column_postion_final - 1] == self.pieses_white and
                        self.board[row_postion_final + 2][column_postion_final - 2] == '◼' or
                        
                        self.board[row_postion_final - 1][column_postion_final - 1] == self.pieses_queen_white and
                        self.board[row_postion_final - 2][column_postion_final - 2] == '◼' or
                        self.board[row_postion_final - 1][column_postion_final + 1] == self.pieses_queen_white and
                        self.board[row_postion_final - 2][column_postion_final + 2] == '◼' or
                        self.board[row_postion_final + 1][column_postion_final + 1] == self.pieses_queen_white and
                        self.board[row_postion_final + 2][column_postion_final + 2] == '◼' or
                        self.board[row_postion_final + 1][column_postion_final - 1] == self.pieses_queen_white and
                        self.board[row_postion_final + 2][column_postion_final - 2] == '◼'):

                            self.presentation()
                            Start.turn = False
                            self.movement_pieses2(Row_Final)

                    elif(self.winner()==False):
                        print("Game Over")

                    else:
                        Start.turn = True
            else:
                print("Invalid Movement, try again")


    def presentation(self):
        os.system('clear')
        super().state()


    def clear_changeturn(self):
        if(Start.turn == True):
            self.change_queen()
            self.presentation()
            Start.turn = False
            print("shift change, black")

        elif(Start.turn == False):
            self.change_queen()
            self.presentation()
            Start.turn = True
            print("shift change, white")

    def detect(self):# encontrar piezas
        pieseswhite = [self.pieses_white, self.pieses_queen_white]
        piesesblack = [self.pieses_black, self.pieses_queen_black]
        white_pieces = False
        black_pieces = False
        for i in range (1,9):
            for j in range(1,9):
                
                if(self.board[i][j] in pieseswhite):
                    white_pieces = True
                elif(self.board[i][j] in piesesblack):
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

Game = Start()
Game.players()
Game.movement_pieses()
