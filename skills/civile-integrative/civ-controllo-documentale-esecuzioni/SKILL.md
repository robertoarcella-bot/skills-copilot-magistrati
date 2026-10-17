---
name: civ-controllo-documentale-esecuzioni
description: Controllo documentale per il giudice dell'esecuzione civile, nei limiti dell'uso ammesso dal CSM (controllo della documentazione e delle certificazioni prodotte in atti). Esecuzione immobiliare - checklist della documentazione ex art. 567 c.p.c. (certificazione notarile sostitutiva o documentazione ipocatastale, copertura del ventennio, continuità delle trascrizioni, iscrizioni e trascrizioni pregiudizievoli), avvisi ai creditori iscritti e ai comproprietari, stato e contenuto della relazione di stima, interventi. Esecuzione mobiliare e presso terzi - dati del pignoramento, notifiche, dichiarazione del terzo, interventi e titoli. Solo esiti descrittivi con localizzatore, nessuna valutazione di regolarità. Produce CONTROLLO_ESECUZIONE_[RGE].md. Usare quando il G.E. chiede di controllare la documentazione ipocatastale, la certificazione notarile, il ventennio, gli avvisi ai creditori, la perizia, gli interventi o la dichiarazione del terzo.
---

# Controllo documentale nelle esecuzioni (giudice dell'esecuzione)

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

Le procedure esecutive richiedono controlli documentali ripetitivi e minuziosi. La skill li ordina in tabelle verificabili, con le date e i dati che servono al G.E. Le valutazioni (completezza della documentazione, idoneità del titolo, ammissibilità degli interventi, provvedimenti conseguenti) restano al giudice.

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

## Input e preliminari

Atto di pignoramento e nota di trascrizione; istanza di vendita; certificazione notarile o documentazione ipocatastale; relazione di stima e allegati; atti di intervento con titoli; avvisi ex art. 498 e art. 599 c.p.c. con prova della notifica; per il presso terzi, atto di pignoramento, dichiarazione del terzo, eventuali contestazioni.

Richieste all'agente Normattiva nella versione applicabile alla data del pignoramento: artt. 498, 499, 543, 547, 548, 549, 555, 557, 567, 568, 569, 599, 600 c.p.c. e art. 173-bis disp. att. c.p.c.; norme speciali indicate negli atti.

**CHECKPOINT 1.** Elencare i documenti con sigle (PIGN, NOTA TRASCR, IST VEND, CERT NOT, ISP n, PERIZIA, INT n, AVV n, DICH TERZO) e chiedere conferma; attendere i testi delle norme.

Dati personali: i nominativi dei debitori e dei terzi sono ammessi nel tenant; se la procedura riguarda abitazione principale con minori o soggetti fragili risultanti dagli atti, pseudonimizzare tali dati.

---

## Workflow – Esecuzione immobiliare

### Fase 1 – Beni pignorati

Per ogni bene: dati catastali come da pignoramento e come da nota di trascrizione, con segnalazione delle differenze testuali tra i due documenti e con la perizia.

### Fase 2 – Certificazione e ventennio

1. Data della trascrizione del pignoramento; data finale coperta dalla certificazione; data iniziale coperta.
2. Ricostruzione della catena dei titoli in tabella, dall'atto più recente al primo anteriore al ventennio: titolo, data, trascrizione (registro particolare e generale), dante causa e avente causa.
3. Calcolo verificabile della copertura: anni, mesi, giorni tra la trascrizione del primo titolo indicato e la trascrizione del pignoramento. Il calcolo segue il testo della norma acquisito; il criterio adottato si dichiara.
4. Segnalazione descrittiva di salti nella continuità (passaggi senza titolo trascritto indicato, successioni senza accettazione trascritta indicata), con l'estratto della certificazione.

### Fase 3 – Formalità pregiudizievoli e creditori

Iscrizioni e trascrizioni indicate nella certificazione; per ogni creditore iscritto, presenza in atti dell'avviso, data e prova della notifica; comproprietari risultanti e avviso ex art. 599. Dati, non valutazioni.

### Fase 4 – Relazione di stima

