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
    global wcisniety, ile_bialych, ile_czarnych, kolejne_bicie
    ile_bialych = 12
    ile_czarnych = 12
    warcaby.destroy()
    wcisniety = False
    kolejne_bicie = False
    gracz.set('Tura gracza 1')
    plansza()


def koniec_gry(zwyciezca):
    messagebox.showinfo(title="Zwycięstwo", message="Wygrał " + zwyciezca)
    reset1()

def kolejne_bicie_Bd():
    global kolejne_bicie, kolejne_bicie_X, kolejne_bicie_Y
    # Sprawdzam czy możliwe jest kolejne bicie
    if wcisnietyX < 2:
        if poprzedniY < 2:
            if (napis[poprzedniX + 1][poprzedniY + 1].get() == "C") or (
                    napis[poprzedniX + 1][poprzedniY + 1].get() == "Cd"):
                if napis[poprzedniX + 2][poprzedniY + 2].get() == "":
                    gracz.set('Tura gracza 1')
                    kolejne_bicie = True
                    kolejne_bicie_X = poprzedniX
                    kolejne_bicie_Y = poprzedniY

        elif poprzedniY > 5:
            if (napis[poprzedniX + 1][poprzedniY - 1].get() == "C") or (
                    napis[poprzedniX + 1][poprzedniY - 1].get() == "Cd"):
                if napis[poprzedniX + 2][poprzedniY - 2].get() == "":
                    gracz.set('Tura gracza 1')
                    kolejne_bicie = True
                    kolejne_bicie_X = poprzedniX
                    kolejne_bicie_Y = poprzedniY

        else:
            if (napis[poprzedniX + 1][poprzedniY + 1].get() == "C" or
                    napis[poprzedniX + 1][poprzedniY + 1].get() == "Cd") and (
                    napis[poprzedniX + 2][poprzedniY + 2].get() == ""):
                gracz.set('Tura gracza 1')
                kolejne_bicie = True
                kolejne_bicie_X = poprzedniX
                kolejne_bicie_Y = poprzedniY

            elif (napis[poprzedniX + 1][poprzedniY - 1].get() == "C" or
                    napis[poprzedniX + 1][poprzedniY - 1].get() == "Cd") and (
                    napis[poprzedniX + 2][poprzedniY - 2].get() == ""):
                gracz.set('Tura gracza 1')
                kolejne_bicie = True
                kolejne_bicie_X = poprzedniX
                kolejne_bicie_Y = poprzedniY

    elif wcisnietyX > 5:
        if poprzedniY < 2:
            if (napis[poprzedniX - 1][poprzedniY + 1].get() == "C") or (
                    napis[poprzedniX - 1][poprzedniY + 1].get() == "Cd"):
                if napis[poprzedniX - 2][poprzedniY + 2].get() == "":
                    gracz.set('Tura gracza 1')
                    kolejne_bicie = True
                    kolejne_bicie_X = poprzedniX
                    kolejne_bicie_Y = poprzedniY

        elif poprzedniY > 5:
            if (napis[poprzedniX - 1][poprzedniY - 1].get() == "C") or (
                    napis[poprzedniX - 1][poprzedniY - 1].get() == "Cd"):
                if napis[poprzedniX - 2][poprzedniY - 2].get() == "":
                    gracz.set('Tura gracza 1')
                    kolejne_bicie = True
                    kolejne_bicie_X = poprzedniX
                    kolejne_bicie_Y = poprzedniY

        else:
            if (napis[poprzedniX - 1][poprzedniY - 1].get() == "C" or
                    napis[poprzedniX - 1][poprzedniY - 1].get() == "Cd") and (
                    napis[poprzedniX - 2][poprzedniY - 2].get() == ""):
                gracz.set('Tura gracza 1')
                kolejne_bicie = True
                kolejne_bicie_X = poprzedniX
                kolejne_bicie_Y = poprzedniY

            elif (napis[poprzedniX - 1][poprzedniY + 1].get() == "C" or
                    napis[poprzedniX - 1][poprzedniY + 1].get() == "Cd") and (
                    napis[poprzedniX - 2][poprzedniY + 2].get() == ""):
                gracz.set('Tura gracza 1')
                kolejne_bicie = True
                kolejne_bicie_X = poprzedniX
                kolejne_bicie_Y = poprzedniY

    else:
        if poprzedniY < 2:
            if (napis[poprzedniX - 1][poprzedniY + 1].get() == "C") or (
                    napis[poprzedniX - 1][poprzedniY + 1].get() == "Cd"):
                if napis[poprzedniX - 2][poprzedniY + 2].get() == "":
                    gracz.set('Tura gracza 1')
                    kolejne_bicie = True
                    kolejne_bicie_X = poprzedniX
                    kolejne_bicie_Y = poprzedniY

            elif (napis[poprzedniX + 1][poprzedniY + 1].get() == "C") or (
                    napis[poprzedniX + 1][poprzedniY + 1].get() == "Cd"):
                if napis[poprzedniX + 2][poprzedniY + 2].get() == "":
                    gracz.set('Tura gracza 1')
                    kolejne_bicie = True
                    kolejne_bicie_X = poprzedniX
                    kolejne_bicie_Y = poprzedniY

        elif poprzedniY > 5:
            if (napis[poprzedniX - 1][poprzedniY - 1].get() == "C") or (
                    napis[poprzedniX - 1][poprzedniY - 1].get() == "Cd"):
                if napis[poprzedniX - 2][poprzedniY - 2].get() == "":
                    gracz.set('Tura gracza 1')
                    kolejne_bicie = True
                    kolejne_bicie_X = poprzedniX
                    kolejne_bicie_Y = poprzedniY

            elif (napis[poprzedniX + 1][poprzedniY - 1].get() == "C") or (
                    napis[poprzedniX + 1][poprzedniY - 1].get() == "Cd"):
                if napis[poprzedniX + 2][poprzedniY - 2].get() == "":
                    gracz.set('Tura gracza 1')
                    kolejne_bicie = True
                    kolejne_bicie_X = poprzedniX
                    kolejne_bicie_Y = poprzedniY

        else:
            if (napis[poprzedniX - 1][poprzedniY - 1].get() == "C" or
                    napis[poprzedniX - 1][poprzedniY - 1].get() == "Cd") and (
                    napis[poprzedniX - 2][poprzedniY - 2].get() == ""):
                gracz.set('Tura gracza 1')
                kolejne_bicie = True
                kolejne_bicie_X = poprzedniX
                kolejne_bicie_Y = poprzedniY

            elif (napis[poprzedniX - 1][poprzedniY + 1].get() == "C" or
                    napis[poprzedniX - 1][poprzedniY + 1].get() == "Cd") and (
                    napis[poprzedniX - 2][poprzedniY + 2].get() == ""):
                gracz.set('Tura gracza 1')
                kolejne_bicie = True
                kolejne_bicie_X = poprzedniX
                kolejne_bicie_Y = poprzedniY

            elif (napis[poprzedniX + 1][poprzedniY + 1].get() == "C" or
                    napis[poprzedniX + 1][poprzedniY + 1].get() == "Cd") and (
                    napis[poprzedniX + 2][poprzedniY + 2].get() == ""):
                gracz.set('Tura gracza 1')
                kolejne_bicie = True
                kolejne_bicie_X = poprzedniX
                kolejne_bicie_Y = poprzedniY

            elif (napis[poprzedniX + 1][poprzedniY - 1].get() == "C" or
                    napis[poprzedniX + 1][poprzedniY - 1].get() == "Cd") and (
                    napis[poprzedniX + 2][poprzedniY - 2].get() == ""):
                gracz.set('Tura gracza 1')
                kolejne_bicie = True
                kolejne_bicie_X = poprzedniX
                kolejne_bicie_Y = poprzedniY


