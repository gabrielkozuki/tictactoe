import tkinter as tk
import tkinter.font as font
from functools import partial
from tkinter.messagebox import showinfo


class View():
    def __init__(self, controller):
        self.root = tk.Tk()
        self.root.resizable(0, 0)
        self.root.title("Tic Tac Toe")

        self.container = tk.Frame(self.root)
        self.container.grid(row=0, column=0)
        self.controller = controller

        self.tabuleiro = [[], [], []]
        for x in range(3):
            for y in range(3):
                var = tk.StringVar()
                self.tabuleiro[x].append(var)
        
        
        self.nomeJogador1 = tk.StringVar()
        self.nomeJogador2 = tk.StringVar()

        self.inserirTabuleiro()
        self.inserirMenu()
        
    def run(self):
        self.root.mainloop()
    
    def inserirTabuleiro(self):
        frame = tk.Frame(self.container, bg="black")
        frame.grid(row=1, column=0, padx=0, pady=20, ipadx=0, ipady=0)
        
        self.btn00 = tk.Button(frame, textvariable=self.tabuleiro[0][0], width=10, border=0, height=5, font='bold', state="disabled", command=partial(self.controller.jogarRodada, 0, 0))
        self.btn01 = tk.Button(frame, textvariable=self.tabuleiro[0][1], width=10, border=0, height=5, font='bold', state="disabled", command=partial(self.controller.jogarRodada, 0, 1))
        self.btn02 = tk.Button(frame, textvariable=self.tabuleiro[0][2], width=10, border=0, height=5, font='bold', state="disabled", command=partial(self.controller.jogarRodada, 0, 2))
        self.btn10 = tk.Button(frame, textvariable=self.tabuleiro[1][0], width=10, border=0, height=5, font='bold', state="disabled", command=partial(self.controller.jogarRodada, 1, 0))
        self.btn11 = tk.Button(frame, textvariable=self.tabuleiro[1][1], width=10, border=0, height=5, font='bold', state="disabled", command=partial(self.controller.jogarRodada, 1, 1))
        self.btn12 = tk.Button(frame, textvariable=self.tabuleiro[1][2], width=10, border=0, height=5, font='bold', state="disabled", command=partial(self.controller.jogarRodada, 1, 2))
        self.btn20 = tk.Button(frame, textvariable=self.tabuleiro[2][0], width=10, border=0, height=5, font='bold', state="disabled", command=partial(self.controller.jogarRodada, 2, 0))
        self.btn21 = tk.Button(frame, textvariable=self.tabuleiro[2][1], width=10, border=0, height=5, font='bold', state="disabled", command=partial(self.controller.jogarRodada, 2, 1))
        self.btn22 = tk.Button(frame, textvariable=self.tabuleiro[2][2], width=10, border=0, height=5, font='bold', state="disabled", command=partial(self.controller.jogarRodada, 2, 2))
        
        self.btn00.grid(row=1, column=1)
        self.btn01.grid(row=1, column=2)
        self.btn02.grid(row=1, column=3)
        self.btn10.grid(row=2, column=1)
        self.btn11.grid(row=2, column=2, padx=5, pady=5)
        self.btn12.grid(row=2, column=3)
        self.btn20.grid(row=3, column=1)
        self.btn21.grid(row=3, column=2)
        self.btn22.grid(row=3, column=3)
        
    def inserirMenu(self):
        frame = tk.Frame(self.container)
        frame.grid(row=2, column=0, padx=5, pady=5)
        
        self.labelRodada = tk.Label(frame, width=20, text="Rodada:", fg="#BFBFBF")
        self.labelJogador1 = tk.Label(frame, width=20, text="Jogador 1 (X): ", fg="#000")
        self.labelJogador2 = tk.Label(frame, width=20, text="Jogador 2 (O): ", fg="#000")
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
        self.labelTurno.configure(fg="#000")
        
        self.btn00["state"] = tk.NORMAL
        self.btn01["state"] = tk.NORMAL
        self.btn02["state"] = tk.NORMAL
        self.btn10["state"] = tk.NORMAL
        self.btn11["state"] = tk.NORMAL
        self.btn12["state"] = tk.NORMAL
        self.btn20["state"] = tk.NORMAL
        self.btn21["state"] = tk.NORMAL
        self.btn22["state"] = tk.NORMAL

        
    def pararJogo(self):
        self.labelRodada.configure(fg="#BFBFBF")
        self.labelTurno.configure(fg="#BFBFBF")
        
        self.btn00["state"] = tk.DISABLED
        self.btn01["state"] = tk.DISABLED
        self.btn02["state"] = tk.DISABLED
        self.btn10["state"] = tk.DISABLED
        self.btn11["state"] = tk.DISABLED
        self.btn12["state"] = tk.DISABLED
        self.btn20["state"] = tk.DISABLED
        self.btn21["state"] = tk.DISABLED
        self.btn22["state"] = tk.DISABLED
        
    def exibirMensagem(self, msg):
        labelMsg = ""

        if msg == "X":
            labelMsg = self.inputJogador1.get() + " (X) venceu a partida!"
        elif msg == "O":
            labelMsg = self.inputJogador2.get() + " (O) venceu a partida!"
        elif msg == "empate":
            labelMsg = "A partida terminou em empate!"
        
        showinfo(title="Resultado", message=labelMsg)
