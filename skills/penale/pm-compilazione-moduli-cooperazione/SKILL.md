---
name: pm-compilazione-moduli-cooperazione
description: Compilazione assistita dei moduli standardizzati di cooperazione giudiziaria penale - mandato d'arresto europeo (modulo allegato alla decisione quadro 2002/584/GAI; l. n. 69/2005) e ordine europeo di indagine (allegato A della direttiva 2014/41/UE; d.lgs. n. 108/2017) - a partire dagli atti del procedimento, uso espressamente ammesso dal CSM (aggiornamento 22 luglio 2026, § 8, punto 12) con supervisione e completamento obbligatori del magistrato. Riempie i campi descrittivi ricavabili dagli atti indicando la fonte di ogni dato, lascia in segnaposto i campi non ricavabili, e lascia al magistrato i campi valutativi (motivi, necessità e proporzionalità, esigenze, scelta della misura), fornendo solo i dati di supporto; controlla coerenza interna, completezza e corrispondenza con il provvedimento presupposto. Usare quando il PM o il giudice chiede di compilare o preparare un MAE, un mandato d'arresto europeo, un ordine europeo di indagine, un OEI, o di verificare un modulo già compilato.
---

# Compilazione assistita di MAE e OEI

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

Ridurre il tempo e gli errori materiali nella compilazione di moduli lunghi e rigidi, lasciando al magistrato tutte le scelte. La compilazione assistita di atti standardizzati e moduli, «quali i mandati di arresto europeo», è tra gli usi ammessi dall'aggiornamento CSM del 22 luglio 2026, a condizione della supervisione e del completamento obbligatori del magistrato. Il modulo resta un atto del magistrato che lo sottoscrive: la skill prepara una bozza dei soli campi descrittivi e un elenco di controlli.

## Input

- il provvedimento presupposto (ordinanza cautelare, sentenza o ordine di esecuzione per il MAE; decreto o provvedimento che dispone l'atto di indagine per l'OEI);
- gli atti da cui ricavare i dati (identificazione della persona, imputazioni, pene, luoghi);
- il modello ufficiale del modulo nella versione in uso presso l'ufficio (la skill non lo riproduce a memoria: se non è fornito, lo chiede);
- la lingua del modulo e lo Stato di esecuzione.

---

## Regole comuni del Laboratorio – settore penale

1. **Riserva della decisione al magistrato.** Ogni decisione sull'interpretazione e sull'applicazione della legge, sulla valutazione dei fatti e delle prove e sull'adozione dei provvedimenti spetta al magistrato (art. 15, comma 1, l. 23 settembre 2025, n. 132). La regola vale per il giudice e per il pubblico ministero: anche le scelte del PM sull'iscrizione, sulle indagini, sulle misure, sull'archiviazione e sull'esercizio dell'azione penale (art. 112 Cost.) sono valutazioni riservate. Ogni output si chiude con la *Nota di riserva*.

