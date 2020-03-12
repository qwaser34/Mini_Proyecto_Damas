from Damas import DamasChinas
class Queen_Killer(DamasChinas):
    
    def Queen_Killer_WD1(self, Row_Postion_Current,Column_Postion_current,Row_Postion_Late,Column_Postion_Late):
            #izquierda arriba a derecha abajo
            self.Row_Postion_Current = Row_Postion_Current
            self.Column_Postion_current = Column_Postion_current
            self.Row_Postion_Late = Row_Postion_Late
            self.Column_Postion_Late = Column_Postion_Late

            self.Board[Row_Postion_Late - 1][Column_Postion_Late - 1] = '⬛'
            self.Board[Row_Postion_Late][Column_Postion_Late] = self.Pieses_Queen_White
            self.Board[Row_Postion_Current][Column_Postion_current] = '⬛'
    def Queen_Killer_WD2(self, Row_Postion_Current,Column_Postion_current,Row_Postion_Late,Column_Postion_Late):
            # de derecha arriba a izquierda abajo
            self.Row_Postion_Current = Row_Postion_Current
            self.Column_Postion_current = Column_Postion_current
            self.Row_Postion_Late = Row_Postion_Late
            self.Column_Postion_Late = Column_Postion_Late

            self.Board[Row_Postion_Late - 1][Column_Postion_Late + 1] = '⬛'
            self.Board[Row_Postion_Late][Column_Postion_Late] = self.Pieses_Queen_White
            self.Board[Row_Postion_Current][Column_Postion_current] = '⬛'

    def Queen_Killer_WD3(self, Row_Postion_Current,Column_Postion_current,Row_Postion_Late,Column_Postion_Late):
            # de derecha abajo a izquierda arriba
            self.Row_Postion_Current = Row_Postion_Current
            self.Column_Postion_current = Column_Postion_current
            self.Row_Postion_Late = Row_Postion_Late
            self.Column_Postion_Late = Column_Postion_Late

            self.Board[Row_Postion_Late + 1][Column_Postion_Late + 1] = '⬛'
            self.Board[Row_Postion_Late][Column_Postion_Late] = self.Pieses_Queen_White
            self.Board[Row_Postion_Current][Column_Postion_current] = '⬛'
                
    def Queen_Killer_WD4(self, Row_Postion_Current,Column_Postion_current,Row_Postion_Late,Column_Postion_Late):
            # de izquierda abajo a derecha arriba
            self.Row_Postion_Current = Row_Postion_Current
            self.Column_Postion_current = Column_Postion_current
            self.Row_Postion_Late = Row_Postion_Late
            self.Column_Postion_Late = Column_Postion_Late
        
            self.Board[Row_Postion_Late + 1][Column_Postion_Late - 1] = '⬛'
            self.Board[Row_Postion_Late][Column_Postion_Late] = self.Pieses_Queen_White
            self.Board[Row_Postion_Current][Column_Postion_current] = '⬛'
                    
    def Queen_Killer_BD1(self, Row_Postion_Current,Column_Postion_current,Row_Postion_Late,Column_Postion_Late):
            #izquierda arriba a derecha abajo
            self.Row_Postion_Current = Row_Postion_Current
            self.Column_Postion_current = Column_Postion_current
            self.Row_Postion_Late = Row_Postion_Late
            self.Column_Postion_Late = Column_Postion_Late

            self.Board[Row_Postion_Late - 1][Column_Postion_Late - 1] = '⬛'
            self.Board[Row_Postion_Late][Column_Postion_Late] = self.Pieses_Queen_Black
            self.Board[Row_Postion_Current][Column_Postion_current] = '⬛'

    def Queen_Killer_BD2(self, Row_Postion_Current,Column_Postion_current,Row_Postion_Late,Column_Postion_Late):
             # de derecha arriba a izquierda abajo
            self.Row_Postion_Current = Row_Postion_Current
            self.Column_Postion_current = Column_Postion_current
            self.Row_Postion_Late = Row_Postion_Late
            self.Column_Postion_Late = Column_Postion_Late

            self.Board[Row_Postion_Late - 1][Column_Postion_Late + 1] = '⬛'
            self.Board[Row_Postion_Late][Column_Postion_Late] = self.Pieses_Queen_Black
            self.Board[Row_Postion_Current][Column_Postion_current] = '⬛'

    def Queen_Killer_BD3(self, Row_Postion_Current,Column_Postion_current,Row_Postion_Late,Column_Postion_Late):
             # de derecha abajo a izquierda arriba
            self.Row_Postion_Current = Row_Postion_Current
            self.Column_Postion_current = Column_Postion_current
            self.Row_Postion_Late = Row_Postion_Late
            self.Column_Postion_Late = Column_Postion_Late

            self.Board[Row_Postion_Late + 1][Column_Postion_Late + 1] = '⬛'
            self.Board[Row_Postion_Late][Column_Postion_Late] = self.Pieses_Queen_Black
            self.Board[Row_Postion_Current][Column_Postion_current] = '⬛'
                
    def Queen_Killer_BD4(self, Row_Postion_Current,Column_Postion_current,Row_Postion_Late,Column_Postion_Late):
            # de izquierda abajo a derecha arriba
            self.Row_Postion_Current = Row_Postion_Current
            self.Column_Postion_current = Column_Postion_current
            self.Row_Postion_Late = Row_Postion_Late
            self.Column_Postion_Late = Column_Postion_Late

            self.Board[Row_Postion_Late + 1][Column_Postion_Late - 1] = '⬛'
            self.Board[Row_Postion_Late][Column_Postion_Late] = self.Pieses_Queen_Black
            self.Board[Row_Postion_Current][Column_Postion_current] = '⬛'
