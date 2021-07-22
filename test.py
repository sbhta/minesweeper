from tkinter import *
#Create an instance of window or frame
win= Tk()
#Set the geometry
win.geometry("700x600")
win.resizable(0,0)
win.config(cursor= "fleur")
#Let us create a text label
Label(win, text= "Hover on each of these buttons", font=('Poppins', 20)).pack(pady=20)

#Create some buttons with cursor property
b1= Button(win, text= "Star",cursor="star")
b1.pack(pady=20)
b2= Button(win, text= "Arrow",cursor="arrow")
b2.pack(pady=20)
b3= Button(win, text= "Circle",cursor="circle")
b3.pack(pady=20)
b4= Button(win, text= "Clock",cursor="clock")
b4.pack(pady=20)
b5= Button(win, text= "Heart",cursor="heart")
b5.pack(pady=20)
b6= Button(win, text= "Man",cursor="man")
b6.pack(pady=20)
b7= Button(win, text= "Mouse",cursor="mouse")
b7.pack(pady=20)

#Keep Running the window

win.mainloop()