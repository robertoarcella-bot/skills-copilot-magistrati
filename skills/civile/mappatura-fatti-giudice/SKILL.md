---
name: mappatura-fatti-giudice
description: Mappatura dei fatti di una causa civile per il magistrato, in posizione di terzietà - per ogni fatto allegato da ciascuna parte riporta l'estratto testuale con localizzatore e la presa di posizione dell'altra parte (o la sua assenza), separa i fatti sui quali le posizioni coincidono da quelli controversi, ricostruisce il thema probandum con mezzi richiesti, ammessi ed esiti, segnala in modo simmetrico incongruenze interne agli atti di ciascuna parte e allegazioni da vagliare rispetto alle preclusioni, inventaria i documenti. Sintesi solo estrattive, con mappa di copertura. Produce MAPPATURA_FATTI_[RG].md, aggiornabile. Usare quando il giudice chiede i fatti di causa, i fatti pacifici o controversi, il thema probandum, la preparazione dell'udienza ex art. 183 c.p.c. o dell'ordinanza istruttoria, o la verifica delle non contestazioni.
---

# Mappatura dei fatti (per il magistrato)

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

Mettere a disposizione del giudice, fatto per fatto, ciò che ciascuna parte ha allegato e come l'altra parte ha preso posizione, con il testo degli atti a portata di mano. La mappatura prepara le valutazioni riservate al giudice (non contestazione ex art. 115 c.p.c., riparto dell'onere ex art. 2697 c.c., ammissibilità e rilevanza delle prove, preclusioni) e non le compie.

---

## Regole comuni del Laboratorio

1. **Riserva della decisione al magistrato** (art. 101, secondo comma, Cost.; art. 15 l. 23 settembre 2025, n. 132). Ogni output si chiude con la *Nota di riserva*.
2. **Terzietà.**
   - Ruoli processuali al posto di espressioni di appartenenza.
   - Le sezioni dedicate a ciascuna parte hanno identica struttura e identico livello di dettaglio.
   - Le incongruenze si cercano negli atti di **tutte** le parti con la stessa intensità; se per una parte non se ne rilevano, lo si dichiara.
   - Nessun aggettivo valutativo; nessuna qualificazione definitiva («ammesso», «pacifico», «tardivo»): si usano le categorie descrittive indicate sotto e le valutazioni si rimettono al giudice.
   - Nessun fatto estraneo agli atti; nessuna ricerca esterna. I possibili fatti notori si segnalano come tali.
3. **Sintesi estrattive** (skill `sintesi-estrattiva`): ogni fatto è un estratto tra caporali con localizzatore [SIGLA, p. n, § n]; ogni presa di posizione è un estratto, oppure la dichiarazione motivata della sua assenza.
4. **Giurisprudenza**: nessuna ricerca autonoma; per le questioni sul riparto dell'onere o sulla non contestazione si suggeriscono parole chiave per Italgiure (skill `ricerca-italgiure`).
5. **Norme**: tramite l'agente Normattiva del Ministero (vedi sotto).
6. **Lingua**: accenti corretti, niente trattino lungo, registro piano.

### Uso dell'agente Normattiva

