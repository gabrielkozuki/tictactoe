from velha import Velha
from view import View

class Controller():
    
    def __init__(self) -> None:
        self.view = View(self)
        self.velha = Velha()
        
        self.view.run()
    
    def jogarRodada(self, row, col):
        
        jogada = self.velha.jogarRodada(row, col)
        
        if jogada is None:
            # pop-up dizendo "jogada inválida"
            pass
        else:
            self.view.atualizarTabuleiro()
            verificar = self.velha.verificarGanhador(self.vez)
            
            if verificar is None:
                pass
            else:
                if verificar == 0:
                    # pop-up jogador 1 vence
                    pass
                elif verificar == 1:
                    # pop-up jogador 2 vence
                    pass
                else:
                    # empate
                    pass
                
                self.reiniciarJogo()
    
    def reiniciarJogo(self):
        self.velha = Velha()
        # limpar view