---
name: analisi-fascicolo-giudice
description: Scheda di studio del fascicolo civile per il magistrato, redatta in posizione di terzietà - dati identificativi e regime processuale, parti, indice di atti e provvedimenti, timeline, domande, conclusioni, eccezioni, questioni rilevabili d'ufficio da segnalare, stato istruttorio, mappa neutrale delle questioni con set di parole chiave per Italgiure e richieste per l'agente Normattiva, lacune e mappa di copertura. Tutte le sintesi sono estrattive. Produce SCHEDA_FASCICOLO_[RG].md, aggiornabile. Usare quando il giudice chiede di studiare, schedare o riepilogare un fascicolo, preparare un'udienza o una decisione, o aggiornare la scheda dopo nuovi depositi.
---

# Scheda di studio del fascicolo (per il magistrato)

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

Fornire al giudice una visione completa e verificabile del fascicolo, utile per l'udienza, per i provvedimenti istruttori e per la decisione. La scheda descrive il fascicolo: non valuta la fondatezza delle domande e non suggerisce esiti.

## Input

Gli atti e i documenti caricati o presenti nella cartella del fascicolo (PDF, anche firmati digitalmente, DOCX, TXT). Se nella cartella esiste già `SCHEDA_FASCICOLO_[RG].md`, si procede in **modalità aggiornamento** (vedi in fondo).

---

## Regole comuni del Laboratorio

