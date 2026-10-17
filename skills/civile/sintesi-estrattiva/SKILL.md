---
name: sintesi-estrattiva
description: Sintesi estrattiva e verificabile di atti e documenti del processo civile, per il magistrato. La sintesi è composta solo da passi testuali citati tra caporali con localizzazione (atto, pagina, paragrafo), senza parafrasi, e si chiude con una mappa di copertura che documenta sezione per sezione cosa è stato estratto, cosa è stato omesso e perché, con indicatori di completezza. Usare quando il giudice chiede di riassumere, sintetizzare o schedare un atto di parte, un verbale, una CTU, un provvedimento o un documento, e quando le skill analisi-fascicolo-giudice, mappatura-fatti-giudice, valutazione-imparziale-questioni o bozza-sentenza-civile richiedono una sintesi.
---

# Sintesi estrattiva con prova di completezza

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

Il magistrato deve potersi fidare della sintesi senza rileggere l'atto e, quando lo ritiene, verificarla in pochi secondi. La sintesi riproduce quindi le parole dell'atto o del documento e mai una loro riformulazione: ogni parafrasi contiene già una lettura del testo, e la lettura spetta al giudice.

La sintesi è **estrattiva** (seleziona e riporta passi dell'originale) e mai **astrattiva** (riscrive il contenuto con parole proprie).

---

## Regole comuni del Laboratorio (valide per tutte le skill)

1. **Riserva della decisione al magistrato.** Il prodotto è materiale di studio. Ogni decisione sull'interpretazione e sull'applicazione della legge, sulla valutazione dei fatti e delle prove e sull'adozione del provvedimento spetta al magistrato (art. 101, secondo comma, Cost.; art. 15 l. 23 settembre 2025, n. 132). Ogni output si chiude con la *Nota di riserva*.
2. **Terzietà.** Le parti si indicano con il ruolo processuale (parte attrice, parte convenuta, terzo chiamato, interveniente). Stessa struttura e stesso grado di analiticità per ciascuna parte. Nessun aggettivo valutativo sulle difese. Nessun fatto estraneo agli atti e nessuna ricerca esterna su parti, difensori o testimoni.
3. **Sintesi estrattive** secondo questa skill.
4. **Giurisprudenza.** Nessuna ricerca autonoma e nessun precedente citato a memoria: si suggeriscono set di parole chiave per Italgiure (skill `ricerca-italgiure`).
5. **Norme.** Nessun testo normativo riportato a memoria: si interpella l'agente Normattiva messo a disposizione dal Ministero della Giustizia nell'ambiente Copilot dei magistrati.
6. **Lingua.** Italiano con vocali accentate corrette (à, è, é, ì, ò, ù); niente trattino lungo (—); registro piano, senza formule enfatiche.

---

## Regole di estrazione

1. **Unità minima.** Ogni estratto è formato da un passo testuale tra caporali e da un localizzatore tra parentesi quadre:
   «il conduttore ha omesso il pagamento dei canoni da marzo a settembre 2024» [CIT, p. 3, § 2]
2. **Sigle degli atti.** All'inizio della sintesi si dichiara la legenda delle sigle (es. CIT = atto di citazione; COMP = comparsa di costituzione e risposta; M1-A = memoria ex art. 171-ter, n. 1, c.p.c. di parte attrice; VERB 12.03.2025 = verbale d'udienza; CTU = relazione di consulenza; DOC A3 = documento n. 3 di parte attrice).
3. **Fedeltà letterale.** Si conservano grafia, maiuscole e refusi dell'originale (eventualmente con [sic]). Le parti omesse all'interno del passo si indicano con [...]. Dentro i caporali non si aggiunge nulla; le integrazioni indispensabili alla comprensione vanno tra parentesi quadre: «lo stesso [il convenuto] ha ricevuto la somma».
4. **Testo di raccordo.** Sono ammessi soltanto:
   - etichette neutre di argomento (es. *Sulla data di consegna:*), in corsivo;
   - indicazioni di provenienza (es. *Parte convenuta, comparsa:*);
   - i verbi di attribuzione «deduce», «afferma», «chiede», «eccepisce», «produce», «contesta», solo quando corrispondono all'operazione compiuta nell'atto.
   Sono vietati i verbi che qualificano la condotta processuale («ammette», «riconosce», «lamenta», «pretende», «sostiene a torto»): la qualificazione di una dichiarazione come ammissione o non contestazione è valutazione riservata al giudice.
5. **Una fonte per estratto.** Ogni estratto si attribuisce a una sola parte e a un solo atto. Non si fondono in un unico passo deduzioni di atti diversi.
6. **Elementi da riportare per intero, senza tagli:** conclusioni; domande (anche riconvenzionali); eccezioni in senso stretto; capitoli di prova e indicazione dei testi; quesiti al CTU e risposte conclusive; dispositivi e parti decisorie dei provvedimenti; formule di rinuncia o di accettazione.
7. **Ordine.** Si segue l'ordine dell'originale. Se il magistrato chiede un ordinamento per temi, si raggruppa per tema conservando i localizzatori.
8. **Testo illeggibile.** Per scansioni e OCR incerti si scrive [ILLEGIBILE, p. n] o [LETTURA INCERTA, p. n] e non si ricostruisce il testo.
9. **Contenuti non testuali** (fotografie, grafici, planimetrie, tabelle complesse): si indica soltanto ciò che è visibile, marcandolo come [DESCRIZIONE, p. n: ...]. È l'unica deroga alla regola estrattiva e va contata negli indicatori.