def kolejne_bicie_Cd():
    global kolejne_bicie, kolejne_bicie_X, kolejne_bicie_Y
    # Sprawdzam czy możliwe jest kolejne bicie
    if wcisnietyX < 2:
        if poprzedniY < 2:
            if (napis[poprzedniX + 1][poprzedniY + 1].get() == "B") or (
                    napis[poprzedniX + 1][poprzedniY + 1].get() == "Bd"):
                if napis[poprzedniX + 2][poprzedniY + 2].get() == "":
                    gracz.set('Tura gracza 2')
                    kolejne_bicie = True
                    kolejne_bicie_X = poprzedniX
                    kolejne_bicie_Y = poprzedniY

        elif poprzedniY > 5:
            if (napis[poprzedniX + 1][poprzedniY - 1].get() == "B") or (
                    napis[poprzedniX + 1][poprzedniY - 1].get() == "Bd"):
                if napis[poprzedniX + 2][poprzedniY - 2].get() == "":
                    gracz.set('Tura gracza 2')
                    kolejne_bicie = True
                    kolejne_bicie_X = poprzedniX
                    kolejne_bicie_Y = poprzedniY

        else:
            if (napis[poprzedniX + 1][poprzedniY + 1].get() == "B" or
                    napis[poprzedniX + 1][poprzedniY + 1].get() == "Bd") and (
                    napis[poprzedniX + 2][poprzedniY + 2].get() == ""):
                gracz.set('Tura gracza 2')
                kolejne_bicie = True
                kolejne_bicie_X = poprzedniX
                kolejne_bicie_Y = poprzedniY

            elif (napis[poprzedniX + 1][poprzedniY - 1].get() == "B" or
                    napis[poprzedniX + 1][poprzedniY - 1].get() == "Bd") and (
                    napis[poprzedniX + 2][poprzedniY - 2].get() == ""):
                gracz.set('Tura gracza 2')
                kolejne_bicie = True
                kolejne_bicie_X = poprzedniX
                kolejne_bicie_Y = poprzedniY

    elif wcisnietyX > 5:
        if poprzedniY < 2:
            if (napis[poprzedniX - 1][poprzedniY + 1].get() == "B") or (
                    napis[poprzedniX - 1][poprzedniY + 1].get() == "Bd"):
                if napis[poprzedniX - 2][poprzedniY + 2].get() == "":
                    gracz.set('Tura gracza 2')
                    kolejne_bicie = True
                    kolejne_bicie_X = poprzedniX
                    kolejne_bicie_Y = poprzedniY

        elif poprzedniY > 5:
            if (napis[poprzedniX - 1][poprzedniY - 1].get() == "B") or (
                    napis[poprzedniX - 1][poprzedniY - 1].get() == "Bd"):
                if napis[poprzedniX - 2][poprzedniY - 2].get() == "":
                    gracz.set('Tura gracza 2')
                    kolejne_bicie = True
                    kolejne_bicie_X = poprzedniX
                    kolejne_bicie_Y = poprzedniY

        else:
            if (napis[poprzedniX - 1][poprzedniY - 1].get() == "B" or
                    napis[poprzedniX - 1][poprzedniY - 1].get() == "Bd") and (
                    napis[poprzedniX - 2][poprzedniY - 2].get() == ""):
                gracz.set('Tura gracza 2')
                kolejne_bicie = True
                kolejne_bicie_X = poprzedniX
                kolejne_bicie_Y = poprzedniY

            elif (napis[poprzedniX - 1][poprzedniY + 1].get() == "B" or
                    napis[poprzedniX - 1][poprzedniY + 1].get() == "Bd") and (
                    napis[poprzedniX - 2][poprzedniY + 2].get() == ""):
                gracz.set('Tura gracza 2')
                kolejne_bicie = True
                kolejne_bicie_X = poprzedniX
                kolejne_bicie_Y = poprzedniY

    else:
        if poprzedniY < 2:
            if (napis[poprzedniX - 1][poprzedniY + 1].get() == "B") or (
                    napis[poprzedniX - 1][poprzedniY + 1].get() == "Bd"):
                if napis[poprzedniX - 2][poprzedniY + 2].get() == "":
                    gracz.set('Tura gracza 2')
                    kolejne_bicie = True
                    kolejne_bicie_X = poprzedniX
                    kolejne_bicie_Y = poprzedniY

            elif (napis[poprzedniX + 1][poprzedniY + 1].get() == "B") or (
                    napis[poprzedniX + 1][poprzedniY + 1].get() == "Bd"):
                if napis[poprzedniX + 2][poprzedniY + 2].get() == "":
                    gracz.set('Tura gracza 2')
                    kolejne_bicie = True
                    kolejne_bicie_X = poprzedniX
                    kolejne_bicie_Y = poprzedniY

        elif poprzedniY > 5:
            if (napis[poprzedniX - 1][poprzedniY - 1].get() == "B") or (
                    napis[poprzedniX - 1][poprzedniY - 1].get() == "Bd"):
                if napis[poprzedniX - 2][poprzedniY - 2].get() == "":
                    gracz.set('Tura gracza 2')
                    kolejne_bicie = True
                    kolejne_bicie_X = poprzedniX
                    kolejne_bicie_Y = poprzedniY

            elif (napis[poprzedniX + 1][poprzedniY - 1].get() == "B") or (
                    napis[poprzedniX + 1][poprzedniY - 1].get() == "Bd"):
                if napis[poprzedniX + 2][poprzedniY - 2].get() == "":
                    gracz.set('Tura gracza 2')
                    kolejne_bicie = True
                    kolejne_bicie_X = poprzedniX
                    kolejne_bicie_Y = poprzedniY

        else:
            if (napis[poprzedniX - 1][poprzedniY - 1].get() == "B" or
                    napis[poprzedniX - 1][poprzedniY - 1].get() == "Bd") and (
                    napis[poprzedniX - 2][poprzedniY - 2].get() == ""):
                gracz.set('Tura gracza 2')
                kolejne_bicie = True
                kolejne_bicie_X = poprzedniX
                kolejne_bicie_Y = poprzedniY

            elif (napis[poprzedniX - 1][poprzedniY + 1].get() == "B" or
                    napis[poprzedniX - 1][poprzedniY + 1].get() == "Bd") and (
                    napis[poprzedniX - 2][poprzedniY + 2].get() == ""):
                gracz.set('Tura gracza 2')
                kolejne_bicie = True
                kolejne_bicie_X = poprzedniX
                kolejne_bicie_Y = poprzedniY

            elif (napis[poprzedniX + 1][poprzedniY + 1].get() == "B" or
                    napis[poprzedniX + 1][poprzedniY + 1].get() == "Bd") and (
                    napis[poprzedniX + 2][poprzedniY + 2].get() == ""):
                gracz.set('Tura gracza 2')
                kolejne_bicie = True
                kolejne_bicie_X = poprzedniX
                kolejne_bicie_Y = poprzedniY

            elif (napis[poprzedniX + 1][poprzedniY - 1].get() == "B" or
                    napis[poprzedniX + 1][poprzedniY - 1].get() == "Bd") and (
                    napis[poprzedniX + 2][poprzedniY - 2].get() == ""):
                gracz.set('Tura gracza 2')
                kolejne_bicie = True
                kolejne_bicie_X = poprzedniX
                kolejne_bicie_Y = poprzedniY


