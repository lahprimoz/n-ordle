import random

class Besede:
    def __init__(self, beseda):
        self.beseda = beseda

    @staticmethod
    def izberi_besedo_wordle():
        indeks = random.randrange(12972)
        with open("besede/besede_uradne.txt") as dat:
            for _ in range(indeks):
                beseda = dat.readline()
            return beseda

    @staticmethod
    def izberi_besedo_sprejemljive(dolzina):
        ime = "besede/sprejemljive_dolzine_" + dolzina + ".txt"
        indeks = random.randrange(62000)
        with open(ime) as dat:
            for _ in range(indeks):
                beseda = dat.readline()
                if beseda == "":
                    dat.seek(0)
                    beseda = dat.readline()
            return beseda

    @staticmethod
    def izberi_besedo_vse(dolzina):
        ime = "besede/vse_dolzine_" + dolzina + ".txt"
        indeks = random.randrange(62000)
        with open(ime) as dat:
            for _ in range(indeks):
                beseda = dat.readline()
                if beseda == "":
                    dat.seek(0)
                    beseda = dat.readline()
            return beseda

    def preveri_besedo_wordle(self):
        pravilna = Besede.izberi_besedo_wordle()
        rezultat = []
        for i in self.beseda.lower():
            if i in pravilna.lower():
                if self.beseda.index(i) == pravilna.index(i):
                    rezultat.append("G")
                else:
                    rezultat.append("Y")
            else:
                rezultat.append("B")
        return rezultat

    def preveri_besedo_sprejemljive(self):
        pravilna = Besede.izberi_besedo_sprejemljive()
        rezultat = []
        for i in self.beseda.lower():
            if i in pravilna.lower():
                if self.beseda.index(i) == pravilna.index(i):
                    rezultat.append("G")
                else:
                    rezultat.append("Y")
            else:
                rezultat.append("B")
        return rezultat

    def preveri_besedo_vse(self):
        pravilna = Besede.izberi_besedo_vse()
        rezultat = []
        for i in self.beseda.lower():
            if i in pravilna.lower():
                if self.beseda.index(i) == pravilna.index(i):
                    rezultat.append("G")
                else:
                    rezultat.append("Y")
            else:
                rezultat.append("B")
        return rezultat

    def preveri_rezultat_wordle(self):
        rezultat = Besede.preveri_besedo_wordle()
        for i in rezultat:
            if i != "G":
                return False
        return True

    def preveri_rezultat_sprejemljive(self):
        rezultat = Besede.preveri_besedo_sprejemljive()
        for i in rezultat:
            if i != "G":
                return False
        return True

    def preveri_rezultat_vse(self):
        rezultat = Besede.preveri_besedo_vse()
        for i in rezultat:
            if i != "G":
                return False
        return True