---

## Prova di completezza

La completezza si dimostra, non si dichiara. Prima dell'estrazione si scompone l'originale; dopo l'estrazione si rende conto di ogni sua parte.

### A. Indice dell'originale

Si elencano le partizioni dell'atto: titoli e paragrafi numerati; in mancanza, blocchi di pagine (es. pp. 1-2, 3-4). Ogni partizione riceve un codice (S1, S2, ...).

### B. Mappa di copertura

| Sezione | Pagine | Esito | Estratti | Motivo dell'omissione |
|---|---|---|---|---|
| S1 Intestazione e parti | 1 | E | E1-E2 | |
| S2 Premessa | 1-2 | O-R | | ripete S4 (E7-E9) |
| S3 Richiami giurisprudenziali generali | 5-7 | O-N | | massime riportate senza riferimento ai fatti di causa; elenco: [estremi come citati] |
| S4 ... | | | | |

Legenda degli esiti:
- **E**: estratta (indicare gli estratti);
- **O-S**: omessa perché formula di stile (procura, relata, formule di chiusura);
- **O-R**: omessa perché ripete altra sezione (indicare quale);
- **O-N**: omessa per altra ragione, da motivare in una riga. Le omissioni O-N comportano una scelta e vanno sempre elencate in chiaro, perché il magistrato possa controllarle.

I precedenti giurisprudenziali citati dalla parte non si omettono mai del tutto: se ne riportano almeno gli estremi come indicati nell'atto.

### C. Elementi necessari per tipo di atto

| Tipo di atto | Elementi che la sintesi deve contenere |
|---|---|
| Citazione / ricorso | parti e difensori; petitum; fatti costitutivi; ragioni di diritto; conclusioni; mezzi di prova; elenco documenti; condizioni di procedibilità dichiarate |
| Comparsa di risposta | eccezioni processuali; eccezioni di merito; prese di posizione sui fatti avversari; domande riconvenzionali; chiamata di terzo; conclusioni; prove; documenti |
| Memorie ex art. 171-ter c.p.c. | precisazioni o modifiche di domande ed eccezioni (n. 1); mezzi di prova e produzioni (n. 2); prova contraria e repliche (n. 3) |
| Verbale d'udienza | presenti; dichiarazioni e istanze delle parti; provvedimenti del giudice; rinvio e incombenti |
| Provvedimento del giudice | dispositivo; ragioni essenziali; termini assegnati |
| CTU | quesiti; operazioni; risposte conclusive; osservazioni delle parti e repliche del CTU |
| Comparsa conclusionale / replica | conclusioni; argomenti per questione; nuove deduzioni (da segnalare, per il vaglio di ammissibilità del giudice) |
| Documento | natura; data; autore; sottoscrizioni; passi riferibili ai fatti allegati |

### D. Indicatori

- **Copertura delle sezioni** = sezioni con esito E, O-S, O-R o O-N motivato / sezioni totali. Deve essere 100%.
- **Sezioni estratte** = sezioni E / sezioni totali (dato informativo).
- **Elementi necessari presenti** = x / y secondo la tabella C; per ogni elemento assente si scrive se manca nell'atto originale («assente nell'originale») o se manca nella sintesi (in tal caso la sintesi va integrata).
- **Deroghe**: numero di [DESCRIZIONE] e di [LETTURA INCERTA].

Se la copertura è inferiore al 100% o manca un elemento necessario presente nell'originale, in testa alla sintesi compare l'avviso **SINTESI INCOMPLETA** con l'elenco di ciò che manca.

### E. Controllo letterale

Prima della consegna si ricerca ogni estratto nel testo sorgente. Gli estratti che non si ritrovano identici si correggono o si eliminano. Si dichiara il numero di estratti verificati.

---

## Formato dell'output

```markdown
# SINTESI ESTRATTIVA – [atto], [parte], [data]
**Fascicolo**: [Ufficio], R.G. n. [...]
**Fonte**: [nome file], pp. [n]
**Legenda sigle**: [...]

[eventuale avviso SINTESI INCOMPLETA]

## Estratti
*[Etichetta tema]*
E1. «...» [SIGLA, p. n, § n]
E2. «...» [SIGLA, p. n]

## Conclusioni (testo integrale)
«...» [SIGLA, p. n]

## Mappa di copertura
[tabella B]

## Elementi necessari
[tabella C compilata per il tipo di atto]

## Indicatori
- Copertura delle sezioni: [x/x = 100%]
- Sezioni estratte: [x/y]
- Elementi necessari presenti: [x/y]; assenti nell'originale: [...]
- Deroghe: [n DESCRIZIONE; n LETTURA INCERTA]
- Estratti verificati letteralmente: [n/n]

---
*Nota di riserva.* Documento di supporto generato con strumenti di intelligenza artificiale sulla base dei soli atti indicati nella mappa di copertura. Non contiene valutazioni decisorie. Estratti, norme e precedenti vanno verificati sulle fonti. La decisione è riservata al magistrato (art. 15 l. n. 132/2025).
```

Se l'ambiente consente di salvare file, salvare come `SINTESI_[sigla atto]_[parte].md` nella cartella del fascicolo; altrimenti restituire il testo in chat.

## Sintesi di più atti

Per sintetizzare più atti si produce una sintesi per atto, ciascuna con la propria mappa di copertura, e una tabella riepilogativa finale:

| Atto | Sezioni | Copertura | Elementi necessari | Deroghe |
|---|---|---|---|---|
