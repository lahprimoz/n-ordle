% rebase("osnova.tpl")
% from model import Besede
% stanje = Besede.preberi_iz_datoteke("stanje.json")
% end

<article>
    <p>
        {{Besede.izpisi_pravilnost(stanje.seznam_pravilnosti, stanje.ugibanje_1)}} <br>
        {{Besede.izpisi_pravilnost(stanje.seznam_pravilnosti, stanje.ugibanje_2)}} <br>
        {{Besede.izpisi_pravilnost(stanje.seznam_pravilnosti, stanje.ugibanje_3)}} <br>
        {{Besede.izpisi_pravilnost(stanje.seznam_pravilnosti, stanje.ugibanje_4)}} <br>
        {{Besede.izpisi_pravilnost(stanje.seznam_pravilnosti, stanje.ugibanje_5)}} <br>
        {{Besede.izpisi_pravilnost(stanje.seznam_pravilnosti, stanje.ugibanje_6)}} <br>
        Beseda je: {{stanje.odgovor}}
    </p>
</article>

<form method="POST" action="/nova_beseda/">
<button>Nova beseda</button>
</form>