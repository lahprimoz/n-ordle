dolzine_sprejemljivih = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 27, 28, 29, 31]
dolzine_vseh = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 31, 45]
prava_beseda = "test"

def zacetni_pozdrav():
    print("Pozdravljeni v n-ordle")
    ponudi_vrste_iger()

def odgovor(ugibanje, prava_beseda):
    pravilno = []
    for crka in ugibanje:
        if crka.lower() in prava_beseda.lower():
            if ugibanje[ugibanje.index(crka)] == prava_beseda[prava_beseda.index(crka)]:
                pravilno.append(crka.upper())
            else:
                pravilno.append(crka.lower())
        else:
            pravilno.append(" ")
    print(pravilno)

def uganil():
    print("Bravo! Beseda je pravilna.")
    print("Če želite igrati ponovno v enaki konfiguraciji vnesite 1")
    print("Če želite igrati z novo konfiguracijo vnesite 2")
    print("Če želite zaključiti z igro vnesite 3")
    zakljucek()

def vpisi_ugibanje():
        beseda = input("Vnesite besedo, ki jo ugibate: ")
        if len(beseda) != len(prava_beseda):
            print(f"Vnesi besedo z dolžino {len(prava_beseda)}")
        elif beseda.lower() == prava_beseda.lower():
            uganil()
        else:
            odgovor(beseda, prava_beseda)



def ponudi_dolzino_vse():
    dolzina = input("Izberi željeno dolžino besede: ")
    if int(dolzina) in dolzine_vseh:
        vpisi_ugibanje()
    else:
        print("Besede s to dolžino ni v naši bazi. poskusite ponovno.")
        ponudi_dolzino_vse()

def ponudi_dolzino_sprejemljive():
    dolzina = input("Izberi željeno dolžino besede: ")
    if int(dolzina) in dolzine_sprejemljivih:
        vpisi_ugibanje()
    else:
        print("Besede s to dolžino ni v naši bazi. poskusite ponovno.")
        ponudi_dolzino_sprejemljive()

def ponudi_vrste_iger():
    print("Na voljo so 3 vrste igre:")
    print("1) Originalen Wordle")
    print("2) Wordle z običajnimi besedami")
    print("3) Wordle z besedami, ki vsebujejo tudi števila in posebne znake")
    vhod = input("Izberi vrsto igre: ")
    if vhod == "1":
        ponudi_dolzino_sprejemljive()

def zakljucek():
    vnos = input("> ")
    if vnos == "1":
        vpisi_ugibanje()
    elif vnos == "2":
        ponudi_vrste_iger()
    elif vnos == "3":
        exit

zacetni_pozdrav()