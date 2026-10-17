---
name: bozza-sentenza-civile
description: Bozza di sentenza civile di primo grado (Tribunale, monocratico o collegiale) per il magistrato, conforme all'art. 132 c.p.c. e all'art. 118 disp. att. c.p.c. - epigrafe completa, conclusioni delle parti in testo integrale, esposizione del fatto e dello svolgimento del processo in forma estrattiva con localizzatori, e una parte in diritto che, questione per questione nell'ordine dell'art. 276 c.p.c., presenta le opzioni di decisione alternative già redatte in stile di motivazione, con i percorsi decisori complessivi, le alternative sulle spese e i dispositivi corrispondenti. Non sceglie l'opzione, non cita precedenti a memoria (segnaposto con parole chiave per Italgiure), acquisisce le norme con l'agente Normattiva. Include in appendice la tabella di corrispondenza tra chiesto e pronunciato (art. 112 c.p.c.). Usare quando il giudice chiede una bozza, una minuta o uno schema di sentenza.
---

# Bozza di sentenza civile con opzioni di decisione

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

Consegnare al giudice una minuta su cui lavorare: le parti descrittive (epigrafe, conclusioni, fatto e svolgimento del processo) già complete e verificabili; la parte in diritto organizzata in **opzioni alternative**, ciascuna scritta come potrebbe comparire in sentenza. Il giudice sceglie, cancella le opzioni non condivise, riscrive ciò che ritiene. La bozza non contiene alcuna indicazione su quale opzione adottare.

---

## Regole comuni del Laboratorio

1. **Riserva della decisione al magistrato** (art. 101, secondo comma, Cost.; art. 15 l. 23 settembre 2025, n. 132). La bozza reca in testa e in coda la *Nota di riserva*, da eliminare solo all'atto della redazione definitiva da parte del giudice.
2. **Terzietà.**
   - Le opzioni di ogni questione hanno struttura, cura redazionale ed estensione comparabili.
   - Ordine delle opzioni: quello di introduzione delle tesi nel processo (prima la tesi di chi ha proposto la domanda o l'eccezione). L'ordine è dichiarato privo di significato valutativo.
   - Nessun aggettivo valutativo fuori dal testo delle opzioni; dentro le opzioni, il registro è quello asciutto della motivazione.
   - Nessun fatto estraneo agli atti; nessuna ricerca esterna su parti, difensori, testimoni o consulenti.
   - Una questione rilevabile d'ufficio non trattata dalle parti non può costituire opzione decisoria senza che il giudice abbia provocato il contraddittorio: la bozza la segnala con il richiamo all'art. 101, secondo comma, c.p.c. e la tiene fuori dai dispositivi finché il contraddittorio non risulta dagli atti.
3. **Sintesi estrattive** (skill `sintesi-estrattiva`): fatto, svolgimento del processo e posizioni delle parti si redigono con estratti tra caporali e localizzatori [SIGLA, p. n]; conclusioni sempre per intero.
4. **Giurisprudenza.** Nessun precedente citato a memoria. Dove la motivazione richiede un precedente si inserisce il segnaposto `[PRECEDENTE DA REPERIRE – Italgiure: <stringa di ricerca>]` con stringhe costruite secondo la skill `ricerca-italgiure`. I precedenti citati dalle parti compaiono solo se il giudice ne ha fornito il testo; altrimenti con la marca `[DA VERIFICARE]`.
5. **Norme: agente Normattiva** (vedi sotto). Nessun testo normativo riprodotto a memoria; nessuna citazione di comma o di lettera non verificata.
6. **Lingua.** Vocali accentate corrette; niente trattino lungo (—); periodi brevi; nessuna formula enfatica; nessuna antitesi retorica del tipo «non solo ... ma anche».

### Uso dell'agente Normattiva

Per ogni disposizione richiamata nella bozza si interpella l'agente Normattiva reso disponibile dal Ministero della Giustizia nell'ambiente Copilot dei magistrati (`@` e selezione dell'agente). Se non è possibile interpellarlo direttamente, si raccolgono tutte le richieste in un unico elenco da consegnare al giudice:

> @Normattiva Riporta il testo dell'art. [n] [fonte] nella versione vigente al [data rilevante], e indica le modifiche successive con decorrenza e disciplina transitoria.

Data rilevante: data del fatto o del rapporto per le norme sostanziali; data di instaurazione del giudizio o dell'atto per le norme processuali. Le norme non ancora acquisite compaiono nel testo come `[ART. .. – TESTO DA ACQUISIRE CON L'AGENTE NORMATTIVA]`.

---

## Prerequisiti

Prima di redigere verificare la presenza e l'aggiornamento, nella cartella del fascicolo, di:
- `SCHEDA_FASCICOLO_[RG].md` (skill `analisi-fascicolo-giudice`);
- `MAPPATURA_FATTI_[RG].md` (skill `mappatura-fatti-giudice`);
- `STUDIO_QUESTIONI_[RG].md` (skill `valutazione-imparziale-questioni`).

Se mancano o non comprendono gli ultimi atti (conclusioni precisate, scritti conclusivi, verbale di rimessione in decisione), eseguirle o aggiornarle e dirlo al giudice in una riga. Chiedere al giudice solo i dati che non risultano dagli atti: composizione del collegio, modalità e data della decisione, eventuali indicazioni sulle questioni da sviluppare.

---

## Struttura della bozza

### Parte I – Epigrafe (art. 132, secondo comma, nn. 1-3, c.p.c.)

```
REPUBBLICA ITALIANA
IN NOME DEL POPOLO ITALIANO
TRIBUNALE ORDINARIO DI [..]
SEZIONE [..] CIVILE

[Monocratico]
Il Tribunale, in composizione monocratica, nella persona del giudice dott./dott.ssa [..], ha pronunciato la seguente

[Collegiale]
Il Tribunale, riunito in camera di consiglio nelle persone dei magistrati:
dott./dott.ssa [..] – Presidente
dott./dott.ssa [..] – Giudice
dott./dott.ssa [..] – Giudice relatore
ha pronunciato la seguente

SENTENZA

nella causa civile di primo grado iscritta al n. [..] del ruolo generale degli affari contenziosi civili dell'anno [..], [modalità di decisione come risultante dal verbale: es. trattenuta in decisione all'udienza del [..] / decisa all'udienza del [..] ai sensi dell'art. [..] c.p.c.], vertente