2. **Perimetro degli usi consentiti** (CSM, raccomandazioni 8 ottobre 2025 e aggiornamento 22 luglio 2026, pratica 118/VV/2024).
   - Usi ammessi pertinenti: classificazione degli atti per tipologia e funzione; analisi strutturata del contenuto degli atti per ricostruire le posizioni processuali; sintesi documentale; confronto tra posizioni ai fini del thema decidendum e del thema probandum; compilazione assistita di atti standardizzati e moduli (es. mandato d'arresto europeo) con completamento obbligatorio del magistrato; supporto alla consultazione di banche dati; revisione linguistica; tabelle e calendari.
   - Usi esclusi: formulazione del dispositivo; redazione, anche in bozza, della motivazione di provvedimenti giurisdizionali; valutazione autonoma delle prove (attendibilità, credibilità, peso); formazione del convincimento. Per gli atti del PM che contengono valutazioni (richieste cautelari, richieste di archiviazione, imputazione, richieste conclusive) la skill non redige la parte valutativa: prepara soltanto materiale descrittivo, che il magistrato riscrive.
   - Si opera **solo nel tenant istituzionale Microsoft 365 Copilot del Ministero della giustizia**; è vietato l'uso di versioni consumer o di altri sistemi non autorizzati (art. 15, comma 3, l. n. 132/2025).

3. **Checkpoint bloccanti.** Il flusso si ferma a ogni CHECKPOINT indicato nel workflow e riprende solo dopo la validazione espressa del magistrato («confermo», con eventuali correzioni). In assenza di validazione la skill non passa alla fase successiva e non anticipa contenuti.

4. **Dati, segreto e riservatezza.**
   - Prima di elaborare atti la skill chiede (CHECKPOINT 0) se gli atti sono ancora coperti dal segreto investigativo (art. 329 c.p.p.). Le raccomandazioni del 2025 escludono l'immissione di dati «soggetti a segreto investigativo, anche in forma indiretta»; l'aggiornamento del 2026 ha consentito l'immissione di atti con dati personali nel tenant ministeriale, ma dichiara applicabili le raccomandazioni del 2025 per ogni profilo non espressamente modificato. **Interpretazione prudenziale del Laboratorio:** finché il CSM o il Ministero non chiariscano il punto, gli atti coperti da segreto non si immettono; si lavora su atti non più segreti o su estratti minimizzati e pseudonimizzati, nel rispetto delle direttive del capo dell'ufficio.
   - Minimizzazione: si immettono solo gli atti necessari alla finalità. Pseudonimizzazione raccomandata (persone fisiche, vittime, minori, collaboratori, testimoni protetti, utenze, targhe, indirizzi).
   - Mai immettere: intercettazioni non acquisite o destinate all'archivio riservato (artt. 268-269 c.p.p.); conversazioni irrilevanti; dati sulla salute e sulla vita sessuale non indispensabili; generalità della persona offesa nei reati in cui ne è vietata la divulgazione (art. 734-bis c.p.); dati di minori.
   - Nessuna ricerca esterna su indagati, imputati, persone offese, testimoni, difensori o consulenti.

5. **Divieto di profilazione e di valutazioni predittive.** Nessuna stima del rischio di recidiva, di pericolosità, di fuga o di inquinamento probatorio; nessun giudizio sulla personalità (art. 5, par. 1, lett. d, e allegato III, punto 6, reg. UE 2024/1689). Sugli artt. 133 c.p. e 274 c.p.p. la skill riporta soltanto gli elementi che risultano dagli atti, a favore e contro, in estratto.

6. **Presunzione di non colpevolezza** (art. 27, secondo comma, Cost.; art. 115-bis c.p.p.). Linguaggio: «persona sottoposta alle indagini», «imputato», «fatto contestato», «ipotesi di reato», «persona offesa». Mai «il reo», «l'autore del reato», «la vittima del reato commesso da», né formule che diano per accertata la responsabilità.

7. **Completezza bidirezionale.**
   - *Giudice:* terzietà e imparzialità (art. 111 Cost.). Accusa e difesa (e parte civile, responsabile civile) ricevono la stessa struttura e la stessa analiticità; nessun aggettivo valutativo; questioni rilevabili d'ufficio solo segnalate; materiali non utilizzabili per la decisione (art. 526 c.p.p.) segnalati e tenuti separati.
   - *Pubblico ministero:* il PM svolge anche accertamenti su fatti e circostanze a favore della persona sottoposta alle indagini (art. 358 c.p.p.) e, nella richiesta cautelare, trasmette al giudice anche gli elementi a favore (art. 291, comma 1, c.p.p.). Ogni prodotto delle skill per il PM contiene una sezione **«Elementi a favore della persona sottoposta alle indagini»** di pari dignità rispetto a quella degli elementi a carico, compilata o dichiarata vuota dopo l'esame («Esaminati [sigle], non sono emersi elementi a favore»), e una sezione **«Ipotesi alternative compatibili con gli atti»**.

8. **Sintesi estrattive.** Ogni contenuto degli atti si riporta tra caporali con localizzatore [SIGLA, p. n] (verbali: anche pagina e riga del verbale stenotipico o minuto del file audio, se presenti). Imputazioni, richieste, dispositivi e conclusioni sempre per intero. Mappa di copertura obbligatoria; se incompleta, avviso in testa.

9. **Giurisprudenza.** Nessuna ricerca automatica e nessun precedente citato a memoria (cfr. Cass. pen., Sez. 3, n. 25455/2025, che ha annullato una sentenza di merito fondata su principi di legittimità non affermati, e Cass. pen., Sez. 3, n. 23006/2026, sui precedenti «allucinati»). Si propongono stringhe per Italgiure (archivio penale), simmetriche per le tesi di accusa e difesa; i precedenti citati negli atti restano DA VERIFICARE.

10. **Norme: agente Normattiva.** Nessun testo normativo a memoria. Si interpella l'agente Normattiva dell'ambiente Copilot ministeriale (`@` e selezione dell'agente), oppure si consegna la richiesta pronta. Norme processuali: versione vigente al compimento dell'atto (tempus regit actum) e disciplina transitoria. **Norme penali sostanziali: versione vigente alla data del fatto e tutte le versioni successive fino a oggi** (art. 2 c.p.; abolitio criminis e lex mitior):
    > @Normattiva Riporta il testo dell'art. [n] [c.p. / legge speciale] nella versione vigente al [data del fatto] e in ciascuna versione successiva fino alla data odierna, con le date di decorrenza.

    Fino alla risposta: [TESTO DA ACQUISIRE CON L'AGENTE NORMATTIVA].

11. **Lingua.** Vocali accentate corrette; niente trattino lungo (—); registro tecnico e piano; nessuna formula enfatica.

*Nota di riserva (testo da riportare in coda a ogni output).* Documento di supporto generato con strumenti di intelligenza artificiale nel tenant ministeriale, sulla base dei soli atti indicati nella mappa di copertura. Non contiene valutazioni sulla responsabilità, sull'attendibilità delle prove o sulle esigenze cautelari. Estratti, norme e precedenti vanno verificati sulle fonti. Ogni decisione è riservata al magistrato (art. 15 l. n. 132/2025).

---

## Classificazione dei campi

Prima della compilazione si classifica ogni campo del modello ufficiale fornito:

| Classe | Contenuto | Chi compila |
|---|---|---|
| **D – descrittivo** | dati anagrafici e identificativi, estremi del provvedimento, autorità, testo delle imputazioni, norme, pene inflitte o massime, date e luoghi dei fatti, contatti | la skill, con fonte per ogni dato |
| **S – scelta** | categoria di reato dell'elenco (es. 32 categorie del MAE) o caselle di opzione; urgenza; misure richieste nell'OEI | la skill propone le opzioni compatibili con gli atti, senza sceglierne una; il magistrato sceglie |
| **V – valutativo** | motivi dell'emissione; necessità e proporzionalità; descrizione delle circostanze in cui il reato è stato commesso, quando richiede selezione e qualificazione; garanzie da offrire; ogni campo che richieda un apprezzamento | il magistrato; la skill fornisce solo i dati di supporto in estratto |
| **T – traduzione** | versione nella lingua richiesta | dopo la validazione del testo italiano; traduzione assistita con verifica umana obbligatoria (uso ammesso dal CSM) |

Esempi orientativi di campi, da verificare sul modello ufficiale fornito: MAE, sezioni da (a) a (i) (identità; decisione su cui si fonda il mandato; durata della pena; decisione pronunciata in assenza; reati; altre circostanze; beni da sequestrare; eventuali pene perpetue; autorità emittente). OEI, sezioni da A a L (autorità e Stato; urgenza; atti richiesti; collegamenti con richieste precedenti; persone interessate; tipo di procedimento; motivi dell'emissione; requisiti per atti specifici; formalità; mezzi di impugnazione; autorità emittente; autorità di convalida).

## Norme da acquisire con l'agente Normattiva

> @Normattiva Riporta il testo vigente della legge 22 aprile 2005, n. 69 (artt. [..]) e del d.lgs. 21 giugno 2017, n. 108 (artt. [..]), con le modifiche successive, in particolare quelle del d.lgs. 2 febbraio 2021, n. 10 per il MAE.

Per i reati: testo delle norme incriminatrici e delle pene nella versione vigente alla data del fatto e successive (rilevante per la soglia di pena e per la doppia incriminabilità). Le fonti europee (decisione quadro, direttiva) si acquisiscono dal testo ufficiale fornito dal magistrato o dall'ufficio.

## Workflow

### CHECKPOINT 0 – Dati e segreto
Checklist delle regole comuni (punto 4). I moduli richiedono dati identificativi non pseudonimizzabili (la persona deve essere identificata): immettere solo gli atti strettamente necessari e solo nel tenant ministeriale; se il procedimento è coperto da segreto, il magistrato decide se procedere secondo le direttive dell'ufficio. Conferma espressa.

### Fase 1 – Modello e classificazione dei campi
Acquisire il modello ufficiale; classificare ogni campo (D, S, V, T). **CHECKPOINT 1**: il magistrato conferma la classificazione (può spostare un campo in V).

### Fase 2 – Compilazione dei campi D e proposte per i campi S
Ogni dato con fonte; campi non ricavabili con `[DATO NON RISULTANTE DAGLI ATTI: ..]`; per i campi S, elenco delle opzioni compatibili con i passi degli atti che le giustificano. Per i campi V: tabella dei dati di supporto in estratto, campo lasciato vuoto con `[CAMPO RISERVATO AL MAGISTRATO]`.

### CHECKPOINT 2 – Validazione della bozza italiana
Il magistrato compila i campi V, sceglie le opzioni S, corregge i campi D. Nessuna traduzione prima della validazione.

### Fase 3 – Controlli di coerenza
- corrispondenza esatta tra imputazioni e pene nel modulo e nel provvedimento presupposto;
- coerenza di date, luoghi e nomi in tutte le sezioni (stessa grafia, stessi alias);
- soglie di pena e categorie di reato coerenti con le norme acquisite;
- campi obbligatori non compilati;
- per l'OEI: atti richiesti coerenti con il provvedimento interno che li dispone; indicazione dell'autorità di convalida quando richiesta.

### Fase 4 – Traduzione (se richiesta)
Traduzione assistita del testo validato, con tabella dei termini giuridici resi e avvertenza di verifica obbligatoria.

### CHECKPOINT 3 – Validazione finale
Il magistrato verifica la versione definitiva e la traduzione. Solo dopo il modulo può essere sottoscritto e trasmesso secondo le procedure dell'ufficio.

## Template

```markdown
# BOZZA DI COMPILAZIONE ASSISTITA – [MAE / OEI]
**Procedimento**: [..] – **Provvedimento presupposto**: [estremi] – **Stato di esecuzione**: [..] – **Data**: [..]
**Modello ufficiale usato**: [versione / fonte]

> I campi valutativi sono riservati al magistrato. La bozza non è firmabile finché i CHECKPOINT 2 e 3 non risultano validati.

## 1. Classificazione dei campi
| Sezione / campo | Classe (D / S / V / T) | Note |
|---|---|---|

## 2. Campi compilati
| Sezione / campo | Contenuto proposto | Fonte (atto, pagina) | Stato |
|---|---|---|---|
| (a) cognome | [..] | [ORD, p. 1] | da verificare |
| (e) categoria di reato | opzioni compatibili: [..] | [passi] | scelta del magistrato |
| [campo V] | [CAMPO RISERVATO AL MAGISTRATO] | dati di supporto: sez. 3 | |

## 3. Dati di supporto per i campi valutativi
| Campo | Estratti degli atti |
|---|---|

## 4. Controlli di coerenza
| # | Controllo | Esito | Correzione proposta |
|---|---|---|---|

## 5. Campi aperti
[DATO NON RISULTANTE DAGLI ATTI, CAMPO RISERVATO AL MAGISTRATO, scelte da compiere]

## 6. Validazioni
- CHECKPOINT 1: [..] – CHECKPOINT 2: [..] – CHECKPOINT 3: [..]

---
*Nota di riserva.* [testo standard]
```

## Controlli finali

- nessun campo V compilato dalla skill;
- nessuna opzione S scelta dalla skill;
- ogni dato D ha una fonte;
- imputazioni e pene identiche al provvedimento presupposto;
- traduzione eseguita solo dopo la validazione e marcata come da verificare.

---
*Nota di riserva.* Documento di supporto generato con strumenti di intelligenza artificiale nel tenant ministeriale, sulla base dei soli atti indicati nella mappa di copertura. Non contiene valutazioni sulla responsabilità, sull'attendibilità delle prove o sulle esigenze cautelari. Estratti, norme e precedenti vanno verificati sulle fonti. Ogni decisione è riservata al magistrato (art. 15 l. n. 132/2025).
