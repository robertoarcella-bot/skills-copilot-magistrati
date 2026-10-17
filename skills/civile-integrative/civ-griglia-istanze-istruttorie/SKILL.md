---
name: civ-griglia-istanze-istruttorie
description: Griglia descrittiva delle istanze istruttorie di una causa civile per il magistrato - per ogni capitolo di prova (testimoniale, interrogatorio formale, giuramento) e per ogni altra istanza (CTU, esibizione, ordine di ispezione, richiesta di informazioni alla PA) indica la parte, l'atto e il termine di deduzione, il fatto cui si riferisce con il codice di presa di posizione della mappatura (DC, CS, CN, NP, PI), i testi indicati e indicatori descrittivi (presenza di apprezzamenti, riferimento a fatti documentali, ripetizioni, prova contraria, capitoli identici tra le parti), in modo simmetrico tra le parti. L'ammissibilità e la rilevanza restano al giudice. Produce GRIGLIA_ISTRUTTORIA_[RG].md. Usare quando il giudice prepara l'ordinanza istruttoria, l'udienza ex art. 183 c.p.c., la decisione sulle prove, o chiede di esaminare i capitoli di prova.
---

# Griglia delle istanze istruttorie (giudice civile)

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

Consentire al giudice di decidere sulle prove con tutti i capitoli davanti, ciascuno collegato al fatto cui si riferisce e alla presa di posizione dell'altra parte. La griglia descrive: non dice se un capitolo è ammissibile, rilevante o generico.

---

## Regole comuni del Laboratorio – settore civile

1. **Riserva della decisione al magistrato.** Ogni decisione sull'interpretazione e sull'applicazione della legge, sulla valutazione dei fatti e delle prove e sull'adozione dei provvedimenti spetta al magistrato (art. 101, secondo comma, Cost.; art. 15, comma 1, l. 23 settembre 2025, n. 132). Ogni output si chiude con la *Nota di riserva*.
2. **Perimetro degli usi consentiti** (CSM, raccomandazioni 8 ottobre 2025 e aggiornamento 22 luglio 2026, pratica 118/VV/2024).
   - Usi ammessi pertinenti: classificazione degli atti per tipologia e funzione; analisi strutturata del contenuto degli atti delle parti per ricostruire le posizioni processuali; sintesi documentale; confronto tra le posizioni ai fini del thema decidendum e del thema probandum; supporto agli uffici «affari semplici» per attività seriali a bassa complessità; controllo della documentazione contabile e delle certificazioni prodotte in atti; supporto alla consultazione di banche dati; revisione linguistica e stilistica; tabelle e calendari.
   - Usi esclusi: formulazione del dispositivo; affidamento della redazione dei provvedimenti giurisdizionali, anche in bozza; valutazione autonoma delle prove; formazione del convincimento del giudice.
   - Si opera **solo nel tenant istituzionale Microsoft 365 Copilot del Ministero della giustizia**; è vietato l'uso di versioni consumer o di altri sistemi non autorizzati (art. 15, comma 3, l. n. 132/2025).
