# Problém globálního stavu

Tento příklad ukazuje typický způsob, jak začínající programátoři sdílejí stav
mezi funkcemi — pomocí globálních proměnných. Na první pohled kód funguje,
ale obsahuje skryté problémy.

## Scénář

Program sleduje skóre hráče v kvízové hře. Skóre, počet správných odpovědí
a celkový počet otázek jsou uloženy v globálních proměnných.

## Spuštění

```bash
python main.py
```

## Kde je problém?

Kód zdánlivě funguje pro jednoho hráče. Zkuste odpovědět na tyto otázky:

- Co se stane, pokud chceme sledovat skóre dvou hráčů **zároveň**?
- Jak ověříme správnost funkce `answer_question` v izolaci (unit test),
  aniž bychom záviseli na globálním stavu?
- Závisí výsledek na **pořadí**, ve kterém funkce voláme?

Globální proměnné vytvářejí **skrytou závislost** — funkce nejsou nezávislé,
sdílejí stav, který není vidět v jejich signatuře.