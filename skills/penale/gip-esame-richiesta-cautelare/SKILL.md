---
name: gip-esame-richiesta-cautelare
description: Scheda di lettura della richiesta di misura cautelare personale o reale per il giudice per le indagini preliminari, in posizione di terzietà - richiesta e imputazione provvisoria in testo integrale, elementi indicati dal PM con fonte e regime di utilizzabilità, verifica descrittiva della trasmissione degli elementi a favore e delle memorie difensive (art. 291, comma 1, c.p.p.), elementi relativi alle esigenze cautelari e ai criteri di scelta della misura riportati solo in estratto (a favore e contro), date e termini (interrogatorio preventivo o di garanzia, durata), lacune degli atti trasmessi. Non valuta gravità indiziaria, pericolosità o adeguatezza e non redige l'ordinanza. Produce SCHEDA_CAUTELARE_[RGNR].md. Usare quando il GIP chiede di leggere, schedare o riepilogare una richiesta di misura cautelare, di custodia, di misura interdittiva, di sequestro preventivo, o di preparare l'interrogatorio.
---

# Scheda di lettura della richiesta cautelare (per il GIP)

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

Mettere il giudice in condizione di dominare rapidamente la richiesta del pubblico ministero e gli atti trasmessi, con il testo a portata di mano e con la verifica, puramente descrittiva, che tra gli atti siano presenti anche gli elementi a favore. La scheda **non** valuta la gravità degli indizi (art. 273 c.p.p.), le esigenze cautelari (art. 274 c.p.p.) né l'adeguatezza e la proporzionalità della misura (art. 275 c.p.p.), e **non redige l'ordinanza**, né in bozza né per parti: la motivazione e il dispositivo dei provvedimenti giurisdizionali sono esclusi dagli usi consentiti (CSM, aggiornamento 22 luglio 2026, § 8).

## Input