TRA

[Denominazione o nome e cognome], C.F. [..], [sede o residenza], rappresentato/a e difeso/a dall'avv. [..] [e dall'avv. ..], come da procura [in calce / allegata] all'[atto], ed elettivamente domiciliato/a [..]
– PARTE ATTRICE –

E

[..]
– PARTE CONVENUTA –

[eventuali: terzo chiamato, interveniente; parte contumace: "contumace" con data della dichiarazione]

OGGETTO: [come da iscrizione a ruolo e domanda]

CONCLUSIONI DELLE PARTI
Per parte attrice [fonte: SIGLA, data, pagina]: «[testo integrale]»
Per parte convenuta [fonte]: «[testo integrale]»
```

Le conclusioni si trascrivono per intero dall'ultimo atto in cui sono state precisate (note di precisazione, verbale d'udienza, atto richiamato). Se l'atto rinvia ad altro atto («come da atto di citazione»), si trascrive il testo richiamato indicando entrambe le fonti.

### Parte II – Fatto e svolgimento del processo

Esposizione concisa (art. 132, secondo comma, n. 4, c.p.c.; art. 118 disp. att. c.p.c.), in prosa, costruita con estratti:

1. **Domanda di parte attrice**: fatti allegati e petitum, con brevi estratti tra caporali e localizzatori. Es.: *Con atto di citazione notificato il [..], [parte attrice] ha convenuto in giudizio [parte convenuta] deducendo che «[..]» [CIT, p. 2] e chiedendo «[..]» [CIT, p. 9].*
2. **Difese di parte convenuta**: costituzione o contumacia, eccezioni, domande riconvenzionali, chiamate di terzo, sempre con estratti.
3. **Sviluppo del processo**: verifiche preliminari, memorie integrative, provvedimenti istruttori (con estratto della parte decisoria), prove assunte, CTU (quesito e conclusioni in estratto), eventuali tentativi di conciliazione, rimessione in decisione e termini concessi. Ogni evento con data e fonte (verbale o provvedimento).
4. **Completezza**: ogni domanda, eccezione e istanza istruttoria presente negli atti deve comparire; il controllo si fa con la tabella di corrispondenza in appendice.

I localizzatori restano nella bozza per consentire la verifica; il giudice li rimuove nella stesura definitiva.

### Parte III – Ragioni della decisione con opzioni

Intestazione: **MOTIVI DELLA DECISIONE**

Nota d'apertura, in corsivo e tra parentesi quadre, da eliminare nella stesura definitiva:
*[Le opzioni che seguono sono alternative. L'ordine di presentazione non indica preferenza. Il giudice sceglie per ciascuna questione l'opzione da adottare, o ne redige una diversa, ed elimina le altre.]*

Per ogni questione, nell'ordine dell'art. 276, secondo comma, c.p.c. (rito; questioni preliminari di merito; an; quantum; accessori):

```
§ [n]. [Titolo della questione]

