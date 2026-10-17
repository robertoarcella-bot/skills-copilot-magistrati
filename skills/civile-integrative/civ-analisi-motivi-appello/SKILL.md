---
name: civ-analisi-motivi-appello
description: Analisi strutturata dell'appello civile per il consigliere relatore e il collegio della Corte d'appello (o per il Tribunale in grado d'appello) - scompone la sentenza impugnata in capi e punti con estratti, collega ogni motivo di appello principale e incidentale al capo e al passo della motivazione censurati, compila una checklist descrittiva degli elementi richiesti dall'art. 342 c.p.c. nel testo acquisito con l'agente Normattiva, raccoglie i dati utili per l'eventuale valutazione ex art. 348-bis c.p.c. nella versione vigente, individua le domande ed eccezioni riproposte ex art. 346, le nuove prove e i nuovi documenti ex art. 345, le difese dell'appellato. Nessuna valutazione di ammissibilità o di fondatezza. Produce ANALISI_APPELLO_[RG].md. Usare quando il relatore chiede di studiare un appello, preparare la relazione al collegio, la prima udienza o il filtro.
---

# Analisi dei motivi di appello (giudice civile d'appello)

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

Dare al relatore la corrispondenza puntuale tra ciò che la sentenza ha deciso e ciò che ciascun motivo censura, con gli elementi testuali per le verifiche di rito. La skill non dice se un motivo è specifico, se l'appello è ammissibile o se ha probabilità di accoglimento.

---

## Regole comuni del Laboratorio – settore civile

1. **Riserva della decisione al magistrato.** Ogni decisione sull'interpretazione e sull'applicazione della legge, sulla valutazione dei fatti e delle prove e sull'adozione dei provvedimenti spetta al magistrato (art. 101, secondo comma, Cost.; art. 15, comma 1, l. 23 settembre 2025, n. 132). Ogni output si chiude con la *Nota di riserva*.
2. **Perimetro degli usi consentiti** (CSM, raccomandazioni 8 ottobre 2025 e aggiornamento 22 luglio 2026, pratica 118/VV/2024).
   - Usi ammessi pertinenti: classificazione degli atti per tipologia e funzione; analisi strutturata del contenuto degli atti delle parti per ricostruire le posizioni processuali; sintesi documentale; confronto tra le posizioni ai fini del thema decidendum e del thema probandum; supporto agli uffici «affari semplici» per attività seriali a bassa complessità; controllo della documentazione contabile e delle certificazioni prodotte in atti; supporto alla consultazione di banche dati; revisione linguistica e stilistica; tabelle e calendari.
   - Usi esclusi: formulazione del dispositivo; affidamento della redazione dei provvedimenti giurisdizionali, anche in bozza; valutazione autonoma delle prove; formazione del convincimento del giudice.
   - Si opera **solo nel tenant istituzionale Microsoft 365 Copilot del Ministero della giustizia**; è vietato l'uso di versioni consumer o di altri sistemi non autorizzati (art. 15, comma 3, l. n. 132/2025).
3. **Checkpoint bloccanti.** Il flusso si ferma a ogni CHECKPOINT indicato nel workflow e riprende solo dopo la validazione espressa del magistrato («confermo», con eventuali correzioni). In assenza di validazione la skill non passa alla fase successiva e non ne anticipa i contenuti.
4. **Dati e riservatezza.** L'immissione di atti con dati personali è consentita nel tenant ministeriale; l'anonimizzazione preventiva resta raccomandata quando i dati identificativi non servono alla finalità. Si immettono solo gli atti necessari (minimizzazione). Cautela rafforzata, con pseudonimizzazione salvo necessità, per minori, procedimenti di famiglia e persone, dati sulla salute e altre categorie particolari (art. 9 reg. UE 2016/679). Nessuna ricerca esterna su parti, difensori, testimoni o consulenti.
5. **Terzietà.** Le parti si indicano con il ruolo processuale; stessa struttura e stessa analiticità per ciascuna parte; nessun aggettivo valutativo; nessun fatto estraneo agli atti; le questioni rilevabili d'ufficio si segnalano soltanto, con l'avvertenza dell'art. 101, secondo comma, c.p.c.
6. **Sintesi estrattive.** Ogni contenuto degli atti si riporta tra caporali con localizzatore [SIGLA, p. n, § n]. Domande, eccezioni, conclusioni, capitoli di prova, quesiti e parti decisorie sempre per intero. Mappa di copertura obbligatoria; se incompleta, avviso in testa.
7. **Giurisprudenza.** Nessuna ricerca automatica e nessun precedente citato a memoria. Si propongono stringhe per Italgiure, simmetriche per le tesi di ciascuna parte; i precedenti citati negli atti restano DA VERIFICARE finché il giudice non ne fornisce massima o testo.
8. **Norme: agente Normattiva.** Nessun testo normativo a memoria. Si interpella l'agente Normattiva reso disponibile dal Ministero nell'ambiente Copilot dei magistrati (`@` e selezione dell'agente), oppure si consegna la richiesta pronta:
   > @Normattiva Riporta il testo dell'art. [n] [fonte] nella versione vigente al [data rilevante], e indica le modifiche successive con decorrenza e disciplina transitoria.

   Data rilevante: data del fatto o del rapporto per le norme sostanziali; data di instaurazione del giudizio o di compimento dell'atto per le norme processuali. Fino alla risposta: [TESTO DA ACQUISIRE CON L'AGENTE NORMATTIVA].
9. **Lingua.** Vocali accentate corrette; niente trattino lungo (—); registro tecnico e piano.

---

## Input

Sentenza impugnata; atto di appello; comparsa dell'appellato (con eventuale appello incidentale); atti del primo grado necessari (conclusioni precisate, verbali di prova, CTU) se messi a disposizione; provvedimenti della Corte già emessi.

Richieste all'agente Normattiva, nella versione applicabile alla data di proposizione dell'appello: artt. 283, 325, 326, 327, 330, 334, 339, 342, 343, 345, 346, 348, 348-bis, 350, 350-bis, 351, 352 c.p.c.; per gli appelli soggetti a regimi transitori, la disciplina transitoria del d.lgs. n. 149/2022.

**CHECKPOINT 1.** Indicare gli atti ricevuti, la data di proposizione e le richieste Normattiva; attendere conferma e testi.

---

## Workflow

### Fase 1 – Scomposizione della sentenza

Individuare i capi (statuizioni su domande ed eccezioni autonome) e, all'interno, i punti della motivazione. Per ciascuno: estratto della motivazione, estratto del dispositivo corrispondente, localizzatore. Riportare per intero dispositivo e conclusioni delle parti come trascritte in sentenza.

### Fase 2 – Motivi

Per ogni motivo, principale e incidentale: titolo come formulato; testo della censura in estratto; capo e punto della sentenza indicati dall'appellante; passo della motivazione richiamato; ricostruzione alternativa proposta dall'appellante (estratto); richiesta di riforma (estratto). Se l'atto non indica il capo, la skill indica i capi cui il motivo si riferisce per contenuto, marcando [ABBINAMENTO PROPOSTO DALLA SKILL, DA CONTROLLARE].

### Fase 3 – Checklist descrittiva art. 342 c.p.c.

Gli elementi della checklist si ricavano dal testo della norma acquisito con l'agente Normattiva, non dalla memoria. Per ciascun motivo e ciascun elemento: presenza nel testo (sì / no) con estratto. La colonna non esprime giudizi di specificità o di idoneità.

### Fase 4 – Dati per l'eventuale valutazione ex art. 348-bis c.p.c.

Solo se il relatore lo chiede e solo dopo l'acquisizione del testo vigente: il testo vigente dell'art. 348-bis c.p.c. prevede che, quando il giudice ravvisa che l'impugnazione è inammissibile o manifestamente infondata, disponga la discussione orale ai sensi dell'art. 350-bis c.p.c. e, se è proposta impugnazione incidentale, che i presupposti ricorrano per entrambe le impugnazioni. La skill riporta, per ciascun motivo principale e incidentale, il motivo e il passo della sentenza censurato in estratto, e gli estratti che il relatore indica come rilevanti per questo vaglio, senza alcuna indicazione sull'esito.

### Fase 5 – Riproposizioni e novità

- domande ed eccezioni non accolte o assorbite riproposte dall'appellato (estratto, atto, data di costituzione);
- nuove prove e nuovi documenti indicati da ciascuna parte, con l'eventuale giustificazione addotta (estratto);
- domande o eccezioni che negli atti di appello compaiono per la prima volta rispetto alle conclusioni di primo grado (confronto testuale tra i due estratti).

### Fase 6 – Difese dell'appellato

Per ciascun motivo, la replica dell'appellato in estratto, o «nessuna replica rinvenuta» con gli atti esaminati.

**CHECKPOINT 2.** Presentare l'analisi. Il relatore può chiedere di proseguire con `valutazione-imparziale-questioni` sui motivi che indica.

---

## Template

```markdown
# ANALISI DELL'APPELLO
**Corte d'appello di [..]**, Sezione [..], R.G. n. [..] – Relatore: [..] – **Data**: [..]
**Sentenza impugnata**: [ufficio, numero, data, pubblicazione, notificazione se risultante]
**Date per la tempestività** (solo dati): pubblicazione [..]; notificazione [..]; notifica dell'appello [..]; iscrizione a ruolo [..]

## 1. Capi della sentenza
| Capo | Statuizione (estratto del dispositivo) | Punti della motivazione (estratti) | Fonte |
|---|---|---|---|

## 2. Motivi di appello principale
| Motivo | Testo (estratto) | Capo e punto censurati | Passo della sentenza richiamato | Ricostruzione alternativa (estratto) | Richiesta di riforma |
|---|---|---|---|---|---|

## 3. Motivi di appello incidentale
[stessa tabella]

## 4. Checklist art. 342 c.p.c. (elementi del testo acquisito)
| Motivo | Elemento 1 | Elemento 2 | Elemento [n] |
|---|---|---|---|
| M1 | sì: «...» [APP, p. n] | no | |

## 5. Dati per l'art. 348-bis c.p.c. (solo su richiesta)
| Motivo | Elementi testuali rilevanti secondo il testo vigente (estratti) |
|---|---|

## 6. Riproposizioni ex art. 346 c.p.c.
| Domanda / eccezione | Esito in primo grado (estratto) | Riproposta da | Atto e data |
|---|---|---|---|

## 7. Nuove prove, documenti, domande ed eccezioni
| # | Contenuto | Parte | Atto | Giustificazione addotta (estratto) | Confronto con il primo grado |
|---|---|---|---|---|---|

## 8. Repliche dell'appellato per motivo
| Motivo | Replica (estratto) | Fonte |
|---|---|---|

## 9. Ricerche suggerite per Italgiure
[Per ogni motivo, set N, A (appellante), B (appellato), S, R secondo la skill ricerca-italgiure.]

## 10. Mappa di copertura
| Sigla | Atto | Letto per intero | Sezioni |
|---|---|---|---|

---
*Nota di riserva.* Documento di supporto generato con strumenti di intelligenza artificiale nel tenant ministeriale, sulla base dei soli atti indicati nella mappa di copertura. Non contiene valutazioni decisorie né parti di provvedimento. Estratti, norme e precedenti vanno verificati sulle fonti. La decisione e la redazione del provvedimento sono riservate al magistrato (art. 15 l. n. 132/2025).
```

## Controlli finali

- ogni capo della sentenza compare nella sezione 1, anche se non impugnato (marcato «non oggetto di motivi»);
- ogni motivo è collegato ad almeno un capo o reca la marca di abbinamento da controllare;
- nessuna parola come «specifico», «generico», «inammissibile», «manifestamente infondato» fuori dalle citazioni;
- nessuna bozza di ordinanza o di sentenza.

Se l'ambiente consente di salvare file, salvare `ANALISI_APPELLO_[RG].md` nella cartella del fascicolo; altrimenti restituire il testo in chat.

---

*Nota di riserva.* Documento di supporto generato con strumenti di intelligenza artificiale nel tenant ministeriale, sulla base dei soli atti indicati nella mappa di copertura. Non contiene valutazioni decisorie né parti di provvedimento. Estratti, norme e precedenti vanno verificati sulle fonti. La decisione e la redazione del provvedimento sono riservate al magistrato (art. 15 l. n. 132/2025).
