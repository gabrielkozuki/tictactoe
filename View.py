import tkinter as tk

def donothing():
    pass

class View():
    def __init__(self, controller):
        self.root = tk.Tk()
        self.root.resizable(0, 0)
        self.container = tk.Frame(self.root)
        self.container.grid(row=0, column=0)
        
        self.controller = controller
        self.jogador1 = "X"
        self.jogador2 = "O"
        
        self.nomeJogador1 = tk.StringVar()
        self.nomeJogador2 = tk.StringVar()

        self.inserirTabuleiro()
        self.inserirMenu()
        
    def run(self):
        self.root.mainloop()
    
    def inserirTabuleiro(self):
        frame = tk.Frame(self.container)
        frame.grid(row=1, column=0, padx=5, pady=5)
        
        self.btn11 = tk.Button(frame, text="", width=10, height=5, command=donothing)
        self.btn12 = tk.Button(frame, text="", width=10, height=5, command=donothing)
        self.btn13 = tk.Button(frame, text="", width=10, height=5, command=donothing)
        self.btn21 = tk.Button(frame, text="", width=10, height=5, command=donothing)
        self.btn22 = tk.Button(frame, text="", width=10, height=5, command=donothing)
        self.btn23 = tk.Button(frame, text="", width=10, height=5, command=donothing)
        self.btn31 = tk.Button(frame, text="", width=10, height=5, command=donothing)
        self.btn32 = tk.Button(frame, text="", width=10, height=5, command=donothing)
        self.btn33 = tk.Button(frame, text="", width=10, height=5, command=donothing)
        
        self.btn11.grid(row=1, column=1, padx=5, pady=5)
        self.btn12.grid(row=1, column=2, padx=5, pady=5)
        self.btn13.grid(row=1, column=3, padx=5, pady=5)
        self.btn21.grid(row=2, column=1, padx=5, pady=5)
        self.btn22.grid(row=2, column=2, padx=5, pady=5)
        self.btn23.grid(row=2, column=3, padx=5, pady=5)
        self.btn31.grid(row=3, column=1, padx=5, pady=5)
        self.btn32.grid(row=3, column=2, padx=5, pady=5)
        self.btn33.grid(row=3, column=3, padx=5, pady=5)
        
    def inserirMenu(self):
        frame = tk.Frame(self.container)
        frame.grid(row=2, column=0, padx=5, pady=5)
        
        self.labelRodada = tk.Label(frame, width=20, text="Rodada:", fg="#BFBFBF")
        self.labelJogador1 = tk.Label(frame, width=20, text="Jogador 1 (X): ", fg="#BFBFBF")
        self.labelJogador2 = tk.Label(frame, width=20, text="Jogador 2 (O): ", fg="#BFBFBF")
        self.labelTurno = tk.Label(frame, width=20, text="Vez de:", fg="#BFBFBF")
        self.btnJogo = tk.Button(frame, text="Iniciar jogo", width=10, command=self.controller.setJogo)
        self.inputJogador1 = tk.Entry(frame, width=20, textvariable=self.nomeJogador1)
        self.inputJogador2 = tk.Entry(frame, width=20, textvariable=self.nomeJogador2)
        
        self.labelRodada.grid(row=1, column=0, pady=2)
        self.labelJogador1.grid(row=2, column=1, pady=2)
        self.labelJogador2.grid(row=2, column=2, pady=2)
        self.labelTurno.grid(row=2, column=0, pady=2)
        self.btnJogo.grid(row=3, column=0, pady=6)
        self.inputJogador1.grid(row=3, column=1, pady=6)
        self.inputJogador2.grid(row=3, column=2, pady=6)
    
    def iniciarJogo(self):
        self.labelRodada.configure(fg="#000")
        self.labelJogador1.configure(fg="#000")
        self.labelJogador2.configure(fg="#000")
        self.labelTurno.configure(fg="#000")
        
    def pararJogo(self):
        self.labelRodada.configure(fg="#BFBFBF")
        self.labelJogador1.configure(fg="#BFBFBF")
        self.labelJogador2.configure(fg="#BFBFBF")
        self.labelTurno.configure(fg="#BFBFBF")