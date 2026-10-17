---
name: pen-pseudonimizzazione-atti
description: Prepara una versione minimizzata e pseudonimizzata di un atto penale prima di ogni ulteriore elaborazione con Copilot - persone fisiche (indagati, imputati, persone offese, testimoni, minori, collaboratori, agenti sotto copertura, difensori, consulenti), utenze telefoniche, IMEI, IMSI, targhe e telai, IBAN e conti, indirizzi, coordinate, account e indirizzi IP, codici fiscali, numeri di procedimento, luoghi localizzanti - con pseudonimi coerenti (PSI-1, PO-1, T-1, MIN-1...) e [omissis]; omette le parti non necessarie alla finalità (intercettazioni non acquisite, conversazioni irrilevanti, categorie particolari di dati, generalità protette dall'art. 734-bis c.p.); restituisce al magistrato la tabella di corrispondenza da custodire fuori dal sistema e l'avvertenza sul rischio di reidentificazione indicato dal CSM. Usare quando il magistrato chiede di anonimizzare, pseudonimizzare, oscurare, minimizzare un atto penale, o quando pen-perimetro-ia o un CHECKPOINT 0 lo richiedono.
---

# Pseudonimizzazione e minimizzazione degli atti penali

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

Consentire l'elaborazione di un atto penale riducendo al minimo i dati personali immessi. Il CSM raccomanda l'anonimizzazione preventiva come buona pratica, specie quando non è necessario che il sistema operi su dati identificativi (aggiornamento 22 luglio 2026, § 4), e richiama il rischio di reidentificazione anche di dati pseudonimizzati, per incrocio di dataset (delibera 8 ottobre 2025, § 4).

Il risultato è una **pseudonimizzazione**, non un'anonimizzazione: chi dispone della tabella di corrispondenza può ricondurre gli pseudonimi alle persone. La tabella resta al magistrato.

## Limite strutturale

Questa skill opera dentro Copilot: per pseudonimizzare, il testo originale deve essere letto dal sistema. Se l'atto è coperto da segreto investigativo o contiene dati che non devono essere immessi neppure per pochi istanti, la pseudonimizzazione **non** va fatta con Copilot ma con il software di anonimizzazione eventualmente fornito dall'ufficio o a mano, e a Copilot si consegna solo il testo già trattato. La skill lo ricorda al CHECKPOINT 0 e, in quel caso, si limita a fornire la tabella delle categorie da oscurare come istruzione operativa.

## Input

L'atto (o il testo già parzialmente oscurato); la finalità dell'elaborazione successiva (es. sintesi, mappatura); eventuali indicazioni del magistrato su soggetti da non pseudonimizzare (es. enti pubblici).

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

## Categorie e pseudonimi

| Categoria | Sostituzione | Note |
|---|---|---|
| Persona sottoposta alle indagini / imputato | PSI-1, PSI-2 ... / IMP-1 ... | stesso pseudonimo in tutti gli atti dello stesso procedimento |
| Persona offesa | PO-1 ... | nei reati dell'art. 734-bis c.p. anche luoghi, rapporti di parentela e dettagli idonei a identificarla: [omissis] |
| Testimone / persona informata | T-1 ... | |
| Minore | MIN-1 ...; età indicata solo se rilevante per la fattispecie | scuola, quartiere, parenti: [omissis] |
| Collaboratore di giustizia, testimone protetto, agente sotto copertura | [SOGGETTO PROTETTO] | nessun dato identificativo, neppure indiretto (ruolo nell'organizzazione, luoghi di residenza) |
| Difensori, consulenti, periti, interpreti | DIF-1, CT-1, PER-1 ... | |
| Ufficiali e agenti di PG | PG-1 ... o qualifica + reparto generico | salvo indicazione contraria del magistrato |
| Persone giuridiche private | SOC-ALFA, SOC-BETA ... | |
| Utenze, IMEI, IMSI, targhe, telai, IBAN, conti, carte, codici fiscali, account, IP, e-mail | [UTENZA-1], [IMEI-1], [TARGA-1], [IBAN-1] ... | numerazione coerente: la stessa utenza ha sempre lo stesso pseudonimo, perché i collegamenti tra utenze possono essere rilevanti |
| Indirizzi, coordinate, celle | [LUOGO-1] ... o [omissis] | se la distanza tra luoghi è rilevante, il magistrato decide se mantenerla |
| Numeri di R.G.N.R., R.G. GIP, altri procedimenti | [PROC-1] ... | |
| Date | conservate, salvo richiesta | sono quasi sempre necessarie per i termini e per la cronologia |

**Si conservano**: norme, ipotesi di reato, qualifiche giuridiche, enti pubblici non localizzanti, autorità giudiziaria procedente (se il magistrato lo consente), date, importi (salvo richiesta), precedenti giurisprudenziali.

## Minimizzazione

Prima di pseudonimizzare, eliminare le parti non necessarie alla finalità, sostituendole con un segnaposto che ne indica la natura e l'estensione:

- `[OMESSO: intercettazione non acquisita / conversazione irrilevante, pp. ..]`
- `[OMESSO: dati sanitari non rilevanti, pp. ..]`
- `[OMESSO: parti estranee alla finalità indicata, pp. ..]`

Le omissioni si elencano nella mappa delle omissioni, così che il magistrato sappia cosa l'elaborazione successiva non ha visto. Una sintesi o una mappatura costruita su un testo minimizzato deve dichiararlo in testa.

## Workflow

### CHECKPOINT 0 – Ammissibilità del trattamento in Copilot
Domandare: l'atto è coperto da segreto investigativo? contiene materiale che non può essere immesso (intercettazioni non acquisite, archivio riservato, soggetti protetti)? Se sì: STOP; consegnare la tabella delle categorie come istruzione per il trattamento fuori sistema e attendere il testo già trattato.

### Fase 1 – Censimento
Elencare tutte le occorrenze dei dati delle categorie sopra, con pagina, incluse le varianti (cognome da solo, soprannome, iniziali, nome storpiato nella trascrizione, utenze scritte con o senza prefisso). **CHECKPOINT 1**: consegnare il censimento e la proposta di pseudonimi; il magistrato conferma, corregge, indica cosa conservare.

### Fase 2 – Sostituzione e minimizzazione
Applicare gli pseudonimi in modo coerente; sostituire prima le stringhe più lunghe (nome e cognome prima del solo cognome); adattare articoli e preposizioni. Inserire i segnaposto di omissione.

### Fase 3 – Controllo dei residui
Cercare nel testo trattato ogni dato originale censito (cognomi, radici dei nomi, soprannomi, numeri). Cercare anche gli **identificatori indiretti**: combinazioni di professione, luogo, relazione familiare ed evento che consentono di riconoscere la persona. Elencare i residui e correggerli.

### CHECKPOINT 2 – Consegna
Consegnare: testo trattato; tabella di corrispondenza; mappa delle omissioni; esito del controllo dei residui; avvertenza sulla reidentificazione. Il magistrato custodisce la tabella fuori da Copilot (es. file locale protetto) e la cancella dalla conversazione.

## Template di output

```markdown
# VERSIONE PSEUDONIMIZZATA – [atto], [data]
**Finalità dell'elaborazione successiva**: [..]
**Livello**: [solo pseudonimizzazione / pseudonimizzazione e minimizzazione]

[testo trattato]

---
## Mappa delle omissioni
| # | Pagine | Natura | Motivo |
|---|---|---|---|

## Controllo dei residui
- Dati censiti: [n]; occorrenze sostituite: [n]; residui trovati e corretti: [n]
- Identificatori indiretti rilevati: [elenco o "nessuno"]

## Avvertenza
Il testo è pseudonimizzato, non anonimo: con la tabella di corrispondenza o per incrocio con altri dati le persone possono essere reidentificate (CSM, delibera 8 ottobre 2025, § 4). Immettere solo quanto necessario alla finalità indicata.
```

```markdown
# TABELLA DI CORRISPONDENZA – DA CUSTODIRE FUORI DA COPILOT
| Pseudonimo | Dato originale | Categoria | Pagine |
|---|---|---|---|
```

## Controlli finali

- nessun residuo dei dati censiti;
- pseudonimi coerenti tra atti dello stesso procedimento (se si tratta più atti, riusare la tabella confermata);
- omissioni dichiarate e motivate;
- tabella di corrispondenza consegnata separatamente, con l'invito a rimuoverla dalla conversazione.

## Modalità aggiornamento

Per atti successivi dello stesso procedimento il magistrato fornisce la tabella già confermata (o solo l'elenco degli pseudonimi, senza i dati originali, se l'atto nuovo è già trattato): i nuovi soggetti ricevono il primo pseudonimo libero della categoria.

---
*Nota di riserva.* Documento di supporto generato con strumenti di intelligenza artificiale nel tenant ministeriale, sulla base dei soli atti indicati nella mappa di copertura. Non contiene valutazioni sulla responsabilità, sull'attendibilità delle prove o sulle esigenze cautelari. Estratti, norme e precedenti vanno verificati sulle fonti. Ogni decisione è riservata al magistrato (art. 15 l. n. 132/2025).