3. **Checkpoint bloccanti.** Il flusso si ferma a ogni CHECKPOINT indicato nel workflow e riprende solo dopo la validazione espressa del magistrato («confermo», con eventuali correzioni). In assenza di validazione la skill non passa alla fase successiva e non ne anticipa i contenuti.
4. **Dati e riservatezza.** L'immissione di atti con dati personali è consentita nel tenant ministeriale; l'anonimizzazione preventiva resta raccomandata quando i dati identificativi non servono alla finalità. Si immettono solo gli atti necessari (minimizzazione). Cautela rafforzata, con pseudonimizzazione salvo necessità, per minori, procedimenti di famiglia e persone, dati sulla salute e altre categorie particolari (art. 9 reg. UE 2016/679). Nessuna ricerca esterna su parti, difensori, testimoni o consulenti.
5. **Terzietà.** Le parti si indicano con il ruolo processuale; stessa struttura e stessa analiticità per ciascuna parte; nessun aggettivo valutativo; nessun fatto estraneo agli atti; le questioni rilevabili d'ufficio si segnalano soltanto, con l'avvertenza dell'art. 101, secondo comma, c.p.c.
6. **Sintesi estrattive.** Ogni contenuto degli atti si riporta tra caporali con localizzatore [SIGLA, p. n, § n]. Domande, eccezioni, conclusioni, capitoli di prova, quesiti e parti decisorie sempre per intero. Mappa di copertura obbligatoria; se incompleta, avviso in testa.
7. **Giurisprudenza.** Nessuna ricerca automatica e nessun precedente citato a memoria. Si propongono stringhe per Italgiure, simmetriche per le tesi di ciascuna parte; i precedenti citati negli atti restano DA VERIFICARE finché il giudice non ne fornisce massima o testo.
8. **Norme: agente Normattiva.** Nessun testo normativo a memoria. Si interpella l'agente Normattiva reso disponibile dal Ministero nell'ambiente Copilot dei magistrati (`@` e selezione dell'agente), oppure si consegna la richiesta pronta:
   > @Normattiva Riporta il testo dell'art. [n] [fonte] nella versione vigente al [data rilevante], e indica le modifiche successive con decorrenza e disciplina transitoria.

   Data rilevante: data del fatto o del rapporto per le norme sostanziali; data di instaurazione del giudizio o di compimento dell'atto per le norme processuali. Fino alla risposta: [TESTO DA ACQUISIRE CON L'AGENTE NORMATTIVA].
9. **Lingua.** Vocali accentate corrette; niente trattino lungo (—); registro tecnico e piano.

---

## Prerequisiti

Se nella cartella esiste `MAPPATURA_FATTI_[RG].md` (skill `mappatura-fatti-giudice`) aggiornata alle memorie istruttorie, usarne la numerazione dei fatti (A1, B1, ...) e i codici. Se manca, eseguire la mappatura o, su indicazione del giudice, procedere segnalando che i codici sono provvisori.

Atti da leggere: atti introduttivi; memorie ex art. 171-ter c.p.c. (o ex art. 183, sesto comma, nel regime previgente); verbali; eventuali provvedimenti istruttori già emessi.

**CHECKPOINT 1.** Indicare gli atti individuati come contenenti istanze istruttorie e la versione della mappatura usata; attendere conferma.

---

## Indicatori descrittivi

Ogni indicatore è un dato osservabile nel testo, non un giudizio. Si segnala con «sì» e con l'estratto che lo fa emergere.

| Codice | Indicatore | Come si rileva |
|---|---|---|
| I1 | contiene termini di apprezzamento o di qualificazione giuridica | presenza nel capitolo di parole quali «inadempiente», «colpevole», «illegittimo», «grave» (estratto) |
| I2 | riguarda un fatto risultante da documento prodotto | rinvio a DOC [n] o coincidenza con il contenuto di un documento (indicarlo) |
| I3 | riproduce, in tutto o in parte, un altro capitolo | numero del capitolo coincidente |
| I4 | è formulato come prova contraria su capitolo avversario | capitolo avversario corrispondente |
| I5 | è identico o speculare a un capitolo dell'altra parte | capitolo corrispondente |
| I6 | si riferisce a un fatto con codice DC nella mappatura | rif. A/B |
| I7 | indica circostanze di tempo e di luogo | sì / no, con estratto |
| I8 | il teste indicato è anche parte, rappresentante o legato alla parte secondo gli atti | solo ciò che risulta dagli atti (estratto); nessuna ricerca esterna |
| I9 | dedotto in atto il cui deposito va confrontato con il termine (date) | data di deposito e termine risultante |

La valutazione su capacità a testimoniare, genericità, valutatività, superfluità, tardività resta al giudice: gli indicatori servono a trovarle, non a deciderle.

---

## Workflow

