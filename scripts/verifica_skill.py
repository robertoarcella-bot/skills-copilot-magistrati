"""Controllo di forma delle skill del Laboratorio.

Uso: python scripts/verifica_skill.py [cartella]   (default: skills)

Per ogni SKILL.md verifica:
- frontmatter YAML delimitato da '---' con 'name' e 'description';
- 'name' uguale al nome della cartella, solo minuscole, cifre e trattini, max 64 caratteri;
- 'description' non vuota, max 1024 caratteri;
- presenza della 'Nota di riserva', del blocco 'Vincolo anti-allucinazione' e del richiamo all'art. 15;
- testo sotto i 20.000 caratteri (limite degli agenti di Microsoft 365 Copilot);
- assenza del trattino lungo.
Avvisa (senza bloccare) se trova sequenze che somigliano a numeri di ruolo reali.
Esce con codice 1 se c'è almeno un errore.
"""

import re
import sys
from pathlib import Path

NOME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
RUOLO_RE = re.compile(r"\b(?:R\.?G\.?(?:N\.?R\.?)?|RGNR)\s*(?:n\.?\s*)?\d{2,6}\s*/\s*\d{2,4}\b", re.I)
LIMITE_CARATTERI = 20000


def leggi_frontmatter(testo):
    if not testo.startswith("---"):
        return None, testo
    fine = testo.find("\n---", 3)
    if fine == -1:
        return None, testo
    blocco = testo[3:fine]
    campi = {}
    for riga in blocco.splitlines():
        m = re.match(r"^([A-Za-z_-]+):\s*(.*)$", riga)
        if m:
            campi[m.group(1)] = m.group(2).strip().strip('"').strip("'")
    return campi, testo[fine + 4:]


def verifica(percorso):
    errori, avvisi = [], []
    testo = percorso.read_text(encoding="utf-8")
    cartella = percorso.parent.name
    campi, corpo = leggi_frontmatter(testo)
    if campi is None:
        return ["frontmatter assente o non chiuso"], avvisi
    nome = campi.get("name", "")
    descr = campi.get("description", "")
    if not nome:
        errori.append("campo 'name' mancante")
    else:
        if nome != cartella:
            errori.append(f"'name' ({nome}) diverso dalla cartella ({cartella})")
        if not NOME_RE.match(nome) or len(nome) > 64:
            errori.append("'name' non conforme (minuscole, cifre, trattini; max 64)")
    if not descr:
        errori.append("campo 'description' mancante o vuoto")
    elif len(descr) > 1024:
        errori.append(f"'description' troppo lunga ({len(descr)} > 1024)")
    if "Nota di riserva" not in testo:
        errori.append("manca la 'Nota di riserva'")
    if "Vincolo anti-allucinazione" not in testo:
        errori.append("manca il blocco 'Vincolo anti-allucinazione'")
    if not re.search(r"art\.\s*15", testo):
        errori.append("manca il richiamo all'art. 15 l. n. 132/2025")
    if len(testo) > LIMITE_CARATTERI:
        errori.append(f"testo di {len(testo)} caratteri, oltre {LIMITE_CARATTERI}")
    # "(—)" è ammesso: è la regola che vieta il trattino lungo, citata nel testo.
    if "—" in testo.replace("(—)", ""):
        errori.append("presente il trattino lungo")
    for m in RUOLO_RE.finditer(corpo):
        if not re.search(r"\[|\.\.|x{2,}|0000", m.group(0), re.I):
            avvisi.append(f"possibile numero di ruolo reale: '{m.group(0)}'")
    return errori, avvisi


def main():
    radice = Path(sys.argv[1] if len(sys.argv) > 1 else "skills")
    files = sorted(radice.rglob("SKILL.md"))
    if not files:
        print(f"Nessun SKILL.md in {radice}")
        return 0
    totale_errori = 0
    for f in files:
        errori, avvisi = verifica(f)
        stato = "OK" if not errori else "ERRORE"
        print(f"[{stato}] {f}")
        for e in errori:
            print(f"    errore: {e}")
        for a in avvisi:
            print(f"    avviso: {a}")
        totale_errori += len(errori)
    print(f"\n{len(files)} skill controllate, {totale_errori} errori.")
    return 1 if totale_errori else 0


if __name__ == "__main__":
    sys.exit(main())
