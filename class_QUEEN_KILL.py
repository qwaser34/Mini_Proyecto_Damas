from Damas import Damas
class QueenKiller(Damas):
    
    def queen_killer_w(self, row_postion_initial, column_postion_initial, row_postion_final, column_postion_final):
        #para que coman las reinas blancas
        self.row_postion_initial = row_postion_initial
        self.column_postion_initial = column_postion_initial
        self.row_postion_final = row_postion_final
        self.column_postion_final = column_postion_final

        Value_Row_White = (row_postion_initial - row_postion_final)
        Value_Col_White = (column_postion_initial - column_postion_final)
        Value_row_int = int(Value_Row_White/2)
        Value_col_int = int(Value_Col_White/2)

        postion_final_row_int = row_postion_final + Value_row_int
        postion_final_col_int = column_postion_final + Value_col_int

        self.board[postion_final_row_int][postion_final_col_int] = '◼'
        self.board[row_postion_final][column_postion_final] = self.pieses_queen_white
        self.board[row_postion_initial][column_postion_initial] = '◼'

    def queen_killer_b(self, row_postion_initial, column_postion_initial, row_postion_final, column_postion_final):
        #para que coman las reinas negras
        self.row_postion_initial = row_postion_initial
        self.column_postion_initial = column_postion_initial
        self.row_postion_final = row_postion_final
        self.column_postion_final = column_postion_final

        Value_Row_White = (row_postion_initial - row_postion_final)
        Value_Col_White = (column_postion_initial - column_postion_final)
        Value_row_int = int(Value_Row_White/2)
        Value_col_int = int(Value_Col_White/2)

        postion_final_row_int = row_postion_final + Value_row_int
        postion_final_col_int = column_postion_final + Value_col_int

        self.board[postion_final_row_int][postion_final_col_int] = '◼'
        self.board[row_postion_final][column_postion_final] = self.pieses_queen_black
        self.board[row_postion_initial][column_postion_initial] = '◼'