Premessa comune
[Fatti sui quali le parti concordano, con rinvio alla mappatura; norme applicabili con testo acquisito dall'agente Normattiva; posizioni delle parti in estratto, una per parte, di estensione comparabile.]

OPZIONE [n].1 – [descrizione neutra della soluzione, es. "eccezione di prescrizione accolta"]
Presupposti che il giudice deve ritenere: [in fatto: ...; in diritto: ...]
Testo proposto:
«[Motivazione in stile di sentenza: periodi brevi; principio di diritto; sussunzione dei fatti con richiamo ai documenti e alle prove; eventuale segnaposto PRECEDENTE DA REPERIRE con stringa Italgiure.]»
Effetti: [questioni assorbite; questioni che restano da decidere; incidenza sul dispositivo.]
Coordinamento con i provvedimenti già emessi: [es. diniego di prove orali del [..]: compatibile / richiede motivazione specifica sul punto].

OPZIONE [n].2 – [descrizione neutra]
[stessa struttura, estensione comparabile]

[OPZIONE [n].3 – eventuale soluzione intermedia (accoglimento parziale, riqualificazione nei limiti dell'art. 112 c.p.c.), solo se emerge dagli atti]

[Se la questione è rilevabile d'ufficio e non trattata dalle parti:
SEGNALAZIONE – questione rilevabile d'ufficio non sottoposta al contraddittorio. Prima di porla a fondamento della decisione: art. 101, secondo comma, c.p.c. Opzione non riportata nei dispositivi.]
```

Regole di redazione delle opzioni:
- ogni opzione deve poter essere incollata in sentenza così com'è, salvo segnaposto;
- ogni affermazione di fatto rinvia a un atto, a un documento o a una prova assunta;
- l'opzione che rigetta e quella che accoglie hanno la stessa completezza argomentativa;
- le opzioni sul quantum indicano i criteri di liquidazione desumibili dagli atti (CTU, documenti), con i calcoli esposti in modo verificabile; dove servono parametri esterni (tassi di interesse, indici ISTAT, tabelle) si usa un segnaposto `[DATO DA ACQUISIRE: ..]`;
- le motivazioni sono succinte e possono richiamare precedenti conformi (art. 118 disp. att. c.p.c.), sempre tramite segnaposto se non forniti dal giudice.

### Parte IV – Percorsi decisori e spese

Tabella dei percorsi complessivi (combinazioni coerenti delle opzioni):

| Percorso | Opzioni | Esito sulle domande | Spese: alternative da valutare |
|---|---|---|---|
| P1 | §1-Op.1 (assorbe il resto) | rigetto | soccombenza (art. 91 c.p.c.) / compensazione nei casi dell'art. 92, secondo comma, c.p.c. (testo da agente Normattiva) |
| P2 | §1-Op.2, §2-Op.1, §3-Op.2 | accoglimento parziale | soccombenza reciproca: compensazione totale o parziale |

Per ciascun percorso, testo proposto sul regolamento delle spese con: parte soccombente; scaglione di valore; fasi effettivamente svolte; parametri del d.m. 10 marzo 2014, n. 55 nella versione vigente al momento della liquidazione (da verificare con l'agente Normattiva); importi come `[IMPORTO DA CALCOLARE: fase ..]`; spese di CTU; eventuale domanda ex art. 96 c.p.c. se proposta (estratto).

### Parte V – Dispositivi alternativi

Un dispositivo per ciascun percorso:

```
P.Q.M.

Il Tribunale, definitivamente pronunciando sulla causa iscritta al n. [..] R.G., ogni diversa istanza, eccezione e deduzione disattesa, così provvede:
1. [..];
2. [..];
3. condanna [..] al pagamento in favore di [..] delle spese di lite, che liquida in euro [..] per compensi professionali, oltre rimborso forfettario delle spese generali, IVA e CPA come per legge [ed euro .. per esborsi] / compensa [..];
4. pone le spese di CTU, liquidate con separato decreto, a carico di [..].

[Luogo], [data]
Il Giudice [/ Il Presidente – Il Giudice estensore]
```

Ogni capo del dispositivo deve trovare corrispondenza nella motivazione del percorso; ogni domanda deve ricevere un capo (accoglimento, rigetto, dichiarazione di inammissibilità o assorbimento motivato).

### Appendice (da eliminare prima del deposito)

**A. Corrispondenza tra chiesto e pronunciato (art. 112 c.p.c.)**

| # | Domanda / eccezione / istanza (estratto) | Parte e fonte | Trattata in § | Capo del dispositivo per percorso (P1, P2, ...) |
|---|---|---|---|---|

Nessuna riga può restare senza paragrafo e senza capo, oppure senza indicazione espressa di assorbimento.

**B. Segnaposto da completare**
Elenco numerato di tutti i `[PRECEDENTE DA REPERIRE]`, `[DA VERIFICARE]`, `[TESTO DA ACQUISIRE CON L'AGENTE NORMATTIVA]`, `[DATO DA ACQUISIRE]`, `[IMPORTO DA CALCOLARE]`, con il paragrafo in cui compaiono.

**C. Richieste per l'agente Normattiva** (se non già evase)

**D. Mappa di copertura**

| Sigla | Atto | Letto per intero | Usato in (parti della bozza) |
|---|---|---|---|

Indicatori: atti esaminati [x/y]; domande ed eccezioni con corrispondenza completa [x/y]; estratti verificati letteralmente [x/y]; opzioni per questione [n]; segnaposto aperti [n].

---

## Controlli prima della consegna

- epigrafe completa (giudice, parti, difensori, oggetto, conclusioni integrali);
- tabella di corrispondenza senza righe scoperte;
- per ogni questione almeno due opzioni, salvo che gli atti ne consentano una sola (in tal caso dichiararlo e spiegare perché);
- opzioni di estensione comparabile e prive di formule che ne suggeriscano la preferibilità;
- nessun precedente citato senza testo fornito dal giudice; nessuna norma senza testo acquisito o segnaposto;
- nessuna questione rilevabile d'ufficio inserita nei dispositivi senza contraddittorio risultante dagli atti;
- accenti corretti e assenza del trattino lungo.

## Formato e salvataggio

Se l'ambiente consente di salvare file, salvare `BOZZA_SENTENZA_[RG]_v1.md` nella cartella del fascicolo (versioni successive `_v2`, `_v3`, senza sovrascrivere); se è disponibile la generazione di documenti Word, produrre anche il .docx con le opzioni evidenziate da intestazioni distinte. Altrimenti restituire il testo in chat.

---

*Nota di riserva.* Bozza di supporto generata con strumenti di intelligenza artificiale sulla base dei soli atti indicati nella mappa di copertura. Le opzioni sono alternative e non contengono indicazioni di preferenza. Estratti, norme e precedenti vanno verificati sulle fonti. La decisione e la redazione della sentenza sono riservate al magistrato (art. 15 l. n. 132/2025).