def action():
    global wcisnietyX, wcisnietyY
    global wcisniety
    global poprzedniX, poprzedniY
    global gracz, ile_bialych, ile_czarnych, kolejne_bicie, kolejne_bicie_X, kolejne_bicie_Y

    if wcisniety == False:
        if kolejne_bicie == True:
            if (wcisnietyX == kolejne_bicie_X) and (wcisnietyY == kolejne_bicie_Y):
                if (gracz.get() == 'Tura gracza 2'):
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

                if (gracz.get() == 'Tura gracza 1'):
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
                messagebox.showerror(title="Zły wybór", message="Wykonaj kolejne bicie tym samym pionkiem")
        else:
            if (gracz.get() == 'Tura gracza 2'):
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

            if (gracz.get() == 'Tura gracza 1'):
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
        if kolejne_bicie == False:
            # przełączanie między pionkami 2 gracza
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
                if (napis[wcisnietyX][wcisnietyY].get() == "C") or (napis[wcisnietyX][wcisnietyY].get() == "Cd"):
                    messagebox.showerror(title="Zły ruch", message="Niedozwolony ruch")
        else:
            messagebox.showerror(title="Zły wybór", message="Wykonaj kolejne bicie tym samym pionkiem")

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
                                    kolejne_bicie = False
                                    gracz.set('Tura gracza 2')
                                    ile_czarnych -= 1
                                    if ile_czarnych == 0:
                                        koniec_gry("Gracz 1")
                                # pionek B
                                else:
                                    napis[wcisnietyX][wcisnietyY].set("B")
                                    napis[poprzedniX][poprzedniY].set("")
                                    napis[wcisnietyX - 1][wcisnietyY - 1].set("")
                                    poprzedniX = wcisnietyX
                                    poprzedniY = wcisnietyY
                                    wcisniety = False
                                    kolejne_bicie = False
                                    gracz.set('Tura gracza 2')
                                    ile_czarnych -= 1
                                    if ile_czarnych == 0:
                                        koniec_gry("Gracz 1")
                                    # sprawdzam czy możliwe jest kolejne bicie
                                    if wcisnietyX < 6:
                                        if poprzedniY < 2:
                                            if (napis[poprzedniX + 1][poprzedniY + 1].get() == "C") or (
                                                    napis[poprzedniX + 1][poprzedniY + 1].get() == "Cd"):
                                                if napis[poprzedniX + 2][poprzedniY + 2].get() == "":
                                                    gracz.set('Tura gracza 1')
                                                    kolejne_bicie = True
                                                    kolejne_bicie_X = poprzedniX
                                                    kolejne_bicie_Y = poprzedniY

                                        elif poprzedniY > 5:
                                            if (napis[poprzedniX + 1][poprzedniY - 1].get() == "C") or (
                                                    napis[poprzedniX + 1][poprzedniY - 1].get() == "Cd"):
                                                if napis[poprzedniX + 2][poprzedniY - 2].get() == "":
                                                    gracz.set('Tura gracza 1')
                                                    kolejne_bicie = True
                                                    kolejne_bicie_X = poprzedniX
                                                    kolejne_bicie_Y = poprzedniY

                                        else:
                                            if (napis[poprzedniX + 1][poprzedniY + 1].get() == "C" or
                                                    napis[poprzedniX + 1][poprzedniY + 1].get() == "Cd") and (
                                                    napis[poprzedniX + 2][poprzedniY + 2].get() == ""):
                                                gracz.set('Tura gracza 1')
                                                kolejne_bicie = True
                                                kolejne_bicie_X = poprzedniX
                                                kolejne_bicie_Y = poprzedniY

                                            elif (napis[poprzedniX + 1][poprzedniY - 1].get() == "C" or
                                                    napis[poprzedniX + 1][poprzedniY - 1].get() == "Cd") and (
                                                    napis[poprzedniX + 2][poprzedniY - 2].get() == ""):
                                                gracz.set('Tura gracza 1')
                                                kolejne_bicie = True
                                                kolejne_bicie_X = poprzedniX
                                                kolejne_bicie_Y = poprzedniY

                            else:
                               messagebox.showerror(title="Zły ruch", message="Niedozwolony ruch")

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
                                    kolejne_bicie = False
                                    gracz.set('Tura gracza 2')
                                    ile_czarnych -= 1
                                    if ile_czarnych == 0:
                                        koniec_gry("Gracz 1")
                                    # pionek B
                                else:
                                    napis[wcisnietyX][wcisnietyY].set("B")
                                    napis[poprzedniX][poprzedniY].set("")
                                    napis[wcisnietyX - 1][wcisnietyY + 1].set("")
                                    poprzedniX = wcisnietyX
                                    poprzedniY = wcisnietyY
                                    wcisniety = False
                                    kolejne_bicie = False
                                    gracz.set('Tura gracza 2')
                                    ile_czarnych -= 1
                                    if ile_czarnych == 0:
                                        koniec_gry("Gracz 1")
                                    # sprawdzam czy możliwe jest kolejne bicie
                                    if poprzedniX < 6:
                                        if poprzedniY < 2:
                                            if (napis[poprzedniX + 1][poprzedniY + 1].get() == "C" ) or (
                                                    napis[poprzedniX + 1][poprzedniY + 1].get() == "Cd"):
                                                if napis[poprzedniX + 2][poprzedniY + 2].get() == "":
                                                    gracz.set('Tura gracza 1')
                                                    kolejne_bicie = True
                                                    kolejne_bicie_X = poprzedniX
                                                    kolejne_bicie_Y = poprzedniY

                                        elif poprzedniY > 5:
                                            if (napis[poprzedniX + 1][poprzedniY - 1].get() == "C" or
                                                    napis[poprzedniX + 1][poprzedniY - 1].get() == "Cd"):
                                                if napis[poprzedniX + 2][poprzedniY - 2].get() == "":
                                                    gracz.set('Tura gracza 1')
                                                    kolejne_bicie = True
                                                    kolejne_bicie_X = poprzedniX
                                                    kolejne_bicie_Y = poprzedniY

                                        else:
                                            if (napis[poprzedniX + 1][poprzedniY + 1].get() == "C" or
                                                    napis[poprzedniX + 1][poprzedniY + 1].get() == "Cd") and (
                                                    napis[poprzedniX + 2][poprzedniY + 2].get() == ""):
                                                gracz.set('Tura gracza 1')
                                                kolejne_bicie = True
                                                kolejne_bicie_X = poprzedniX
                                                kolejne_bicie_Y = poprzedniY

                                            elif (napis[poprzedniX + 1][poprzedniY - 1].get() == "C" or
                                                    napis[poprzedniX + 1][poprzedniY - 1].get() == "Cd") and (
                                                    napis[poprzedniX + 2][poprzedniY - 2].get() == ""):
                                                gracz.set('Tura gracza 1')
                                                kolejne_bicie = True
                                                kolejne_bicie_X = poprzedniX
                                                kolejne_bicie_Y = poprzedniY

                            else:
                                messagebox.showerror(title="Zły ruch", message="Niedozwolony ruch")
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
                                    kolejne_bicie = False
                                    gracz.set('Tura gracza 1')
                                    ile_bialych -= 1
                                    if ile_bialych == 0:
                                        koniec_gry("Gracz 2")
                                # pionek C
                                else:
                                    napis[wcisnietyX][wcisnietyY].set("C")
                                    napis[poprzedniX][poprzedniY].set("")
                                    napis[wcisnietyX + 1][wcisnietyY - 1].set("")
                                    poprzedniX = wcisnietyX
                                    poprzedniY = wcisnietyY
                                    wcisniety = False
                                    kolejne_bicie = False
                                    gracz.set('Tura gracza 1')
                                    ile_bialych -= 1
                                    if ile_bialych == 0:
                                        koniec_gry("Gracz 2")
                                    # sprawdzam czy możliwe jest kolejne bicie
                                    if poprzedniX > 1:
                                        if poprzedniY < 2:
                                            if (napis[poprzedniX - 1][poprzedniY + 1].get() == "B") or (
                                                    napis[poprzedniX - 1][poprzedniY + 1].get() == "Bd"):
                                                if napis[poprzedniX - 2][poprzedniY + 2].get() == "":
                                                    gracz.set('Tura gracza 2')
                                                    kolejne_bicie = True
                                                    kolejne_bicie_X = poprzedniX
                                                    kolejne_bicie_Y = poprzedniY

                                        elif poprzedniY > 5:
                                            if (napis[poprzedniX - 1][poprzedniY - 1].get() == "B") or (
                                                    napis[poprzedniX - 1][poprzedniY - 1].get() == "Bd"):
                                                if napis[poprzedniX - 2][poprzedniY - 2].get() == "":
                                                    gracz.set('Tura gracza 2')
                                                    kolejne_bicie = True
                                                    kolejne_bicie_X = poprzedniX
                                                    kolejne_bicie_Y = poprzedniY

                                        else:
                                            if (napis[poprzedniX - 1][poprzedniY + 1].get() == "B" or
                                                    napis[poprzedniX - 1][poprzedniY + 1].get() == "Bd") and (
                                                    napis[poprzedniX - 2][poprzedniY + 2].get() == ""):
                                                gracz.set('Tura gracza 2')
                                                kolejne_bicie = True
                                                kolejne_bicie_X = poprzedniX
                                                kolejne_bicie_Y = poprzedniY

                                            elif (napis[poprzedniX - 1][poprzedniY - 1].get() == "B" or
                                                    napis[poprzedniX - 1][poprzedniY - 1].get() == "Bd") and (
                                                    napis[poprzedniX - 2][poprzedniY - 2].get() == ""):
                                                gracz.set('Tura gracza 2')
                                                kolejne_bicie = True
                                                kolejne_bicie_X = poprzedniX
                                                kolejne_bicie_Y = poprzedniY

                            else:
                                messagebox.showerror(title="Zły ruch", message="Niedozwolony ruch")

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
                                    kolejne_bicie = False
                                    gracz.set('Tura gracza 1')
                                    ile_bialych -= 1
                                    if ile_bialych == 0:
                                        koniec_gry("Gracz 2")
                                # pionek C
                                else:
                                    napis[wcisnietyX][wcisnietyY].set("C")
                                    napis[poprzedniX][poprzedniY].set("")
                                    napis[wcisnietyX + 1][wcisnietyY + 1].set("")
                                    poprzedniX = wcisnietyX
                                    poprzedniY = wcisnietyY
                                    wcisniety = False
                                    kolejne_bicie = False
                                    gracz.set('Tura gracza 1')
                                    ile_bialych -= 1
                                    if ile_bialych == 0:
                                        koniec_gry("Gracz 2")
                                    # sprawdzam czy możliwe jest kolejne bicie
                                    if poprzedniX > 1:
                                        if poprzedniY < 2:
                                            if (napis[poprzedniX - 1][poprzedniY + 1].get() == "B") or (
                                                    napis[poprzedniX - 1][poprzedniY + 1].get() == "Bd"):
                                                if napis[poprzedniX - 2][poprzedniY + 2].get() == "":
                                                    gracz.set('Tura gracza 2')
                                                    kolejne_bicie = True
                                                    kolejne_bicie_X = poprzedniX
                                                    kolejne_bicie_Y = poprzedniY

                                        elif poprzedniY > 5:
                                            if (napis[poprzedniX - 1][poprzedniY - 1].get() == "B") or (
                                                    napis[poprzedniX - 1][poprzedniY - 1].get() == "Bd"):
                                                if napis[poprzedniX - 2][poprzedniY - 2].get() == "":
                                                    gracz.set('Tura gracza 2')
                                                    kolejne_bicie = True
                                                    kolejne_bicie_X = poprzedniX
                                                    kolejne_bicie_Y = poprzedniY

                                        else:
                                            if (napis[poprzedniX - 1][poprzedniY - 1].get() == "B" or
                                                    napis[poprzedniX - 1][poprzedniY - 1].get() == "Bd") and (
                                                    napis[poprzedniX - 2][poprzedniY - 2].get() == ""):
                                                gracz.set('Tura gracza 2')
                                                kolejne_bicie = True
                                                kolejne_bicie_X = poprzedniX
                                                kolejne_bicie_Y = poprzedniY

                                            elif (napis[poprzedniX - 1][poprzedniY + 1].get() == "B" or
                                                    napis[poprzedniX - 1][poprzedniY + 1].get() == "Bd") and (
                                                    napis[poprzedniX - 2][poprzedniY + 2].get() == ""):
                                                gracz.set('Tura gracza 2')
                                                kolejne_bicie = True
                                                kolejne_bicie_X = poprzedniX
                                                kolejne_bicie_Y = poprzedniY

                            else:
                                messagebox.showerror(title="Zły ruch", message="Niedozwolony ruch")
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
                                kolejne_bicie = False
                                gracz.set('Tura gracza 2')
                                ile_czarnych -= 1
                                if ile_czarnych == 0:
                                    koniec_gry("Gracz 1")
                                kolejne_bicie_Bd()
                        elif (wcisnietyX == poprzedniX + 2)and(wcisnietyY == poprzedniY - 2):
                            if (napis[wcisnietyX - 1][wcisnietyY + 1].get() == "C")or(napis[wcisnietyX - 1][wcisnietyY + 1].get() == "Cd"):
                                napis[wcisnietyX][wcisnietyY].set("Bd")
                                napis[poprzedniX][poprzedniY].set("")
                                napis[wcisnietyX - 1][wcisnietyY + 1].set("")
                                poprzedniX = wcisnietyX
                                poprzedniY = wcisnietyY
                                wcisniety = False
                                kolejne_bicie = False
                                gracz.set('Tura gracza 2')
                                ile_czarnych -= 1
                                if ile_czarnych == 0:
                                    koniec_gry("Gracz 1")
                                kolejne_bicie_Bd()
                        elif (wcisnietyX == poprzedniX - 2)and(wcisnietyY == poprzedniY - 2):
                            if (napis[wcisnietyX + 1][wcisnietyY + 1].get() == "C")or(napis[wcisnietyX + 1][wcisnietyY + 1].get() == "Cd"):
                                napis[wcisnietyX][wcisnietyY].set("Bd")
                                napis[poprzedniX][poprzedniY].set("")
                                napis[wcisnietyX + 1][wcisnietyY + 1].set("")
                                poprzedniX = wcisnietyX
                                poprzedniY = wcisnietyY
                                wcisniety = False
                                kolejne_bicie = False
                                gracz.set('Tura gracza 2')
                                ile_czarnych -= 1
                                if ile_czarnych == 0:
                                    koniec_gry("Gracz 1")
                                kolejne_bicie_Bd()
                        elif (wcisnietyX == poprzedniX - 2)and(wcisnietyY == poprzedniY + 2):
                            if (napis[wcisnietyX + 1][wcisnietyY - 1].get() == "C")or(napis[wcisnietyX + 1][wcisnietyY - 1].get() == "Cd"):
                                napis[wcisnietyX][wcisnietyY].set("Bd")
                                napis[poprzedniX][poprzedniY].set("")
                                napis[wcisnietyX + 1][wcisnietyY - 1].set("")
                                poprzedniX = wcisnietyX
                                poprzedniY = wcisnietyY
                                wcisniety = False
                                kolejne_bicie = False
                                gracz.set('Tura gracza 2')
                                ile_czarnych -= 1
                                if ile_czarnych == 0:
                                    koniec_gry("Gracz 1")
                                kolejne_bicie_Bd()
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
                                kolejne_bicie = False
                                gracz.set('Tura gracza 1')
                                ile_bialych -= 1
                                if ile_bialych == 0:
                                    koniec_gry("Gracz 2")
                                kolejne_bicie_Cd()
                        elif (wcisnietyX == poprzedniX + 2)and(wcisnietyY == poprzedniY - 2):
                            if (napis[wcisnietyX - 1][wcisnietyY + 1].get() == "B")or(napis[wcisnietyX - 1][wcisnietyY + 1].get() == "Bd"):
                                napis[wcisnietyX][wcisnietyY].set("Cd")
                                napis[poprzedniX][poprzedniY].set("")
                                napis[wcisnietyX - 1][wcisnietyY + 1].set("")
                                poprzedniX = wcisnietyX
                                poprzedniY = wcisnietyY
                                wcisniety = False
                                kolejne_bicie = False
                                gracz.set('Tura gracza 1')
                                ile_bialych -= 1
                                if ile_bialych == 0:
                                    koniec_gry("Gracz 2")
                                kolejne_bicie_Cd()
                        elif (wcisnietyX == poprzedniX - 2)and(wcisnietyY == poprzedniY - 2):
                            if (napis[wcisnietyX + 1][wcisnietyY + 1].get() == "B")or(napis[wcisnietyX + 1][wcisnietyY + 1].get() == "Bd"):
                                napis[wcisnietyX][wcisnietyY].set("Cd")
                                napis[poprzedniX][poprzedniY].set("")
                                napis[wcisnietyX + 1][wcisnietyY + 1].set("")
                                poprzedniX = wcisnietyX
                                poprzedniY = wcisnietyY
                                wcisniety = False
                                kolejne_bicie = False
                                gracz.set('Tura gracza 1')
                                ile_bialych -= 1
                                if ile_bialych == 0:
                                    koniec_gry("Gracz 2")
                                kolejne_bicie_Cd()
                        elif (wcisnietyX == poprzedniX - 2)and(wcisnietyY == poprzedniY + 2):
                            if (napis[wcisnietyX + 1][wcisnietyY - 1].get() == "B")or(napis[wcisnietyX + 1][wcisnietyY - 1].get() == "Bd"):
                                napis[wcisnietyX][wcisnietyY].set("Cd")
                                napis[poprzedniX][poprzedniY].set("")
                                napis[wcisnietyX + 1][wcisnietyY - 1].set("")
                                poprzedniX = wcisnietyX
                                poprzedniY = wcisnietyY
                                wcisniety = False
                                kolejne_bicie = False
                                gracz.set('Tura gracza 1')
                                ile_bialych -= 1
                                if ile_bialych == 0:
                                    koniec_gry("Gracz 2")
                                kolejne_bicie_Cd()
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
kolejne_bicie = False
ile_bialych = 12
ile_czarnych = 12
gracz = StringVar()
gracz.set('Tura gracza 1')
tura = Label(okno, textvariable=gracz)
tura.pack()

okno.bind("<Button-1>", click)
plansza()
okno.mainloop()

