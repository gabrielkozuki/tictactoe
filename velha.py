class Velha():
    
    def __init__(self):
        self.tab = [
            ["", "", ""], 
            ["", "", ""], 
            ["", "", ""]
        ]
        self.rodada = 1
        self.vez = "X"
        
    def getPos(self, row, col):
        return self.tab[row][col]
        
    def getVez(self):
        return self.vez
    
    def getRodada(self):
        return self.rodada
        
    def setJogada(self, row, col):
        if self.tab[row][col] != "":
            return None
        else:
            self.tab[row][col] = self.vez
        
    def verificarGanhador(self):
        resRow0 = self.tab[0][0] + self.tab[0][1] + self.tab[0][2]
        resRow1 = self.tab[1][0] + self.tab[1][1] + self.tab[1][2]
        resRow2 = self.tab[2][0] + self.tab[2][1] + self.tab[2][2]
        resCol0 = self.tab[0][0] + self.tab[1][0] + self.tab[2][0]
        resCol1 = self.tab[0][1] + self.tab[1][1] + self.tab[2][1]
        resCol2 = self.tab[0][2] + self.tab[1][2] + self.tab[2][2]
        resDiag1 = self.tab[0][0] + self.tab[1][1] + self.tab[2][2]
        resDiag2 = self.tab[0][2] + self.tab[1][1] + self.tab[2][0]

        jogador = self.vez + self.vez + self.vez
        
        if resRow0 == jogador or resRow1 == jogador or resRow2 == jogador\
            or resCol0 == jogador or resCol1 == jogador or resCol2 == jogador\
            or resDiag1 == jogador or resDiag2 == jogador:
            
            return self.vez
        elif self.rodada == 9:
            return 'empate'
        else:
            return None
        
    def jogarRodada(self, row, col):
        self.setJogada(row, col)
        result = self.verificarGanhador()

        self.rodada = self.rodada + 1
        if self.vez == "X":
            self.vez = "O"
        elif self.vez == "O":
            self.vez = "X"

        return result
        