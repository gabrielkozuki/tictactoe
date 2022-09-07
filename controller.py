import tkinter as tk
from velha import Velha
from view import View

class Controller():
    
    def __init__(self) -> None:
        self.view = View(self)
        self.velha = Velha()
        
        self.gameStatus = False
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
            self.velha = Velha()
            self.atualizarView()
            self.gameStatus = True

            self.view.labelRodada["text"] = "Rodada " + str(self.velha.getRodada())
            if self.velha.getVez() == "X":
                self.view.labelTurno["text"] = "Vez de: " + self.view.nomeJogador1.get()
            elif self.velha.getVez() == "O":
                self.view.labelTurno["text"] = "Vez de: " + self.view.nomeJogador2.get()

            
    def jogarRodada(self, row, col):
        result = self.velha.jogarRodada(row, col)

        if result != None:
            self.encerrarJogo()
            self.view.exibirMensagem(result)

        self.atualizarView()
        
    def atualizarView(self):
        for row in range(3):
            for col in range(3):
                pos = self.velha.getPos(row, col)
                
                if pos == "X":
                    self.view.tabuleiro[row][col].set("X")
                elif pos == "O":
                    self.view.tabuleiro[row][col].set("O")
                else:
                    self.view.tabuleiro[row][col].set("")
        
        self.view.labelRodada["text"] = "Rodada " + str(self.velha.getRodada())
        if self.velha.getVez() == "X":
            self.view.labelTurno["text"] = "Vez de: " + self.view.nomeJogador1.get()
        elif self.velha.getVez() == "O":
            self.view.labelTurno["text"] = "Vez de: " + self.view.nomeJogador2.get()
            
    def encerrarJogo(self):
        self.setJogo()
        pass
