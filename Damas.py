class DamasChinas:
    def __init__(self,Board):
        self.Board = Board
        for i in range(9):
            self.Board.append(['']*9)

        for i in range(0,9):
            for j in range(0,9):

                if(i%2 == 0):
                    self.Board[i][j] = "⬜"
                    if(j%2 == 0):
                        self.Board[i][j] = "⬛"

                if(i%2 != 0):
                    self.Board[i][j] = "⬜"
                    if(j%2 != 0):
                        self.Board[i][j] = "⬛"

                if(i == 0 and j == 0):
                    self.Board[i][j] = "X"
                if(i == 0 and j == 1):
                    self.Board[i][j] = "1"
                if(i == 0 and j == 2):
                    self.Board[i][j] = "2"
                if(i == 0 and j == 3):
                    self.Board[i][j] = "3"
                if(i == 0 and j == 4):
                    self.Board[i][j] = "4"
                if(i == 0 and j == 5):
                    self.Board[i][j] = "5"
                if(i == 0 and j == 6):
                    self.Board[i][j] = "6"
                if(i == 0 and j == 7):
                    self.Board[i][j] = "7"
                if(i == 0 and j == 8):
                    self.Board[i][j] = "8"

                if(i == 1 and j == 0):
                    self.Board[i][j] = "A"
                if(i == 2 and j == 0):
                    self.Board[i][j] = "B"
                if(i == 3 and j == 0):
                    self.Board[i][j] = "C"
                if(i == 4 and j == 0):
                    self.Board[i][j] = "D"
                if(i == 5 and j == 0):
                    self.Board[i][j] = "E"
                if(i == 6 and j == 0):
                    self.Board[i][j] = "F"
                if(i == 7 and j == 0):
                    self.Board[i][j] = "G"
                if(i == 8 and j == 0):
                    self.Board[i][j] = "H"

    def state(self):
        for x in self.Board:
            print(x)

class PiesesWhiteBlack(DamasChinas):

    def PiesesWB(self,Pw,Pb):
        self.Pw = Pw
        self.Pb = Pb
        for i in range(0,9):
            for j in range(0,9):
                if(i == 1 and j == 1):
                    self.Board[i][j] = self.Pw
                if(i == 1 and j == 3):
                    self.Board[i][j] = self.Pw
                if(i == 1 and j == 5):
                    self.Board[i][j] = self.Pw
                if(i == 1 and j == 7):
                    self.Board[i][j] = self.Pw

                if(i == 2 and j == 2):
                    self.Board[i][j] = self.Pw
                if(i == 2 and j == 4):
                    self.Board[i][j] = self.Pw
                if(i == 2 and j == 6):
                    self.Board[i][j] = self.Pw
                if(i == 2 and j == 8):
                    self.Board[i][j] = self.Pw

                if(i == 3 and j == 1):
                    self.Board[i][j] = self.Pw
                if(i == 3 and j == 3):
                    self.Board[i][j] = self.Pw
                if(i == 3 and j == 5):
                    self.Board[i][j] = self.Pw
                if(i == 3 and j == 7):
                    self.Board[i][j] = self.Pw

                if(i == 6 and j == 2):
                    self.Board[i][j] = self.Pb
                if(i == 6 and j == 4):
                    self.Board[i][j] = self.Pb
                if(i == 6 and j == 6):
                    self.Board[i][j] = self.Pb
                if(i == 6 and j == 8):
                    self.Board[i][j] = self.Pb

                if(i == 7 and j == 1):
                    self.Board[i][j] = self.Pb
                if(i == 7 and j == 3):
                    self.Board[i][j] = self.Pb
                if(i == 7 and j == 5):
                    self.Board[i][j] = self.Pb
                if(i == 7 and j == 7):
                    self.Board[i][j] = self.Pb

                if(i == 8 and j == 2):
                    self.Board[i][j] = self.Pb
                if(i == 8 and j == 4):
                    self.Board[i][j] = self.Pb
                if(i == 8 and j == 6):
                    self.Board[i][j] = self.Pb
                if(i == 8 and j == 8):
                    self.Board[i][j] = self.Pb

    def movimiento(self, RPcurrent,CPcurrent,RPlate,CPlate,ficha,turn):
        self.RPcurrent = RPcurrent
        self.CPcurrent = CPcurrent
        self.RPlate = RPlate
        self.CPlate = CPlate
        self.ficha = ficha
         
        if(turn):
            
            if(self.RPlate%2 != 0 and self.CPlate%2 == 0 or self.RPlate%2 == 0 and self.CPlate%2 != 0):
                self.Board[RPcurrent][CPcurrent] = self.Pw
                self.Board[RPlate][CPlate] = '⬜'
            else:  
                if(self.Board[RPlate][CPlate] != ' '):
                    self.Board[RPcurrent][CPcurrent] = ' '
                    self.Board[RPlate][CPlate] = self.Pw
                else:
                    self.Board[RPcurrent][CPcurrent] = self.Pw

        else:
            if(self.RPlate%2 != 0 and self.CPlate%2 == 0 or self.RPlate%2 == 0 and self.CPlate%2 != 0):
                self.Board[RPcurrent][CPcurrent] = self.Pb
                self.Board[RPlate][CPlate] = '⬜'
            else:    
                if(self.Board[RPlate][CPlate] != ' '):
                    self.Board[RPcurrent][CPcurrent] = ' '
                    self.Board[RPlate][CPlate] = self.Pb
                else:
                    self.Board[RPcurrent][CPcurrent] = self.Pb
    
    def play(self):
        self.PiesesWB('W','B')
        self.state()
        turn = False
        while(True):
            ficha = input("que jugador quieres ser? [J1/J2]: ")
            if(ficha == "J1" or ficha == "j1"):
                print("Mueves las Blancas")
                turn = True
                break
            elif(ficha == "J2" or ficha == "j2"):
                print("Mueves las Negras")
                turn = False
                break
            else:
                print("Jugador no existe")

        i = 0
        if turn == False:
            i = 1
            
        while(True):
            print(i)

            RPcurrent = int(input("Introduzca Fila de piesa que quieres mover: "))
            CPcurrent = int(input("Introduzca Columna de pieza que quieres mover: "))
            RPlate = int(input("Introduzca Fila de pieza donde la movera: "))
            CPlate = int(input("Introduzca Columna de pieza donde la movera: "))
            
            if(self.Board[RPcurrent][CPcurrent] == self.Pw and turn and i%2 == 0):
                self.movimiento(RPcurrent,CPcurrent,RPlate,CPlate,ficha,turn)
                self.pre()
                turn = False
                i += 1
            else:
                print(self.Board[RPcurrent][CPcurrent] == self.Pb)
                if(self.Board[RPcurrent][CPcurrent] == self.Pb and turn == False and i%2 != 0):
                    self.movimiento(RPcurrent,CPcurrent,RPlate,CPlate,ficha,turn)
                    self.pre()
                    turn = True
                    i += 1
                else:
                    print("Movimiento Invalido")

    def pre(self):
        super().state()

LPiesesWB = PiesesWhiteBlack([])
LPiesesWB.play()
