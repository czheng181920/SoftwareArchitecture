# All of these functions are placeholders for the actual implementation.
# Must also edit cli.py to import the user input for the required functions
import sqlite3
import uuid

database = 'calendar.db'

def db_create_meeting(meeting_id, title, date_time, location, details):
    connection = sqlite3.connect(database)
    cursor = connection.cursor()

    cursor.execute('PRAGMA foreign_keys = ON')

    meeting_id = str(uuid.uuid4())
    cursor.execute('''
        INSERT INTO Meetings (meeting_id, title, date_time, location, details) 
        VALUES (?, ?, ?, ?, ?);
    ''', (meeting_id, title, date_time, location, details))
    print('Added Meeting!')

    connection.commit()
    connection.close()

def db_query_all_meetings():
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    cursor.execute('PRAGMA foreign_keys = ON')

    cursor.execute('SELECT * FROM Meetings')
    allMeetings = cursor.fetchall()

    for meeting in allMeetings:
        print(meeting)

    connection.close()

def db_delete_meeting(meeting_id):
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    cursor.execute('PRAGMA foreign_keys = ON')

    cursor.execute('DELETE FROM Meetings WHERE meeting_id=?', (meeting_id,))

    connection.commit()
    connection.close()
    print('Deleted Meeting!')

def db_create_calendar(title, details):
    connection = sqlite3.connect(database)
    cursor = connection.cursor()

    cursor.execute('PRAGMA foreign_keys = ON')

    calendar_id = str(uuid.uuid4())
    cursor.execute('''
        INSERT INTO Calendars (calendar_id, title, details) 
        VALUES (?, ?, ?);
    ''', (calendar_id, title, details))
    print('Added Calendar!')

    connection.commit()
    connection.close()

def db_find_all_calendar():
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    cursor.execute('PRAGMA foreign_keys = ON')

    cursor.execute('SELECT * FROM Calendars')
    allCalendars = cursor.fetchall()

    for meeting in allCalendars:
        print(meeting)

    connection.close()

def db_delete_calendar(calendar_id):
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    cursor.execute('PRAGMA foreign_keys = ON')

    cursor.execute('DELETE FROM Calendars WHERE tcalendar_id=?', (calendar_id,))

    connection.commit()
    connection.close()
    print('Deleted Calendar!')

def db_create_associated_calendar(meeting_id, calendar_id):
    print("(to be implemented later)")

def db_create_participant(participant_id, meeting_id, name, email):
    print("(to be implemented later)")

def db_create_attachment(attachment_id, meeting_id, attachment_url):
    print("(to be implemented later)")
