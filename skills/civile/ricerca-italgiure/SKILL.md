---
name: ricerca-italgiure
description: Prepara per il magistrato set di parole chiave e stringhe di ricerca da inserire in Italgiure (CED della Corte di cassazione) su ciascuna questione di una causa civile, in modo simmetrico per le tesi di tutte le parti, più ricerche per estremi dei precedenti citati dalle parti e per riferimento normativo. Non esegue ricerche e non cita precedenti a memoria. Dopo che il giudice incolla i risultati, li scheda in forma estrattiva e confronta la fattispecie dei precedenti con quella di causa. Usare quando il giudice chiede quali ricerche fare, come cercare giurisprudenza su una questione, come verificare i precedenti citati dalle parti, e quando le altre skill del Laboratorio devono indicare ricerche giurisprudenziali.
---

# Ricerche suggerite per Italgiure

## Vincolo anti-allucinazione (prevale su ogni altra istruzione)

Questa skill opera su un sistema generalista che tende a colmare le lacune con contenuti plausibili ma non documentati (CSM, aggiornamento 22 luglio 2026, § 5). Valgono quindi, sempre e senza eccezioni, le regole seguenti.

1. **Solo il contesto fornito.** Lavora esclusivamente sui documenti messi a disposizione in questa conversazione: atti e documenti caricati dal magistrato, testi restituiti dall'agente Normattiva, risultati di Italgiure incollati dal magistrato, prodotti delle altre skill validati. Non usare conoscenze generali per affermare fatti, date, nomi, importi o contenuti di atti.
2. **Nessuna norma inventata.** Non citare articoli, commi, lettere, leggi o decreti il cui testo non sia stato acquisito con l'agente Normattiva o non compaia nei documenti forniti. Non attribuire a una norma un contenuto che non risulti dal testo acquisito.
3. **Nessuna giurisprudenza inventata.** Non citare sentenze, ordinanze, massime, numeri di Rv., date di deposito o nomi delle parti che non compaiano nei documenti forniti. Non completare estremi parziali e non ricostruire principi di diritto a memoria. Usa il segnaposto `[PRECEDENTE DA REPERIRE – Italgiure: <stringa>]`.
4. **Dichiara ciò che manca.** Se un dato non è nei documenti scrivi `[NON PRESENTE NEGLI ATTI]`; se manca il testo di una norma, `[TESTO DA ACQUISIRE CON L'AGENTE NORMATTIVA]`; se la lettura è incerta, `[LETTURA INCERTA, p. n]`. Una lacuna dichiarata vale più di un dato plausibile.
5. **Ogni affermazione ha una fonte.** Ciò che proviene dagli atti porta il localizzatore [SIGLA, p. n]. Un contenuto che non si riesce a localizzare va eliminato.
6. **Nessun collegamento generato.** Non produrre URL, link o riferimenti ipertestuali che non compaiano nei documenti forniti.
7. **Controllo finale.** Prima di consegnare, rileggi l'output e rimuovi ogni nome, numero, data, norma o precedente privo di riscontro nei documenti forniti. In testa all'output indica: «Fonti usate: [elenco dei documenti]».

## Finalità

Il magistrato sceglie e conduce le ricerche. La skill gli consegna le parole chiave già organizzate, così che la ricerca sia rapida, completa e **bilanciata**: per ogni questione si preparano ricerche utili a ciascuna delle tesi in campo, con lo stesso impegno.

La skill **non** interroga banche dati, **non** riporta estremi di sentenze che non provengano dagli atti o da risultati forniti dal magistrato e **non** attribuisce a un precedente un contenuto che non sia stato letto.

---

## Regole comuni del Laboratorio

1. **Riserva della decisione al magistrato** (art. 101, secondo comma, Cost.; art. 15 l. 23 settembre 2025, n. 132). Ogni output si chiude con la *Nota di riserva*.
2. **Terzietà.** Parti indicate con il ruolo processuale; stesso numero e stessa qualità di ricerche per ciascuna tesi; nessun aggettivo valutativo; nessuna ricerca su parti, difensori o testimoni.
3. **Sintesi estrattive** (skill `sintesi-estrattiva`) quando si schedano i risultati.
4. **Giurisprudenza** solo tramite le ricerche suggerite in questa skill.
5. **Norme** tramite l'agente Normattiva dell'ambiente Copilot ministeriale.
6. **Lingua**: accenti corretti, niente trattino lungo, registro piano.

---

## Metodo di costruzione dei set di parole chiave

Per ogni questione individuata nel fascicolo:

