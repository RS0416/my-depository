from tkinter import *
from datetime import date
root= Tk()
root.title("getting started with widgets")
root.geometry("400x300")
# add Label
lbl= Label(text="hey there", fg="white", bg="#072F5F")
# add Label for getting name as input from user
lbl_name= Label(text="full name", bg= "#3895D3")
name_entry= Entry()
def display():
    name= name_entry.get()
    global Message
    Message = "welcome to the application! \nTodays date is :"
    greet="hello"+name+"\n"
    text_box.insert(END, greet)
    text_box.insert(END, Message)
    text_box.insert(END, date.today())
text_box= Text(height=3)
btn= Button(text="begin", command= display , height=1, bg= "#1261a0")
lbl.pack()
lbl.pack()
name_entry.pack()
btn.pack()
text_box.pack()
root.mainloop()