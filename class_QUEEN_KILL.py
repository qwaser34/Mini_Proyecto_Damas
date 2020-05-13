from Damas import DamasChinas
class Queen_Killer(DamasChinas):
    
    def queen_killer_w(self, Row_Postion_Initial,Column_Postion_Initial,Row_Postion_Final,Column_Postion_Final):
        #para que coman las reinas blancas
        self.Row_Postion_Initial = Row_Postion_Initial
        self.Column_Postion_Initial = Column_Postion_Initial
        self.Row_Postion_Final = Row_Postion_Final
        self.Column_Postion_Final = Column_Postion_Final

        Value_Row_White = (Row_Postion_Initial - Row_Postion_Final)
        Value_Col_White = (Column_Postion_Initial - Column_Postion_Final)
        Value_row_int = int(Value_Row_White/2)
        Value_col_int = int(Value_Col_White/2)

        self.Board[Row_Postion_Final + Value_row_int][Column_Postion_Final + Value_col_int] = '◼'
        self.Board[Row_Postion_Final][Column_Postion_Final] = self.Pieses_Queen_White
        self.Board[Row_Postion_Initial][Column_Postion_Initial] = '◼'

    def queen_killer_b(self, Row_Postion_Initial,Column_Postion_Initial,Row_Postion_Final,Column_Postion_Final):
        #para que coman las reinas negras
        self.Row_Postion_Initial = Row_Postion_Initial
        self.Column_Postion_Initial = Column_Postion_Initial
        self.Row_Postion_Final = Row_Postion_Final
        self.Column_Postion_Final = Column_Postion_Final

        Value_Row_White = (Row_Postion_Initial - Row_Postion_Final)
        Value_Col_White = (Column_Postion_Initial - Column_Postion_Final)
        Value_row_int = int(Value_Row_White/2)
        Value_col_int = int(Value_Col_White/2)

        self.Board[Row_Postion_Final + Value_row_int][Column_Postion_Final + Value_col_int] = '◼'
        self.Board[Row_Postion_Final][Column_Postion_Final] = self.Pieses_Queen_Black
        self.Board[Row_Postion_Initial][Column_Postion_Initial] = '◼'
