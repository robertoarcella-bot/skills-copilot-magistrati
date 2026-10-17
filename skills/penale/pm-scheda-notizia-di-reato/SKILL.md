---
name: pm-scheda-notizia-di-reato
description: Scheda di prima lettura della notizia di reato per il pubblico ministero - comunicazione di notizia di reato, annotazione di PG, denuncia, querela, esposto, referto - con fatti narrati in estratto, persone indicate e ruolo attribuito dalla fonte, ipotesi di reato come prospettate dalla PG o dal denunciante, dati rilevanti per l'iscrizione nel registro (art. 335 c.p.p. e disposizioni collegate, testo da acquisire con l'agente Normattiva), condizioni di procedibilità (querela, istanza, richiesta, termini), elementi per la verifica della competenza, termini e atti urgenti, e sezioni obbligatorie sugli elementi a favore della persona indicata e sulle ipotesi alternative compatibili con la narrazione (art. 358 c.p.p.). Non decide sull'iscrizione né sulla qualificazione. Produce SCHEDA_NDR_[n].md. Usare quando il PM chiede di esaminare, schedare o riepilogare una notizia di reato, una CNR, una denuncia o una querela, o di preparare l'iscrizione.
---

# Scheda della notizia di reato (per il pubblico ministero)

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

Mettere a disposizione del PM, in forma verificabile, tutto ciò che la notizia di reato contiene e che serve alle valutazioni iniziali riservate al PM: se e come iscrivere, quale qualificazione dare, se la procedibilità sussiste, se l'ufficio è competente, quali atti urgenti disporre. La scheda descrive la notizia: non qualifica in via definitiva il fatto, non individua l'«autore», non suggerisce l'iscrizione.

La scheda è già bidirezionale: fin dalla prima lettura raccoglie ciò che nella narrazione è favorevole alla persona indicata e le spiegazioni alternative dei fatti che la narrazione stessa consente.

## Input

La notizia di reato e i suoi allegati, nella forma decisa al CHECKPOINT 0. Se la notizia è recente, è di regola coperta da segreto: in tal caso si lavora solo su versione pseudonimizzata e minimizzata (skill `pen-pseudonimizzazione-atti`), nel rispetto delle direttive del Procuratore della Repubblica.

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

## Norme da acquisire con l'agente Normattiva

Non si riportano a memoria. Richieste tipiche:

> @Normattiva Riporta il testo vigente degli artt. 330, 331, 332, 333, 335, 335-bis, 335-ter e 335-quater c.p.p. e indica le modifiche introdotte dal d.lgs. 10 ottobre 2022, n. 150 con la relativa disciplina transitoria.

> @Normattiva Riporta il testo degli artt. 120 e 124 c.p., dell'art. 336 c.p.p. e dell'art. [n] c.p. [reato prospettato] nella versione vigente al [data del fatto] e in ciascuna versione successiva fino a oggi, indicando il regime di procedibilità.

Le norme sulla competenza (artt. 4-16 c.p.p.) si acquisiscono solo se il magistrato chiede la sezione 7.

## Workflow

### CHECKPOINT 0 – Dati e segreto
Checklist delle regole comuni (punto 4). Verificare in particolare: atto coperto da segreto; presenza di dati della persona offesa nei reati dell'art. 734-bis c.p.; minori; allegati con dati sanitari. Applicare le misure; attendere conferma.

### Fase 1 – Indice della notizia e degli allegati
Sigle (CNR, ANN PG, DEN, QUER, ALL 1, ...), data di ricezione dichiarata, autore, pagine. **CHECKPOINT 1**: il PM conferma l'indice e indica se esistono altri atti da considerare (es. iscrizioni precedenti per lo stesso fatto, note di altri uffici).

### Fase 2 – Estrazione
Sintesi estrattiva secondo la skill `pen-sintesi-estrattiva`: fatti narrati in ordine cronologico, distinguendo ciò che la fonte afferma di aver percepito da ciò che riferisce de relato o deduce.

### Fase 3 – Compilazione della scheda
Secondo il template.

### CHECKPOINT 2 – Sezioni bidirezionali
Prima della consegna finale, presentare al PM le sezioni 5 (elementi a favore) e 6 (ipotesi alternative) separatamente: il PM conferma che sono complete o indica altri atti da esaminare.

### Fase 4 – Controlli e consegna

## Template

