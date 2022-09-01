from model import Besede
import bottle

@bottle.get("/")
def zacetna_stran():
    return bottle.template("zacetna_stran.tpl")

@bottle.get("/wordle/")
def igraj_wordle():
    odgovor = Besede(Besede.izberi_besedo_wordle())
    return bottle.template("wordle.tpl")

@bottle.get("/sprejemljive/")
def izberi_dolzino_sprejemljive():
    return bottle.template("sprejemljive_dolzina.tpl")

@bottle.get("/sprejemljive/<dolzina>/")
def igraj_sprejemljive(dolzina):
    odgovor = Besede(Besede.izberi_besedo_sprejemljive(dolzina))
    return bottle.template(f"sprejemljive_{dolzina}")

@bottle.get("/vse/")
def izberi_dolzino_vse():
    return bottle.template("vse_dolzina.tpl")

@bottle.get("/vse/<dolzina>/")
def igraj_vse(dolzina):
    odgovor = Besede(Besede.izberi_besedo_vse(dolzina))
    return bottle.template(f"vse_{dolzina}")



bottle.run(debug=True, reloader=True)