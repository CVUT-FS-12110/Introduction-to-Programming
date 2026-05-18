# Sdílený stav ve třídě

Tento příklad ukazuje, jak lze sdílený stav přehledně zapouzdřit do třídy.
Třída nahrazuje jak globální proměnné, tak ruční předávání slovníku —
stav je přímo svázán s instancí objektu.

## Scénář

Stejná kvízová hra jako v předchozích příkladech, tentokrát implementovaná
jako třída `Player`.

## Spuštění

```bash
python main.py
```

## Kdy použít třídu místo slovníku?

| Slovník (explicitní předávání)      | Třída                                     |
|-------------------------------------|-------------------------------------------|
| Jednoduchý stav bez vlastní logiky  | Stav s metodami, které k němu patří       |
| Funkcionální styl                   | Objektový styl                            |
| Vhodné pro jednorázové transformace | Vhodné pro dlouhodobě žijící entity       |
