# Note
Note taking app

Notes application has the following commands
note create <note_content> - Create a note
note view <note_id> - View a single note
note delete <note_id> - Delete a single note
note list - View a formatted list of all the notes taken
note search <query_string> - View a formatted list of all the notes that can be identified by the query string
note list, note search should have a --limit parameter for setting Athe number of items to display in the resulting list e.g note list --limit 20
next should be invoked to see the next set of data in the current running query
Notes can be saved in memory but a database would be preferred (e.g SQLite or Postgres)
Create a sync command for automatically synchronising notes with online datastore like Firebase or Parse (extra credit)
The Notes should be exportable and importable as CSV or JSON.
