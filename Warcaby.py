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
            reset.grid(row = 8, columnspan = 8)


def reset1():
    global wcisniety
    warcaby.destroy()
    wcisniety = False
    plansza()

def action():
    global wcisnietyX, wcisnietyY
    global wcisniety
    global poprzedniX, poprzedniY

    if wcisniety == False:
        if napis[wcisnietyX][wcisnietyY].get() == "C":
            napis[wcisnietyX][wcisnietyY].set("[C]")
            poprzedniX = wcisnietyX
            poprzedniY = wcisnietyY
            wcisniety = True
        if napis[wcisnietyX][wcisnietyY].get() == "B":
            napis[wcisnietyX][wcisnietyY].set("[B]")
            poprzedniX = wcisnietyX
            poprzedniY = wcisnietyY
            wcisniety = True
    else:
        if napis[poprzedniX][poprzedniY].get() == "[C]":
            if napis[wcisnietyX][wcisnietyY].get() == "C":
                napis[wcisnietyX][wcisnietyY].set("[C]")
                napis[poprzedniX][poprzedniY].set("C")
                poprzedniX = wcisnietyX
                poprzedniY = wcisnietyY

        if napis[poprzedniX][poprzedniY].get() == "[B]":
            if napis[wcisnietyX][wcisnietyY].get() == "B":
                napis[wcisnietyX][wcisnietyY].set("[B]")
                napis[poprzedniX][poprzedniY].set("B")
                poprzedniX = wcisnietyX
                poprzedniY = wcisnietyY

        if napis[poprzedniX][poprzedniY].get() == "[C]":
            if (przycisk[wcisnietyX][wcisnietyY]["background"] == "black"):
                if napis[wcisnietyX][wcisnietyY].get() == "":
                    if (wcisnietyX == poprzedniX - 1) and (wcisnietyY == poprzedniY + 1 or wcisnietyY == poprzedniY - 1):
                        if napis[wcisnietyX][wcisnietyY].get() == "":
                            napis[wcisnietyX][wcisnietyY].set("C")
                            napis[poprzedniX][poprzedniY].set("")
                            poprzedniX = wcisnietyX
                            poprzedniY = wcisnietyY
                            wcisniety = False
                    else:
                        messagebox.showerror(title="Zły ruch", message="Niedozwolony ruch")
            else:
                messagebox.showerror(title="Zły ruch", message="Niedozwolony ruch")

        if napis[poprzedniX][poprzedniY].get() == "[B]":
            if (przycisk[wcisnietyX][wcisnietyY]["background"] == "black"):
                if napis[wcisnietyX][wcisnietyY].get() == "":
                    if (wcisnietyX == poprzedniX + 1) and (wcisnietyY == poprzedniY + 1 or wcisnietyY == poprzedniY - 1):
                        if napis[wcisnietyX][wcisnietyY].get() == "":
                            napis[wcisnietyX][wcisnietyY].set("B")
                            napis[poprzedniX][poprzedniY].set("")
                            poprzedniX = wcisnietyX
                            poprzedniY = wcisnietyY
                            wcisniety = False
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

okno.bind("<Button-1>", click)

plansza()
okno.mainloop()
