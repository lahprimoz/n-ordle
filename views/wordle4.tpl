% rebase("osnova.tpl")
% from model import Besede
% stanje = Besede.preberi_iz_datoteke("stanje.json")
% end

<article>
    <p>
        <form method="POST" action="/wordle/ugibanje4/">
        <input type="text" name="ugibanje" size="2" minlength="5" maxlength="5" required autofocus>
        </form>
    </p>
</article>


<article>
    <p>
        {{ stanje.ugibanje_1 }} <br>
        {{ stanje.ugibanje_2 }} <br>
        {{ stanje.ugibanje_3 }}
    </p>
</article>