Per le norme sulle preclusioni e sui termini (artt. 163, 166, 167, 171-bis, 171-ter, 183 c.p.c. e, per i giudizi del regime previgente, art. 183, sesto comma, c.p.c. nel testo anteriore) non si fa affidamento sulla memoria. Si interpella l'agente Normattiva disponibile nell'ambiente Copilot dei magistrati (`@` e selezione dell'agente), oppure si consegna al giudice la richiesta:

> @Normattiva Riporta il testo dell'art. [n] c.p.c. nella versione applicabile ai giudizi instaurati il [data di instaurazione], e indica le modifiche successive con la decorrenza e la disciplina transitoria.

Fino alla risposta la norma compare come [TESTO DA ACQUISIRE CON L'AGENTE NORMATTIVA].

---

## Categorie descrittive delle prese di posizione

Per ogni fatto allegato da una parte, la reazione dell'altra si classifica soltanto così:

| Codice | Categoria | Contenuto |
|---|---|---|
| **DC** | dichiarazione conforme | l'altra parte afferma lo stesso fatto (estratto) |
| **CS** | contestazione con versione alternativa | l'altra parte nega e indica una diversa ricostruzione (estratto) |
| **CN** | contestazione senza versione alternativa | l'altra parte nega senza indicare circostanze diverse (estratto) |
| **NP** | nessuna presa di posizione rinvenuta | si indicano gli atti dell'altra parte esaminati senza esito (es. COMP, M1-C, M3-C) |
| **PI** | presa di posizione indiretta | l'altra parte allega un fatto incompatibile senza riferirsi espressamente a quello in esame (estratti di entrambi) |

Le categorie CN, NP e PI sono quelle su cui di regola si esercita la valutazione del giudice ai sensi dell'art. 115, primo comma, c.p.c.: la mappatura le evidenzia, senza trarne conclusioni.

---

## Workflow

1. **Indice degli atti** con sigle e date di deposito, e regime processuale (rito riformato per i giudizi instaurati dopo il 28 febbraio 2023; altrimenti regime previgente). Se esiste la `SCHEDA_FASCICOLO_[RG].md` (skill `analisi-fascicolo-giudice`), riusarne l'indice.
2. **Estrazione dei fatti** atto per atto, in ordine cronologico: solo circostanze storiche (chi, cosa, quando, dove). Le qualificazioni giuridiche si annotano a parte (sezione F).
3. **Abbinamento** di ogni fatto con la presa di posizione dell'altra parte, cercata in tutti gli atti successivi.
4. **Thema probandum**: fatti con CS, CN, NP o PI, con i mezzi di prova richiesti, i provvedimenti e gli esiti.
5. **Incongruenze e preclusioni**: confronto trasversale degli atti di ciascuna parte e confronto tra date di deposito e termini (dati, non valutazioni).
6. **Documenti**: inventario per parte, documenti citati e non prodotti, documenti depositati dopo l'ultimo termine per le produzioni risultante dagli atti.
7. **Mappa di copertura** e controlli finali.

---

## Template

```markdown
# MAPPATURA DEI FATTI
**[Ufficio]**, R.G. n. [..] – **Aggiornata al**: [data] – **Versione**: [1.0]
**Regime processuale**: [riformato / previgente] – **Atti esaminati**: [sigle]

[eventuale avviso MAPPATURA INCOMPLETA]

## Indice degli atti
| Sigla | Atto | Parte | Data deposito | Presente |
|---|---|---|---|---|

## A. Fatti allegati da parte attrice
| # | Fatto (estratto) | Fonte | Presa di posizione di parte convenuta (estratto o atti esaminati) | Codice | Documenti richiamati |
|---|---|---|---|---|---|
| A1 | «...» | [CIT, p. 2, § 1] | «...» [COMP, p. 4] | CS | DOC A2 |

## B. Fatti allegati da parte convenuta
| # | Fatto (estratto) | Fonte | Presa di posizione di parte attrice (estratto o atti esaminati) | Codice | Documenti richiamati |
|---|---|---|---|---|---|

[Sezioni ulteriori, con la stessa struttura, per terzi chiamati e intervenienti.]

## C. Quadro riepilogativo
| Codice | Fatti di parte attrice | Fatti di parte convenuta |
|---|---|---|
| DC | A.. | B.. |
| CS | | |
| CN | | |
| NP | | |
| PI | | |

## D. Thema probandum
| # | Fatto (rif. A/B) | Versione di parte attrice | Versione di parte convenuta | Mezzi richiesti (parte, atto, capitolo) | Provvedimento | Esito istruttorio (estratti) |
|---|---|---|---|---|---|---|
> Il riparto dell'onere della prova dipende dalla qualificazione della domanda e delle eccezioni, riservata al giudice. Quando le parti propongono qualificazioni diverse, indicare in una colonna aggiuntiva quale parte risulterebbe onerata secondo ciascuna qualificazione prospettata, senza scegliere.

## E. Segnalazioni per il vaglio del giudice
### E.1 Incongruenze negli atti di parte attrice
| # | Affermazione 1 (estratto, fonte) | Affermazione 2 (estratto, fonte) | Natura dell'incongruenza (descrittiva) |
|---|---|---|---|
### E.2 Incongruenze negli atti di parte convenuta
[stessa tabella]
> Se per una parte non si rilevano incongruenze: "Esaminati [sigle], non sono emerse affermazioni tra loro incompatibili."

### E.3 Allegazioni, eccezioni, istanze e produzioni da vagliare rispetto alle preclusioni
| # | Contenuto (estratto) | Parte | Atto e data di deposito | Termine risultante dagli atti o dalla norma (testo da agente Normattiva) | Osservazione descrittiva |
|---|---|---|---|---|---|
> Questa tabella riporta date e termini. La valutazione di tardività, di novità della domanda o dell'eccezione e di ammissibilità spetta al giudice.

## F. Qualificazioni giuridiche prospettate dalle parti
| # | Qualificazione (estratto) | Parte | Fonte | Fatti su cui si fonda (rif. A/B) |
|---|---|---|---|---|

## G. Documenti
### G.1 Documenti di parte attrice
| Doc. | Descrizione (dati oggettivi: natura, data, autore) | Atto di produzione e data | Fatti cui è riferito dalla parte (rif. A/B) |
|---|---|---|---|
### G.2 Documenti di parte convenuta
[stessa tabella]
### G.3 Documenti citati negli atti e non rinvenuti tra le produzioni
| Documento citato | Parte | Atto e pagina | Ricerca eseguita nelle produzioni |
|---|---|---|---|

## H. Mappa di copertura
| Sigla | Atto | Letto per intero | Fatti estratti | Prese di posizione cercate in |
|---|---|---|---|---|
**Indicatori**: atti esaminati [x/y]; fatti estratti [n attrice / n convenuta]; fatti con presa di posizione abbinata [x/y]; estratti verificati letteralmente [x/y].

## Registro aggiornamenti
| Data | Versione | Atti nuovi | Voci modificate |
|---|---|---|---|

---
*Nota di riserva.* Documento di supporto generato con strumenti di intelligenza artificiale sulla base dei soli atti indicati nella mappa di copertura. Non contiene valutazioni decisorie. Estratti, norme e precedenti vanno verificati sulle fonti. La decisione è riservata al magistrato (art. 15 l. n. 132/2025).
```

---

## Controlli finali

- ogni fatto e ogni presa di posizione ha un localizzatore; ogni NP indica gli atti esaminati;
- le sezioni A e B (e le eventuali ulteriori) hanno la stessa struttura e un livello di dettaglio comparabile;
- E.1 ed E.2 sono state entrambe compilate o dichiarate vuote dopo l'esame;
- nessuna parola valutativa («ammesso», «pacifico», «tardivo», «infondato») fuori dalle citazioni testuali;
- mappa di copertura completa o avviso MAPPATURA INCOMPLETA.

## Modalità aggiornamento

Le voci esistenti non si cancellano. Le nuove prese di posizione si aggiungono sotto quelle precedenti con la marca `[AGG. v[n]: SIGLA, data]`; si aggiornano indice, sezioni interessate, mappa di copertura e registro; la versione cresce di 0.1.

Se l'ambiente consente di salvare file, salvare `MAPPATURA_FATTI_[RG].md` nella cartella del fascicolo; altrimenti restituire il testo in chat.
