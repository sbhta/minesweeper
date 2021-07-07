import tkinter, time
from random import choice

master = tkinter.Tk()
master.geometry("600x650")

spots = []


def press(spot, button):
    if spot.state == 0:
        spot.clicked()
        button.grid_forget()
    if spot.state == 1:
        spot.clicked()
        button.grid_forget()

class Spot:
    def __init__(self, posX, posY, state):
        self.x, self.y = posX, posY
        self.state = state
        self.b_num = 0
        self.button = tkinter.Button(master, command=lambda: press(self, self.button), height=1, width=2)
        self.button.size()

        

    def clicked(self):
        tkinter.Label(master, text=self.b_num).grid(column=self.x, row=self.y)
    def renew(self):
        try:
            if spots[self.y][self.x - 1].state == 1: self.b_num += 1
            elif spots[self.y][self.x - 1].state == 0:
                spots[self.y][self.x - 1].button.grid_forget();spots[self.y][self.x - 1].clicked()
        except:
            pass
        try:
            if spots[self.y][self.x + 1].state == 1: self.b_num += 1
            elif spots[self.y][self.x + 1].state == 0:
                spots[self.y][self.x + 1].button.grid_forget();spots[self.y][self.x - 1].clicked()
        except:
            pass
        try:
            if spots[self.y - 1][self.x].state == 1: self.b_num += 1
            elif spots[self.y-1][self.x].state == 0:
                spots[self.y-1][self.x].button.grid_forget();spots[self.y][self.x - 1].clicked()
        except:
            pass
        try:
            if spots[self.y + 1][self.x].state == 1: self.b_num += 1
            elif spots[self.y+1][self.x].state == 0:
                spots[self.y+1][self.x].button.grid_forget();spots[self.y][self.x - 1].clicked()
        except:
            pass
        try:
            if spots[self.y + 1][self.x - 1].state == 1: self.b_num += 1
        except:
            pass
        try:
            if spots[self.y + 1][self.x + 1].state == 1: self.b_num += 1
        except:
            pass
        try:
            if spots[self.y - 1][self.x - 1].state == 1: self.b_num += 1
        except:
            pass
        try:
            if spots[self.y - 1][self.x + 1].state == 1: self.b_num += 1
        except:
            pass


for y in range(25):
    a = []
    for x in range(25):
        a.append(Spot(x, y, 0))
        a[-1].button.grid(row=y, column=x)
    spots.append(a)

for i in range(25*5):
    choice(choice(spots)).state = 1
for i in spots:
    for j in i:
        j.renew()
master.mainloop()
