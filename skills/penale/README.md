# Skill per Copilot – settore penale – Laboratorio AI del Distretto di Napoli

Diciassette skill per i magistrati del settore penale, requirenti e giudicanti, derivate dall'esperienza delle skill forensi dello studio (analisi del fascicolo, mappatura dei fatti, valutazione da giudice terzo, audit delle citazioni, pseudonimizzazione) e dalle sei skill civili del Laboratorio. Sono riorganizzate secondo la posizione del magistrato penale e i limiti dell'art. 15 l. 23 settembre 2025, n. 132 e delle raccomandazioni CSM dell'8 ottobre 2025, aggiornate il 22 luglio 2026.

Struttura piatta (una cartella per skill, `name` = nome della cartella), come richiesto dagli agenti di Microsoft 365 Copilot. Il prefisso indica il gruppo. Ogni `SKILL.md` è autosufficiente, contiene per intero le regole comuni e resta sotto i 19.000 caratteri; il limite degli agenti M365 è 20.000.

## Stato: sperimentale

Le diciassette skill penali sono **sperimentali**. L'approvazione dell'archivio comune non comporta la validazione delle singole skill. Ciascuna resta sperimentale fino a una verifica documentata in tre parti:
- **tecnica**: controllo automatico e revisione del repository;
- **giuridica**: revisione di settore;
- **funzionale**: prova da parte di magistrati della funzione interessata, su fascicoli fittizi di diversa difficoltà, misurando il tempo complessivo (preparazione, caricamento, aggiornamento, correzione e verifica degli output) rispetto al lavoro ordinario.

Le osservazioni dei magistrati si raccolgono in schede di osservazione numerate. Il CHANGELOG indica le modifiche che ne derivano.

## Gruppo 0 – Skill comuni (requirenti e giudicanti)

| Skill | Prodotto | Quando usarla |
|---|---|---|
| `pen-perimetro-ia` | esito CONSENTITA / CONDIZIONATA / ESCLUSA con riformulazione ammissibile | **sempre per prima**: verifica che la richiesta e i dati rientrino nel perimetro |
| `pen-pseudonimizzazione-atti` | versione minimizzata e pseudonimizzata, tabella di corrispondenza | prima di immettere atti con dati di persone offese, minori, collaboratori, utenze |
| `pen-sintesi-estrattiva` | `SINTESI_[atto].md` | sintesi verificabile di CNR, annotazioni, s.i.t., interrogatori, verbali, consulenze, sentenze |
| `pen-ricerca-italgiure` | set di stringhe per Italgiure (archivio penale) | ricerche simmetriche ACCUSA / DIFESA; verifica dei precedenti citati |

## Gruppo A – Pubblico ministero

| Skill | Prodotto | Quando usarla |
|---|---|---|
| `pm-scheda-notizia-di-reato` | `SCHEDA_NDR_[..].md` | lettura della CNR, denuncia o querela: fatti, persone, ipotesi prospettate, procedibilità, termini |
| `pm-mappatura-elementi-bidirezionale` | `MAPPATURA_ELEMENTI_[RGNR].md` | punto delle indagini: elementi **a carico e a favore** per ogni elemento costitutivo (art. 358 c.p.p.) |
| `pm-piano-accertamenti-bidirezionale` | `PIANO_ACCERTAMENTI_[RGNR].md` | accertamenti possibili, sia per l'ipotesi d'accusa sia per le ipotesi alternative |
| `pm-scadenzario-indagini` | `SCADENZARIO_[RGNR].md` | termini delle indagini, delle misure, delle intercettazioni, del 415-bis (solo dati, norme via Normattiva) |
| `pm-quadro-elementi-esito-indagini` | `QUADRO_ESITO_[RGNR].md` | griglia per le determinazioni finali (ragionevole previsione di condanna), senza indicare l'esito |
| `pm-compilazione-moduli-cooperazione` | MAE / OEI compilati in bozza | moduli standardizzati (uso espressamente ammesso, CSM 22.7.2026, punto 12); utilizzabile anche dal giudice per il MAE processuale |

## Gruppo B – Giudice penale

| Skill | Fase | Prodotto |
|---|---|---|
| `gip-esame-richiesta-cautelare` | GIP | scheda di lettura della richiesta di misura, con verifica descrittiva della trasmissione degli elementi a favore (art. 291, comma 1, c.p.p.) |
| `gip-gup-scheda-fascicolo` | GIP / GUP | scheda per archiviazione, opposizione, udienza preliminare, riti alternativi |
| `dib-scheda-fascicolo-dibattimento` | dibattimento | scheda con separazione tra fascicolo del dibattimento e fascicolo del PM (artt. 431, 526 c.p.p.); modalità essenziale (predefinita) o approfondita |
| `dib-mappatura-prove` | dibattimento | prove assunte per capo ed elemento del fatto, posizioni di accusa, difesa e parte civile; facoltativa, attivabile in ogni fase anche dalle trascrizioni già disponibili |
| `pen-studio-questioni-giudice` | GUP / dibattimento / appello | studio imparziale delle questioni processuali e di merito, checklist anti-bias |
| `app-analisi-motivi-impugnazione` | appello / cassazione | tabella motivi, capi e punti della sentenza impugnata |
| `pen-verifica-provvedimento-redatto` | tutte | controllo di completezza, citazioni e lingua del provvedimento **già scritto dal giudice** |