La richiesta del PM e gli atti trasmessi a corredo (informative, verbali, annotazioni, consulenze, memorie difensive). Se esiste già `SCHEDA_CAUTELARE_[RGNR].md`, si procede in modalità aggiornamento (es. dopo l'interrogatorio o nuove produzioni).

> **Avvertenza.** La richiesta cautelare si colloca di regola nella fase coperta da segreto. Gli atti non ancora conoscibili dalla difesa **non si immettono** nel sistema (vedi regola 4 e CHECKPOINT 0). Si lavora su atti non più segreti o su estratti minimizzati e pseudonimizzati (skill `pen-pseudonimizzazione-atti`), secondo le direttive del capo dell'ufficio.

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

## Workflow

### CHECKPOINT 0 – Segreto e perimetro

Prima di leggere qualsiasi atto, chiedere al giudice:
1. se gli atti da elaborare sono ancora coperti da segreto investigativo e, in caso affermativo, quali sono già conoscibili dalla difesa;
2. se esistono direttive dell'ufficio sull'uso di Copilot con atti cautelari;
3. se gli atti sono stati pseudonimizzati e se contengono intercettazioni, dati di minori, dati sanitari o generalità di persone offese tutelate.

Se gli atti sono segreti e non pseudonimizzati, la skill si ferma e indica come procedere (estratti minimizzati, `pen-pseudonimizzazione-atti`). Riprende solo su conferma espressa.

### Fase 1 – Indice degli atti trasmessi

Assegnare le sigle (RICH = richiesta del PM; CNR; ANN [n]; VSIT [nome pseudonimizzato, data]; INT [progressivo] per le intercettazioni già trascritte e trasmesse; CT; MEM-DIF [data]) e compilare l'indice. Per gli atti richiamati nella richiesta ma non trasmessi: [RICHIAMATO, NON TRASMESSO].

**CHECKPOINT 1** – il giudice conferma l'indice e la completezza dell'elenco prima dell'estrazione.

### Fase 2 – Richiesta e imputazione provvisoria

Estratto integrale delle conclusioni della richiesta (misura, persona, capi) e dell'imputazione provvisoria per ciascun capo. Norme da acquisire con l'agente Normattiva: fattispecie contestate (versione alla data del fatto e successive) e disposizioni processuali applicabili (artt. 273, 274, 275, 280, 287 c.p.p. o, per le misure reali, art. 321 c.p.p.), nella versione vigente alla data della richiesta.

### Fase 3 – Elementi indicati dal PM

Per ciascun capo, ogni elemento richiamato nella richiesta: estratto del passo della richiesta, estratto dell'atto fonte, natura dell'atto e regime che risulta dagli atti (es. dichiarazione resa senza difensore; intercettazione con decreto autorizzativo presente / non presente tra gli atti). Il regime di utilizzabilità è solo **descritto**: la valutazione spetta al giudice.

### Fase 4 – Elementi a favore e memorie difensive (art. 291, comma 1, c.p.p.)

1. Elencare gli atti che la richiesta dichiara di trasmettere a favore e le memorie difensive già depositate.
2. Leggere tutti gli atti trasmessi ed elencare, in estratto, i passi che **appaiono** favorevoli alla persona sottoposta alle indagini o incompatibili con l'ipotesi d'accusa, anche se non indicati come tali dal PM.
3. Segnalare atti richiamati negli atti trasmessi che potrebbero contenere elementi a favore e che non risultano trasmessi (dato descrittivo, senza conclusioni sulla completezza della trasmissione).

### Fase 5 – Elementi relativi alle esigenze e alla scelta della misura

Soltanto estratti, divisi per colonna «elementi indicati a sostegno» ed «elementi di segno contrario risultanti dagli atti», per ciascuna esigenza prospettata dal PM e per i criteri di scelta. Nessuna stima di pericolosità, di fuga o di inquinamento (regola 5). Dati oggettivi: incensuratezza o precedenti come risultano dal certificato in atti, condizioni personali documentate, tempo trascorso dal fatto.

### Fase 6 – Date e termini

Data del fatto, della richiesta, eventuale arresto o fermo; interrogatorio preventivo o di garanzia (verificare con l'agente Normattiva la disciplina vigente dell'art. 291, comma 1-quater, c.p.p. e dell'art. 294 c.p.p.); termini di durata della misura richiesta (art. 303 c.p.p.). Solo dati.

**CHECKPOINT 2** – il giudice valida la scheda; su sua richiesta si prepara l'elenco dei temi dell'interrogatorio come **elenco degli atti e dei passi** su cui la persona potrà essere sentita, senza domande suggestive né valutazioni.

---

## Template

```markdown
# SCHEDA DI LETTURA DELLA RICHIESTA CAUTELARE
**Ufficio GIP di [..]** – R.G.N.R. n. [..] – R.G. GIP n. [..]
**Data**: [..] – **Versione**: [1.0] – **Atti esaminati**: [sigle]
**Segreto**: [atti segreti esclusi / atti pseudonimizzati / atti non più segreti] (CHECKPOINT 0 del [data])

[eventuale avviso SCHEDA INCOMPLETA]

## 1. Richiesta (testo integrale delle conclusioni)
«...» [RICH, p. n]

## 2. Imputazione provvisoria (testo integrale, per capo)
**Capo [a]** «...» [RICH, p. n] – Data del fatto: [..] – Norme: [richiesta Normattiva]

## 3. Indice degli atti trasmessi
| Sigla | Atto | Autore | Data | Trasmesso |
|---|---|---|---|---|

## 4. Elementi indicati dal PM
| # | Capo | Passo della richiesta | Estratto dell'atto fonte | Natura e regime risultante dagli atti |
|---|---|---|---|---|

## 5. Elementi a favore e memorie difensive
### 5.1 Atti trasmessi come favorevoli e memorie difensive
### 5.2 Passi degli atti trasmessi che appaiono a favore o incompatibili con l'ipotesi d'accusa
| # | Estratto | Fonte | Capo cui si riferisce |
|---|---|---|---|
> Se nessuno: "Esaminati [sigle], non sono emersi passi a favore."
### 5.3 Atti richiamati e non trasmessi
| Atto richiamato | Dove è richiamato | Possibile pertinenza (descrittiva) |
|---|---|---|

## 6. Esigenze cautelari e scelta della misura (solo estratti)
| Esigenza o criterio prospettato | Elementi indicati a sostegno (estratti) | Elementi di segno contrario risultanti dagli atti (estratti) |
|---|---|---|
> Nessuna valutazione. Le categorie seguono la richiesta; la qualificazione spetta al giudice.

## 7. Date e termini
| Evento / termine | Data | Fonte | Norma (Normattiva) |
|---|---|---|---|

## 8. Precedenti citati nella richiesta
| Estremi come citati | Pagina | Stringa Italgiure (pen-ricerca-italgiure) | Stato |
|---|---|---|---|
| | | | DA VERIFICARE |

## 9. Lacune e limiti
## 10. Mappa di copertura
| Sigla | Letto per intero | Usato in sezioni |
|---|---|---|

---
*Nota di riserva.* [testo della regola comune]
```

---

## Controlli finali

- richiesta e imputazioni riportate per intero; ogni elemento con doppio localizzatore (richiesta e atto fonte);
- sezione 5 compilata o dichiarata vuota dopo l'esame di tutti gli atti trasmessi;
- sezione 6 senza parole valutative («concreto», «attuale», «elevato», «grave») fuori dalle citazioni;
- nessun testo di ordinanza, nessuna proposta di misura, nessuna motivazione;
- nessun atto segreto immesso senza la conferma del CHECKPOINT 0.

## Modalità aggiornamento

Dopo l'interrogatorio o nuove memorie: aggiungere gli estratti con la marca `[AGG. v[n]: SIGLA, data]`, aggiornare le sezioni 5 e 6, l'indice e la mappa di copertura; la versione cresce di 0.1. Salvare `SCHEDA_CAUTELARE_[RGNR].md` nella cartella del procedimento se l'ambiente lo consente, altrimenti restituire il testo in chat.
