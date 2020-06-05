from tkinter import *
from tkinter import messagebox


def plansza():
    global warcaby
    warcaby = Frame(okno)
    warcaby.pack()
    global przycisk
    global napis
    przycisk = [[0 for x in range(8)] for y in range(8)]
    napis = [[0 for x in range(8)] for y in range(8)]
    kolor = "black"
    for x in range(8):
        if kolor == "white":
            kolor = "black"
        else:
            kolor = "white"
        for y in range(8):
            napis[x][y] = StringVar()
            napis[x][y].set("")
            przycisk[x][y] = Button(warcaby, height=3, width=6, bg=kolor, fg="white",
                                    textvariable=napis[x][y], command=action)
            przycisk[x][y].grid(row=x, column=y)
            if kolor == "white":
                kolor = "black"
            else:
                if x < 3:
                    napis[x][y].set("B")
                if x > 4:
                    napis[x][y].set("C")
                kolor = "white"


            reset = Button(warcaby, text="Reset", command=reset1)
            reset.grid(row=8, columnspan=8)

def reset1():
    global wcisniety
    warcaby.destroy()
    wcisniety = False
    gracz.set('Tura gracza 1')
    plansza()

def action():
    global wcisnietyX, wcisnietyY
    global wcisniety
    global poprzedniX, poprzedniY
    global gracz

    if wcisniety == False:
        if(gracz.get()=='Tura gracza 2'):
            # wybranie pionka C
            if napis[wcisnietyX][wcisnietyY].get() == "C":
                napis[wcisnietyX][wcisnietyY].set("[C]")
                poprzedniX = wcisnietyX
                poprzedniY = wcisnietyY
                wcisniety = True
            # wybranie pionka Cd
            elif napis[wcisnietyX][wcisnietyY].get() == "Cd":
                napis[wcisnietyX][wcisnietyY].set("[Cd]")
                poprzedniX = wcisnietyX
                poprzedniY = wcisnietyY
                wcisniety = True
            else:
                messagebox.showerror(title="Zły wybór", message="Ruch gracza 2")

        if(gracz.get()=='Tura gracza 1'):
            # wybranie pionka B
            if napis[wcisnietyX][wcisnietyY].get() == "B":
                napis[wcisnietyX][wcisnietyY].set("[B]")
                poprzedniX = wcisnietyX
                poprzedniY = wcisnietyY
                wcisniety = True
            # wybranie pionka Bd
            elif napis[wcisnietyX][wcisnietyY].get() == "Bd":
                napis[wcisnietyX][wcisnietyY].set("[Bd]")
                poprzedniX = wcisnietyX
                poprzedniY = wcisnietyY
                wcisniety = True
            else:
                messagebox.showerror(title="Zły wybór", message="Ruch gracza 1")
    else:
        #przełączanie między pionkami 2 gracza
        if napis[poprzedniX][poprzedniY].get() == "[C]":
            if napis[wcisnietyX][wcisnietyY].get() == "C":
                napis[wcisnietyX][wcisnietyY].set("[C]")
                napis[poprzedniX][poprzedniY].set("C")
                poprzedniX = wcisnietyX
                poprzedniY = wcisnietyY
            if napis[wcisnietyX][wcisnietyY].get() == "Cd":
                napis[wcisnietyX][wcisnietyY].set("[Cd]")
                napis[poprzedniX][poprzedniY].set("C")
                poprzedniX = wcisnietyX
                poprzedniY = wcisnietyY
            if (napis[wcisnietyX][wcisnietyY].get() == "B") or (napis[wcisnietyX][wcisnietyY].get() == "Bd"):
                messagebox.showerror(title="Zły ruch", message="Niedozwolony ruch")
        if napis[poprzedniX][poprzedniY].get() == "[Cd]":
            if napis[wcisnietyX][wcisnietyY].get() == "C":
                napis[wcisnietyX][wcisnietyY].set("[C]")
                napis[poprzedniX][poprzedniY].set("Cd")
                poprzedniX = wcisnietyX
                poprzedniY = wcisnietyY
            if napis[wcisnietyX][wcisnietyY].get() == "Cd":
                napis[wcisnietyX][wcisnietyY].set("[Cd]")
                napis[poprzedniX][poprzedniY].set("Cd")
                poprzedniX = wcisnietyX
                poprzedniY = wcisnietyY
            if (napis[wcisnietyX][wcisnietyY].get() == "B") or (napis[wcisnietyX][wcisnietyY].get() == "Bd"):
                messagebox.showerror(title="Zły ruch", message="Niedozwolony ruch")

        # przełączanie między pionkami pierwszego gracza
        if napis[poprzedniX][poprzedniY].get() == "[B]":
            if napis[wcisnietyX][wcisnietyY].get() == "B":
                napis[wcisnietyX][wcisnietyY].set("[B]")
                napis[poprzedniX][poprzedniY].set("B")
                poprzedniX = wcisnietyX
                poprzedniY = wcisnietyY
            elif napis[wcisnietyX][wcisnietyY].get() == "Bd":
                napis[wcisnietyX][wcisnietyY].set("[Bd]")
                napis[poprzedniX][poprzedniY].set("B")
                poprzedniX = wcisnietyX
                poprzedniY = wcisnietyY
            if (napis[wcisnietyX][wcisnietyY].get() == "C") or (napis[wcisnietyX][wcisnietyY].get() == "Cd"):
                messagebox.showerror(title="Zły ruch", message="Niedozwolony ruch")
        if napis[poprzedniX][poprzedniY].get() == "[Bd]":
            if napis[wcisnietyX][wcisnietyY].get() == "B":
                napis[wcisnietyX][wcisnietyY].set("[B]")
                napis[poprzedniX][poprzedniY].set("Bd")
                poprzedniX = wcisnietyX
                poprzedniY = wcisnietyY
            if napis[wcisnietyX][wcisnietyY].get() == "Bd":
                napis[wcisnietyX][wcisnietyY].set("[Bd]")
                napis[poprzedniX][poprzedniY].set("Bd")
                poprzedniX = wcisnietyX
                poprzedniY = wcisnietyY
            if (napis[wcisnietyX][wcisnietyY].get() == "C")or(napis[wcisnietyX][wcisnietyY].get() == "Cd"):
                messagebox.showerror(title="Zły ruch", message="Niedozwolony ruch")

        # Po wybraniu pionka B
        if napis[poprzedniX][poprzedniY].get() == "[B]":
            if (przycisk[wcisnietyX][wcisnietyY]["background"] == "black"):
                if napis[wcisnietyX][wcisnietyY].get() == "":
                    # Przesunięcie pionka o jedno pole
                    if (wcisnietyX == poprzedniX + 1) and (wcisnietyY == poprzedniY + 1 or wcisnietyY == poprzedniY - 1):
                        if napis[wcisnietyX][wcisnietyY].get() == "":
                            # zamiana pionka B na Bd
                            if wcisnietyX == 7:
                                napis[wcisnietyX][wcisnietyY].set("Bd")
                                napis[poprzedniX][poprzedniY].set("")
                                poprzedniX = wcisnietyX
                                poprzedniY = wcisnietyY
                                wcisniety = False
                                gracz.set('Tura gracza 2')
                            # pionek B
                            else:
                                napis[wcisnietyX][wcisnietyY].set("B")
                                napis[poprzedniX][poprzedniY].set("")
                                poprzedniX = wcisnietyX
                                poprzedniY = wcisnietyY
                                wcisniety = False
                                gracz.set('Tura gracza 2')
                    # Pojedyńcze bicie pionkiem
                    elif (wcisnietyX == poprzedniX + 2) and (wcisnietyY == poprzedniY + 2 or wcisnietyY == poprzedniY - 2):
                        if (wcisnietyY == poprzedniY + 2):
                            if (napis[wcisnietyX - 1][wcisnietyY - 1].get() == "C")or(napis[wcisnietyX - 1][wcisnietyY - 1].get() == "Cd"):
                                # zamiana pionka B na Bd
                                if wcisnietyX == 7:
                                    napis[wcisnietyX][wcisnietyY].set("Bd")
                                    napis[poprzedniX][poprzedniY].set("")
                                    napis[wcisnietyX - 1][wcisnietyY - 1].set("")
                                    poprzedniX = wcisnietyX
                                    poprzedniY = wcisnietyY
                                    wcisniety = False
                                    gracz.set('Tura gracza 2')
                                # pionek B
                                else:
                                    napis[wcisnietyX][wcisnietyY].set("B")
                                    napis[poprzedniX][poprzedniY].set("")
                                    napis[wcisnietyX - 1][wcisnietyY - 1].set("")
                                    poprzedniX = wcisnietyX
                                    poprzedniY = wcisnietyY
                                    wcisniety = False
                                    # sprawdzam czy możliwe jest kolejne bicie
                                    if wcisnietyX < 6:
                                        if poprzedniY < 2:
                                            if (napis[poprzedniX + 1][poprzedniY + 1].get() == "C") or (
                                                    napis[poprzedniX + 1][poprzedniY + 1].get() == "Cd"):
                                                if napis[poprzedniX + 2][poprzedniY + 2].get() == "":
                                                    gracz.set('Tura gracza 1')
                                                else:
                                                    gracz.set('Tura gracza 2')
                                        elif poprzedniY > 6:
                                            if (napis[poprzedniX + 1][poprzedniY - 1].get() == "C") or (
                                                    napis[poprzedniX + 1][poprzedniY - 1].get() == "Cd"):
                                                if napis[poprzedniX + 2][poprzedniY - 2].get() == "":
                                                    gracz.set('Tura gracza 1')
                                                else:
                                                    gracz.set('Tura gracza 2')
                                        else:
                                            if (napis[poprzedniX + 1][poprzedniY + 1].get() == "C") or (
                                                    napis[poprzedniX + 1][poprzedniY + 1].get() == "Cd"):
                                                if napis[poprzedniX + 2][poprzedniY + 2].get() == "":
                                                    gracz.set('Tura gracza 1')
                                                else:
                                                    gracz.set('Tura gracza 2')
                                            if (napis[poprzedniX + 1][poprzedniY - 1].get() == "C") or (
                                                    napis[poprzedniX + 1][poprzedniY - 1].get() == "Cd"):
                                                if napis[poprzedniX + 2][poprzedniY - 2].get() == "":
                                                    gracz.set('Tura gracza 1')
                                                else:
                                                    gracz.set('Tura gracza 2')
                                            else:
                                                gracz.set('Tura gracza 2')
                                    else:
                                        gracz.set('Tura gracza 2')

                        elif (wcisnietyY == poprzedniY - 2):
                            if (napis[wcisnietyX - 1][wcisnietyY + 1].get() == "C")or(napis[wcisnietyX - 1][wcisnietyY + 1].get() == "Cd"):
                                # zamiana pionka B na Bd
                                if wcisnietyX == 7:
                                    napis[wcisnietyX][wcisnietyY].set("Bd")
                                    napis[poprzedniX][poprzedniY].set("")
                                    napis[wcisnietyX - 1][wcisnietyY + 1].set("")
                                    poprzedniX = wcisnietyX
                                    poprzedniY = wcisnietyY
                                    wcisniety = False
                                    gracz.set('Tura gracza 2')
                                    # pionek B
                                else:
                                    napis[wcisnietyX][wcisnietyY].set("B")
                                    napis[poprzedniX][poprzedniY].set("")
                                    napis[wcisnietyX - 1][wcisnietyY + 1].set("")
                                    poprzedniX = wcisnietyX
                                    poprzedniY = wcisnietyY
                                    wcisniety = False
                                    # sprawdzam czy możliwe jest kolejne bicie
                                    if poprzedniX < 6:
                                        if poprzedniY < 2:
                                            if (napis[poprzedniX + 1][poprzedniY + 1].get() == "C") or (
                                                    napis[poprzedniX + 1][poprzedniY + 1].get() == "Cd"):
                                                if napis[poprzedniX + 2][poprzedniY + 2].get() == "":
                                                    gracz.set('Tura gracza 1')
                                                else:
                                                    gracz.set('Tura gracza 2')
                                        elif poprzedniY > 6:
                                            if (napis[poprzedniX + 1][poprzedniY - 1].get() == "C") or (
                                                    napis[poprzedniX + 1][poprzedniY - 1].get() == "Cd"):
                                                if napis[poprzedniX + 2][poprzedniY - 2].get() == "":
                                                    gracz.set('Tura gracza 1')
                                                else:
                                                    gracz.set('Tura gracza 2')
                                        else:
                                            if (napis[poprzedniX + 1][poprzedniY + 1].get() == "C") or (
                                                    napis[poprzedniX + 1][poprzedniY + 1].get() == "Cd"):
                                                if napis[poprzedniX + 2][poprzedniY + 2].get() == "":
                                                    gracz.set('Tura gracza 1')
                                                else:
                                                    gracz.set('Tura gracza 2')
                                            if (napis[poprzedniX + 1][poprzedniY - 1].get() == "C") or (
                                                    napis[poprzedniX + 1][poprzedniY - 1].get() == "Cd"):
                                                if napis[poprzedniX + 2][poprzedniY - 2].get() == "":
                                                    gracz.set('Tura gracza 1')
                                                else:
                                                    gracz.set('Tura gracza 2')
                                            else:
                                                gracz.set('Tura gracza 2')
                                    else:
                                        gracz.set('Tura gracza 2')
                        else:
                            messagebox.showerror(title="Zły ruch", message="Niedozwolony ruch")
                    else:
                        messagebox.showerror(title="Zły ruch", message="Niedozwolony ruch")
            else:
                messagebox.showerror(title="Zły ruch", message="Niedozwolony ruch")

        # Po wybraniu pionka C
        if napis[poprzedniX][poprzedniY].get() == "[C]":
            if (przycisk[wcisnietyX][wcisnietyY]["background"] == "black"):
                if napis[wcisnietyX][wcisnietyY].get() == "":
                    # Przesunięcie pionka o jedno pole
                    if (wcisnietyX == poprzedniX - 1) and (wcisnietyY == poprzedniY + 1 or wcisnietyY == poprzedniY - 1):
                        if napis[wcisnietyX][wcisnietyY].get() == "":
                            # zamiana C na Cd
                            if wcisnietyX == 0:
                                napis[wcisnietyX][wcisnietyY].set("Cd")
                                napis[poprzedniX][poprzedniY].set("")
                                poprzedniX = wcisnietyX
                                poprzedniY = wcisnietyY
                                wcisniety = False
                                gracz.set('Tura gracza 1')
                            # pionek C
                            else:
                                napis[wcisnietyX][wcisnietyY].set("C")
                                napis[poprzedniX][poprzedniY].set("")
                                poprzedniX = wcisnietyX
                                poprzedniY = wcisnietyY
                                wcisniety = False
                                gracz.set('Tura gracza 1')
                    # Pojedyńcze bicie pionkiem
                    elif (wcisnietyX == poprzedniX - 2) and (wcisnietyY == poprzedniY + 2 or wcisnietyY == poprzedniY - 2):
                        if (wcisnietyY == poprzedniY + 2):
                            if (napis[wcisnietyX + 1][wcisnietyY - 1].get() == "B")or(napis[wcisnietyX + 1][wcisnietyY - 1].get() == "Bd"):
                                # zamiana C na Cd
                                if wcisnietyX == 0:
                                    napis[wcisnietyX][wcisnietyY].set("Cd")
                                    napis[poprzedniX][poprzedniY].set("")
                                    napis[wcisnietyX + 1][wcisnietyY - 1].set("")
                                    poprzedniX = wcisnietyX
                                    poprzedniY = wcisnietyY
                                    wcisniety = False
                                    gracz.set('Tura gracza 1')
                                # pionek C
                                else:
                                    napis[wcisnietyX][wcisnietyY].set("C")
                                    napis[poprzedniX][poprzedniY].set("")
                                    napis[wcisnietyX + 1][wcisnietyY - 1].set("")
                                    poprzedniX = wcisnietyX
                                    poprzedniY = wcisnietyY
                                    wcisniety = False
                                    # sprawdzam czy możliwe jest kolejne bicie
                                    if poprzedniX > 1:
                                        if poprzedniY < 2:
                                            if (napis[poprzedniX - 1][poprzedniY + 1].get() == "B") or (
                                                    napis[poprzedniX - 1][poprzedniY + 1].get() == "Bd"):
                                                if napis[poprzedniX - 2][poprzedniY + 2].get() == "":
                                                    gracz.set('Tura gracza 2')
                                                else:
                                                    gracz.set('Tura gracza 1')
                                        elif poprzedniY > 6:
                                            if (napis[poprzedniX - 1][poprzedniY - 1].get() == "B") or (
                                                    napis[poprzedniX - 1][poprzedniY - 1].get() == "Bd"):
                                                if napis[poprzedniX - 2][poprzedniY - 2].get() == "":
                                                    gracz.set('Tura gracza 2')
                                                else:
                                                    gracz.set('Tura gracza 1')
                                        else:
                                            if (napis[poprzedniX - 1][poprzedniY + 1].get() == "B") or (
                                                    napis[poprzedniX - 1][poprzedniY + 1].get() == "Bd"):
                                                if napis[poprzedniX - 2][poprzedniY + 2].get() == "":
                                                    gracz.set('Tura gracza 2')
                                                else:
                                                    gracz.set('Tura gracza 1')
                                            if (napis[poprzedniX - 1][poprzedniY - 1].get() == "B") or (
                                                    napis[poprzedniX - 1][poprzedniY - 1].get() == "Bd"):
                                                if napis[poprzedniX - 2][poprzedniY - 2].get() == "":
                                                    gracz.set('Tura gracza 2')
                                                else:
                                                    gracz.set('Tura gracza 1')
                                            else:
                                                gracz.set('Tura gracza 1')
                                    else:
                                        gracz.set('Tura gracza 1')

                        elif (wcisnietyY == poprzedniY - 2):
                            if (napis[wcisnietyX + 1][wcisnietyY + 1].get() == "B")or(napis[wcisnietyX + 1][wcisnietyY + 1].get() == "Bd"):
                                # zamiana C na Cd
                                if wcisnietyX == 0:
                                    napis[wcisnietyX][wcisnietyY].set("Cd")
                                    napis[poprzedniX][poprzedniY].set("")
                                    napis[wcisnietyX + 1][wcisnietyY + 1].set("")
                                    poprzedniX = wcisnietyX
                                    poprzedniY = wcisnietyY
                                    wcisniety = False
                                    gracz.set('Tura gracza 1')
                                # pionek C
                                else:
                                    napis[wcisnietyX][wcisnietyY].set("C")
                                    napis[poprzedniX][poprzedniY].set("")
                                    napis[wcisnietyX + 1][wcisnietyY + 1].set("")
                                    poprzedniX = wcisnietyX
                                    poprzedniY = wcisnietyY
                                    wcisniety = False
                                    # sprawdzam czy możliwe jest kolejne bicie
                                    if poprzedniX > 1:
                                        if poprzedniY < 2:
                                            if (napis[poprzedniX - 1][poprzedniY + 1].get() == "B") or (
                                                    napis[poprzedniX - 1][poprzedniY + 1].get() == "Bd"):
                                                if napis[poprzedniX - 2][poprzedniY + 2].get() == "":
                                                    gracz.set('Tura gracza 2')
                                                else:
                                                    gracz.set('Tura gracza 1')
                                        elif poprzedniY > 6:
                                            if (napis[poprzedniX - 1][poprzedniY - 1].get() == "B") or (
                                                    napis[poprzedniX - 1][poprzedniY - 1].get() == "Bd"):
                                                if napis[poprzedniX - 2][poprzedniY - 2].get() == "":
                                                    gracz.set('Tura gracza 2')
                                                else:
                                                    gracz.set('Tura gracza 1')
                                        else:
                                            if (napis[poprzedniX - 1][poprzedniY - 1].get() == "B") or (
                                                    napis[poprzedniX - 1][poprzedniY - 1].get() == "Bd"):
                                                if napis[poprzedniX - 2][poprzedniY - 2].get() == "":
                                                    gracz.set('Tura gracza 2')
                                                else:
                                                    gracz.set('Tura gracza 1')
                                            if (napis[poprzedniX - 1][poprzedniY + 1].get() == "B") or (
                                                    napis[poprzedniX - 1][poprzedniY + 1].get() == "Bd"):
                                                if napis[poprzedniX - 2][poprzedniY + 2].get() == "":
                                                    gracz.set('Tura gracza 2')
                                                else:
                                                    gracz.set('Tura gracza 1')
                                            else:
                                                gracz.set('Tura gracza 1')
                                    else:
                                        gracz.set('Tura gracza 1')
                        else:
                            messagebox.showerror(title="Zły ruch", message="Niedozwolony ruch")
                    else:
                        messagebox.showerror(title="Zły ruch", message="Niedozwolony ruch")
            else:
                messagebox.showerror(title="Zły ruch", message="Niedozwolony ruch")

        # Po wybraniu pionka Cd
        if napis[poprzedniX][poprzedniY].get() == "[Cd]":
            if (przycisk[wcisnietyX][wcisnietyY]["background"] == "black"):
                if napis[wcisnietyX][wcisnietyY].get() == "":
                    # Przesunięcie damki o jedno pole
                    if (wcisnietyX == poprzedniX - 1 or wcisnietyX == poprzedniX +1) and (wcisnietyY == poprzedniY + 1 or wcisnietyY == poprzedniY - 1):
                        if napis[wcisnietyX][wcisnietyY].get() == "":
                            napis[wcisnietyX][wcisnietyY].set("Cd")
                            napis[poprzedniX][poprzedniY].set("")
                            poprzedniX = wcisnietyX
                            poprzedniY = wcisnietyY
                            wcisniety = False
                            gracz.set('Tura gracza 1')

                    # Pojedyńcze bicie damką
                    elif (wcisnietyX == poprzedniX - 2 or wcisnietyX == poprzedniX + 2) and (wcisnietyY == poprzedniY + 2 or wcisnietyY == poprzedniY - 2):
                        if (wcisnietyX == poprzedniX + 2)and(wcisnietyY == poprzedniY + 2):
                            if (napis[wcisnietyX - 1][wcisnietyY - 1].get() == "B")or(napis[wcisnietyX - 1][wcisnietyY - 1].get() == "Bd"):
                                napis[wcisnietyX][wcisnietyY].set("Cd")
                                napis[poprzedniX][poprzedniY].set("")
                                napis[wcisnietyX - 1][wcisnietyY - 1].set("")
                                poprzedniX = wcisnietyX
                                poprzedniY = wcisnietyY
                                wcisniety = False
                                gracz.set('Tura gracza 1')
                        elif (wcisnietyX == poprzedniX + 2)and(wcisnietyY == poprzedniY - 2):
                            if (napis[wcisnietyX - 1][wcisnietyY + 1].get() == "B")or(napis[wcisnietyX - 1][wcisnietyY - 1].get() == "Bd"):
                                napis[wcisnietyX][wcisnietyY].set("Cd")
                                napis[poprzedniX][poprzedniY].set("")
                                napis[wcisnietyX - 1][wcisnietyY + 1].set("")
                                poprzedniX = wcisnietyX
                                poprzedniY = wcisnietyY
                                wcisniety = False
                                gracz.set('Tura gracza 1')
                        elif (wcisnietyX == poprzedniX - 2)and(wcisnietyY == poprzedniY - 2):
                            if (napis[wcisnietyX + 1][wcisnietyY + 1].get() == "B")or(napis[wcisnietyX - 1][wcisnietyY - 1].get() == "Bd"):
                                napis[wcisnietyX][wcisnietyY].set("Cd")
                                napis[poprzedniX][poprzedniY].set("")
                                napis[wcisnietyX + 1][wcisnietyY + 1].set("")
                                poprzedniX = wcisnietyX
                                poprzedniY = wcisnietyY
                                wcisniety = False
                                gracz.set('Tura gracza 1')
                        elif (wcisnietyX == poprzedniX - 2)and(wcisnietyY == poprzedniY + 2):
                            if (napis[wcisnietyX + 1][wcisnietyY - 1].get() == "B")or(napis[wcisnietyX - 1][wcisnietyY - 1].get() == "Bd"):
                                napis[wcisnietyX][wcisnietyY].set("Cd")
                                napis[poprzedniX][poprzedniY].set("")
                                napis[wcisnietyX + 1][wcisnietyY - 1].set("")
                                poprzedniX = wcisnietyX
                                poprzedniY = wcisnietyY
                                wcisniety = False
                                gracz.set('Tura gracza 1')
                        else:
                            messagebox.showerror(title="Zły ruch", message="Niedozwolony ruch")
                    else:
                        messagebox.showerror(title="Zły ruch", message="Niedozwolony ruch")
            else:
                messagebox.showerror(title="Zły ruch", message="Niedozwolony ruch")


        # Po wybraniu pionka Bd
        if napis[poprzedniX][poprzedniY].get() == "[Bd]":
            if (przycisk[wcisnietyX][wcisnietyY]["background"] == "black"):
                if napis[wcisnietyX][wcisnietyY].get() == "":
                    # Przesunięcie damki o jedno pole
                    if (wcisnietyX == poprzedniX - 1 or wcisnietyX == poprzedniX +1) and (wcisnietyY == poprzedniY + 1 or wcisnietyY == poprzedniY - 1):
                        if napis[wcisnietyX][wcisnietyY].get() == "":
                            napis[wcisnietyX][wcisnietyY].set("Bd")
                            napis[poprzedniX][poprzedniY].set("")
                            poprzedniX = wcisnietyX
                            poprzedniY = wcisnietyY
                            wcisniety = False
                            gracz.set('Tura gracza 2')

                    # Pojedyńcze bicie damką
                    elif (wcisnietyX == poprzedniX - 2 or wcisnietyX == poprzedniX + 2) and (wcisnietyY == poprzedniY + 2 or wcisnietyY == poprzedniY - 2):
                        if (wcisnietyX == poprzedniX + 2)and(wcisnietyY == poprzedniY + 2):
                            if (napis[wcisnietyX - 1][wcisnietyY - 1].get() == "C")or(napis[wcisnietyX - 1][wcisnietyY - 1].get() == "Cd"):
                                napis[wcisnietyX][wcisnietyY].set("Bd")
                                napis[poprzedniX][poprzedniY].set("")
                                napis[wcisnietyX - 1][wcisnietyY - 1].set("")
                                poprzedniX = wcisnietyX
                                poprzedniY = wcisnietyY
                                wcisniety = False
                                gracz.set('Tura gracza 2')
                        elif (wcisnietyX == poprzedniX + 2)and(wcisnietyY == poprzedniY - 2):
                            if (napis[wcisnietyX - 1][wcisnietyY + 1].get() == "C")or(napis[wcisnietyX - 1][wcisnietyY - 1].get() == "Cd"):
                                napis[wcisnietyX][wcisnietyY].set("Bd")
                                napis[poprzedniX][poprzedniY].set("")
                                napis[wcisnietyX - 1][wcisnietyY + 1].set("")
                                poprzedniX = wcisnietyX
                                poprzedniY = wcisnietyY
                                wcisniety = False
                                gracz.set('Tura gracza 2')
                        elif (wcisnietyX == poprzedniX - 2)and(wcisnietyY == poprzedniY - 2):
                            if (napis[wcisnietyX + 1][wcisnietyY + 1].get() == "C")or(napis[wcisnietyX - 1][wcisnietyY - 1].get() == "Cd"):
                                napis[wcisnietyX][wcisnietyY].set("Bd")
                                napis[poprzedniX][poprzedniY].set("")
                                napis[wcisnietyX + 1][wcisnietyY + 1].set("")
                                poprzedniX = wcisnietyX
                                poprzedniY = wcisnietyY
                                wcisniety = False
                                gracz.set('Tura gracza 2')
                        elif (wcisnietyX == poprzedniX - 2)and(wcisnietyY == poprzedniY + 2):
                            if (napis[wcisnietyX + 1][wcisnietyY - 1].get() == "C")or(napis[wcisnietyX - 1][wcisnietyY - 1].get() == "Cd"):
                                napis[wcisnietyX][wcisnietyY].set("Bd")
                                napis[poprzedniX][poprzedniY].set("")
                                napis[wcisnietyX + 1][wcisnietyY - 1].set("")
                                poprzedniX = wcisnietyX
                                poprzedniY = wcisnietyY
                                wcisniety = False
                                gracz.set('Tura gracza 2')
                        else:
                            messagebox.showerror(title="Zły ruch", message="Niedozwolony ruch")
                    else:
                        messagebox.showerror(title="Zły ruch", message="Niedozwolony ruch")
            else:
                messagebox.showerror(title="Zły ruch", message="Niedozwolony ruch")

def click(event):
    global wcisnietyX, wcisnietyY
    x = event.x_root - warcaby.winfo_rootx()
    y = event.y_root - warcaby.winfo_rooty()
    wcisnietyY, wcisnietyX = warcaby.grid_location(x, y)


okno = Tk()
okno.title("Warcaby")
wcisniety = False

gracz = StringVar()
gracz.set('Tura gracza 1')
tura = Label(okno, textvariable=gracz)
tura.pack()

okno.bind("<Button-1>", click)
plansza()
okno.mainloop()
