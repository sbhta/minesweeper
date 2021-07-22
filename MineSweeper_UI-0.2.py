from tkinter import *
from random import randint, choice


# 30x16 size in tiles
root = Tk()
root.geometry("960x512")

# loading all of the textures
empty_block = PhotoImage(file="./images/empty-block.png"); empty_block = empty_block.subsample(1, 1)
unclicked_bomb = PhotoImage(file="./images/unclicked-bomb.png")
clicked_bomb = PhotoImage(file="./images/bomb-at-clicked-block.png")
flag = PhotoImage(file="./images/flag.png")
b0 = PhotoImage(file="./images/0.png")
b1 = PhotoImage(file="./images/1.png")
b2 = PhotoImage(file="./images/2.png")
b3 = PhotoImage(file="./images/3.png")
b4 = PhotoImage(file="./images/4.png")
b5 = PhotoImage(file="./images/5.png")
b6 = PhotoImage(file="./images/6.png")
b7 = PhotoImage(file="./images/7.png")
b8 = PhotoImage(file="./images/8.png")
listOfImages = [b0, b1, b2, b3, b4, b5, b6, b7, b8]

class Tile:
    def __init__(self, x, y, state=0):
        self.x = x
        self.y = y
        self.state = state
        self.neighbors = 0
        self.button = Button(root, image=empty_block, height=26, width=26)


    def listNeighbors(self):
        adj = []
        try:
            if self.x - 1 > 0: adj.append(spots[self.y][self.x - 1])
        except:pass

        try:
            if self.y - 1 > 0:adj.append(spots[self.y - 1][self.x])
        except:pass

        try: adj.append(spots[self.y][self.x + 1])
        except:pass
        try: adj.append(spots[self.y + 1][self.x])
        except:pass

        self.neighbors = len(adj)
            # if spots[self.y][self.x - 1].state == 1: self.neighbors += 1
            # if spots[self.y][self.x + 1].state == 1: self.neighbors += 1
            # if spots[self.y + 1][self.x].state == 1: self.neighbors += 1
            # if spots[self.y - 1][self.x].state == 1: self.neighbors += 1




# global variables
spots = []
max_count = 40


# creating the board and all of the tiles
for y in range(16):
    row = []
    for x in range(30):
        row.append(Tile(x, y))
        row[-1].button.grid(row=y, column=x)
    spots.append(row)
# choosing witch tiles are mines
for i in range(randint(50, 100)):
    choice(choice(spots)).state = 1
for y in spots:
    for x in y:
        if x.state == 0:
            x.listNeighbors()
        if x.state == 1:
            x.button.config(image=unclicked_bomb)
for y in spots:
    for x in y:
        x.button.config(image=listOfImages[x.neighbors])
# mainloop of the game
root.mainloop()
