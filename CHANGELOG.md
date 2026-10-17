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

### Da verificare prima della versione 1.0.0
- Compatibilità della skill `bozza-sentenza-civile` con l'aggiornamento CSM del 22.7.2026, che esclude «la formulazione del dispositivo e l'affidamento della redazione dei provvedimenti giurisdizionali».
