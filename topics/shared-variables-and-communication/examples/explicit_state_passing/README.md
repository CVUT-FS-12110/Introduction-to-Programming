# Explicitní předávání stavu

Tento příklad přepisuje `global_variable_problem` tak, aby funkce
nepracovaly se sdíleným globálním stavem.

Stav každého hráče je uložen ve slovníku, který funkce dostávají jako
parametr. Každý hráč má svůj vlastní objekt stavu — žádné sdílení,
žádný reset.

## Spuštění

```bash
python main.py
```

## Co se zlepšilo?

- Každý hráč má **vlastní stav** — přidání třetího hráče vyžaduje pouze
  vytvoření nového slovníku.
- Funkce jsou **testovatelné v izolaci** — výsledek závisí pouze
  na předaných argumentech.
- Není potřeba funkce `reset()` — každý hráč začíná s čistým slovníkem
  z `create_player()`.

## Poznámka

Funkce `answer_question` záměrně modifikuje předaný slovník — to je
její výslovný účel (*command*, nikoli *query*). Viz příklad
`mutable_argument_trap`, kde k nechtěné modifikaci dochází skrytě.
