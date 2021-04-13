#!python3
import tkinter as tk 
from tkinter import *
from tkinter import ttk

window = tk.Tk()
window.title("T-Town Veterinary Clinic Database")

dogphoto = PhotoImage(file="dog.png")
lable7 = tk.Label(window, image=dogphoto, borderwidth=3)

button1 = tk.Button(window,text="Search by Name")
entry1 = tk.Entry(window,text="Entry widgets can be typed in", width=15)

lable1 = tk.Label(window, text="Clinic Database")

lable2 = tk.Label(window, text="Name")
lable3 = tk.Label(window, text="Type")
lable4 = tk.Label(window, text="Breed")
lable5 = tk.Label(window, text="Owner")
lable6 = tk.Label(window, text="Birthdate")

entry2 = tk.Entry(window,text="Entry widgets can be typed in", width=10)
entry3 = tk.Entry(window,text="Entry widgets can be typed in", width=10)
entry4 = tk.Entry(window,text="Entry widgets can be typed in", width=10)
entry5 = tk.Entry(window,text="Entry widgets can be typed in", width=10)
entry6 = tk.Entry(window,text="Entry widgets can be typed in", width=10)

button2 = tk.Button(window,text="Previous", width=8)
button3 = tk.Button(window,text="Save Entry", width=8)
button4 = tk.Button(window,text="Next", width=8)
###############################################################################
lable7.grid(row = 1, column = 1, rowspan = 2)

button1.grid(row = 1, column = 4)
entry1.grid(row = 1, column = 5)

lable1.grid(row = 2, column = 3)

lable2.grid(row = 3, column = 1)
lable3.grid(row = 3, column = 2)
lable4.grid(row = 3, column = 3)
lable5.grid(row = 3, column = 4)
lable6.grid(row = 3, column = 5)

entry2.grid(row = 4, column = 1)
entry3.grid(row = 4, column = 2)
entry4.grid(row = 4, column = 3)
entry5.grid(row = 4, column = 4)
entry6.grid(row = 4, column = 5)

button2.grid(row = 5, column = 1)
button3.grid(row = 5, column = 3)
button4.grid(row = 5, column = 5)


window.mainloop()