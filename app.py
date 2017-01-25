# Note taking application
# Author Evans

# In the beginning...
# Imports
import sqlite3

# Start with connecting to db
conn = sqlite3.connect('Note.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS Notes (title, note, author)''')

# Menu
def nameEntry():
    print(' Welcome to Note')
    global author
    author = input('\n Please enter your name: ')

    if author == '':
        print(' Your name cannot be empty')
        nameEntry()
    else:
        menuChoises()


# Menu
def menuChoises():
    entry = input('\n    NOTE MENU\n ################\n # 1. Create a note\n # 2. View note\n # 3. Delete note\n # 4. List all notes\n # 5. Search note \n # 6. Exit\n\n')
    if entry == '1':
        createNote()
    elif entry == '2':
        viewNote()
    elif entry == '3':
        deleteNote()
    elif entry == '4':
        listNotes()
    elif entry == '5':
        searchNote()
    elif entry == '6':
        exitApp()
    else:
        print('\n Reply with the choises given only\n You replied with an incorrect input')
        menuChoises()


# Create note function
def createNote():
    title = input('Please enter name title:\n\n')
    note = input('Type your note below:\n\n')

    title = str(title)
    note = str(note)

    def confirmNoteCreation():
        # Verify data
        err = [' \n']
        if title == '':
            err.append(' # Title cannot be empty')
        if note == '':
            err.append(' # Note cannot be empty')
        if err != [' \n']:
            for error in err:
                print(error)
        elif err == [' \n']:
            # Vie note
            print(' ' + title + '\n')
            print(' ' + note)
            conf = input('\n Reply with (y/n)\n Is this the note you want to create?')

            if conf == 'y':
                c.execute('INSERT INTO Notes VALUES (?, ?, ?)', (title, note, author))
                conn.commit()
                conn.close()
                print('\n Note created successfully')
                menuChoises()
            elif conf == 'n':
                menuChoises()
            else:
                print('You need to reply with either (y/n)')
                confirmNoteCreation
        else:
            print('Unkown error')
    confirmNoteCreation()


# View note function
def viewNote():
    for notes in c.execute('SELECT ROWID, title, note, author FROM Notes'):
        print(notes)
    noteid = input('\n Please enter id of note you\'d like to view: ')
    noteid = int(noteid)
    for note in c.execute('SELECT * FROM Notes WHERE ROWID =:noteid', {"noteid":noteid}):
        print(note)
    menuChoises()


# Delete note function
def deleteNote():
    for notes in c.execute('SELECT ROWID, title, note, author FROM Notes'):
        print(notes)
    delid = input('\n Please enter id of note you\'d like to delete')
    for note in c.execute('SELECT * FROM Notes WHERE ROWID =:delid', {"delid":delid}):
        print(note)

    conf = input(' Reply with (y/n)\n Is this the note you\'d like to delete? ')
    if conf == 'y':
        c.execute('DELETE FROM Notes WHERE ROWID =:delid', {"delid":delid})
        conn.commit()
        conn.close()
        print(' Note deleted successfuly')
        menuChoises()
    elif conf == 'n':
        deleteNote()
    else:
        print('You neeed to reply eith either (y/n)')

# List function
def listNotes():
    for notes in c.execute('SELECT * FROM Notes'):
        print(notes)
    menuChoises()


# SearchNote function
def searchNote():
    query = input('Please enter note you\'d like to search: ')
    query = '%' + query + '%'
    for search in c.execute('SELECT * FROM Notes WHERE note LIKE ?', (query,)):
        print(search)
    menuChoises()

# Exit app
def exitApp():
    exit()

# Start application
nameEntry()
