% rebase("osnova.tpl")
<h2>
    Pozdravljeni v n-ordle.
</h2>

<h2>Izberite način igre:</h2>
<ol>
    <li> <a href="/wordle/"> <button> Klasični wordle </button> <a> </li>
    <li> <a href="/sprejemljive/"> <button> Wordle z običajnimi besedami </button> <a> </li>
    <li> <a href="/vse/"> <button> Wordle z besedami, ki lahko vsebujejo števila in/ali posebne znake </button> <a> </li>
</ol>

<form method="POST" action="/nova_beseda/">
<button>Nova beseda</button>
</form>