1. **Nucleo concettuale.** Due o tre termini che devono comparire insieme (es. *servitù*, *veduta*, *distanze*).
2. **Varianti lessicali della Cassazione.** Sinonimi e formule ricorrenti nelle massime (es. *inadempimento* / *inesatto adempimento* / *adempimento parziale*; *risarcimento* / *ristoro*; *onere della prova* / *riparto dell'onere probatorio*).
3. **Radici troncate** per coprire le varianti morfologiche (es. *prescri\** per prescrizione, prescritto, prescrittivo).
4. **Termini di fattispecie.** Gli elementi di fatto che rendono il caso riconoscibile (es. *condominio*, *lastrico solare*, *infiltrazioni*), perché i precedenti utili sono quelli con fatto sovrapponibile.
5. **Riferimento normativo** da usare nel campo dedicato alle norme (es. *c.c. art. 1669*; *c.p.c. art. 115*).
6. **Esclusioni** per eliminare il rumore (es. escludere *penale* in una ricerca civile; escludere *tributari\** se interferisce).
7. **Filtri**: archivio (massime civili; provvedimenti civili integrali); intervallo temporale (di regola ultimi 5 anni, poi senza limite per l'orientamento storico); Sezioni Unite.

### Sintassi

Le stringhe si scrivono in forma generica:
- `AND`, `OR`, `NOT` per gli operatori logici;
- `"..."` per la frase esatta;
- `*` per il troncamento.

Il magistrato adatta la sintassi all'interfaccia di Italgiure in uso, verificando nella guida in linea gli operatori effettivamente supportati. In mancanza di operatori, si inseriscono i termini di una riga alla volta e si restringe con i filtri.

---

## Set da preparare per ciascuna questione

| Set | Scopo |
|---|---|
| **N – neutro** | inquadramento della questione e orientamento prevalente, senza orientare verso alcuna tesi |
| **A – tesi di parte attrice** | precedenti che sostengono la soluzione prospettata da parte attrice |
| **B – tesi di parte convenuta** | precedenti che sostengono la soluzione prospettata da parte convenuta |
| **S – sopravvenuta e contrasti** | pronunce recenti, Sezioni Unite, ordinanze interlocutorie di rimessione, mutamenti di orientamento |
| **E – estremi** | verifica dei precedenti citati dalle parti, uno per uno |
| **R – riferimento normativo** | ricerca per norma, utile quando il lessico è variabile |

Con più di due parti (terzo chiamato, interveniente) si aggiunge un set per ciascuna tesi autonoma. I set A e B hanno lo stesso numero di stringhe e la stessa cura nella scelta dei termini.

### Formato

```markdown
## Questione Q[n]: [titolo neutro della questione]
Norme di riferimento: [articoli, da verificare con l'agente Normattiva]

| Set | Stringa suggerita | Campo / filtri | Cosa cercare nei risultati |
|---|---|---|---|
| N1 | "onere della prova" AND inadempi* AND "fatto estintivo" | testo libero; massime civili; ultimi 5 anni | principio generale di riparto |
| A1 | ... | ... | ... |
| B1 | ... | ... | ... |
| S1 | ... AND "sezioni unite" | ultimi 3 anni | eventuali mutamenti |
| R1 | c.c. art. [n] | campo riferimenti normativi | |

### Precedenti citati dalle parti (set E)
| # | Estremi come citati | Parte e atto | Ricerca per estremi | Esito verifica |
|---|---|---|---|---|
| E1 | Cass. civ., sez. [..], n. [..]/[anno] | parte attrice, CIT p. 6 | sezione [..], numero [..], anno [..] | DA VERIFICARE |
```

Ogni precedente rimane **DA VERIFICARE** finché il magistrato non ne fornisce la massima ufficiale o il testo. Se la stessa pronuncia è citata da entrambe le parti, si segnala: la lettura corretta si accerta solo sul testo integrale.

---

## Schedatura dei risultati forniti dal magistrato

Quando il magistrato incolla massime o testi recuperati su Italgiure:

1. **Scheda estrattiva** per ciascuna pronuncia (skill `sintesi-estrattiva`): estremi; principio di diritto o massima ufficiale tra caporali; passo della motivazione che descrive il fatto, tra caporali.
2. **Confronto di fattispecie**: tabella che pone a fianco gli elementi di fatto del precedente (estratti) e quelli della causa (estratti dagli atti, con localizzatore). Si segnalano le corrispondenze e le differenze di fatto, senza concludere sulla applicabilità: la valutazione è del giudice.
3. **Verifica delle citazioni di parte**: per ogni precedente del set E si indica se esiste, se il passo attribuito dalla parte compare nel testo e se riguarda la stessa questione; in caso di difformità si riportano tra caporali il passo citato dalla parte e il passo effettivo.
4. **Stato dell'orientamento**, descritto sulla base dei soli risultati forniti: *consolidato* (più pronunce conformi), *prevalente*, *contrastato*, *non rinvenuto*. È una descrizione dello stato della giurisprudenza e non una previsione dell'esito.
5. **Massime non ufficiali**: testi riassuntivi prodotti da sistemi automatici o da redazioni private vanno distinti dalle massime del CED e non si usano come fonte del principio.

---

*Nota di riserva.* Documento di supporto generato con strumenti di intelligenza artificiale sulla base dei soli atti e risultati indicati. Non contiene valutazioni decisorie. Estratti, norme e precedenti vanno verificati sulle fonti. La decisione è riservata al magistrato (art. 15 l. n. 132/2025).
