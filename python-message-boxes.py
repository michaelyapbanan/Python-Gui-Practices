from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Icons, Images, Exit Buttons")

# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno

def popup():
    # showinfo(titlebar, message)
    response = messagebox.askyesno("This is my popup!", "Hello World!")
    if (response ==1):
        Label(root, text="You said yes!").pack()
    else:
        Label(root, text="You said no!").pack()
    
    
Button(root, text="Popup", command=popup).pack()


root.mainloop()