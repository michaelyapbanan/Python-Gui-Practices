from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image

root = Tk()
root.title("File Dialogue example")
def open():
    root.filename = filedialog.askopenfile(initialdir=r"C:\Users\banan\Pictures\Saved Pictures", title="Select a file", filetypes=(("png files", "*.png"), ("all files", "*")))
    my_img = ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label = Label(image=my_img).pack()

b = Button(root, text="Open File", command=open).pack()

root.mainloop()