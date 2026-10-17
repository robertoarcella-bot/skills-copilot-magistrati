---
name: gip-gup-scheda-fascicolo
description: Scheda di studio del fascicolo per il GIP e il GUP, in posizione di terzietà, per la decisione sulla richiesta di archiviazione e sull'opposizione della persona offesa, per l'udienza preliminare e per i riti alternativi - indice degli atti, imputazioni o notizie di reato in testo integrale, richieste e conclusioni di tutte le parti, elementi a carico e a favore in estratto con localizzatore, regola di giudizio da acquisire con l'agente Normattiva (artt. 408 e 425 c.p.p.), questioni processuali da segnalare (nullità, competenza, costituzione di parte civile, termini delle indagini), checklist dei dati di ammissibilità dei riti alternativi, lacune e mappa di copertura. Non indica esiti e non redige provvedimenti. Produce SCHEDA_GIP_GUP_[RGNR].md. Usare quando il giudice chiede di studiare o riepilogare un fascicolo per archiviazione, opposizione, udienza preliminare, abbreviato, patteggiamento, messa alla prova o decreto penale.
---

# Scheda di studio del fascicolo (GIP e GUP)

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

Dare al giudice una visione completa e verificabile del fascicolo nella sede in cui deve decidere se il procedimento prosegue (archiviazione, imputazione coatta, rinvio a giudizio, non luogo a procedere) o se ammettere un rito alternativo. La scheda descrive gli atti e affianca, con pari struttura, gli elementi a carico e quelli a favore. **Non** applica la regola di giudizio, **non** indica l'esito e **non** redige decreti, ordinanze o sentenze (CSM, aggiornamento 22 luglio 2026, § 8).

## Input

Il fascicolo trasmesso con la richiesta del PM, le memorie e l'eventuale atto di opposizione della persona offesa, i verbali delle udienze camerali o preliminari, le richieste di rito alternativo. Se esiste `SCHEDA_GIP_GUP_[RGNR].md`, modalità aggiornamento.

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

### CHECKPOINT 0 – Segreto, dati e sede

Chiedere al giudice: (a) la sede della decisione (archiviazione; opposizione; udienza preliminare; rito alternativo; decreto penale); (b) se vi sono atti ancora coperti da segreto o riservati (es. stralci di indagine collegati, intercettazioni non acquisite) da escludere; (c) se gli atti sono pseudonimizzati e se riguardano minori o persone offese tutelate. Senza risposta il flusso non prosegue.

### Fase 1 – Indice e sigle

Sigle: CNR, ANN [n], VSIT, VINT (interrogatori), CT-PM, CT-DIF, RICH-ARCH, OPP-PO, RICH-RG (richiesta di rinvio a giudizio), MEM-DIF, MEM-PO, VERB-UP [data], RICH-RITO. Indice cronologico con [RICHIAMATO, NON PRESENTE] per gli atti mancanti.

### Fase 2 – Dati del procedimento

Data di iscrizione della notizia di reato e di ciascun indagato (dato rilevante per i termini delle indagini e per l'utilizzabilità degli atti successivi alla scadenza, da verificare con l'agente Normattiva sugli artt. 405, 406, 407 e 407-bis c.p.p.); proroghe; avviso ex art. 415-bis c.p.p. e attività difensiva successiva; condizioni di procedibilità (querela, remissione) come risultano dagli atti.

**CHECKPOINT 1** – il giudice valida indice e dati del procedimento.

### Fase 3 – Imputazioni e richieste

Testo integrale delle imputazioni o della notizia di reato come formulata nella richiesta; testo integrale delle richieste e conclusioni di PM, difesa, persona offesa o parte civile. Norme sostanziali con richiesta all'agente Normattiva (data del fatto e versioni successive).

### Fase 4 – Elementi a carico e a favore

Per ciascun capo e per ciascun elemento costitutivo della fattispecie (condotta, evento, nesso, elemento soggettivo, circostanze contestate):
- elementi indicati dall'accusa (estratti, fonte);
- elementi indicati dalla difesa o risultanti dagli atti a favore (estratti, fonte);
- per l'opposizione della persona offesa: indagini suppletive indicate e relativi elementi di prova (estratti), come prescritto dalla norma da acquisire con l'agente Normattiva.

