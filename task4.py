#!python3
import tkinter as tk 
from tkinter import *
from tkinter import ttk

window = tk.Tk()
window.title("Example")
nF = Frame()

dogphoto = PhotoImage(file="dog.png")
lable1 = tk.Label(window, image=dogphoto, borderwidth=3)

lable2 = tk.Label(window, text="Pochancco!")

lable3 = Label(window,text="A cuddly little puppy! This is from the same\n creators that brought you Keropi and Kero Kero", background="#aaffff")
###############################################################################
lable1.place(x=50,y=10)

lable2.place(x=120,y=60)

lable3.place(x=-1,y=120)





window.mainloop()