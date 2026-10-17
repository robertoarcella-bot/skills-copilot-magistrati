---
name: pm-mappatura-elementi-bidirezionale
description: Mappatura bidirezionale degli elementi acquisiti nelle indagini per il pubblico ministero - per ogni ipotesi di reato e per ogni elemento costitutivo affianca in tabelle simmetriche gli elementi a carico e gli elementi a favore della persona sottoposta alle indagini (art. 358 c.p.p.), in estratto con fonte, natura dell'atto e regime di utilizzabilità prospettabile (solo segnalato, per la valutazione del PM); evidenzia le lacune in entrambe le direzioni, le contraddizioni tra fonti in forma descrittiva, gli elementi riferibili alle esigenze cautelari (art. 274 c.p.p.) senza valutarli, e gli elementi da trasmettere al giudice in caso di richiesta cautelare (art. 291, comma 1, c.p.p.). Produce MAPPATURA_ELEMENTI_[RGNR].md, aggiornabile. Usare quando il PM chiede di fare il punto delle indagini, di mappare gli elementi a carico e a favore, di preparare una richiesta cautelare, il 415-bis o le determinazioni finali, o di verificare la completezza delle indagini.
---

# Mappatura bidirezionale degli elementi (per il pubblico ministero)

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

Dare al PM, per ogni elemento costitutivo di ogni ipotesi di reato, il quadro completo di ciò che gli atti offrono in entrambe le direzioni. La mappatura serve a preparare le valutazioni riservate al PM (completezza delle indagini, richiesta di misure, determinazioni finali) e rende visibile, già nella struttura, il dovere di accertare anche i fatti e le circostanze a favore della persona sottoposta alle indagini (art. 358 c.p.p.).

La mappatura non pesa gli elementi, non valuta l'attendibilità delle fonti, non conclude sulla gravità indiziaria né sulle esigenze cautelari.

## Input

Gli atti di indagine, nella forma decisa al CHECKPOINT 0; la scheda della notizia di reato (`SCHEDA_NDR_[n].md`) se esistente; le memorie e gli atti della difesa eventualmente depositati (art. 367 c.p.p.; per le investigazioni difensive, artt. 391-bis ss. c.p.p.).

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

## Categorie descrittive

**Natura dell'atto** (indicare sempre): atto ripetibile / irripetibile; dichiarativo / documentale / tecnico / reale; compiuto dal PM / dalla PG di iniziativa / dalla PG delegata / dalla difesa; con o senza partecipazione del difensore; incidente probatorio.

**Utilizzabilità prospettabile** (solo segnalazione, la valutazione è del PM e del giudice):

