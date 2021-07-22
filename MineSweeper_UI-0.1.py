import tkinter, sys
from random import choice, randint

master = tkinter.Tk()
master.geometry("780x447")
spots = []
count = 0


def press(spot):
    global count
    if spot.state == 0:
        spot.clicked()
    if spot.state == 1:
        for i in spots:
            for j in i:
                j.button.config(state=tkinter.DISABLED)
                j.button.config(cursor="arrow")
                if j.state == 1:
                    j.button.config(state=tkinter.DISABLED)
                    j.button.config(relief="sunken")
                    j.button.config(text="💣")
        spot.button.config(bg="red")


class Spot:
    def __init__(self, posX, posY, state):
        self.x, self.y = posX, posY
        self.state = state
        self.b_num = 0
        self.button = tkinter.Button(master, command=lambda: press(self), bg="#bdbdbd",bd=3,height=1, width=2, cursor="hand2")
        self.button.size()

    def clicked(self):
        global count
        tkinter.Label(master, text=self.b_num, bg="#bdbdbd").grid(column=self.x, row=self.y)
        self.button.config(state=tkinter.DISABLED)
        self.button.config(relief="sunken")
        self.button.config(bd=4)
        self.button.config(cursor="arrow")
        count += 1
        if count < 50:
            try:
                if spots[self.y][self.x - 1].state == 0 and self.x - 1 != -1: spots[self.y][self.x - 1].clicked()
                if spots[self.y][self.x + 1].state == 0 and self.x + 1 != 31: spots[self.y][self.x + 1].clicked()
                if spots[self.y - 1][self.x].state == 0 and self.y - 1 != -1: spots[self.y - 1][self.x].clicked()
                if spots[self.y + 1][self.x].state == 0 and self.y + 1 != 17: spots[self.y + 1][self.x].clicked()
            except IndexError:
                pass

    def renew(self):
        try:
            if spots[self.y][self.x - 1].state == 1: self.b_num += 1
        except:
            pass
        try:
            if spots[self.y][self.x + 1].state == 1: self.b_num += 1
        except:
            pass
        try:
            if spots[self.y - 1][self.x].state == 1: self.b_num += 1
        except:
            pass
        try:
            if spots[self.y + 1][self.x].state == 1: self.b_num += 1
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


for y in range(16):
    a = []
    for x in range(30):
        a.append(Spot(x, y, 0))
        a[-1].button.grid(row=y, column=x)
    spots.append(a)

for i in range(40):
    choice(choice(spots)).state = 1
for i in spots:
    for j in i:
        j.renew()

master.mainloop()
