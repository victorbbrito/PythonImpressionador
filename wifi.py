from cProfile import label
import tkinter as tk
import pyautogui as pg

for i in range(100):
    pg.hotkey('win','r')
    pg.write('explorer')
    pg.hotkey('enter')



root = tk.Tk()
canvas1 = tk.Canvas(root, width=200, height=200)
canvas1.pack()

root.title('Status')
label1 = tk.Label(root, text='Feito!', fg='black',
                  font=('helvetica', 12, 'bold'))
canvas1.create_window(100, 100, window=label1)

root.mainloop()
