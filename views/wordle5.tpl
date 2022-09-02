% rebase("osnova.tpl")
% from model import Besede
% stanje = Besede.preberi_iz_datoteke("stanje.json")
% end

<article>
    <p>
        <form method="POST" action="/wordle/ugibanje5/">
        <input type="text" name="ugibanje" size="2" minlength="5" maxlength="5" required autofocus>
        </form>
    </p>
</article>


<article>
    <p>
        {{Besede.izpisi_pravilnost(stanje.seznam_pravilnosti, stanje.ugibanje_1)}} <br>
        {{Besede.izpisi_pravilnost(stanje.seznam_pravilnosti, stanje.ugibanje_2)}} <br>
        {{Besede.izpisi_pravilnost(stanje.seznam_pravilnosti, stanje.ugibanje_3)}} <br>
        {{Besede.izpisi_pravilnost(stanje.seznam_pravilnosti, stanje.ugibanje_4)}}
    </p>
</article>