from tkinter import *


class Warcaby(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master
        self.frame = None
        self.uklad_poczatkowy()

    def uklad_poczatkowy(self):
        if self.frame is None:
            self.frame = Frame(self.master)
            self.frame.pack()

            pierwszy_rzad = Frame(self.frame)
            drugi_rzad = Frame(self.frame)
            trzeci_rzad = Frame(self.frame)
            czwarty_rzad = Frame(self.frame)
            piaty_rzad = Frame(self.frame)
            szosty_rzad = Frame(self.frame)
            siodmy_rzad = Frame(self.frame)
            osmy_rzad = Frame(self.frame)

            pierwszy_rzad.pack()
            drugi_rzad.pack()
            trzeci_rzad.pack()
            czwarty_rzad.pack()
            piaty_rzad.pack()
            szosty_rzad.pack()
            siodmy_rzad.pack()
            osmy_rzad.pack()

            reset = Button(self.frame, text="Reset", command=self.reset)
            reset.pack(fill=X)

            przycisk = [[0 for x in range(8)] for y in range(8)]

            # Pierwszy rzad przyciskow
            przycisk[0][0] = Button(pierwszy_rzad, width=6, height=3, bg="white").pack(side=LEFT)
            przycisk[0][1] = Button(pierwszy_rzad, text="C", width=6, height=3, bg="black", fg="white").pack(side=LEFT)
            przycisk[0][2] = Button(pierwszy_rzad, width=6, height=3, bg="white").pack(side=LEFT)
            przycisk[0][3] = Button(pierwszy_rzad, text="C", width=6, height=3, bg="black", fg="white").pack(side=LEFT)
            przycisk[0][4] = Button(pierwszy_rzad, width=6, height=3, bg="white").pack(side=LEFT)
            przycisk[0][5] = Button(pierwszy_rzad, text="C", width=6, height=3, bg="black", fg="white").pack(side=LEFT)
            przycisk[0][6] = Button(pierwszy_rzad, width=6, height=3, bg="white").pack(side=LEFT)
            przycisk[0][7] = Button(pierwszy_rzad, text="C", width=6, height=3, bg="black", fg="white").pack(side=LEFT)

            # Drugi rzad przyciskow
            przycisk[1][0] = Button(drugi_rzad, text="C", width=6, height=3, bg="black", fg="white").pack(side=LEFT)
            przycisk[1][1] = Button(drugi_rzad, width=6, height=3, bg="white").pack(side=LEFT)
            przycisk[1][2] = Button(drugi_rzad, text="C", width=6, height=3, bg="black", fg="white").pack(side=LEFT)
            przycisk[1][3] = Button(drugi_rzad, width=6, height=3, bg="white").pack(side=LEFT)
            przycisk[1][4] = Button(drugi_rzad, text="C", width=6, height=3, bg="black", fg="white").pack(side=LEFT)
            przycisk[1][5] = Button(drugi_rzad, width=6, height=3, bg="white").pack(side=LEFT)
            przycisk[1][6] = Button(drugi_rzad, text="C", width=6, height=3, bg="black", fg="white").pack(side=LEFT)
            przycisk[1][7] = Button(drugi_rzad, width=6, height=3, bg="white").pack(side=LEFT)

            # Trzeci rzad przyciskow
            przycisk[2][0] = Button(trzeci_rzad, width=6, height=3, bg="white").pack(side=LEFT)
            przycisk[2][1] = Button(trzeci_rzad, text="C", width=6, height=3, bg="black", fg="white").pack(side=LEFT)
            przycisk[2][2] = Button(trzeci_rzad, width=6, height=3, bg="white").pack(side=LEFT)
            przycisk[2][3] = Button(trzeci_rzad, text="C", width=6, height=3, bg="black", fg="white").pack(side=LEFT)
            przycisk[2][4] = Button(trzeci_rzad, width=6, height=3, bg="white").pack(side=LEFT)
            przycisk[2][5] = Button(trzeci_rzad, text="C", width=6, height=3, bg="black", fg="white").pack(side=LEFT)
            przycisk[2][6] = Button(trzeci_rzad, width=6, height=3, bg="white").pack(side=LEFT)
            przycisk[2][7] = Button(trzeci_rzad, text="C", width=6, height=3, bg="black", fg="white").pack(side=LEFT)

            # Czwarty rzad przyciskow
            przycisk[3][0] = Button(czwarty_rzad, width=6, height=3, bg="black", fg="white").pack(side=LEFT)
            przycisk[3][1] = Button(czwarty_rzad, width=6, height=3, bg="white").pack(side=LEFT)
            przycisk[3][2] = Button(czwarty_rzad, width=6, height=3, bg="black", fg="white").pack(side=LEFT)
            przycisk[3][3] = Button(czwarty_rzad, width=6, height=3, bg="white").pack(side=LEFT)
            przycisk[3][4] = Button(czwarty_rzad, width=6, height=3, bg="black", fg="white").pack(side=LEFT)
            przycisk[3][5] = Button(czwarty_rzad, width=6, height=3, bg="white").pack(side=LEFT)
            przycisk[3][6] = Button(czwarty_rzad, width=6, height=3, bg="black", fg="white").pack(side=LEFT)
            przycisk[3][7] = Button(czwarty_rzad, width=6, height=3, bg="white").pack(side=LEFT)

            # Piaty rzad przyciskow
            przycisk[4][0] = Button(piaty_rzad, width=6, height=3, bg="white").pack(side=LEFT)
            przycisk[4][1] = Button(piaty_rzad, width=6, height=3, bg="black", fg="white").pack(side=LEFT)
            przycisk[4][2] = Button(piaty_rzad, width=6, height=3, bg="white").pack(side=LEFT)
            przycisk[4][3] = Button(piaty_rzad, width=6, height=3, bg="black", fg="white").pack(side=LEFT)
            przycisk[4][4] = Button(piaty_rzad, width=6, height=3, bg="white").pack(side=LEFT)
            przycisk[4][5] = Button(piaty_rzad, width=6, height=3, bg="black", fg="white").pack(side=LEFT)
            przycisk[4][6] = Button(piaty_rzad, width=6, height=3, bg="white").pack(side=LEFT)
            przycisk[4][7] = Button(piaty_rzad, width=6, height=3, bg="black", fg="white").pack(side=LEFT)

            # Szosty rzad przyciskow
            przycisk[5][0] = Button(szosty_rzad, text="B", width=6, height=3, bg="black", fg="white").pack(side=LEFT)
            przycisk[5][1] = Button(szosty_rzad, width=6, height=3, bg="white").pack(side=LEFT)
            przycisk[5][2] = Button(szosty_rzad, text="B", width=6, height=3, bg="black", fg="white").pack(side=LEFT)
            przycisk[5][3] = Button(szosty_rzad, width=6, height=3, bg="white").pack(side=LEFT)
            przycisk[5][4] = Button(szosty_rzad, text="B", width=6, height=3, bg="black", fg="white").pack(side=LEFT)
            przycisk[5][5] = Button(szosty_rzad, width=6, height=3, bg="white").pack(side=LEFT)
            przycisk[5][6] = Button(szosty_rzad, text="B", width=6, height=3, bg="black", fg="white").pack(side=LEFT)
            przycisk[5][7] = Button(szosty_rzad, width=6, height=3, bg="white").pack(side=LEFT)

            # Siodmy rzad przyciskow
            przycisk[6][0] = Button(siodmy_rzad, width=6, height=3, bg="white").pack(side=LEFT)
            przycisk[6][1] = Button(siodmy_rzad, text="B", width=6, height=3, bg="black", fg="white").pack(side=LEFT)
            przycisk[6][2] = Button(siodmy_rzad, width=6, height=3, bg="white").pack(side=LEFT)
            przycisk[6][3] = Button(siodmy_rzad, text="B", width=6, height=3, bg="black", fg="white").pack(side=LEFT)
            przycisk[6][4] = Button(siodmy_rzad, width=6, height=3, bg="white").pack(side=LEFT)
            przycisk[6][5] = Button(siodmy_rzad, text="B", width=6, height=3, bg="black", fg="white").pack(side=LEFT)
            przycisk[6][6] = Button(siodmy_rzad, width=6, height=3, bg="white").pack(side=LEFT)
            przycisk[6][7] = Button(siodmy_rzad, text="B", width=6, height=3, bg="black", fg="white").pack(side=LEFT)

            # Osmy rzad przyciskow
            przycisk[7][0] = Button(osmy_rzad, text="B", width=6, height=3, bg="black", fg="white").pack(side=LEFT)
            przycisk[7][1] = Button(osmy_rzad, width=6, height=3, bg="white").pack(side=LEFT)
            przycisk[7][2] = Button(osmy_rzad, text="B", width=6, height=3, bg="black", fg="white").pack(side=LEFT)
            przycisk[7][3] = Button(osmy_rzad, width=6, height=3, bg="white").pack(side=LEFT)
            przycisk[7][4] = Button(osmy_rzad, text="B", width=6, height=3, bg="black", fg="white").pack(side=LEFT)
            przycisk[7][5] = Button(osmy_rzad, width=6, height=3, bg="white").pack(side=LEFT)
            przycisk[7][6] = Button(osmy_rzad, text="B", width=6, height=3, bg="black", fg="white").pack(side=LEFT)
            przycisk[7][7] = Button(osmy_rzad, width=6, height=3, bg="white").pack(side=LEFT)

    def reset(self):
        self.frame.destroy()
        self.frame = None
        self.uklad_poczatkowy()


okno = Tk()
okno.title("Warcaby")
warcaby = Warcaby(okno)
okno.mainloop()
