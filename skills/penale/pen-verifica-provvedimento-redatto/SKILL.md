---
name: pen-verifica-provvedimento-redatto
description: Controllo di un provvedimento penale già redatto personalmente dal magistrato (sentenza, ordinanza, decreto, anche del GIP o del giudice dell'impugnazione) - verifica di completezza (ogni imputazione, eccezione, motivo, richiesta e conclusione delle parti trova risposta), corrispondenza formale tra motivazione e dispositivo e tra contestazione e decisione segnalata, elenco dei precedenti citati con stringhe Italgiure per la verifica di esistenza e contenuto, elenco delle norme da verificare con l'agente Normattiva, controllo del linguaggio ai sensi dell'art. 115-bis c.p.p. nei provvedimenti che non decidono sulla responsabilità, revisione linguistica con proposte separate in tabella. Non riscrive il ragionamento né il dispositivo. Produce VERIFICA_[provvedimento]_[RG].md. Usare quando il giudice chiede di rileggere, controllare, verificare le citazioni o rivedere la forma di un provvedimento che ha scritto.
---

# Verifica del provvedimento redatto dal magistrato

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

Il provvedimento è del magistrato e resta suo. La skill lo rilegge come farebbe un collega attento prima del deposito: controlla che nulla di ciò che le parti hanno chiesto sia rimasto senza risposta, che le citazioni esistano e dicano ciò che vi si attribuisce, che le norme siano nel testo applicabile, che la forma sia corretta. **Non riscrive** il ragionamento, **non propone** soluzioni diverse, **non modifica** il dispositivo: le osservazioni sono elencate in tabella e il magistrato decide se e come recepirle. Rientra negli usi consentiti di revisione linguistica e di supporto alla consultazione delle banche dati (CSM, raccomandazioni 8 ottobre 2025 e aggiornamento 22 luglio 2026); è escluso l'affidamento della redazione.

## Input

Il provvedimento redatto dal magistrato; gli atti da cui ricavare ciò che è stato chiesto (imputazioni, conclusioni, eccezioni, motivi di impugnazione, richieste del PM e delle parti), preferibilmente tramite le schede del Laboratorio (`dib-scheda-fascicolo-dibattimento`, `gip-gup-scheda-fascicolo`, `gip-esame-richiesta-cautelare`, `app-analisi-motivi-impugnazione`).

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

### CHECKPOINT 0 – Oggetto del controllo

Chiedere al giudice: tipo di provvedimento; controlli richiesti (completezza, citazioni, norme, linguaggio, forma: tutti per default); se gli atti contengono dati da escludere. Se il provvedimento riguarda atti ancora segreti (es. ordinanza cautelare non ancora eseguita), applicare la regola 4: si lavora solo su testo pseudonimizzato o si rinvia il controllo. Senza conferma il flusso non prosegue.

### Fase 1 – Tabella di corrispondenza

Elencare tutto ciò su cui il provvedimento doveva pronunciarsi:
- sentenza di merito: ogni capo d'imputazione e ogni modifica; ogni eccezione processuale; ogni richiesta e conclusione di PM, difese, parte civile e responsabile civile (incluse statuizioni civili, provvisionale, spese, confische, benefici, pene accessorie);
- sentenza d'appello: ogni motivo e ogni motivo nuovo, ogni richiesta di rinnovazione;
- ordinanza cautelare: ogni persona e ogni capo della richiesta, ogni esigenza prospettata, gli elementi a favore e le memorie difensive trasmessi;
- altri provvedimenti: le istanze cui rispondono.

Per ciascuna voce, il paragrafo del provvedimento in cui è trattata (estratto di poche parole) o la dicitura **NON RINVENUTA** con l'indicazione dei paragrafi esaminati. Nessun giudizio sulla sufficienza della risposta.

**CHECKPOINT 1** – il giudice esamina le voci NON RINVENUTE prima dei controlli successivi.

### Fase 2 – Coerenza formale

- Ogni capo del dispositivo ha un paragrafo di motivazione corrispondente e ogni conclusione raggiunta in motivazione ha un capo del dispositivo (corrispondenza solo **formale**: presenza e collocazione, non correttezza).
- Dati identificativi coerenti in tutto il testo (imputati, capi, date del fatto, norme contestate, importi, pene indicate in motivazione e in dispositivo): le discordanze si elencano con i due estratti.
- Fatto ritenuto in sentenza e fatto contestato: se la descrizione del fatto o la qualificazione in sentenza differisce dall'imputazione, segnalarlo con i due estratti, ai fini delle verifiche che il giudice riterrà (artt. 516-522 c.p.p. e contraddittorio sulla diversa qualificazione), senza valutare.

### Fase 3 – Precedenti citati

Per ogni precedente: estremi come scritti; contenuto attribuito (estratto); stringhe Italgiure per estremi e per contenuto (skill `pen-ricerca-italgiure`); stato **DA VERIFICARE** finché il giudice non incolla massima o testo. Se il giudice incolla i risultati: esistenza, corrispondenza degli estremi (sezione, numero, data, Rv.), corrispondenza del principio attribuito con la massima o con il passo della motivazione, in estratto. Si ricorda che citare principi non affermati dalla Corte di legittimità ha determinato l'annullamento di sentenze di merito (Cass. pen., Sez. 3, n. 25455/2025).

### Fase 4 – Norme citate

Elenco di ogni disposizione citata con la richiesta all'agente Normattiva nella versione rilevante (sostanziali: data del fatto e successive; processuali: data dell'atto). Se il testo acquisito non corrisponde a quanto riportato o parafrasato nel provvedimento, si affiancano i due testi.

