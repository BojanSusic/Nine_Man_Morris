


class prazanRed(Exception):
    pass

class Red(object):
    inicijalniKapacitet = 20

    def __init__(self):
        self.elementi = [None] * self.inicijalniKapacitet
        self.velicina = 0
        self.prviEl = 0 #indeks prvog elementa u redu

    def __len__(self):
        return self.velicina

    def is_empty(self):
        return self.velicina == 0

    def prvi(self):
        if self.is_empty():
            raise prazanRed('red je prazan.')
        return self.elementi[self.prviEl]

    def povecajKapacitet(self, kapacitet):
        stari = self.elementi
        self.elementi = [None] * kapacitet
        premotanaKonf = self.prviEl
        for svaki in range(self.velicina):
            self.elementi[svaki] = stari[premotanaKonf]
            premotanaKonf = (1 + premotanaKonf) % len(stari)
        self.prviEl = 0

    def enqueue(self, element):
        if self.velicina == len(self.elementi):
            self.povecajKapacitet(2 * len(self.elementi))
        pomocni = (self.prviEl + self.velicina) % len(self.elementi)
        self.elementi[pomocni] = element
        self.velicina += 1

    def dequeue(self):
        if self.is_empty():
            raise prazanRed('red je prazan.')
        ans = self.elementi[self.prviEl]
        self.elementi[self.prviEl] = None
        self.prviEl = (self.prviEl + 1) % len(self.elementi)
        self.velicina -= 1
        return ans