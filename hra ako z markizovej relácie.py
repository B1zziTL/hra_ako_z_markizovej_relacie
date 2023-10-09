import tkinter
import random
import keyboard

canvas = tkinter.Canvas(width=500, height=700, background="white")
canvas.pack()

hviezdicky = 0
zoznam_slov = ["python","mys","displej","mobil","kniha"]
hadanka = {}

slovo = random.choice(zoznam_slov)

for pismeno in slovo:
    hadanka[pismeno] = "*"


x = random.randint(70,420)
y = 0
def padam():
    global slovo, x, y

    canvas.delete("all")

    for i in hadanka.keys():
        if keyboard.is_pressed(i):
            hadanka[i] = i

    nove_slovo = ' '.join(hadanka.values())
    canvas.create_text(x,y,text=nove_slovo,font="Arial 30")

    if not "*" in hadanka.values():
        return

    y += 10

    if y > 700:
        return koniec()
    
    canvas.after(100,padam)

def koniec():
    canvas.delete("all")
    canvas.create_text(250,350,text="Loser!",font="Arial 100",fill="red")
    
padam()

