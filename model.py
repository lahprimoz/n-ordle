import random
import json
import os

class Besede:
    def __init__(self, odgovor, ugibanje_1=None, 
        ugibanje_2=None, ugibanje_3=None, ugibanje_4=None, 
        ugibanje_5=None, ugibanje_6=None, aktualno_ugibanje=None, 
        seznam_pravilnosti=None, izpis1=None, izpis2=None, izpis3=None,
        izpis4=None, izpis5=None, izpis6=None):
        self.odgovor = odgovor
        self.ugibanje_1 = ugibanje_1
        self.ugibanje_2 = ugibanje_2
        self.ugibanje_3 = ugibanje_3
        self.ugibanje_4 = ugibanje_4
        self.ugibanje_5 = ugibanje_5
        self.ugibanje_6 = ugibanje_6
        self.aktualno_ugibanje = aktualno_ugibanje
        self.seznam_pravilnosti = seznam_pravilnosti
        self.izpis1 = izpis1
        self.izpis2 = izpis2
        self.izpis3 = izpis3
        self.izpis4 = izpis4
        self.izpis5 = izpis5
        self.izpis6 = izpis6

    @staticmethod
    def izberi_besedo_wordle():
        indeks = random.randrange(12972)
        with open("besede/besede_uradne.txt") as dat:
            for _ in range(indeks):
                beseda = dat.readline()
            return beseda[:-1]

#    @staticmethod
#    def izberi_besedo_sprejemljive(dolzina):
#        ime = "besede/sprejemljive_dolzine_" + dolzina + ".txt"
#        indeks = random.randrange(62000)
#        with open(ime) as dat:
#            for _ in range(indeks):
#                beseda = dat.readline()
#                if beseda == "":
#                    dat.seek(0)
#                    beseda = dat.readline()
#            return beseda

#    @staticmethod
#    def izberi_besedo_vse(dolzina):
#        ime = "besede/vse_dolzine_" + dolzina + ".txt"
#        indeks = random.randrange(62000)
#        with open(ime) as dat:
#            for _ in range(indeks):
#                beseda = dat.readline()
#                if beseda == "":
#                    dat.seek(0)
#                    beseda = dat.readline()
#            return beseda

    def preveri_besedo_wordle(self, beseda, pravilna):
        rezultat = []
        for i in beseda.lower():
            if i in pravilna.lower():
                if beseda.index(i) == pravilna.index(i):
                    rezultat.append("G")
                else:
                    rezultat.append("Y")
            else:
                rezultat.append("R")
        return rezultat

#    def preveri_besedo_sprejemljive(self):
#        pravilna = Besede.izberi_besedo_sprejemljive()
#        rezultat = []
#        for i in self.beseda.lower():
#            if i in pravilna.lower():
#                if self.beseda.index(i) == pravilna.index(i):
#                    rezultat.append("&#9989")
#                else:
#                    rezultat.append("Y")
#            else:
#                rezultat.append("B")
#        return rezultat

#        pravilna = Besede.izberi_besedo_vse()
#    def preveri_besedo_vse(self):
#        rezultat = []
#        for i in self.beseda.lower():
#            if i in pravilna.lower():
#                if self.beseda.index(i) == pravilna.index(i):
#                    rezultat.append("G")
#                else:
#                    rezultat.append("Y")
#            else:
#                rezultat.append("B")
#        return rezultat

    def preveri_rezultat_wordle(self):
        rezultat = Besede.preveri_besedo_wordle()
        for i in rezultat:
            if i != "G":
                return False
        return True

#    def preveri_rezultat_sprejemljive(self):
#        rezultat = Besede.preveri_besedo_sprejemljive()
#        for i in rezultat:
#            if i != "G":
#                return False
#        return True

#    def preveri_rezultat_vse(self):
#        rezultat = Besede.preveri_besedo_vse()
#        for i in rezultat:
#            if i != "G":
#                return False
#        return True

    def v_slovar(self):
        return {
            "odgovor": self.odgovor,
            "ugibanje_1": self.ugibanje_1,
            "ugibanje_2": self.ugibanje_2,
            "ugibanje_3": self.ugibanje_3,
            "ugibanje_4": self.ugibanje_4,
            "ugibanje_5": self.ugibanje_5,
            "ugibanje_6": self.ugibanje_6,
            "aktualno_ugibanje": self.aktualno_ugibanje,
            "seznam_pravilnosti": self.seznam_pravilnosti,
            "izpis1": self.izpis1,
            "izpis2": self.izpis2,
            "izpis3": self.izpis3,
            "izpis4": self.izpis4,
            "izpis5": self.izpis5,
            "izpis6": self.izpis6
        }

    @staticmethod
    def iz_slovarja(slovar):
        return Besede(
            slovar["odgovor"],
            slovar["ugibanje_1"],
            slovar["ugibanje_2"],
            slovar["ugibanje_3"],
            slovar["ugibanje_4"],
            slovar["ugibanje_5"],
            slovar["ugibanje_6"],
            slovar["aktualno_ugibanje"],
            slovar["seznam_pravilnosti"],
            slovar["izpis1"],
            slovar["izpis2"],
            slovar["izpis3"],
            slovar["izpis4"],
            slovar["izpis5"],
            slovar["izpis6"]
        )

    def shrani_v_datoteko(self, ime_dat):
        with open(ime_dat, "w") as dat:
            slovar = self.v_slovar()
            json.dump(slovar, dat, indent=4, ensure_ascii=False)

    @staticmethod
    def preberi_iz_datoteke(ime_dat):
        with open(ime_dat) as dat:
            slovar = json.load(dat)
            return Besede.iz_slovarja(slovar)

    @staticmethod
    def izpisi_pravilnost(seznam, beseda):
        niz = ""
        i = 0
        for znak in seznam:
            if znak == "G":
                niz += beseda[i].upper() + " "
            elif znak == "Y":
                niz += beseda[i].lower() + " "
            elif znak == "R":
                niz += "_ "
            i += 1
        return niz

    @staticmethod
    def izbrisi(ime="stanje.json"):
        os.remove(ime)
        return None