Sequenze tipiche:
- **PM:** perimetro, scheda NDR, mappatura bidirezionale, piano accertamenti, scadenzario, quadro finale.
- **GIP cautelare:** perimetro, pseudonimizzazione (se gli atti sono segreti), esame della richiesta.
- **Dibattimento:** scheda del fascicolo, mappatura delle prove, studio delle questioni; poi il giudice scrive la sentenza e usa la verifica.

## Principi comuni

1. **Riserva al magistrato** (art. 15, comma 1, l. n. 132/2025), per il giudice e per il PM. Nessuna skill redige motivazioni, dispositivi o la parte valutativa di richieste del PM (richiesta cautelare, richiesta di archiviazione, imputazione). Il CSM, con l'aggiornamento del 22.7.2026, esclude «la formulazione del dispositivo e l'affidamento della redazione dei provvedimenti giurisdizionali». Per questo **non esiste una skill «bozza di sentenza penale»**.
2. **Checkpoint bloccanti**: il flusso si ferma e riprende solo dopo la validazione espressa del magistrato (CSM 22.7.2026, § 4).
3. **Segreto investigativo** (CHECKPOINT 0 in ogni skill). Le raccomandazioni del 2025 escludono l'immissione di dati coperti da segreto. L'aggiornamento del 2026 consente gli atti con dati personali nel tenant ministeriale, ma lascia fermo ogni profilo non modificato. In via prudenziale gli atti ancora segreti non si immettono, oppure si immettono solo in estratti pseudonimizzati e conformi alle direttive del capo dell'ufficio. Il punto va chiarito con il CSM o con il Ministero.
4. **Completezza bidirezionale**: terzietà per il giudice; per il PM, sezione obbligatoria «Elementi a favore della persona sottoposta alle indagini» e «Ipotesi alternative compatibili con gli atti» (artt. 358 e 291, comma 1, c.p.p.).
5. **Presunzione di non colpevolezza** nel linguaggio (art. 27 Cost.; art. 115-bis c.p.p.).
6. **Divieto di profilazione e di valutazioni predittive** (pericolosità, recidiva, fuga), conforme all'art. 5 e all'allegato III del reg. UE 2024/1689.
7. **Sintesi solo estrattive** con localizzatore e mappa di copertura.
8. **Giurisprudenza**: nessun precedente a memoria; stringhe Italgiure simmetriche. Le stringhe non contengono dati identificativi del procedimento, perché Italgiure è fuori dal tenant.
9. **Norme**: tramite l'agente Normattiva ministeriale. Per le norme penali sostanziali si chiedono la versione alla data del fatto e tutte le successive (art. 2 c.p.).

**Vincolo anti-allucinazione.** Ogni skill, comprese quelle civili originarie, si apre con un blocco che prevale su ogni altra istruzione. Copilot lavora solo sui documenti forniti (atti, testi dell'agente Normattiva, risultati Italgiure incollati dal magistrato). Non cita norme o giurisprudenza assenti da quei documenti. Dichiara le lacune con segnaposto, non genera link e prima della consegna esegue un controllo finale dei riscontri (CSM 22.7.2026, § 5).

## Installazione

Come per le skill civili (vedi `skills-copilot\README.md`). Microsoft 365 Copilot ammette al massimo 8 skill per agente, quindi si consigliano tre agenti:
- **Agente PM**: `pen-perimetro-ia`, `pen-pseudonimizzazione-atti`, `pen-sintesi-estrattiva`, `pen-ricerca-italgiure`, `pm-scheda-notizia-di-reato`, `pm-mappatura-elementi-bidirezionale`, `pm-piano-accertamenti-bidirezionale`, `pm-quadro-elementi-esito-indagini`. Lo scadenzario e i moduli di cooperazione vanno in un secondo agente o nelle istruzioni.
- **Agente GIP/GUP**: le quattro comuni, `gip-esame-richiesta-cautelare`, `gip-gup-scheda-fascicolo`, `pen-studio-questioni-giudice`, `pen-verifica-provvedimento-redatto`.
- **Agente dibattimento e impugnazioni**: `pen-perimetro-ia`, `pen-sintesi-estrattiva`, `pen-ricerca-italgiure`, `dib-scheda-fascicolo-dibattimento`, `dib-mappatura-prove`, `pen-studio-questioni-giudice`, `app-analisi-motivi-impugnazione`, `pen-verifica-provvedimento-redatto`.

**Uso.** Solo nel tenant Microsoft 365 Copilot del Ministero della giustizia e solo dopo la formazione richiesta dal CSM. I numeri di articolo citati nelle skill sono stati verificati su Normattiva il 17 ottobre 2026 (esistenza e pertinenza). Il testo delle norme da applicare va comunque acquisito, a ogni uso, con l'agente Normattiva nella versione rilevante.
