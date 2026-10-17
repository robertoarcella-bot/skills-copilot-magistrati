# Skill per Copilot – Laboratorio AI del Distretto di Napoli

Raccolta di *skill* (istruzioni strutturate in formato `SKILL.md`) per l'uso di Microsoft 365 Copilot da parte dei magistrati, nel rispetto dell'art. 15 della legge 23 settembre 2025, n. 132 e delle raccomandazioni del CSM dell'8 ottobre 2025, aggiornate il 22 luglio 2026.

> **Regola assoluta.** Questo repository contiene solo istruzioni. Non vi si caricano mai atti, provvedimenti, estratti, nomi, numeri di ruolo o altri dati di fascicoli, neppure pseudonimizzati, e neppure come esempio. Gli esempi usano solo dati di fantasia.

## Contenuto

| Cartella | Contenuto |
|---|---|
| `skills/civile/` | skill del magistrato civile (prima serie) |
| `skills/civile-integrative/` | skill civili integrative |
| `skills/penale/` | skill per pubblico ministero e giudice penale, divise per gruppi |
| `scripts/verifica_skill.py` | controllo automatico di forma delle skill |
| `CONTRIBUTING.md` | come proporre modifiche, anche senza competenze tecniche |
| `CHANGELOG.md` | registro delle versioni |

Ogni skill è una cartella con un file `SKILL.md`, il cui nome coincide con il campo `name` del frontmatter. È il formato aperto *Agent Skills*, caricato come skill dagli agenti di Microsoft 365 Copilot (in anteprima).

## Come usarle

**Le skill si usano solo in Microsoft 365 Copilot, nel tenant del Ministero.**
1. Scaricare l'ultima *release* in formato ZIP (pulsante **Releases** a destra, oppure **Code > Download ZIP**).
2. Se nel tenant sono attive le skill degli agenti dichiarativi: in Agent Builder, scheda **Configura > Skill > Aggiungi**, caricare lo ZIP della singola skill (massimo 8 skill per agente; istruzioni sotto i 20.000 caratteri).
3. In alternativa: creare un agente, incollare nelle **Istruzioni** la parte operativa del `SKILL.md` e caricare il file completo tra le **Fonti di conoscenza**.
4. Verificare il nome esatto dell'agente Normattiva ministeriale.


## Principi comuni a tutte le skill

1. Decisione riservata al magistrato (art. 15, comma 1, l. n. 132/2025).
2. Solo usi compresi nel perimetro indicato dal CSM; esclusi il dispositivo e la redazione dei provvedimenti giurisdizionali.
3. Checkpoint bloccanti: la skill si ferma e attende la validazione espressa del magistrato.
4. Sintesi solo estrattive, con localizzatori e mappa di copertura.
5. Vincolo anti-allucinazione: solo i documenti forniti; nessuna norma o giurisprudenza inventata (testi normativi dall'agente Normattiva).
6. Ogni output si chiude con la *Nota di riserva*.

## Stato

Materiale sperimentale del Laboratorio, non validato da organi istituzionali. Le skill vanno verificate da ciascun ufficio prima dell'uso.

## Licenza

Vedi `LICENSE-nota.md` (scelta della licenza ancora da formalizzare).
