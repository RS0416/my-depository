from tkinter import *
from tkinter import messagebox
root= Tk()
root.geometry('200x200')
def msg():
    messagebox.showwarning("alert", "stop, virus found")

button= Button(text= "scan for virus", command=msg)
button.place(x=20, y=40)
root.mainloop()