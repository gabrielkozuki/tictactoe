from ast import For
import tkinter as tk
from velha import Velha
from view import View

class Controller():
    
    def __init__(self) -> None:
        self.tabuleiro = [["", "", ""], ["", "", ""], ["", "", ""]]
        self.view = View(self)
        self.velha = Velha()
        
        self.gameStatus = False
        
        for x in range(3):
            for y in range(3):
                self.tabuleiro[x][y] = tk.StringVar()
        
        self.view.run()
    
    def setJogo(self):
        
        if self.gameStatus:
            self.view.btnJogo.config(text="Iniciar jogo")
            self.view.inputJogador1.config(state="normal")
            self.view.inputJogador2.config(state="normal")
            
            self.view.pararJogo()
            
            self.gameStatus = False
        else:
            self.view.btnJogo.config(text="Parar jogo")
            nomeJogador1 = self.view.inputJogador1.get()
            nomeJogador2 = self.view.inputJogador2.get()
            self.view.inputJogador1.config(state="disabled")
            self.view.inputJogador2.config(state="disabled")
            
            self.view.iniciarJogo()
            self.gameStatus = True
            
    def jogarRodada(self, row, col):
        
        print(row, col)
        
        self.velha.jogarRodada(row, col)
        self.atualizarTabuleiro()
        
    def atualizarJogo(self):
        for row in range(3):
            for col in range(3):
                pos = self.velha.getPos(row, col)
                
                if pos == 1:
                    self.tabuleiro[row][col] = "X"
                elif pos == 2:
                    self.tabuleiro[row][col] = "O"
                else:
                    self.tabuleiro[row][col] = ""
                    
        if self.velha.getVez() == 1:
            self.view.labelTurno["text"] = "Vez de: " + self.view.nomeJogador1
        else:
            self.view.labelTurno["text"] = "Vez de: " + self.view.nomeJogador2
            
        # self.view.labelRodada[""]
            
    def encerrarJogo(self):
        self.setJogo()
        pass