---
name: pen-sintesi-estrattiva
description: Sintesi estrattiva e verificabile di atti del procedimento penale per il magistrato (PM, GIP/GUP, giudice del dibattimento e d'appello) - comunicazioni di notizia di reato, annotazioni e informative di PG, denunce e querele, verbali di sommarie informazioni, interrogatori, verbali di perquisizione e sequestro, verbali dibattimentali di esame e controesame, consulenze tecniche e perizie, memorie difensive, sentenze e ordinanze. Solo passi testuali tra caporali con localizzatore (atto, pagina, riga o minuto), mai parafrasi; mappa di copertura con indicatori; checklist degli elementi necessari per tipo di atto penale; elementi a favore della persona sottoposta alle indagini o dell'imputato sempre estratti. Usare quando il magistrato chiede di riassumere, sintetizzare, schedare o estrarre un atto penale, e quando le altre skill penali del Laboratorio richiedono una sintesi.
---

# Sintesi estrattiva di atti penali con prova di completezza

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

Il magistrato deve potersi fidare della sintesi senza rileggere l'atto e, quando lo ritiene, verificarla in pochi secondi. La sintesi riproduce le parole dell'atto e mai una loro riformulazione: ogni parafrasi contiene già una lettura, e nel processo penale la lettura di una dichiarazione è spesso già una valutazione di attendibilità, riservata al magistrato.

La sintesi è **estrattiva** (seleziona e riporta passi dell'originale) e mai **astrattiva**.

## Input

Uno o più atti del procedimento (PDF, DOCX, TXT, trascrizioni), nella forma decisa al CHECKPOINT 0 (integrale, estratto o versione pseudonimizzata). Indicazione della funzione del magistrato e della fase (indagini, udienza preliminare, dibattimento, impugnazione).

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

## Regole di estrazione

1. **Unità minima.** Passo testuale tra caporali + localizzatore tra parentesi quadre:
   «ho visto l'auto ferma davanti al cancello verso le 22» [SIT T1 12.03.2025, p. 2]
   Per i verbali stenotipici: [VERB DIB 04.06.2026, p. 14, rr. 3-7]; per le registrazioni: [AUDIO ud. 04.06.2026, min. 32:10].
2. **Sigle.** Legenda in testa. Esempi: CNR = comunicazione di notizia di reato; ANN PG [data] = annotazione di PG; DEN / QUER = denuncia / querela; SIT [persona pseudonimizzata, data] = sommarie informazioni; INT [data] = interrogatorio; VPS = verbale di perquisizione e sequestro; CT-PM / CT-DIF = consulenza tecnica del PM / della difesa; PER = perizia; MEM-DIF = memoria difensiva; VERB DIB [data] = verbale dibattimentale; SENT / ORD = sentenza / ordinanza.
3. **Fedeltà letterale.** Grafia, refusi ed espressioni dialettali si conservano ([sic] se necessario); omissioni interne con [...]; integrazioni indispensabili tra parentesi quadre.
4. **Testo di raccordo.** Ammessi solo: etichette neutre di argomento in corsivo; indicazioni di provenienza; verbi di attribuzione corrispondenti all'operazione compiuta («dichiara», «riferisce», «risponde», «annota», «deduce», «chiede», «eccepisce», «produce»). Vietati i verbi che qualificano: «ammette», «confessa», «ritratta», «si contraddice», «conferma», «smentisce», «nega falsamente», «ricorda vagamente». La qualificazione di una dichiarazione come confessione, ritrattazione o contraddizione è valutazione riservata.
5. **Domande e risposte.** Nei verbali di esame si riportano la domanda e la risposta, con l'indicazione della parte che esamina (PM, difesa, parte civile, presidente). Una risposta senza domanda può cambiare significato.
6. **Opposizioni e contestazioni.** Opposizioni, contestazioni ex artt. 500 e 503 c.p.p., letture e provvedimenti del giudice in udienza si riportano per intero: incidono sull'utilizzabilità.
7. **Natura della fonte.** Si distingue sempre ciò che il dichiarante riferisce per conoscenza diretta da ciò che riferisce de relato, riportando il passo dal quale la distinzione risulta, senza qualificarla.
8. **Elementi a favore.** Ogni passo dal quale risultino circostanze favorevoli alla persona sottoposta alle indagini o all'imputato si estrae con lo stesso grado di dettaglio dei passi sfavorevoli, e si elenca nella sezione dedicata.
9. **Testo illeggibile o incerto.** [ILLEGIBILE, p. n] o [LETTURA INCERTA, p. n]; nelle trascrizioni [INCOMPRENSIBILE nella trascrizione, p. n]. Non si ricostruisce.
10. **Contenuti non testuali** (fotogrammi, planimetrie, tabulati): [DESCRIZIONE, p. n: ...], contata negli indicatori.

## Elementi necessari per tipo di atto

| Tipo di atto | Elementi che la sintesi deve contenere |
|---|---|
| CNR / annotazione di PG | autore e data; fonte della notizia; fatti narrati; persone indicate e ruolo attribuito; atti compiuti e allegati; ipotesi di reato prospettate, come prospettate; atti urgenti; circostanze favorevoli eventualmente annotate |
| Denuncia / querela | autore e data; fatti; persone indicate; istanza di punizione (testo integrale); data di conoscenza del fatto dichiarata; documenti allegati; eventuale remissione |
| Sommarie informazioni | dichiarante (pseudonimizzato); qualità; avvisi dati; dichiarazioni in ordine cronologico; fonti indicate di ciò che si riferisce |
| Interrogatorio | avvisi (art. 64 c.p.p., testo da Normattiva); presenza del difensore; scelta di rispondere o no; dichiarazioni; documenti prodotti |
| Perquisizione e sequestro | provvedimento presupposto; luogo, data, presenti; cose sequestrate (elenco integrale); dichiarazioni a verbale; avvisi |
| Verbale dibattimentale | presenti; questioni preliminari; ordinanze (integrale); esame, controesame, riesame; contestazioni; opposizioni; acquisizioni; rinvii |
| Consulenza / perizia | quesiti (integrale); operazioni e partecipanti; metodo indicato; risposte conclusive (integrale); osservazioni dei consulenti delle altre parti |
| Memoria difensiva | richieste; deduzioni per tema; elementi indicati a favore; documenti |
| Sentenza / ordinanza | imputazione o oggetto; dispositivo (integrale); ragioni per capo (estratti); termini e provvedimenti accessori |

## Prova di completezza

### A. Indice dell'originale
Partizioni dell'atto (paragrafi, domande-risposte per blocchi, pagine), ciascuna con codice S1, S2, ...

### B. Mappa di copertura

| Sezione | Pagine | Esito | Estratti | Motivo dell'omissione |
|---|---|---|---|---|

Esiti: **E** estratta; **O-S** formula di stile (intestazioni, avvisi standard già riportati, chiusure); **O-R** ripete altra sezione (indicare quale); **O-N** omessa per altra ragione, da motivare in una riga ed elencare in chiaro. Le parti contenenti circostanze favorevoli non possono essere omesse come O-R se la ripetizione introduce varianti.

### C. Indicatori

- Copertura delle sezioni: deve essere 100%.
- Elementi necessari presenti: x/y; per ogni assente, «assente nell'originale» o integrazione.
- Elementi a favore estratti: n (o dichiarazione «Esaminate le sezioni [..], non risultano circostanze favorevoli»).
- Deroghe: n DESCRIZIONE, n LETTURA INCERTA.
- Estratti verificati letteralmente: n/n.

Copertura inferiore al 100% o elemento necessario mancante: avviso **SINTESI INCOMPLETA** in testa.

## Workflow

### CHECKPOINT 0 – Dati e segreto
Domandare se l'atto è coperto da segreto, se contiene intercettazioni non acquisite, dati di minori, dati della persona offesa protetti dall'art. 734-bis c.p., categorie particolari di dati. Applicare le misure decise (eventuale skill `pen-pseudonimizzazione-atti`). Attendere conferma.

### Fase 1 – Indice dell'originale
Scomporre l'atto in sezioni. **CHECKPOINT 1**: consegnare l'indice; il magistrato conferma o indica le sezioni su cui concentrarsi (ogni esclusione richiesta dal magistrato si registra come O-N «esclusa su indicazione del magistrato»).

### Fase 2 – Estrazione
Estrarre secondo le regole. Compilare mappa e indicatori.

### Fase 3 – Controllo letterale
Ricercare ogni estratto nel testo sorgente; correggere o eliminare quelli non identici; dichiararne il numero.

### CHECKPOINT 2 – Consegna
Consegnare la sintesi. Se il magistrato chiede un ordinamento per temi o per capo d'imputazione, si riordina conservando i localizzatori.

## Template di output

```markdown
# SINTESI ESTRATTIVA – [atto], [autore o dichiarante pseudonimizzato], [data]
**Procedimento**: [n. R.G.N.R. / R.G. GIP / R.G. Dib.] – **Fase**: [..]
**Fonte**: [file], pp. [n] – **Forma immessa**: [integrale / estratto / pseudonimizzata]
**Legenda sigle**: [...]

[eventuale avviso SINTESI INCOMPLETA]

## Estratti
*[Etichetta tema]*
E1. «...» [SIGLA, p. n]
E2. D. (PM) «...» R. «...» [VERB DIB .., p. n, rr. ..]

## Elementi a favore della persona sottoposta alle indagini / dell'imputato
F1. «...» [SIGLA, p. n]
[oppure: Esaminate le sezioni [..], non risultano circostanze favorevoli.]

## Parti da riportare per intero
[imputazione, istanza di punizione, quesiti, conclusioni, dispositivo, ordinanze]

## Mappa di copertura
## Elementi necessari
## Indicatori

---
*Nota di riserva.* [testo standard]
```

Più atti: una sintesi per atto e una tabella riepilogativa (atto, sezioni, copertura, elementi necessari, elementi a favore, deroghe).

## Controlli finali

- nessun verbo qualificativo fuori dalle citazioni;
- ogni estratto ha un localizzatore e una sola fonte;
- sezione «Elementi a favore» compilata o dichiarata vuota dopo l'esame;
- linguaggio conforme alla presunzione di non colpevolezza;
- copertura 100% o avviso SINTESI INCOMPLETA.

Se l'ambiente consente di salvare file: `SINTESI_[sigla]_[data].md` nella cartella del procedimento; altrimenti testo in chat.

---
*Nota di riserva.* Documento di supporto generato con strumenti di intelligenza artificiale nel tenant ministeriale, sulla base dei soli atti indicati nella mappa di copertura. Non contiene valutazioni sulla responsabilità, sull'attendibilità delle prove o sulle esigenze cautelari. Estratti, norme e precedenti vanno verificati sulle fonti. Ogni decisione è riservata al magistrato (art. 15 l. n. 132/2025).
