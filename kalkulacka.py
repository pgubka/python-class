import tkinter as tk

def displachange(value):
    display.config(text=str(value))

okno = tk.Tk()
okno.geometry('500x500')
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

okno.mainloop()
