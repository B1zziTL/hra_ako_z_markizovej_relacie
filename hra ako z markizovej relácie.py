#vlozenie modulov
import tkinter
import random
import keyboard

#vytvorenie platna
canvas = tkinter.Canvas(width=500, height=700, background="white")
canvas.pack()

#zadefinovanie zoznamu a slovnika
zoznam_slov = ["python","mys","displej","mobil","kniha"]
hadanka = {}

#nahodny vyber slova
slovo = random.choice(zoznam_slov)

for pismeno in slovo: #cyklus na zapisanie pismena ako *
    hadanka[pismeno] = "*"

#zadefinovanie x,y suradnic
x = random.randint(70,420)
y = 0
def padam(): #funkcia na padajuce slovo
    #zadefinovanie globalnych premennych
    global slovo, x, y

    #zmazanie platna
    canvas.delete("all")

    for i in hadanka.keys(): #cyklus na zaznamenanie stlacenych pismen
        if keyboard.is_pressed(i):
            hadanka[i] = i

    #vytvorenie noveho slova a jeho vypisanie
    nove_slovo = ' '.join(hadanka.values())
    canvas.create_text(x,y,text=nove_slovo,font="Arial 30")

    if not "*" in hadanka.values(): #podmienka na uspesne ukoncenie
        return

    #zmena suradnice
    y += 10

    if y > 700: #podmienka na neuspesne ukoncenie
        return koniec()

    #opakovanie
    canvas.after(100,padam)

def koniec(): #funkcia na ukoncenie
    canvas.delete("all")
    canvas.create_text(250,350,text="Loser!",font="Arial 100",fill="red")

#spustenie funkcie
padam()