Le due colonne hanno la stessa analiticità. Se una colonna è vuota: «Esaminati [sigle], non sono emersi elementi».

### Fase 5 – Regola di giudizio e questioni processuali

1. Acquisire con l'agente Normattiva il testo vigente degli artt. 408 e 425 c.p.p. (e dell'art. 554-ter c.p.p. per l'udienza predibattimentale, se pertinente) e riportarlo **senza applicarlo**.
2. Segnalare le questioni processuali che emergono dagli atti: competenza per materia e territorio, nullità degli avvisi e delle notifiche, termini delle indagini, legittimazione e costituzione di parte civile, connessione e riunione, prescrizione (soli dati: data del fatto, atti interruttivi risultanti, norme da Normattiva). Ciascuna come «possibile questione», con gli estratti da cui emerge.

### Fase 6 – Riti alternativi (se pertinente)

Checklist descrittiva, per il rito richiesto, dei **dati** di ammissibilità ricavabili dagli atti (soggetto che ha formulato la richiesta, forma e procura speciale, tempestività rispetto alla fase, consenso del PM ove necessario, eventuale integrazione probatoria richiesta, programma di trattamento per la messa alla prova, limiti edittali delle fattispecie con testo da Normattiva). Nessuna valutazione di ammissibilità o di congruità della pena.

### Fase 7 – Ricerche

Stringhe Italgiure (skill `pen-ricerca-italgiure`) per ogni questione, simmetriche per accusa e difesa; precedenti citati nelle richieste e nelle memorie con la marca DA VERIFICARE.

**CHECKPOINT 2** – consegna e validazione della scheda.

---

## Template

```markdown
# SCHEDA DI STUDIO DEL FASCICOLO – GIP/GUP
**Tribunale di [..], Ufficio GIP/GUP** – R.G.N.R. n. [..] – R.G. GIP n. [..] – Giudice: [..]
**Sede della decisione**: [..] – **Aggiornata al**: [..] – **Versione**: [1.0]
**Atti esaminati**: [sigle] – **Esclusioni (CHECKPOINT 0)**: [..]

## 1. Dati del procedimento
| Campo | Dato | Fonte |
|---|---|---|
| Iscrizione notizia di reato / indagati | | |
| Proroghe | | |
| Avviso ex art. 415-bis c.p.p. | | |
| Condizioni di procedibilità | | |

## 2. Parti e difensori
| Soggetto | Qualità | Difensore | Nomina / procura (atto) |
|---|---|---|---|

## 3. Indice degli atti
| Sigla | Atto | Autore | Data | Presente |
|---|---|---|---|---|

## 4. Imputazioni e richieste (testo integrale)
## 5. Elementi per capo
### Capo [a] – [titolo neutro]
| Elemento della fattispecie | Elementi indicati dall'accusa (estratti) | Elementi a favore indicati o risultanti (estratti) |
|---|---|---|

## 6. Regola di giudizio (testo da agente Normattiva, non applicata)
## 7. Possibili questioni processuali
| # | Possibile questione | Estratti da cui emerge | Norme | Nota |
|---|---|---|---|---|

## 8. Riti alternativi: dati di ammissibilità
| Requisito (da norma acquisita) | Dato risultante dagli atti | Fonte |
|---|---|---|

## 9. Precedenti citati e ricerche suggerite
## 10. Lacune
## 11. Mappa di copertura
## Registro aggiornamenti

---
*Nota di riserva.* [testo della regola comune]
```

---

## Controlli finali

- imputazioni e richieste per intero; ogni elemento con localizzatore;
- le colonne «accusa» e «a favore» hanno estensione comparabile; nessuna è stata omessa senza dichiarazione;
- la regola di giudizio è riportata e non applicata; nessuna frase del tipo «gli elementi consentono / non consentono»;
- nessun testo di provvedimento; nessuna indicazione di esito;
- linguaggio conforme all'art. 115-bis c.p.p.

## Modalità aggiornamento

Nuovi atti (memorie, verbali dell'udienza preliminare, integrazioni probatorie ex art. 422 c.p.p.) si aggiungono con `[AGG. v[n]: SIGLA, data]`; si aggiornano indice, sezioni interessate, mappa e registro. Salvare `SCHEDA_GIP_GUP_[RGNR].md` se l'ambiente lo consente, altrimenti restituire in chat.