| Codice | Segnalazione |
|---|---|
| **U-D** | atto in astratto destinato al fascicolo del dibattimento (es. irripetibili, incidente probatorio): dato da verificare |
| **U-I** | atto utilizzabile nelle indagini e nei riti a prova contratta, che in dibattimento richiede l'assunzione della prova |
| **U-?** | profilo di utilizzabilità da verificare (es. dichiarazioni di persona che avrebbe dovuto essere sentita con le garanzie dell'indagato; intercettazioni con presupposti da verificare; acquisizioni informatiche); indicare il dato di fatto che solleva il dubbio |

**Contraddizioni**: si riportano le affermazioni incompatibili tra fonti diverse (o della stessa fonte in tempi diversi) in estratto, con la descrizione oggettiva della divergenza («la fonte A colloca il fatto alle 22, la fonte B alle 23»), senza dire quale sia vera.

## Workflow

### CHECKPOINT 0 – Dati e segreto
Checklist delle regole comuni (punto 4). Nella fase delle indagini gli atti sono di regola coperti da segreto: senza conferma che il trattamento è consentito (atti non più segreti, o versione pseudonimizzata e minimizzata conforme alle direttive dell'ufficio), la skill non procede.

### Fase 1 – Ipotesi ed elementi costitutivi
Per ogni ipotesi di reato (come iscritta o indicata dal PM) acquisire con l'agente Normattiva il testo della norma alla data del fatto e nelle versioni successive, ed elencare gli elementi costitutivi e le circostanze contestabili. **CHECKPOINT 1**: il PM conferma l'elenco delle ipotesi e la scomposizione degli elementi.

### Fase 2 – Indice e sintesi degli atti
Indice con sigle e date; sintesi estrattiva di ciascun atto (skill `pen-sintesi-estrattiva`).

### Fase 3 – Mappatura
Ogni estratto rilevante si colloca sotto l'elemento cui si riferisce, nella colonna a carico o a favore secondo il significato che l'atto stesso gli attribuisce o che è descrittivamente evidente; quando lo stesso elemento può leggersi in entrambi i sensi, lo si riporta in entrambe le colonne con la marca [AMBIVALENTE].

### CHECKPOINT 2 – Verifica della simmetria
Prima di completare, presentare al PM il conteggio degli elementi per colonna e la lista degli atti dai quali non è stato tratto alcun elemento a favore, con la domanda se vi siano atti non ancora immessi (in particolare memorie e investigazioni difensive).

### Fase 4 – Lacune, contraddizioni, sezioni speciali
Compilare le sezioni 4-7 del template.

### Fase 5 – Controlli e consegna

## Template

```markdown
# MAPPATURA BIDIREZIONALE DEGLI ELEMENTI
**Procedimento**: R.G.N.R. n. [..] – **Persone sottoposte alle indagini**: [PSI-1, PSI-2] – **Aggiornata al**: [..] – **Versione**: 1.0
**Atti esaminati**: [sigle] – **Forma immessa**: [..]

## 1. Ipotesi di reato e norme
| # | Ipotesi | PSI | Norma (testo acquisito il [..]; versioni alla data del fatto e successive) | Data e luogo del fatto (come risultano) |
|---|---|---|---|---|

## 2. Mappa per elemento costitutivo
### Ipotesi H1 – [titolo] – PSI-1
#### Elemento: [es. condotta]
| Elementi a carico (estratto) | Fonte | Natura / Utilizzabilità prospettabile | Elementi a favore (estratto) | Fonte | Natura / Utilizzabilità prospettabile |
|---|---|---|---|---|---|
| «...» | [SIT T-1, p. 2] | dichiarativo, PG delegata / U-I | «...» | [MEM-DIF, p. 3] | documentale, difesa / U-? |
> Se una colonna resta vuota: "Esaminati [sigle], non risultano elementi [a carico / a favore] su questo elemento."

[ripetere per evento, nesso causale, elemento soggettivo, circostanze, qualità soggettive]

## 3. Riepilogo
| Ipotesi | Elemento | n. a carico | n. a favore | n. ambivalenti | Elemento privo di elementi in una o entrambe le colonne |
|---|---|---|---|---|---|
> Il riepilogo è un conteggio e non una misura della consistenza degli elementi.

## 4. Lacune
### 4.1 Lacune rispetto all'ipotesi d'accusa
| # | Elemento | Dato mancante | Atti che lo menzionano o lo presuppongono |
|---|---|---|---|
### 4.2 Lacune rispetto alle ipotesi alternative e alle circostanze a favore
| # | Ipotesi alternativa o circostanza | Dato mancante | Atti che la rendono compatibile |
|---|---|---|---|
> Le lacune alimentano la skill `pm-piano-accertamenti-bidirezionale`.

## 5. Contraddizioni tra fonti
| # | Affermazione 1 (estratto, fonte, data) | Affermazione 2 (estratto, fonte, data) | Divergenza (descrizione oggettiva) |
|---|---|---|---|

## 6. Elementi riferibili all'art. 274 c.p.p. (solo se il PM lo chiede)
| Lettera (testo da agente Normattiva) | Elementi degli atti nel senso della sussistenza (estratti) | Elementi degli atti nel senso dell'insussistenza (estratti) |
|---|---|---|
> Nessuna valutazione del pericolo. Divieto di stime di rischio e di profilazione (reg. UE 2024/1689, art. 5, par. 1, lett. d).

## 7. Elementi a favore da trasmettere al giudice in caso di richiesta cautelare (art. 291, comma 1, c.p.p.)
| # | Elemento | Atto | Pagine | Già inserito nell'elenco di trasmissione (sì / no) |
|---|---|---|---|---|
> Elenco ricavato dalle colonne "a favore" e "ambivalenti" e dalle memorie difensive depositate. La selezione degli atti da trasmettere è del PM.

## 8. Mappa di copertura
| Sigla | Atto | Letto per intero | Elementi a carico tratti | Elementi a favore tratti |
|---|---|---|---|---|
**Indicatori**: atti letti [x/y]; elementi costitutivi mappati [x/y]; elementi a carico [n]; a favore [n]; ambivalenti [n]; estratti verificati [n/n].

## Registro aggiornamenti
| Data | Versione | Atti nuovi | Voci modificate |
|---|---|---|---|

---
*Nota di riserva.* [testo standard]
```

## Controlli finali

- ogni elemento costitutivo ha entrambe le colonne compilate o dichiarate vuote dopo l'esame;
- nessun aggettivo valutativo («grave», «solido», «debole», «attendibile», «inverosimile») fuori dalle citazioni;
- le segnalazioni di utilizzabilità indicano il dato di fatto e non concludono;
- nessuna valutazione delle esigenze cautelari; sezione 6 solo su richiesta;
- linguaggio conforme alla presunzione di non colpevolezza;
- copertura 100% o avviso MAPPATURA INCOMPLETA.

## Modalità aggiornamento

Le voci esistenti non si cancellano: i nuovi elementi si aggiungono con la marca `[AGG. v[n]: SIGLA, data]`; se un atto nuovo modifica il senso di un elemento già mappato (es. ritrattazione, esito di consulenza), si aggiunge una riga collegata e non si sostituisce la precedente. Si aggiornano riepilogo, lacune, mappa di copertura e registro; la versione cresce di 0.1.

---
*Nota di riserva.* Documento di supporto generato con strumenti di intelligenza artificiale nel tenant ministeriale, sulla base dei soli atti indicati nella mappa di copertura. Non contiene valutazioni sulla responsabilità, sull'attendibilità delle prove o sulle esigenze cautelari. Estratti, norme e precedenti vanno verificati sulle fonti. Ogni decisione è riservata al magistrato (art. 15 l. n. 132/2025).