### Fase 5 – Linguaggio e presunzione di non colpevolezza

Nei provvedimenti diversi da quelli che decidono sulla responsabilità (ordinanze cautelari, decreti, provvedimenti istruttori, provvedimenti nei confronti di coimputati separati), elencare le espressioni che potrebbero presentare la persona come colpevole prima della decisione definitiva, ai fini dell'art. 115-bis c.p.p. (testo da Normattiva). In ogni provvedimento: segnalare dati personali non necessari (generalità della persona offesa tutelata, dati sanitari, minori) per le valutazioni del giudice sull'oscuramento.

### Fase 6 – Revisione linguistica

Refusi, accordi, punteggiatura, accenti, periodi di lunghezza eccessiva, ripetizioni, sigle non sciolte, uniformità delle citazioni. Ogni proposta in tabella **originale / proposta / motivo**, senza modificare il significato giuridico; le proposte che toccano il contenuto non si formulano.

**CHECKPOINT 2** – consegna del rapporto. Il testo del provvedimento non viene restituito modificato.

---

## Template

```markdown
# VERIFICA DEL PROVVEDIMENTO REDATTO
**Provvedimento**: [tipo, ufficio, R.G., data della bozza del giudice] – **Data del controllo**: [..]
**Controlli eseguiti**: [completezza / coerenza / precedenti / norme / linguaggio / forma]

## 1. Corrispondenza tra chiesto e trattato
| # | Voce (capo, eccezione, motivo, richiesta) | Parte e fonte | Trattata al § | Esito |
|---|---|---|---|---|
| | | | | rinvenuta / NON RINVENUTA (§§ esaminati) |

## 2. Coerenza formale
### 2.1 Motivazione e dispositivo
### 2.2 Discordanze di dati
| Dato | Estratto 1 (§) | Estratto 2 (§) |
|---|---|---|
### 2.3 Fatto contestato e fatto ritenuto (segnalazione)

## 3. Precedenti citati
| # | Estremi come scritti | Contenuto attribuito (estratto, §) | Stringhe Italgiure | Stato |
|---|---|---|---|---|

## 4. Norme citate
| Disposizione | § | Versione rilevante | Richiesta Normattiva | Esito confronto |
|---|---|---|---|---|

## 5. Linguaggio e dati personali
| § | Espressione (estratto) | Profilo (art. 115-bis c.p.p. / dato non necessario) |
|---|---|---|

## 6. Revisione linguistica
| § | Testo originale | Proposta | Motivo |
|---|---|---|---|

---
*Nota di riserva.* [testo della regola comune]
```

---

## Controlli finali

- nessun paragrafo del provvedimento riscritto; nessuna proposta che modifichi ragionamento, qualificazione, pena o dispositivo;
- tutte le voci NON RINVENUTE indicano i paragrafi esaminati;
- ogni precedente ha stringhe di verifica e stato; nessun precedente dichiarato esistente senza testo fornito dal giudice;
- proposte linguistiche separate dal testo, in tabella.

Salvare `VERIFICA_[provvedimento]_[RG].md` se l'ambiente lo consente, altrimenti restituire in chat.
