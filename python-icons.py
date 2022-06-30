from tkinter import *
from PIL import ImageTk, Image

# my_img = ImageTk.PhotoImage(Image.open("meg-november2.png"))
label = Label(image=my_img)
label.pack()

root = Tk()
root.title("Icons, Images, Exit Buttons")

# change icon
# root.iconbitmap('[insert ico file here]')

button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.pack()

root.mainloop()