from model import Besede
import bottle

IME_DATOTEKE = "stanje.json"
try:
    stanje = Besede.preberi_iz_datoteke(IME_DATOTEKE)
except FileNotFoundError:
    stanje = Besede(odgovor=Besede.izberi_besedo_wordle())

@bottle.get("/")
def zacetna_stran():
    return bottle.template("zacetna_stran.tpl")

@bottle.post("/nova_beseda/")
def nova_beseda():
    Besede.izbrisi("stanje.json")
    bottle.redirect("/wordle/")

@bottle.get("/wordle/")
def igraj_wordle():
    iskana_beseda = Besede(Besede.izberi_besedo_wordle())
    stanje.shrani_v_datoteko(IME_DATOTEKE)
    return bottle.template("wordle.tpl")

@bottle.post("/wordle/ugibanje1/")
def preveri_wordle():
    trenutno_stanje = stanje.preberi_iz_datoteke(IME_DATOTEKE)
    trenutni_odgovor = trenutno_stanje.odgovor
    ugibanje = bottle.request.forms["ugibanje"]
    stanje.ugibanje_1 = ugibanje
    seznam = Besede.preveri_besedo_wordle(self=None, beseda=ugibanje, pravilna=trenutni_odgovor)
    stanje.seznam_pravilnosti = seznam
    stanje.izpis1 = Besede.izpisi_pravilnost(stanje.seznam_pravilnosti, stanje.ugibanje_1)
    stanje.shrani_v_datoteko(IME_DATOTEKE)
    bottle.redirect("/wordle2/")

@bottle.get("/wordle2/")
def igraj_wordle():
    iskana_beseda = Besede(Besede.izberi_besedo_wordle())
    stanje.shrani_v_datoteko(IME_DATOTEKE)
    return bottle.template("wordle2.tpl")

@bottle.post("/wordle/ugibanje2/")
def preveri_wordle():
    trenutno_stanje = stanje.preberi_iz_datoteke(IME_DATOTEKE)
    trenutni_odgovor = trenutno_stanje.odgovor
    ugibanje = bottle.request.forms["ugibanje"]
    stanje.ugibanje_2 = ugibanje
    seznam = Besede.preveri_besedo_wordle(self=None, beseda=ugibanje, pravilna=trenutni_odgovor)
    stanje.seznam_pravilnosti = seznam
    stanje.izpis2 = Besede.izpisi_pravilnost(stanje.seznam_pravilnosti, stanje.ugibanje_2)
    stanje.shrani_v_datoteko(IME_DATOTEKE)
    bottle.redirect("/wordle3/")

@bottle.get("/wordle3/")
def igraj_wordle():
    iskana_beseda = Besede(Besede.izberi_besedo_wordle())
    stanje.shrani_v_datoteko(IME_DATOTEKE)
    return bottle.template("wordle3.tpl")

@bottle.post("/wordle/ugibanje3/")
def preveri_wordle():
    trenutno_stanje = stanje.preberi_iz_datoteke(IME_DATOTEKE)
    trenutni_odgovor = trenutno_stanje.odgovor
    ugibanje = bottle.request.forms["ugibanje"]
    stanje.ugibanje_3 = ugibanje
    seznam = Besede.preveri_besedo_wordle(self=None, beseda=ugibanje, pravilna=trenutni_odgovor)
    stanje.seznam_pravilnosti = seznam
    stanje.izpis3 = Besede.izpisi_pravilnost(stanje.seznam_pravilnosti, stanje.ugibanje_3)
    stanje.shrani_v_datoteko(IME_DATOTEKE)
    bottle.redirect("/wordle4/")

@bottle.get("/wordle4/")
def igraj_wordle():
    iskana_beseda = Besede(Besede.izberi_besedo_wordle())
    stanje.shrani_v_datoteko(IME_DATOTEKE)
    return bottle.template("wordle4.tpl")