```markdown
# SCHEDA DELLA NOTIZIA DI REATO
**Ufficio**: Procura della Repubblica presso il Tribunale di [..] – **Riferimento**: [n. modello / protocollo]
**Data di ricezione (come risulta dall'atto)**: [..] – **Aggiornata al**: [..] – **Versione**: 1.0
**Forma immessa**: [integrale / pseudonimizzata / minimizzata]

## 1. Fonte della notizia
| Campo | Dato | Fonte |
|---|---|---|
| Tipo (CNR, denuncia, querela, esposto, referto, altro) | | |
| Autore | | |
| Data dell'atto e della ricezione | | |
| Atti urgenti già compiuti dalla PG | | |
| Allegati | | |

## 2. Fatti narrati (estratti)
| # | Fatto (estratto) | Fonte | Percezione diretta / de relato / deduzione della fonte (passo da cui risulta) |
|---|---|---|---|

## 3. Persone indicate
| Pseudonimo | Ruolo attribuito dalla fonte (estratto) | Fonte | Dati identificativi presenti nell'atto (sì / no / parziali) |
|---|---|---|---|
> Il ruolo è quello attribuito dalla fonte. Se la fonte indica una persona senza attribuirle condotte specifiche, lo si riporta.

## 4. Ipotesi di reato prospettate
| # | Ipotesi come prospettata (estratto) | Prospettata da | Fatti cui è riferita (rif. sez. 2) | Norme (agente Normattiva, alla data del fatto e successive) |
|---|---|---|---|---|
> Altre qualificazioni astrattamente compatibili con i fatti narrati si elencano separatamente, con la marca [QUALIFICAZIONE NON PROSPETTATA DALLA FONTE], senza preferenza.

## 5. Elementi a favore della persona indicata (art. 358 c.p.p.)
| # | Elemento (estratto) | Fonte | Fatto cui si riferisce |
|---|---|---|---|
[oppure: Esaminati [sigle], non sono emersi elementi a favore.]

## 6. Ipotesi alternative compatibili con la narrazione
| # | Ipotesi alternativa (descrittiva) | Passi degli atti che la rendono compatibile (estratti) | Accertamenti che consentirebbero di verificarla |
|---|---|---|---|
> Esempi di categorie: fatto non avvenuto o avvenuto diversamente; fatto avvenuto ma attribuibile ad altri; fatto attribuibile ma privo di rilevanza penale; ricorrenza di una scriminante o di una causa di non punibilità; difetto dell'elemento soggettivo.

## 7. Dati rilevanti per l'iscrizione (la decisione è del PM)
| Campo | Dato risultante dagli atti | Fonte |
|---|---|---|
| Fatto descritto in termini storici | | |
| Data e luogo del fatto | | |
| Persone alle quali il fatto è attribuito dalla fonte | | |
| Elementi indicati a carico di ciascuna persona (rif. sez. 2) | | |
| Iscrizioni precedenti per lo stesso fatto (se indicate) | | |
> Norme: art. 335 c.p.p. e disposizioni collegate, testo da acquisire con l'agente Normattiva. La valutazione dei presupposti dell'iscrizione nominativa e della sua data è riservata al PM.

## 8. Procedibilità
| Ipotesi | Regime di procedibilità (da agente Normattiva, alla data del fatto e attuale) | Querela / istanza presente | Data di presentazione | Data di conoscenza del fatto dichiarata | Remissione o rinuncia |
|---|---|---|---|---|---|

## 9. Competenza (se richiesta)
| Elemento | Dato risultante dagli atti | Fonte |
|---|---|---|
| Luogo di consumazione indicato | | |
| Ipotesi più grave prospettata | | |
| Connessioni con altri procedimenti indicate | | |

## 10. Termini e atti urgenti
| Termine o urgenza | Dato di partenza (estratto) | Norma (agente Normattiva) | Nota |
|---|---|---|---|

## 11. Lacune
[Allegati citati e non presenti; persone indicate senza dati; fatti con data incerta; pagine illeggibili.]

## 12. Mappa di copertura
| Sigla | Atto | Letto per intero | Sezioni in cui è usato |
|---|---|---|---|
**Indicatori**: atti letti [x/y]; fatti estratti [n]; elementi a favore [n o "nessuno, dopo esame"]; ipotesi alternative [n]; estratti verificati [n/n].

## Registro aggiornamenti
| Data | Versione | Atti nuovi | Sezioni modificate |
|---|---|---|---|

---
*Nota di riserva.* [testo standard]
```

## Controlli finali

- nessuna formula che dia per accertata la responsabilità o l'identità dell'autore;
- sezioni 5 e 6 compilate o dichiarate vuote dopo l'esame;
- le ipotesi di reato non prospettate sono marcate come tali e non ordinate per preferenza;
- nessuna norma riportata a memoria; date di riferimento sempre indicate;
- copertura 100% o avviso SCHEDA INCOMPLETA.

## Modalità aggiornamento

Nuove annotazioni o integrazioni si aggiungono con la marca `[AGG. v[n]: SIGLA, data]` senza cancellare le voci precedenti; si aggiornano indice, sezioni interessate, mappa di copertura e registro. Il passo successivo naturale è la skill `pm-mappatura-elementi-bidirezionale`, da proporre in una riga.

---
*Nota di riserva.* Documento di supporto generato con strumenti di intelligenza artificiale nel tenant ministeriale, sulla base dei soli atti indicati nella mappa di copertura. Non contiene valutazioni sulla responsabilità, sull'attendibilità delle prove o sulle esigenze cautelari. Estratti, norme e precedenti vanno verificati sulle fonti. Ogni decisione è riservata al magistrato (art. 15 l. n. 132/2025).
