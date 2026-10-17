---
name: app-analisi-motivi-impugnazione
description: Analisi strutturata dei motivi di impugnazione penale per il giudice d'appello e, con gli adattamenti indicati, per il consigliere di cassazione - tabella che collega ogni motivo ai capi e ai punti della sentenza impugnata con estratti del motivo e della sentenza, checklist descrittiva dei requisiti di forma e specificità (art. 581 c.p.p. nel testo vigente, da acquisire con l'agente Normattiva), perimetro devolutivo (art. 597 c.p.p.), richieste di rinnovazione dell'istruttoria (art. 603 c.p.p.), segnalazione del divieto di reformatio in peius, impugnazioni del PM, incidentali e della parte civile, motivi nuovi e memorie. Non valuta ammissibilità né fondatezza e non redige la sentenza. Produce ANALISI_MOTIVI_[RG].md. Usare quando il giudice o il relatore chiede di schedare un atto d'appello o un ricorso, collegare i motivi alla sentenza, preparare la relazione o l'udienza.
---

# Analisi dei motivi di impugnazione (giudice penale dell'impugnazione)

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

Mettere a fianco, per ciascun motivo, ciò che l'impugnante chiede e ciò che la sentenza impugnata ha detto sul punto, così che il giudice veda subito il perimetro della cognizione e i passaggi della decisione di primo grado investiti. La skill **descrive**: non dichiara un motivo generico o specifico, ammissibile o inammissibile, fondato o infondato, e **non redige** la sentenza né la relazione decisoria (CSM, aggiornamento 22 luglio 2026, § 8).

## Input

Sentenza impugnata; atti di impugnazione (PM, imputati, parte civile, responsabile civile); eventuali impugnazioni incidentali, motivi nuovi, memorie; se richiesto, i verbali del primo grado indicati nei motivi (preferibilmente tramite `dib-mappatura-prove` del primo grado). Se esiste `ANALISI_MOTIVI_[RG].md`, modalità aggiornamento.

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

### CHECKPOINT 0 – Atti e regime

Confermare con il giudice gli atti caricati e il grado (appello o ricorso per cassazione). Acquisire con l'agente Normattiva, nella versione vigente alla data di proposizione dell'impugnazione, gli artt. 568, 571, 576, 581, 585, 591, 593, 593-bis, 595, 597, 603 c.p.p. per l'appello, e gli artt. 606, 610, 611 c.p.p. per la cassazione, con la disciplina transitoria delle modifiche intervenute. Senza conferma il flusso non prosegue.

### Fase 1 – Mappa della sentenza impugnata

Scomporre la sentenza in **capi** (un capo per ciascuna imputazione e per ciascuna statuizione autonoma: responsabilità, qualificazione, circostanze, pena, benefici, pene accessorie, confisca, statuizioni civili, spese) e, per ciascun capo, in **punti** (le questioni decise: es. attendibilità di una fonte, sussistenza del dolo, bilanciamento delle circostanze). Per ogni punto: estratto della sentenza con pagina. Dispositivo per intero.

**CHECKPOINT 1** – il giudice valida la scomposizione in capi e punti.

### Fase 2 – Mappa dei motivi

Per ciascun atto di impugnazione: dati formali risultanti (parte, difensore, data di deposito, modalità, eventuali allegati richiesti dalla norma come acquisita); richieste per intero; ciascun motivo con estratto integrale della parte che enuncia la censura, le ragioni di diritto e gli elementi di fatto indicati, e le prove richiamate.

### Fase 3 – Collegamento motivi-sentenza

Tabella che collega ogni motivo al capo e ai punti investiti, con l'estratto corrispondente della sentenza. Per ogni motivo si registra, descrittivamente:
- se indica i capi e i punti cui si riferisce;
- se indica le prove delle quali si deduce l'inesistenza, l'omessa assunzione o l'omessa o erronea valutazione;
- se indica le richieste, anche istruttorie;
- se si confronta con un passo identificato della sentenza (citazione testuale o rinvio a pagina) oppure no.

Le voci seguono gli elementi richiesti dalla norma acquisita con l'agente Normattiva; la tabella riporta **presenza o assenza** dell'elemento con estratto, mai il giudizio di specificità. Per il ricorso per cassazione si aggiunge la colonna «caso dell'art. 606 c.p.p. indicato dal ricorrente».

### Fase 4 – Perimetro e segnalazioni

