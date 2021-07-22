from tkinter import *

root = Tk()

image0 = PhotoImage(file="images/empty-block.png")
image1 = PhotoImage(file="images/0.png")
a = [image0, image1]
b = Button(root, image=a[1])
b.pack()
root.mainloop()