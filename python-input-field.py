from tkinter import *

root = Tk()

# Input box (Entry Widget)
# can change bg, fg, width, borderwidth
entry = Entry(root)
entry.pack()
# insert(index, text placeholder)
entry.insert(0, "Enter your name")


def handleClick():
    myLabel = Label(root, text="Hello " + entry.get())
    myLabel.pack()

myButton = Button(root, text="Enter your name", command=handleClick)
myButton.pack()

root.mainloop()