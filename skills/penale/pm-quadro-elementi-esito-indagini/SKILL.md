---
name: pm-quadro-elementi-esito-indagini
description: Griglia di supporto alle determinazioni del pubblico ministero al termine delle indagini (archiviazione o esercizio dell'azione penale), costruita sulla regola di giudizio della ragionevole previsione di condanna (artt. 408 e 425 c.p.p., d.lgs. n. 150/2022) - per ogni ipotesi e ogni elemento costitutivo affianca elementi a carico e a favore, con l'utilizzabilità prospettabile in dibattimento; elenca i profili da verificare su cause di non punibilità e di estinzione (prescrizione: solo dati e date; particolare tenuità del fatto ex art. 131-bis c.p.: solo elementi degli atti), procedibilità e riti alternativi. Non indica l'esito, non esprime la previsione, non redige richieste di archiviazione, decreti di citazione o richieste di rinvio a giudizio. Produce QUADRO_ESITO_[RGNR].md. Usare quando il PM chiede di fare il punto finale delle indagini, di preparare le determinazioni ex art. 405 o 408 c.p.p., di valutare archiviazione o azione, o di verificare la tenuità del fatto o la prescrizione.
---

# Quadro degli elementi per le determinazioni finali (per il pubblico ministero)

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

Ordinare, per la valutazione che spetta esclusivamente al PM, tutti gli elementi che la regola di giudizio richiede di considerare. Dopo il d.lgs. n. 150/2022 la scelta tra archiviazione ed esercizio dell'azione si misura sulla possibilità di formulare una ragionevole previsione di condanna (o di applicazione di una misura di sicurezza diversa dalla confisca): una prognosi che riguarda anche la tenuta degli elementi nel dibattimento. La griglia rende visibili gli elementi in entrambe le direzioni e i profili da verificare; non formula la prognosi.

Le richieste che seguono la decisione (richiesta di archiviazione, decreto di citazione diretta, richiesta di rinvio a giudizio, richieste di riti alternativi) **non** si redigono con questa skill: contengono la valutazione dei fatti e delle prove riservata al magistrato (art. 15, comma 1, l. n. 132/2025).

## Input

- `MAPPATURA_ELEMENTI_[RGNR].md` aggiornata a tutti gli atti (se manca o è superata: eseguirla o aggiornarla prima, e dirlo in una riga);
- `SCADENZARIO_[RGNR].md` per i dati sui termini e sulla prescrizione;
- memorie, richieste e atti della difesa successivi all'avviso ex art. 415-bis c.p.p., se notificato;
- le indicazioni del PM sulle ipotesi da considerare.

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

> @Normattiva Riporta il testo vigente degli artt. 405, 408, 411, 415-bis e 425 c.p.p. e indica le modifiche introdotte dal d.lgs. 10 ottobre 2022, n. 150 con la disciplina transitoria.

> @Normattiva Riporta il testo dell'art. 131-bis c.p. e degli artt. 157-161 c.p. nella versione vigente al [data del fatto] e in ciascuna versione successiva fino a oggi.

Altre: norma incriminatrice (versioni alla data del fatto e successive); regime di procedibilità; norme sui riti alternativi solo se il PM le richiede. Fino alla risposta: [TESTO DA ACQUISIRE CON L'AGENTE NORMATTIVA].

## Workflow

### CHECKPOINT 0 – Dati e segreto
Checklist delle regole comuni (punto 4). Se l'avviso ex art. 415-bis è stato notificato, gli atti depositati non sono più segreti nei confronti dell'indagato: indicarlo, ferme le cautele sui dati personali e sulle intercettazioni. Conferma del PM.

### Fase 1 – Verifica dei prerequisiti
Controllare che la mappatura copra tutti gli atti e le memorie difensive. **CHECKPOINT 1**: il PM conferma il perimetro (ipotesi, persone, atti).

### Fase 2 – Griglia per elemento costitutivo
Per ogni ipotesi e persona, riprendere dalla mappatura gli elementi a carico e a favore e aggiungere, per ciascuno, la **prospettiva dibattimentale**: come l'elemento potrebbe entrare nel giudizio (atto destinato al fascicolo del dibattimento; prova da assumere oralmente; elemento utilizzabile solo nei riti a prova contratta) e quali profili di utilizzabilità risultano da verificare. Nessuna valutazione della tenuta.

### Fase 3 – Profili da verificare
Compilare le sezioni 3-7 del template con soli dati ed estratti.

### CHECKPOINT 2 – Completezza
Presentare al PM la sezione 6 (completezza delle indagini) e la sezione 2 limitatamente alle colonne «a favore»: il PM conferma che non vi sono elementi o richieste difensive non considerati.

### Fase 4 – Consegna
La skill si ferma alla consegna della griglia. Se il PM chiede di «scrivere la richiesta» o di «dire se archiviare», rispondere che l'operazione è esclusa dal perimetro e proporre, se utile, la tabella dei contenuti che la richiesta dovrà trattare (sezione 8).

## Template

```markdown
# QUADRO DEGLI ELEMENTI PER LE DETERMINAZIONI FINALI
**Procedimento**: R.G.N.R. n. [..] – **Persone**: [PSI-1 ..] – **Data**: [..]
**Basi**: MAPPATURA_ELEMENTI v[..]; SCADENZARIO v[..]; memorie difensive [sigle]

> **Metodo.** La griglia non contiene la previsione sull'esito né indicazioni sulla determinazione da assumere, riservate al PM. Gli elementi sono elencati nell'ordine degli elementi costitutivi.

## 1. Regola di giudizio
Testo degli artt. 408 e 425 c.p.p. acquisito dall'agente Normattiva il [..]: [testo / TESTO DA ACQUISIRE]

## 2. Griglia per ipotesi ed elemento costitutivo
### H1 – [ipotesi] – PSI-1
| Elemento | Elementi a carico (rif. mappatura) | Prospettiva dibattimentale e profili di utilizzabilità | Elementi a favore (rif. mappatura) | Prospettiva dibattimentale e profili di utilizzabilità | Contraddizioni tra fonti (rif.) |
|---|---|---|---|---|---|

## 3. Qualificazione giuridica
| Qualificazione iscritta | Qualificazioni alternative compatibili con i fatti (senza preferenza) | Effetti di ciascuna su procedibilità, competenza, prescrizione (dati) |
|---|---|---|

## 4. Procedibilità
| Ipotesi | Regime (alla data del fatto e attuale) | Querela / istanza | Remissione | Nota |
|---|---|---|---|---|

## 5. Cause di non punibilità e di estinzione da verificare
### 5.1 Prescrizione: dati
| Ipotesi | Data del fatto | Norme applicabili | Atti interruttivi / sospensivi | Calcolo |
|---|---|---|---|---|
| | | | | [rinvio allo SCADENZARIO / CALCOLO DA VERIFICARE] |
### 5.2 Particolare tenuità del fatto (art. 131-bis c.p.): elementi degli atti
| Profilo previsto dalla norma (testo acquisito) | Elementi nel senso della ricorrenza (estratti) | Elementi in senso contrario (estratti) |
|---|---|---|
> Nessuna valutazione; nessun giudizio sulla personalità o sull'abitualità oltre i dati risultanti dagli atti (es. certificato del casellario, se presente).
### 5.3 Altre cause (scriminanti, cause di non punibilità speciali, estinzione per condotte riparatorie, oblazione, remissione)
| Causa | Norma | Elementi degli atti (estratti, a favore e contro) |
|---|---|---|

## 6. Completezza delle indagini
| # | Lacuna (rif. mappatura 4.1 e 4.2) | Accertamento possibile (rif. piano) | Stato (compiuto / non compiuto / non disposto) |
|---|---|---|---|
| | | | |
### Richieste e deduzioni della difesa
| # | Richiesta o deduzione (estratto) | Atto e data | Esito risultante dagli atti |
|---|---|---|---|

## 7. Riti e definizioni alternative astrattamente rilevanti (solo se il PM lo chiede)
| Istituto | Presupposti (norma acquisita) | Dati degli atti pertinenti |
|---|---|---|

## 8. Contenuti che la determinazione dovrà trattare (promemoria, senza testo)
| # | Contenuto | Rif. griglia |
|---|---|---|
| 1 | ogni ipotesi iscritta e ogni persona | sez. 2 |
| 2 | elementi a favore e deduzioni difensive | sez. 2, 6 |
| 3 | qualificazione | sez. 3 |
| 4 | procedibilità e cause di estinzione | sez. 4, 5 |

## 9. Limiti del quadro
[atti non immessi; norme non acquisite; calcoli non eseguiti]

---
*Nota di riserva.* [testo standard]
```

## Controlli finali

- nessuna formula di prognosi («la condanna è ragionevolmente prevedibile», «gli elementi non reggono», «il fatto è tenue»);
- per ogni elemento costitutivo, entrambe le colonne compilate o dichiarate vuote;
- deduzioni difensive tutte riportate con il loro esito risultante dagli atti;
- prescrizione e tenuità ridotte a dati ed estratti;
- nessuna bozza di richiesta o di decreto;
- linguaggio conforme alla presunzione di non colpevolezza (art. 115-bis c.p.p.).

## Modalità aggiornamento

Nuovi atti (esito di accertamenti, memorie dopo l'avviso, interrogatori richiesti dalla difesa) si integrano prima nella mappatura e poi nel quadro, con la marca `[AGG. v[n]]`; la versione cresce di 0.1.

---
*Nota di riserva.* Documento di supporto generato con strumenti di intelligenza artificiale nel tenant ministeriale, sulla base dei soli atti indicati nella mappa di copertura. Non contiene valutazioni sulla responsabilità, sull'attendibilità delle prove o sulle esigenze cautelari. Estratti, norme e precedenti vanno verificati sulle fonti. Ogni decisione è riservata al magistrato (art. 15 l. n. 132/2025).
