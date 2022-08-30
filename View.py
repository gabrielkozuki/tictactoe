import tkinter as tk

def donothing():
    pass

class View():
    def __init__(self):
        self.root = tk.Tk()
        self.root.resizable(0, 0)
        self.container = tk.Frame(self.root)
        self.container.grid(row=0, column=0)
        
        self.inserirTabuleiro()
        self.inserirMenu()
        
        self.root.mainloop()
    
    def inserirTabuleiro(self):
        frame = tk.Frame(self.container)
        frame.grid(row=1, column=0, padx=5, pady=5)
        
        btn11 = tk.Button(frame, text="", width=10, height=5, command=donothing)
        btn12 = tk.Button(frame, text="", width=10, height=5, command=donothing)
        btn13 = tk.Button(frame, text="", width=10, height=5, command=donothing)
        btn21 = tk.Button(frame, text="", width=10, height=5, command=donothing)
        btn22 = tk.Button(frame, text="", width=10, height=5, command=donothing)
        btn23 = tk.Button(frame, text="", width=10, height=5, command=donothing)
        btn31 = tk.Button(frame, text="", width=10, height=5, command=donothing)
        btn32 = tk.Button(frame, text="", width=10, height=5, command=donothing)
        btn33 = tk.Button(frame, text="", width=10, height=5, command=donothing)
        
        btn11.grid(row=1, column=1, padx=5, pady=5)
        btn12.grid(row=1, column=2, padx=5, pady=5)
        btn13.grid(row=1, column=3, padx=5, pady=5)
        btn21.grid(row=2, column=1, padx=5, pady=5)
        btn22.grid(row=2, column=2, padx=5, pady=5)
        btn23.grid(row=2, column=3, padx=5, pady=5)
        btn31.grid(row=3, column=1, padx=5, pady=5)
        btn32.grid(row=3, column=2, padx=5, pady=5)
        btn33.grid(row=3, column=3, padx=5, pady=5)
        
    def inserirMenu(self):
        frame = tk.Frame(self.container)
        frame.grid(row=2, column=0, padx=5, pady=5)
        
        labelPlacar = tk.Label(frame, width=20, text="Pontuação")
        labelP1 = tk.Label(frame, width=20, text="Jogador 1:")
        labelP2 = tk.Label(frame, width=20, text="Jogador 2:")
        labelTurno = tk.Label(frame, width=20, text="Vez de:")
        labelRodada = tk.Label(frame, width=20, text="Rodada")
        btnIniciar = tk.Button(frame, text="Iniciar jogo", width=10, command=donothing)
        btnParar = tk.Button(frame, text="Parar jogo", width=10, command=donothing)
        
        labelPlacar.grid(row=1, column=0, pady=2)
        labelP1.grid(row=1, column=1, pady=2)
        labelP2.grid(row=1, column=2, pady=2)
        labelTurno.grid(row=2, column=0, pady=2)
        labelRodada.grid(row=2, column=1, pady=2)
        btnIniciar.grid(row=3, column=0, pady=2)
        btnParar.grid(row=3, column=1, pady=2)
        
    

if __name__ == '__main__':
    v = View()