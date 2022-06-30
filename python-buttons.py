from tkinter import *

root = Tk()

def handleClick():
    myLabel = Label(root, text="I clicked the button!")
    myLabel.pack()

# Standard button example
# myButton = Button(root, text="click me!")

# Buttons can have states
# myButton = Button(root, text="click me!", state=DISABLED)

# Can also change the size + style it
# myButton = Button(root, text="click me!", padx=50, pady=50)
# (fg="blue") means foreground color (text color)
# (bg="red") means background color

# insert function
myButton = Button(root, text="click me!", command=handleClick)




myButton.pack()

root.mainloop()