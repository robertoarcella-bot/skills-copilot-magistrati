# Skill per Copilot – Laboratorio AI del Distretto di Napoli

Sei skill per il lavoro del magistrato civile, derivate dalle skill forensi *analisi-fascicolo*, *mappatura-fatti* e *valutazione-giudice-terzo* e riadattate alla posizione del giudice.

| Skill | Prodotto | Quando usarla |
|---|---|---|
| `sintesi-estrattiva` | `SINTESI_[atto]_[parte].md` | riassumere un atto, un verbale, una CTU, un documento |
| `ricerca-italgiure` | set di parole chiave per Italgiure | preparare le ricerche giurisprudenziali; schedare i risultati |
| `analisi-fascicolo-giudice` | `SCHEDA_FASCICOLO_[RG].md` | studio del fascicolo, preparazione dell'udienza |
| `mappatura-fatti-giudice` | `MAPPATURA_FATTI_[RG].md` | fatti allegati e prese di posizione, thema probandum |
| `valutazione-imparziale-questioni` | `STUDIO_QUESTIONI_[RG].md` | esame delle questioni e delle soluzioni possibili |
| `bozza-sentenza-civile` | `BOZZA_SENTENZA_[RG]_v1.md` | minuta di sentenza con opzioni di decisione |

Sequenza tipica: scheda del fascicolo, mappatura dei fatti, studio delle questioni, bozza di sentenza. Le skill `sintesi-estrattiva` e `ricerca-italgiure` sono trasversali e richiamate dalle altre.

## Principi comuni

1. **Decisione riservata al magistrato** (art. 101, secondo comma, Cost.; art. 15 l. 23 settembre 2025, n. 132). Nessuna skill stima probabilità di esito, ordina le soluzioni per preferenza o raccomanda una decisione. Ogni prodotto si chiude con una *Nota di riserva*.
2. **Terzietà**: ruoli processuali al posto di espressioni di appartenenza; trattamento simmetrico delle parti (stessa struttura, stessa estensione, ricerche speculari); niente aggettivi valutativi; niente fatti estranei agli atti; questioni rilevabili d'ufficio solo segnalate, con richiamo all'art. 101, secondo comma, c.p.c.
3. **Sintesi estrattive**: solo passi testuali tra caporali con localizzatore [atto, pagina, paragrafo]. La completezza si dimostra con la *mappa di copertura* (ogni sezione dell'originale risulta estratta o omessa con motivo), la checklist degli *elementi necessari* per tipo di atto e gli *indicatori* (copertura 100%, elementi presenti, estratti verificati). Se la copertura è incompleta il documento lo dichiara in testa.
4. **Giurisprudenza**: nessuna ricerca automatica e nessun precedente citato a memoria. Le skill propongono set di parole chiave per Italgiure, simmetrici per le tesi di ciascuna parte; il magistrato esegue le ricerche e, se vuole, incolla i risultati per la schedatura.
5. **Norme**: testo acquisito tramite l'**agente Normattiva** messo a disposizione dal Ministero della Giustizia nell'ambiente Copilot dei magistrati, nella versione vigente alla data rilevante. Se l'agente non può essere interpellato direttamente, la skill fornisce la richiesta pronta da inviare (`@Normattiva ...`) e lascia un segnaposto nel testo.

**Vincolo anti-allucinazione.** Ogni skill, comprese quelle civili originarie, si apre con un blocco che prevale su ogni altra istruzione. Copilot lavora solo sui documenti forniti (atti, testi dell'agente Normattiva, risultati Italgiure incollati dal magistrato). Non cita norme o giurisprudenza assenti da quei documenti. Dichiara le lacune con segnaposto, non genera link e prima della consegna esegue un controllo finale dei riscontri (CSM 22.7.2026, § 5).

## Installazione

**Microsoft 365 Copilot (agenti).** In Agent Builder creare un agente per ciascuna skill (o un unico agente per l'intero flusso): incollare nelle istruzioni la parte operativa del `SKILL.md` e caricare il file completo tra le fonti di conoscenza. Verificare che l'agente Normattiva ministeriale sia visibile nell'elenco agenti e annotarne il nome esatto, da usare al posto di `@Normattiva` se diverso.

**Uso.** Lavorare solo nell'ambiente Copilot autorizzato dal Ministero e solo su atti del fascicolo. Il nome dell'agente Normattiva e la sintassi degli operatori di Italgiure vanno verificati in fase di prima configurazione.
