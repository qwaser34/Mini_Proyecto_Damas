from Damas import DamasChinas
class kill_Pieces(DamasChinas):
    
    def kill_pieses(self, Row_Postion_Initial,Column_Postion_Initial,Row_Postion_Final,Column_Postion_Final):
        #izquierda arriba a derecha abajo
        self.Row_Postion_Initial = Row_Postion_Initial
        self.Column_Postion_Initial = Column_Postion_Initial
        self.Row_Postion_Final = Row_Postion_Final
        self.Column_Postion_Final = Column_Postion_Final

        Value_Row_Pieses = (Row_Postion_Initial - Row_Postion_Final)
        Value_Col_Pieses = (Column_Postion_Initial - Column_Postion_Final)
        Value_row_int = int(Value_Row_Pieses/2)
        Value_col_int = int(Value_Col_Pieses/2)

        if(self.Board[Row_Postion_Final + Value_row_int][Column_Postion_Final + Value_col_int] != self.Board[Row_Postion_Initial][Column_Postion_Initial]):
            self.Board[Row_Postion_Final + Value_row_int][Column_Postion_Final + Value_col_int] = '◼'
            self.Board[Row_Postion_Final][Column_Postion_Final] = self.Board[Row_Postion_Initial][Column_Postion_Initial]
            self.Board[Row_Postion_Initial][Column_Postion_Initial] = '◼'


    
    def kill_function(self, Row_Postion_Initial,Column_Postion_Initial,Row_Postion_Final,Column_Postion_Final):
        self.Row_Postion_Initial = Row_Postion_Initial
        self.Column_Postion_Initial = Column_Postion_Initial
        self.Row_Postion_Final = Row_Postion_Final
        self.Column_Postion_Final = Column_Postion_Final
        # Value_Row_Pieses = (Row_Postion_Initial - Row_Postion_Final)
        # Value_Col_Pieses = (Column_Postion_Initial - Column_Postion_Final)
        # Value_row_int = int(Value_Row_Pieses/2)
        # Value_col_int = int(Value_Col_Pieses/2)

        # while(True):
        if(self.Board[Row_Postion_Final -1][Column_Postion_Final -1] != self.Board[Row_Postion_Initial][Column_Postion_Initial]):
            kill_Pieces.kill_pieses(self,Row_Postion_Final,Column_Postion_Final,Row_Postion_Final-2,Column_Postion_Final-2)
            return kill_Pieces.kill_function(self, Row_Postion_Initial,Column_Postion_Initial,Row_Postion_Final,Column_Postion_Final)
            
            # elif(self.Board[Row_Postion_Final -1][Column_Postion_Final +1] != self.Board[Row_Postion_Initial][Column_Postion_Initial]):
            #     kill_Pieces.kill_pieses(self,Row_Postion_Final,Column_Postion_Final,Row_Postion_Final-2,Column_Postion_Final-2)
            #     return kill_Pieces.recursive_kill_function(self, Row_Postion_Initial,Column_Postion_Initial,Row_Postion_Final,Column_Postion_Final)
            # else:
            #     break





