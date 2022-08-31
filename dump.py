#slovar = {}
#
#with open("besede_sprejemljive.txt") as dat:
#    i = 0
#    for beseda in dat:
#        slovar[beseda[:-1]] = len(beseda[:-1])
#
#
#for beseda in slovar:
#    ime = "sprejemljive dolzina " + str(len(beseda)) 
#    with open(ime, "a") as datoteka:
#        datoteka.write(beseda)
#
#print("done")


seznam = []

with open("besede_sprejemljive.txt") as dat:
    for beseda in dat:
        seznam.append(beseda[:-1])

for beseda in seznam:
    i = 0
    ime = "sprejemljive_dolzine_" + str(len(beseda))  + ".txt"
    with open(ime, "a") as datoteka:
        print(beseda)
        datoteka.write(beseda + "\n")
        if i % 10000 == 0:
            print(beseda)
        i += 1

print("done")