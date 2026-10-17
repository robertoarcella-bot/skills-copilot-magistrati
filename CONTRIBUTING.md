# Come contribuire

Non serve saper programmare. Ci sono tre modi di partecipare, dal più semplice al più completo.

## Prima di tutto: niente dati dei fascicoli

Nelle segnalazioni, nelle proposte e nelle modifiche **non si incollano mai** atti, provvedimenti, estratti, nomi di parti, numeri di R.G. o di R.G.N.R., né output di Copilot generati su atti reali. Se serve un esempio, lo si inventa. Un contributo che contiene dati reali viene cancellato, anche dalla cronologia.

## 1. Segnalare un problema o proporre un'idea (Issue)

1. Aprire la scheda **Issues** del repository e scegliere **New issue**.
2. Scegliere il modulo adatto:
   - **Segnalazione di problema**: la skill ha prodotto un risultato sbagliato, incompleto o non neutrale;
   - **Proposta di nuova skill**: un'attività ricorrente che una skill potrebbe agevolare;
   - **Verifica di conformità CSM**: un dubbio sulla compatibilità di una skill con l'art. 15 l. n. 132/2025 o con le raccomandazioni del CSM.
3. Compilare i campi e inviare. Un revisore risponde nella stessa pagina.

## 2. Modificare il testo dal browser (pull request)

1. Aprire il file `SKILL.md` da modificare e premere l'icona della matita (**Edit this file**).
2. GitHub crea automaticamente una copia personale (*fork*) se non si hanno permessi di scrittura.
3. Fare le modifiche; in fondo, in **Commit changes**, scrivere in una riga cosa si è cambiato e perché.
4. Scegliere **Propose changes** e poi **Create pull request**.
5. Compilare la lista di controllo che compare. Il controllo automatico verifica la forma del file; un revisore verifica il contenuto.

Nessuna modifica entra nella versione pubblicata senza almeno una revisione approvata.

## 3. Lavorare in locale (per chi ha dimestichezza)

Clonare il repository, creare un ramo (`git switch -c proposta/nome-breve`), modificare, eseguire `python scripts/verifica_skill.py` e aprire una pull request.

## Regole redazionali delle skill

- Il nome della cartella coincide con il campo `name` (minuscole, cifre e trattini).
- Il campo `description` dice cosa fa la skill e quando usarla (massimo 1024 caratteri).
- Il testo del `SKILL.md` resta sotto i 20.000 caratteri (limite degli agenti di Microsoft 365 Copilot).
- Ogni skill contiene il blocco delle regole comuni, i checkpoint bloccanti e la *Nota di riserva* con il richiamo all'art. 15.
- Italiano con accenti corretti; niente trattino lungo.
- Nessuna funzione di redazione del dispositivo o della motivazione di provvedimenti giurisdizionali.

## Chi decide

I *maintainer* del Laboratorio approvano le modifiche (file `CODEOWNERS`). Le modifiche alle regole comuni richiedono due approvazioni, di cui una di un magistrato del settore interessato.
