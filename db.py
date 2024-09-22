import sqlite3
import uuid

database= 'calendar.db'

#create tables
def createTable(database):
    connection = sqlite3.connect(database)
    cursor = connection.cursor()

    # Enable foreign key support in SQLite
    cursor.execute('PRAGMA foreign_keys = ON')

    # Create Meetings table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Meetings (
        meeting_id TEXT PRIMARY KEY,
        title TEXT NOT NULL CHECK(length(title) <= 2000),
        date_time TEXT NOT NULL,
        location TEXT NOT NULL CHECK(length(location) <= 2000),
        details TEXT CHECK(length(details) <= 10000)
    )
    ''')

    # Create Calendars table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Calendars (
        calendar_id TEXT PRIMARY KEY,
        title TEXT NOT NULL CHECK(length(title) <= 2000),
        details TEXT CHECK(length(details) <= 10000)
    )
    ''')

    # Create Meetings_Calendars (many-to-many relationship)
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Meetings_Calendars (
        meeting_id TEXT,
        calendar_id TEXT,
        PRIMARY KEY (meeting_id, calendar_id),
        FOREIGN KEY (meeting_id) REFERENCES Meetings(meeting_id) ON DELETE CASCADE,
        FOREIGN KEY (calendar_id) REFERENCES Calendars(calendar_id) ON DELETE CASCADE
    )
    ''')

    # Create Participants table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Participants (
        participant_id TEXT PRIMARY KEY,
        meeting_id TEXT,
        name TEXT NOT NULL CHECK(length(name) <= 600),
        email TEXT NOT NULL,
        FOREIGN KEY (meeting_id) REFERENCES Meetings(meeting_id) ON DELETE CASCADE,
        CHECK (email LIKE '%_@__%.__%')
    )
    ''')

    # Create Attachments table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Attachments (
        attachment_id TEXT PRIMARY KEY,
        meeting_id TEXT,
        url TEXT NOT NULL,
        FOREIGN KEY (meeting_id) REFERENCES Meetings(meeting_id) ON DELETE CASCADE
    )
    ''')

    connection.commit()
    
    # Check if tables were created
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    print("Tables in the database:", tables)
    connection.close()

# create tables
createTable('calendar.db')



#print data from certain table
def getData():
    connection = sqlite3.connect(database)
    cursor = connection.cursor

    cursor.execute('SELECT * FROM test2')
    data = cursor.fetchall()

    connection.close()
    return data


def getConnection():
    return sqlite3.connect(database)




