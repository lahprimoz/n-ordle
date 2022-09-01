% rebase("osnova.tpl")
% from model import Besede
% stanje = Besede.preberi_iz_datoteke("stanje.json")
% end

<article>
    <p>
        {{ stanje.ugibanje_1 }} <br>
        {{ stanje.ugibanje_2 }} <br>
        {{ stanje.ugibanje_3 }} <br>
        {{ stanje.ugibanje_4 }} <br>
        {{ stanje.ugibanje_5 }} <br>
        {{ stanje.ugibanje_6 }} <br>
    </p>
</article>

<form method="POST" action="/nova_beseda/">
<button>Nova beseda</button>
</form>