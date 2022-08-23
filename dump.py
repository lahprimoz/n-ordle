import json

slovar = {}

with open("besede_uradne.txt") as dat:
    i = 0
    for beseda in dat:
        slovar[beseda[:-1]] = len(beseda[:-1])

with open("besede_uradne.json", "w") as datoteka:
    json.dump(slovar, datoteka, indent=4)
