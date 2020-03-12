from Damas import DamasChinas
class kill_Pieces(DamasChinas):
    def kill_pieses_W1(self, Row_Postion_Current,Column_Postion_current,Row_Postion_Late,Column_Postion_Late):
        #izquierda arriba a derecha abajo
        self.Row_Postion_Current = Row_Postion_Current
        self.Column_Postion_current = Column_Postion_current
        self.Row_Postion_Late = Row_Postion_Late
        self.Column_Postion_Late = Column_Postion_Late
         
        self.Board[Row_Postion_Late - 1][Column_Postion_Late - 1] = '⬛'
        self.Board[Row_Postion_Late][Column_Postion_Late] = self.Pieses_White
        self.Board[Row_Postion_Current][Column_Postion_current] = '⬛'

    def kill_pieses_W2(self, Row_Postion_Current,Column_Postion_current,Row_Postion_Late,Column_Postion_Late):
        # derecha arriba a izquierda abajo
        self.Row_Postion_Current = Row_Postion_Current
        self.Column_Postion_current = Column_Postion_current
        self.Row_Postion_Late = Row_Postion_Late
        self.Column_Postion_Late = Column_Postion_Late

        self.Board[Row_Postion_Late - 1][Column_Postion_Late + 1] = '⬛'
        self.Board[Row_Postion_Late][Column_Postion_Late] = self.Pieses_White
        self.Board[Row_Postion_Current][Column_Postion_current] = '⬛'

    def kill_pieses_B1(self, Row_Postion_Current,Column_Postion_current,Row_Postion_Late,Column_Postion_Late):
        # de derecha abajo a izquierda arriba
        self.Row_Postion_Current = Row_Postion_Current
        self.Column_Postion_current = Column_Postion_current
        self.Row_Postion_Late = Row_Postion_Late
        self.Column_Postion_Late = Column_Postion_Late

        self.Board[Row_Postion_Late + 1][Column_Postion_Late + 1] = '⬛'
        self.Board[Row_Postion_Late][Column_Postion_Late] = self.Pieses_Black
        self.Board[Row_Postion_Current][Column_Postion_current] = '⬛'

    def kill_pieses_B2(self, Row_Postion_Current,Column_Postion_current,Row_Postion_Late,Column_Postion_Late):
        # de izquierda abajo a derecha arriba
        self.Row_Postion_Current = Row_Postion_Current
        self.Column_Postion_current = Column_Postion_current
        self.Row_Postion_Late = Row_Postion_Late
        self.Column_Postion_Late = Column_Postion_Late

        self.Board[Row_Postion_Late + 1][Column_Postion_Late - 1] = '⬛'
        self.Board[Row_Postion_Late][Column_Postion_Late] = self.Pieses_Black
        self.Board[Row_Postion_Current][Column_Postion_current] = '⬛'

