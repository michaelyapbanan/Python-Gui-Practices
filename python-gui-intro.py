from tkinter import *

root = Tk()

myLabela = Label(root, text="Hello World!")
myLabelb = Label(root, text="Good Bye World!")
myLabela.grid(row=0, column=0)
myLabelb.grid(row=1, column=0)
# myLabela.pack()

root.mainloop()