1. Estrarre per intero ogni capitolo e ogni istanza, nell'ordine dell'atto, con localizzatore.
2. Collegare ciascun capitolo al fatto della mappatura e riportarne il codice.
3. Compilare gli indicatori, solo con «sì» motivato da estratto; lasciare vuoto se non ricorre.
4. Compilare la tabella delle altre istanze (CTU, esibizione, ispezione, informazioni).
5. Verificare la simmetria: stesse colonne e stesso grado di dettaglio per tutte le parti.

**CHECKPOINT 2.** Presentare la griglia. Su richiesta del giudice, aggiungere un prospetto dei fatti controversi privi di qualunque istanza istruttoria (dato descrittivo, senza conseguenze sull'onere della prova).

---

## Template

```markdown
# GRIGLIA DELLE ISTANZE ISTRUTTORIE
**[Ufficio]**, R.G. n. [..] – **Data**: [..] – **Mappatura usata**: [versione]
**Atti esaminati**: [sigle] – **Termini per le istanze risultanti dagli atti**: [date e fonte]

## 1. Prove orali di parte attrice
| Cap. | Testo integrale | Fonte | Fatto (rif.) | Codice | Testi indicati | Indicatori (codice: estratto) |
|---|---|---|---|---|---|---|

## 2. Prove orali di parte convenuta
[stessa tabella]

[Sezioni ulteriori, identiche, per terzi chiamati e intervenienti.]

## 3. Interrogatorio formale e giuramento
| Parte istante | Capitoli (testo integrale) | Fonte | Destinatario | Fatto (rif.) | Indicatori |
|---|---|---|---|---|---|

## 4. Altre istanze
| # | Istanza (testo integrale) | Parte | Atto e data | Oggetto | Fatti cui si riferisce | Documenti o dati indicati a sostegno |
|---|---|---|---|---|---|---|
> Per le istanze di CTU: riportare i quesiti proposti dalla parte. Per l'esibizione: documento richiesto e detentore indicati dalla parte.

## 5. Provvedimenti istruttori già emessi
| Provvedimento | Parte decisoria (estratto) | Capitoli o istanze interessati |
|---|---|---|

## 6. Quadro di simmetria
| Parte | Capitoli | Testi | Altre istanze | Capitoli con almeno un indicatore |
|---|---|---|---|---|

## 7. Fatti controversi senza istanze istruttorie (solo su richiesta)
| Fatto (rif.) | Codice | Parte che lo ha allegato |
|---|---|---|

## 8. Mappa di copertura
| Sigla | Atto | Letto per intero | Capitoli e istanze estratti |
|---|---|---|---|
**Indicatori**: capitoli estratti [n per parte]; capitoli collegati a un fatto [x/y]; estratti verificati letteralmente [x/y].

---
*Nota di riserva.* Documento di supporto generato con strumenti di intelligenza artificiale nel tenant ministeriale, sulla base dei soli atti indicati nella mappa di copertura. Non contiene valutazioni decisorie né parti di provvedimento. Estratti, norme e precedenti vanno verificati sulle fonti. La decisione e la redazione del provvedimento sono riservate al magistrato (art. 15 l. n. 132/2025).
```

## Controlli finali

- tutti i capitoli trascritti per intero, nessuno parafrasato;
- ogni «sì» negli indicatori è accompagnato da estratto;
- nessuna parola come «inammissibile», «generico», «valutativo», «superfluo» fuori dalle citazioni testuali;
- le sezioni delle parti hanno la stessa struttura;
- nessuna bozza di ordinanza.

Se l'ambiente consente di salvare file, salvare `GRIGLIA_ISTRUTTORIA_[RG].md` nella cartella del fascicolo; altrimenti restituire il testo in chat.

---

*Nota di riserva.* Documento di supporto generato con strumenti di intelligenza artificiale nel tenant ministeriale, sulla base dei soli atti indicati nella mappa di copertura. Non contiene valutazioni decisorie né parti di provvedimento. Estratti, norme e precedenti vanno verificati sulle fonti. La decisione e la redazione del provvedimento sono riservate al magistrato (art. 15 l. n. 132/2025).
