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
            
            self.gameStatus = True
        
        print(nomeJogador1)
        print(nomeJogador2)
        
    def encerrarJogo():
        pass