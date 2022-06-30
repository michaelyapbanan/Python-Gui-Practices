from tkinter import *

root = Tk()
root.title("Icons, Images, Exit Buttons")

# Second window opens simulataneously
# top = Toplevel()
# label = Label(top, text="Hello World").pack()

def open():
    top = Toplevel()
    label = Label(top, text="You opened a 2nd window").pack()
    b2 = Button(top, text="Close window", command=top.destroy).pack()

button = Button(root, text="Open 2nd Window", command=open).pack()


root.mainloop()