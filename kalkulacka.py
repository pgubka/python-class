import tkinter as tk

def prirataj(znamienko, cislo):
    global vysledok
    if znamienko == "+":
        vysledok = vysledok + cislo
    else:
        pass


def displachange(value):
    global vysledok
    global displaytext
    global znamienko
    global medzicislo

    if value==0:
        if medzicislo == 0:
            pass
        else:
            medzicislo = medzicislo*10 + value
    elif value in [1,2,3,4,5,6,7,8,9]:
        medzicislo = medzicislo*10 + value
        displaytext = str(medzicislo)
    elif value in ["+","-","*","/"]:
        znamienko = value
        prirataj(value, medzicislo)
        medzicislo=0
        displaytext=str(vysledok)
    elif value == "=":
        prirataj(znamienko, medzicislo)
        medzicislo = 0
        displaytext=str(vysledok)
    elif value == "ce":
        vysledok=0
        medzicislo=0
        znamienko="+"
        displaytext=str(vysledok)
    else:
        raise Exception("Nezname hodnota {}".format(value))

    display.config(text=str(displaytext))

vysledok=0
medzicislo=0
znamienko="+"
displaytext=str(vysledok)

okno = tk.Tk()
okno.geometry('500x800')
#root.resizable(False, False)
okno.title('Kalkulacka')

display = tk.Label(okno, text="0")
display.pack()

b1 = tk.Button(okno, text ="1", command = lambda: displachange(1))
b1.pack()
b2 = tk.Button(okno, text ="2", command = lambda: displachange(2))
b2.pack()
b3 = tk.Button(okno, text ="3", command = lambda: displachange(3))
b3.pack()
b4 = tk.Button(okno, text ="4", command = lambda: displachange(4))
b4.pack()
b5 = tk.Button(okno, text ="5", command = lambda: displachange(5))
b5.pack()
b6 = tk.Button(okno, text ="6", command = lambda: displachange(6))
b6.pack()
b7 = tk.Button(okno, text ="7", command = lambda: displachange(7))
b7.pack()
b8 = tk.Button(okno, text ="8", command = lambda: displachange(8))
b8.pack()
b9 = tk.Button(okno, text ="9", command = lambda: displachange(9))
b9.pack()
b0 = tk.Button(okno, text ="0", command = lambda: displachange(0))
b0.pack()
brovn = tk.Button(okno, text ="=", command = lambda: displachange("="))
brovn.pack()
bplus = tk.Button(okno, text ="+", command = lambda: displachange("+"))
bplus.pack()
bminus = tk.Button(okno, text ="-", command = lambda: displachange("-"))
bminus.pack()
bkrat = tk.Button(okno, text ="*", command = lambda: displachange("*"))
bkrat.pack()
bdel = tk.Button(okno, text ="/", command = lambda: displachange("/"))
bdel.pack()
bce = tk.Button(okno, text ="ce", command = lambda: displachange("ce"))
bce.pack()

okno.mainloop()
