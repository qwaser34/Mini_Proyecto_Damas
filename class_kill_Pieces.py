from Damas import Damas
class killPieces(Damas):
    
    def kill_pieses(self, row_postion_initial, column_postion_initial, row_postion_final, column_postion_final):
        #izquierda arriba a derecha abajo
        self.row_postion_initial = row_postion_initial
        self.column_postion_initial = column_postion_initial
        self.row_postion_final = row_postion_final
        self.column_postion_final = column_postion_final

        Value_Row_Pieses = (row_postion_initial - row_postion_final)
        Value_Col_Pieses = (column_postion_initial - column_postion_final)
        Value_row_int = int(Value_Row_Pieses/2)
        Value_col_int = int(Value_Col_Pieses/2)

        postion_final_row_int = row_postion_final + Value_row_int
        postion_final_col_int = column_postion_final + Value_col_int


        if(self.board[postion_final_row_int][postion_final_col_int] != self.board[row_postion_initial][column_postion_initial]):
            self.board[postion_final_row_int][postion_final_col_int] = '◼'
            self.board[row_postion_final][column_postion_final] = self.board[row_postion_initial][column_postion_initial]
            self.board[row_postion_initial][column_postion_initial] = '◼'


   

