# Šablona prezentací

Projektová šablona vychází z původního motivu [CVUT presentation beamer latex](https://github.com/CVUT-FS-12110/CVUT_presentation_beamer_latex).

Oproti původní verzi:

- neobsahuje ani nevyžaduje písmo Technika,
- používá standardní a přenosné písmo Latin Modern Sans dodávané s LaTeXem,
- zachovává poměr stran podkladových obrázků, takže logo ČVUT není deformované,
- funguje s pdfLaTeXem i XeLaTeXem,
- bezpečně zpracuje prázdného autora, instituci a datum,
- používá jednotné české pozadí uložené pouze v této složce.

## Použití

1. Zkopírujte `template.tex` do `topics/<tema>/lecture/presentation.tex`.
2. Upravte název a obsah prezentace.
3. Ze složky `lecture` spusťte:

```powershell
pdflatex -interaction=nonstopmode -halt-on-error presentation.tex
pdflatex -interaction=nonstopmode -halt-on-error presentation.tex
```

Relativní cesta `../../../utils/presentation-template` předpokládá standardní umístění `topics/<tema>/lecture/`.

Do složky tématu patří pouze `presentation.tex`, výsledný `presentation.pdf` a skutečné zdroje prezentace, například vlastní obrázky nebo data. Pomocné soubory LaTeXu jsou ignorované pomocí kořenového `.gitignore`.
