# Registro delle versioni

Il formato segue *Keep a Changelog*; la numerazione segue il versionamento semantico:
- **MAGGIORE** (2.0.0): modifica delle regole comuni o del perimetro d'uso (es. nuova delibera CSM);
- **MINORE** (1.1.0): nuova skill o nuova sezione;
- **CORRETTIVA** (1.0.1): correzioni redazionali o di forma.

## [Non pubblicato]

### Aggiunto
- Skill civili (prima serie): `sintesi-estrattiva`, `ricerca-italgiure`, `analisi-fascicolo-giudice`, `mappatura-fatti-giudice`, `valutazione-imparziale-questioni`, `bozza-sentenza-civile`.
- Skill civili integrative (cartella `skills/civile-integrative/`).
- Skill penali per pubblico ministero e giudice (cartella `skills/penale/`).
- Moduli per Issue, modello di pull request, controllo automatico `scripts/verifica_skill.py`.

### Modificato (scheda di osservazione n. 1)
- `dib-scheda-fascicolo-dibattimento`: modalità **essenziale** (predefinita: parti, imputazioni, prove ammesse e loro stato, udienze, questioni aperte) e modalità **approfondita** attivabile in qualsiasi fase, con riuso della scheda già validata; aggiornamento non più legato a ogni udienza; colonna facoltativa per il tempo di verifica del giudice.
- `dib-mappatura-prove`: mappatura facoltativa, **progressiva o retrospettiva** dalle trascrizioni PDF già disponibili, elaborate a blocchi (udienza o dichiarante) con mappa di copertura; ambito limitabile a capi, elementi o dichiaranti; scomposizione per elementi facoltativa; riuso dei dati della scheda anche essenziale; nessuna elaborazione di file audio o video.
- `dib-mappatura-prove`: il quadro riepilogativo non contiene più la colonna «Nessuna prova assunta», sostituita da conteggio degli estratti, prove richiamate dalle parti e atti esaminati, con la formula «nessun estratto individuato negli atti esaminati»; nuovi controlli finali contro formule di esito sulla prova.
- `skills/penale/README.md`: le skill penali sono dichiarate **sperimentali** fino a verifica tecnica, giuridica e funzionale documentata; approvazione dell'archivio distinta da quella delle singole skill.

### Da verificare prima della versione 1.0.0
- Compatibilità della skill `bozza-sentenza-civile` con l'aggiornamento CSM del 22.7.2026, che esclude «la formulazione del dispositivo e l'affidamento della redazione dei provvedimenti giurisdizionali».
