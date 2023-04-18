import re
import tkinter as tk
from time import strftime


def tic():
    rel['text'] = strftime('%H:%M:%S')


def tac():
    tic()
    rel.after(1000, tac)


rel = tk.Tk()
rel.title("Relógio")
rel = tk.Label()

rel['font'] = 'Roboto 100 bold'
rel.pack()
tac()

rel.mainloop()
