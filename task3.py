#!python3
import tkinter as tk 
from tkinter import *
from tkinter import ttk

window = tk.Tk()
window.title("Example")


dogphoto = PhotoImage(file="dog.png")
lable1 = tk.Label(window, image=dogphoto, borderwidth=3)

lable2 = tk.Label(window, text="Pochancco!")


###############################################################################
lable1.grid(row = 1, column = 1)

lable2.grid(row = 1, column = 2)

nF = Frame()
fLabel = Label(nF,text="A cuddly little puppy! This is from the same creators that brought you Keropi and Kero Kero", background="#aaffff")

nF.grid(row = 2, column = 1, columnspan = 2)


window.mainloop()