- **Devoluzione**: capi e punti non investiti da alcun motivo (dato descrittivo) e questioni rilevabili d'ufficio in ogni stato e grado che emergono dagli atti, solo segnalate.
- **Reformatio in peius**: se l'impugnazione è proposta dal solo imputato, segnalare l'operatività del divieto (art. 597, comma 3, c.p.p., testo da Normattiva) e i capi su cui inciderebbe; se vi è impugnazione del PM, indicare capi e punti da questa investiti.
- **Rinnovazione dell'istruttoria**: per ogni richiesta, prova richiesta, motivo cui si collega, ragioni addotte (estratti); segnalare i casi in cui la richiesta riguarda prove dichiarative ritenute decisive in primo grado e l'impugnazione del PM è contro una sentenza di proscioglimento (art. 603, comma 3-bis, c.p.p., testo da Normattiva). Nessuna valutazione di necessità.
- **Parte civile**: motivi relativi ai soli interessi civili; segnalare le norme sulla decisione agli effetti civili da acquisire.
- **Motivi nuovi e memorie**: data, collegamento con i motivi originari (descrittivo).
- **Termini**: data della sentenza, del deposito della motivazione, della notifica o comunicazione, del deposito dell'impugnazione; norme sui termini da Normattiva; per l'improcedibilità ex art. 344-bis c.p.p., solo date. Nessun calcolo conclusivo.

### Fase 5 – Ricerche

Per ogni motivo, set di stringhe Italgiure (`pen-ricerca-italgiure`) simmetrici per la tesi dell'impugnante e quella della sentenza impugnata o dell'appellato; precedenti citati nei motivi e in sentenza marcati DA VERIFICARE (la verifica dei precedenti citati in sentenza è prioritaria: cfr. Cass. pen., Sez. 3, n. 25455/2025).

**CHECKPOINT 2** – consegna e validazione.

---

## Template

```markdown
# ANALISI DEI MOTIVI DI IMPUGNAZIONE
**Corte d'appello di [..], Sezione penale [..]** – R.G. App. n. [..] – Sentenza impugnata: [giudice, n., data]
**Data**: [..] – **Versione**: [1.0] – **Norme acquisite il**: [..]

## 1. Dispositivo della sentenza impugnata (testo integrale)
## 2. Capi e punti della sentenza
| Capo | Punto | Estratto della sentenza | Pagina |
|---|---|---|---|

## 3. Atti di impugnazione
| Sigla | Parte | Difensore | Deposito | Dati formali risultanti | Richieste (estratto integrale) |
|---|---|---|---|---|---|

## 4. Motivi e collegamento con la sentenza
| Motivo | Atto | Censura (estratto) | Capo / punto investito | Passo della sentenza (estratto) | Elementi richiesti dalla norma: presenza / assenza con estratto | Prove richiamate |
|---|---|---|---|---|---|---|

## 5. Perimetro della cognizione
### 5.1 Capi e punti non investiti
### 5.2 Questioni rilevabili d'ufficio (segnalazione)
### 5.3 Divieto di reformatio in peius
### 5.4 Richieste di rinnovazione dell'istruttoria
| Prova richiesta | Parte | Motivo | Ragioni addotte (estratto) | Segnalazioni normative |
|---|---|---|---|---|
### 5.5 Parte civile e statuizioni civili
### 5.6 Motivi nuovi e memorie

## 6. Date e termini (nessun calcolo conclusivo)
## 7. Precedenti citati (motivi e sentenza) – DA VERIFICARE
## 8. Ricerche suggerite per Italgiure
## 9. Mappa di copertura

---
*Nota di riserva.* [testo della regola comune]
```

---

## Controlli finali

- dispositivo e richieste riportati per intero; ogni motivo collegato ad almeno un capo o dichiarato «non collegabile a un capo identificato» con estratto;
- la colonna sui requisiti contiene solo presenza o assenza con estratto, mai «generico», «specifico», «inammissibile»;
- impugnazioni di tutte le parti trattate con la stessa struttura;
- nessuna indicazione di esito; nessun testo di sentenza o di relazione decisoria.

## Modalità aggiornamento

Motivi nuovi, memorie, esiti di rinnovazione: aggiungere con `[AGG. v[n]: SIGLA, data]`; versione +0.1. Salvare `ANALISI_MOTIVI_[RG].md` se possibile, altrimenti in chat. Lo studio delle questioni prosegue con `pen-studio-questioni-giudice`.
