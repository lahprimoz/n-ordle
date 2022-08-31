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

with open("besede_vse.txt") as dat:
    for beseda in dat:
        seznam.append(beseda[:-1])

i = 0
for beseda in seznam:
    ime = "vse_dolzine_" + str(len(beseda))  + ".txt"
    if i % 5000 == 1:
        print(beseda + " " + str(i))
    i += 1
    with open(ime, "a") as datoteka:
        datoteka.write(beseda.lower() + "\n")

print("done")