@bottle.post("/wordle/ugibanje4/")
def preveri_wordle():
    trenutno_stanje = stanje.preberi_iz_datoteke(IME_DATOTEKE)
    trenutni_odgovor = trenutno_stanje.odgovor
    ugibanje = bottle.request.forms["ugibanje"]
    stanje.ugibanje_4 = ugibanje
    seznam = Besede.preveri_besedo_wordle(self=None, beseda=ugibanje, pravilna=trenutni_odgovor)
    stanje.seznam_pravilnosti = seznam
    stanje.izpis4 = Besede.izpisi_pravilnost(stanje.seznam_pravilnosti, stanje.ugibanje_4)
    stanje.shrani_v_datoteko(IME_DATOTEKE)
    bottle.redirect("/wordle5/")

@bottle.get("/wordle5/")
def igraj_wordle():
    iskana_beseda = Besede(Besede.izberi_besedo_wordle())
    stanje.shrani_v_datoteko(IME_DATOTEKE)
    return bottle.template("wordle5.tpl")

@bottle.post("/wordle/ugibanje5/")
def preveri_wordle():
    trenutno_stanje = stanje.preberi_iz_datoteke(IME_DATOTEKE)
    trenutni_odgovor = trenutno_stanje.odgovor
    ugibanje = bottle.request.forms["ugibanje"]
    stanje.ugibanje_5 = ugibanje
    seznam = Besede.preveri_besedo_wordle(self=None, beseda=ugibanje, pravilna=trenutni_odgovor)
    stanje.seznam_pravilnosti = seznam
    stanje.izpis5 = Besede.izpisi_pravilnost(stanje.seznam_pravilnosti, stanje.ugibanje_5)
    stanje.shrani_v_datoteko(IME_DATOTEKE)
    bottle.redirect("/wordle6/")

@bottle.get("/wordle6/")
def igraj_wordle():
    iskana_beseda = Besede(Besede.izberi_besedo_wordle())
    stanje.shrani_v_datoteko(IME_DATOTEKE)
    return bottle.template("wordle6.tpl")

@bottle.post("/wordle/ugibanje6/")
def preveri_wordle():
    trenutno_stanje = stanje.preberi_iz_datoteke(IME_DATOTEKE)
    trenutni_odgovor = trenutno_stanje.odgovor
    ugibanje = bottle.request.forms["ugibanje"]
    stanje.ugibanje_6 = ugibanje
    seznam = Besede.preveri_besedo_wordle(self=None, beseda=ugibanje, pravilna=trenutni_odgovor)
    stanje.seznam_pravilnosti = seznam
    stanje.izpis6 = Besede.izpisi_pravilnost(stanje.seznam_pravilnosti, stanje.ugibanje_6)
    stanje.shrani_v_datoteko(IME_DATOTEKE)
    bottle.redirect("/wordle7/")

@bottle.get("/wordle7/")
def igraj_wordle():
    iskana_beseda = Besede(Besede.izberi_besedo_wordle())
    stanje.shrani_v_datoteko(IME_DATOTEKE)
    return bottle.template("wordle7.tpl")

# @bottle.get("/sprejemljive/")
# def izberi_dolzino_sprejemljive():
#     return bottle.template("sprejemljive_dolzina.tpl")
# 
# @bottle.get("/sprejemljive/<dolzina>/")
# def igraj_sprejemljive(dolzina):
#     odgovor = Besede(Besede.izberi_besedo_sprejemljive(dolzina))
#     return bottle.template("sprejemljive_igra")
# 
# @bottle.get("/vse/")
# def izberi_dolzino_vse():
#     return bottle.template("vse_dolzina.tpl")
# 
# @bottle.get("/vse/<dolzina>/")
# def igraj_vse(dolzina):
#     odgovor = Besede(Besede.izberi_besedo_vse(dolzina))
#     return bottle.template("vse_igra")



bottle.run(debug=True, reloader=True)