Checklist degli elementi richiesti dal testo acquisito dell'art. 173-bis disp. att. c.p.c.: per ogni elemento, presente (con estratto e pagina) o non rinvenuto. Riportare il valore di stima e i criteri dichiarati dall'esperto in estratto. Nessun giudizio sulla congruità.

### Fase 5 – Interventi

Per ogni intervento: data di deposito rispetto all'udienza indicata, titolo esecutivo o documento posto a fondamento come indicato dall'interveniente, importo dichiarato. Ricalcolo aritmetico solo delle somme dichiarate.

**CHECKPOINT 2.** Presentare le tabelle.

## Workflow – Esecuzione mobiliare e presso terzi

1. Pignoramento: data di notifica al debitore e al terzo; importo precettato; titolo indicato; termini risultanti.
2. Dichiarazione del terzo: testo integrale; data e modalità; rapporti dichiarati e importi; vincoli o pignoramenti anteriori dichiarati.
3. Mancata dichiarazione o contestazioni: date e atti.
4. Interventi: come sopra.

**CHECKPOINT 2.** Presentare le tabelle.

---

## Template

```markdown
# CONTROLLO DOCUMENTALE
**Tribunale di [..]**, R.G.E. n. [..] – G.E.: [..] – **Data**: [..] – **Tipo**: [immobiliare / mobiliare / presso terzi]
**Documenti esaminati**: [sigle]

## 1. Beni o crediti pignorati
| # | Dati come da pignoramento | Dati come da nota di trascrizione | Dati come da perizia | Differenze testuali |
|---|---|---|---|---|

## 2. Catena dei titoli e ventennio
| # | Titolo | Data | Trascrizione (R.G. / R.P.) | Dante causa | Avente causa | Fonte |
|---|---|---|---|---|---|---|
**Copertura calcolata**: dal [..] al [..] = [anni, mesi, giorni]; criterio: [..]
**Segnalazioni di continuità**: [..]

## 3. Formalità e avvisi
| Formalità / soggetto | Dati | Avviso in atti | Data notifica | Fonte |
|---|---|---|---|---|

## 4. Relazione di stima: elementi (testo acquisito)
| Elemento | Presente | Estratto e pagina |
|---|---|---|

## 5. Interventi
| Interveniente | Data deposito | Udienza di riferimento | Titolo o documento indicato | Importo dichiarato | Ricalcolo |
|---|---|---|---|---|---|

## 6. Dichiarazione del terzo (presso terzi)
«[testo integrale]» [DICH TERZO, p. n]

## 7. Punti da vagliare (elenco descrittivo)
| # | Punto | Sezione |
|---|---|---|

## 8. Mappa di copertura
| Sigla | Documento | Letto per intero | Sezioni |
|---|---|---|---|

---
*Nota di riserva.* Documento di supporto generato con strumenti di intelligenza artificiale nel tenant ministeriale, sulla base dei soli atti indicati nella mappa di copertura. Non contiene valutazioni decisorie né parti di provvedimento. Estratti, norme e precedenti vanno verificati sulle fonti. La decisione e la redazione del provvedimento sono riservate al magistrato (art. 15 l. n. 132/2025).
```

## Controlli finali

- ogni dato catastale e ogni formalità ha fonte e pagina;
- calcolo del ventennio esposto passo per passo;
- nessuna parola come «regolare», «completa», «insufficiente», «improcedibile» fuori dalle citazioni;
- nessuna bozza di ordinanza di vendita o di assegnazione.

Se l'ambiente consente di salvare file, salvare `CONTROLLO_ESECUZIONE_[RGE].md` nella cartella della procedura; altrimenti restituire il testo in chat.

---

*Nota di riserva.* Documento di supporto generato con strumenti di intelligenza artificiale nel tenant ministeriale, sulla base dei soli atti indicati nella mappa di copertura. Non contiene valutazioni decisorie né parti di provvedimento. Estratti, norme e precedenti vanno verificati sulle fonti. La decisione e la redazione del provvedimento sono riservate al magistrato (art. 15 l. n. 132/2025).
