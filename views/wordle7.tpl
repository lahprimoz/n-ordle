% rebase("osnova.tpl")
% from model import Besede
% stanje = Besede.preberi_iz_datoteke("stanje.json")
% end

<article>
    <p>
        {{stanje.izpis1}} <br>
        {{stanje.izpis2}} <br>
        {{stanje.izpis3}} <br>
        {{stanje.izpis4}} <br>
        {{stanje.izpis5}} <br>
        {{Besede.izpisi_pravilnost(stanje.seznam_pravilnosti, stanje.ugibanje_6)}} <br>
        Beseda je: {{stanje.odgovor}}
    </p>
</article>

<form method="POST" action="/nova_beseda/">
<button>Nova beseda</button>
</form>