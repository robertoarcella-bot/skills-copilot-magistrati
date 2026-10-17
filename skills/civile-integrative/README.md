# Skill integrative per Copilot – settore civile – Laboratorio AI del Distretto di Napoli

Nove skill che si aggiungono alle sei già presenti in `skills-copilot\`, senza duplicarle. Coprono le fasi del processo civile non ancora trattate: verifiche preliminari, istruttoria, CTU, verifica delle citazioni, appello, esecuzioni, monitorio, controllo del provvedimento scritto dal giudice. Le regole comuni sono quelle delle skill esistenti, integrate con il perimetro CSM dell'8.10.2025 e del 22.7.2026, con i checkpoint bloccanti e con le regole su dati e pseudonimizzazione.

| Skill | Prodotto | Quando usarla |
|---|---|---|
| `civ-perimetro-ia` | esito CONSENTITA / CONDIZIONATA / ESCLUSA e riformulazione ammissibile | **sempre per prima** |
| `civ-verifiche-preliminari` | checklist delle verifiche ex art. 171-bis c.p.c. | prima udienza; notifiche, termini, contumacia, litisconsorzio, procedibilità |
| `civ-griglia-istanze-istruttorie` | griglia di capitoli e istanze istruttorie | preparazione dell'ordinanza istruttoria (decisione del giudice) |
| `civ-analisi-ctu` | quesiti e risposte, osservazioni e repliche | esame della relazione di consulenza |
| `civ-verifica-citazioni-atti` | tabella di verifica dei precedenti e delle norme citati dalle parti | contrasto alle citazioni inesistenti («allucinazioni»), simmetrico per tutte le parti |
| `civ-analisi-motivi-appello` | tabella motivi e capi; checklist artt. 342 e 348-bis c.p.c. | Corte d'appello |
| `civ-controllo-documentale-esecuzioni` | checklist documentale (art. 567 c.p.c., avvisi, perizia; presso terzi) | esecuzioni (uso ammesso CSM 2025, punto 5) |
| `civ-verifica-ricorso-monitorio` | checklist dei requisiti del ricorso per ingiunzione | affari semplici; **non redige il decreto** |
| `civ-verifica-provvedimento-redatto` | controllo chiesto-pronunciato, citazioni, revisione linguistica in tabella | dopo che il giudice ha scritto il provvedimento |

**Vincolo anti-allucinazione.** Ogni skill, comprese quelle civili originarie, si apre con un blocco che prevale su ogni altra istruzione. Copilot lavora solo sui documenti forniti (atti, testi dell'agente Normattiva, risultati Italgiure incollati dal magistrato). Non cita norme o giurisprudenza assenti da quei documenti. Dichiara le lacune con segnaposto, non genera link e prima della consegna esegue un controllo finale dei riscontri (CSM 22.7.2026, § 5).

## Collocazione nel flusso con le skill esistenti

`civ-perimetro-ia`, poi `analisi-fascicolo-giudice`, poi `civ-verifiche-preliminari`, poi `mappatura-fatti-giudice`, poi `civ-griglia-istanze-istruttorie`. Dopo la CTU, `civ-analisi-ctu`; poi `valutazione-imparziale-questioni` e `civ-verifica-citazioni-atti`. Infine il giudice scrive il provvedimento e usa `civ-verifica-provvedimento-redatto`.

## Nota sulla skill esistente `bozza-sentenza-civile`

L'aggiornamento CSM del 22.7.2026 esclude «la formulazione del dispositivo e l'affidamento della redazione dei provvedimenti giurisdizionali» (§ 8) e la loro «predisposizione» (§ 2). `bozza-sentenza-civile` redige invece opzioni di motivazione e dispositivi alternativi: il punto è stato segnalato al coordinamento del Laboratorio, che ha deciso di mantenerla. Chi la usa deve tenerne presente il rapporto con l'aggiornamento CSM. Le skill integrative non la richiamano. Le funzioni di supporto sono coperte da `valutazione-imparziale-questioni`, prima della stesura, e da `civ-verifica-provvedimento-redatto`, dopo.

## Installazione e uso

Come per le skill esistenti (`skills-copilot\README.md`). Negli agenti di Microsoft 365 Copilot valgono al massimo 8 skill per agente e 20.000 caratteri per `SKILL.md`: tutte queste skill stanno sotto gli 11.500 caratteri. Solo nel tenant ministeriale.
