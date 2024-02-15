class Vojak():
    def __init__(self, meno, utok, obrana):
        self.meno = meno
        self.utok = utok
        self.obrana = obrana


class Pesiak(Vojak):
    def __init__(self):
        super().__init__("Vojak", 2,2)

class Lukostrelec(Vojak):
    def __init__(self):
        super().__init__("lokostrelec", 6,1)

class Jazdec(Vojak):
    def __init__(self):
        super().__init__("jazdec", 4,4)


p1= Pesiak()
l1 = Lukostrelec()
j1=Jazdec()
