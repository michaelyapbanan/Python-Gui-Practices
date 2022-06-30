from tkinter import *

root = Tk()
root.title('Learn how to do Python GUI Frames')
root.geometry("400x400")

vertical = Scale(root, from_=0, to=200)
vertical.pack()
horizontal = Scale(root, from_=0, to=400, orient=HORIZONTAL)
horizontal.pack()

label = Label(root, text=horizontal.get()).pack()

# def slide():
#     label = Label(root, text=horizontal.get()).pack()
#     root.geometry(str(horizontal.get()) + str(verical.get()))


# b = Button(root, text="Click me!", command=slide).pack() 
root.mainloop()