1. **Riserva della decisione al magistrato.** Ogni decisione sull'interpretazione e sull'applicazione della legge, sulla valutazione dei fatti e delle prove e sull'adozione del provvedimento spetta al magistrato (art. 101, secondo comma, Cost.; art. 15 l. 23 settembre 2025, n. 132). Ogni output si chiude con la *Nota di riserva*.
2. **Terzietà.**
   - Le parti si indicano con il ruolo processuale (parte attrice, parte convenuta, terzo chiamato, interveniente), mai con espressioni di appartenenza.
   - Stessa struttura e stesso grado di analiticità per ciascuna parte; le posizioni si espongono nell'ordine processuale (prima chi ha introdotto la domanda o l'eccezione).
   - Nessun aggettivo valutativo sulle difese («fondata», «pretestuosa», «convincente», «generica» se non come dato riferito all'art. 115 c.p.c. e rimesso al giudice).
   - Nessun fatto estraneo agli atti; nessuna ricerca esterna su parti, difensori, testimoni o consulenti. I fatti che potrebbero essere notori si segnalano come tali, per la valutazione del giudice ex art. 115, secondo comma, c.p.c.
   - Le questioni rilevabili d'ufficio non sollevate dalle parti si segnalano soltanto, con l'avvertenza che, se il giudice intende porle a fondamento della decisione, deve assegnare il termine ex art. 101, secondo comma, c.p.c.
   - Nessuna sezione «punti di forza», «strategia» o «rischi» riferita a una parte.
3. **Sintesi estrattive** (skill `sintesi-estrattiva`): ogni contenuto degli atti si riporta con estratti tra caporali e localizzatore [SIGLA, p. n, § n]. Domande, eccezioni e conclusioni sempre per intero.
4. **Giurisprudenza.** Nessuna ricerca autonoma e nessun precedente citato a memoria. Per ogni questione si suggeriscono set di parole chiave per Italgiure (skill `ricerca-italgiure`). I precedenti citati dalle parti si riportano come citati, con la marca DA VERIFICARE.
5. **Norme: agente Normattiva.** Vedi sezione dedicata.
6. **Lingua.** Vocali accentate corrette; niente trattino lungo (—); registro tecnico e piano.

### Uso dell'agente Normattiva

Il testo delle disposizioni non si riporta a memoria. Si interpella l'agente Normattiva reso disponibile dal Ministero della Giustizia nell'ambiente Copilot dei magistrati (nell'interfaccia: digitare `@` e selezionare l'agente Normattiva; il nome visualizzato può essere diverso).

- Se l'ambiente consente di interpellare l'agente direttamente, lo si interpella.
- Altrimenti si consegna al magistrato la richiesta già formulata e si attende il testo, senza proseguire sulla base della memoria:

  > @Normattiva Riporta il testo dell'art. [n] [fonte: c.c. / c.p.c. / d.lgs. n. .../...] nella versione vigente al [data], e indica le modifiche intervenute dopo tale data con la relativa decorrenza.

- **Data di riferimento**: per le norme sostanziali, la data del fatto o del rapporto; per le norme processuali, la data di instaurazione del giudizio o del compimento dell'atto (regime transitorio). Va sempre indicata.
- Fino alla risposta, la norma compare come [TESTO DA ACQUISIRE CON L'AGENTE NORMATTIVA].

---

## Workflow

### Fase 1 – Acquisizione e indice

1. Elencare tutti i file disponibili. Per i file firmati (`.p7m`) estrarre il PDF contenuto.
2. Assegnare le sigle (CIT, COMP, M1-A, M1-C, M2-A, ..., VERB [data], ORD [data], CTU, DOC A1, DOC C1).
3. Compilare l'**indice degli atti e dei provvedimenti** in ordine cronologico, inserendo anche gli atti menzionati ma non presenti, con l'indicazione [NON PRESENTE NEL FASCICOLO].

### Fase 2 – Regime processuale

Ricavare dagli atti la data di instaurazione del giudizio e indicare se ricade nel rito riformato (procedimenti instaurati dopo il 28 febbraio 2023, d.lgs. n. 149/2022) o nel regime previgente. Indicare il rito (ordinario, semplificato ex artt. 281-decies ss. c.p.c., lavoro, locazioni, altro), la composizione (monocratica o collegiale) e la presenza di condizioni di procedibilità dichiarate negli atti (mediazione, negoziazione assistita) con l'esito documentato. Le norme processuali si verificano con l'agente Normattiva nella versione applicabile.

### Fase 3 – Lettura integrale ed estrazione

Leggere per intero ogni atto e ogni provvedimento, e i documenti richiamati negli atti come decisivi. Per ciascun atto produrre la sintesi estrattiva con la propria mappa di copertura (skill `sintesi-estrattiva`). La scheda riporta gli estratti rilevanti per sezione; le sintesi complete degli atti si allegano in appendice.

### Fase 4 – Compilazione della scheda

Secondo il template seguente.

### Fase 5 – Controlli finali

- ogni affermazione sul contenuto degli atti ha un localizzatore;
- ogni domanda e ogni eccezione presente negli atti compare nella sezione 5 o 7;
- le conclusioni sono quelle dell'ultimo atto in cui sono state formulate o precisate;
- la mappa di copertura è al 100% o la scheda reca l'avviso SCHEDA INCOMPLETA;
- nessun aggettivo valutativo, nessuna percentuale, nessuna indicazione di esito.

---

## Template

```markdown
# SCHEDA DI STUDIO DEL FASCICOLO
**[Ufficio], Sezione [..]** – R.G. n. [..] – Giudice: [..]
**Aggiornata al**: [gg mese aaaa] – **Versione**: [1.0]
**Basi**: [atti letti integralmente, con sigle]

[eventuale avviso SCHEDA INCOMPLETA]

## 1. Dati identificativi e regime processuale
| Campo | Dato | Fonte |
|---|---|---|
| Ufficio e sezione | | |
| Data di instaurazione | | |
| Regime | riformato / previgente | |
| Rito | | |
| Composizione | monocratica / collegiale | |
| Materia e oggetto (come da iscrizione a ruolo) | | |
| Valore dichiarato | | |
| Condizioni di procedibilità | | |

## 2. Parti e difensori
| Parte | Ruolo | Difensore | Procura (atto, pagina) |
|---|---|---|---|

## 3. Indice degli atti e dei provvedimenti
| Sigla | Atto / provvedimento | Parte o autorità | Data | Presente |
|---|---|---|---|---|

## 4. Timeline del processo
| Data | Evento | Fonte |
|---|---|---|

## 5. Domande
### 5.1 Domande di parte attrice
| # | Domanda (estratto integrale) | Fonte | Fatti costitutivi richiamati (estratti) |
|---|---|---|---|
### 5.2 Domande riconvenzionali e di altre parti
[stessa tabella]
### 5.3 Modifiche e precisazioni successive
| # | Domanda | Testo originario | Testo modificato | Atto e data |
|---|---|---|---|---|

## 6. Conclusioni attuali (testo integrale)
**Parte attrice** [SIGLA, p. n]: «...»
**Parte convenuta** [SIGLA, p. n]: «...»

## 7. Eccezioni
| # | Eccezione (estratto) | Parte | Atto e data | Natura indicata dalla parte | Dati utili per la tempestività |
|---|---|---|---|---|---|
> La colonna "Dati utili per la tempestività" riporta solo date e termini risultanti dagli atti (es. deposito della comparsa e data dell'udienza). La valutazione di tempestività e la qualificazione dell'eccezione spettano al giudice.

## 8. Questioni rilevabili d'ufficio da segnalare
| # | Possibile questione | Elementi degli atti da cui emerge (estratti) | Norme (agente Normattiva) | Nota |
|---|---|---|---|---|
| | | | | se posta a fondamento della decisione: art. 101, secondo comma, c.p.c. |
[Se nessuna: "Dagli atti esaminati non emergono elementi riconducibili a questioni rilevabili d'ufficio non trattate dalle parti."]

## 9. Stato istruttorio
### 9.1 Mezzi di prova richiesti
| # | Mezzo | Parte | Atto | Capitoli o oggetto (estratto) | Provvedimento | Esito |
|---|---|---|---|---|---|---|
### 9.2 Provvedimenti istruttori emessi (estratti della parte decisoria)
### 9.3 CTU: quesiti e risposte conclusive (estratti)

## 10. Mappa delle questioni
Le questioni sono elencate nell'ordine logico dell'art. 276, secondo comma, c.p.c. (rito, questioni preliminari di merito, merito, quantum, accessori e spese). L'ordine non esprime alcuna valutazione.

### Q[n]. [Titolo neutro]
- **Posizione di parte attrice**: «...» [SIGLA, p. n]
- **Posizione di parte convenuta**: «...» [SIGLA, p. n]
- **Norme**: [articoli] – richiesta all'agente Normattiva: [testo della richiesta, con data di riferimento]
- **Precedenti citati dalle parti**: [estremi come citati, parte, atto] – DA VERIFICARE
- **Ricerche suggerite per Italgiure**: [set N, A, B, S secondo la skill ricerca-italgiure, almeno una stringa per set]

## 11. Termini e adempimenti risultanti dai provvedimenti
| Termine | Adempimento | Parte | Provvedimento |
|---|---|---|---|

## 12. Lacune del fascicolo
[Atti menzionati e non presenti; documenti citati e non prodotti; pagine illeggibili.]

## 13. Mappa di copertura del fascicolo
| Sigla | Atto | Letto per intero | Sintesi estrattiva | Copertura | Elementi necessari |
|---|---|---|---|---|---|
**Indicatori complessivi**: atti letti [x/y]; copertura media [..]; elementi necessari mancanti nella scheda [elenco o "nessuno"].

## Appendice – Sintesi estrattive dei singoli atti

## Registro aggiornamenti
| Data | Versione | Atti nuovi esaminati | Sezioni modificate |
|---|---|---|---|

---
*Nota di riserva.* Documento di supporto generato con strumenti di intelligenza artificiale sulla base dei soli atti indicati nella mappa di copertura. Non contiene valutazioni decisorie. Estratti, norme e precedenti vanno verificati sulle fonti. La decisione è riservata al magistrato (art. 15 l. n. 132/2025).
```

---

## Modalità aggiornamento

1. Leggere per intero la scheda esistente e il registro aggiornamenti.
2. Individuare gli atti depositati dopo l'ultimo aggiornamento.
3. Aggiornare solo le sezioni interessate, senza cancellare le voci precedenti: le modifiche si marcano con `[AGG. v[n]: SIGLA, data]`.
4. Aggiornare indice, timeline, mappa di copertura e registro; incrementare la versione di 0.1.

Se l'ambiente consente di salvare file, salvare `SCHEDA_FASCICOLO_[RG].md` nella cartella del fascicolo; altrimenti restituire il testo in chat.
