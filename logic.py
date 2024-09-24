# All of these functions are placeholders for the actual implementation.
# Must also edit cli.py to import the user input for the required functions
import sqlite3
import uuid

database = 'calendar.db'

def db_create_meeting(meeting_id, title, date_time, location, details):
    connection = sqlite3.connect(database)
    cursor = connection.cursor()

    cursor.execute('PRAGMA foreign_keys = ON')

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

    print('All Meetings:')
    for meeting in allMeetings:
        print(meeting)

    connection.close()

def db_query_meeting_by_id(meeting_id):
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    cursor.execute('PRAGMA foreign_keys = ON')

    cursor.execute('SELECT * FROM Meetings WHERE meeting_id=?', (meeting_id,))
    allMeetings = cursor.fetchall()
    
    print('Meeting found:')
    for meeting in allMeetings:
        print(meeting)

    connection.close()

def db_update_meeting(meeting_id, title, date_time, location, details):
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    cursor.execute('PRAGMA foreign_keys = ON')

    cursor.execute('UPDATE Meetings SET title=?, date_time=?, location=?, details=? WHERE meeting_id=?', 
                   (title, date_time, location, details, meeting_id))
    
    print(f'Meeting updated: {meeting_id}')
    connection.close()

def db_delete_meeting(meeting_id):
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    cursor.execute('PRAGMA foreign_keys = ON')

    cursor.execute('DELETE FROM Meetings WHERE meeting_id=?', (meeting_id,))

    connection.commit()
    connection.close()
    print('Deleted Meeting!')
    print(f"Deleted Meeting {meeting_id}")

def db_create_calendar(calendar_id, title, details):
    connection = sqlite3.connect(database)
    cursor = connection.cursor()

    cursor.execute('PRAGMA foreign_keys = ON')
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

def db_query_calendar_by_id(calendar_id):
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    cursor.execute('PRAGMA foreign_keys = ON')

    cursor.execute('SELECT * FROM Calendars WHERE calendar_id=?', (calendar_id,))
    calendar = cursor.fetchone()

    print(f'Calendar found: {calendar_id}')
    print(calendar)

    connection.close()

def db_update_calendar(calendar_id, title, details):
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    cursor.execute('PRAGMA foreign_keys = ON')

    cursor.execute('UPDATE Calendars SET title=?, details=? WHERE calendar_id=?', 
                   (title, details, calendar_id))
    
    print(f'Calendar updated: {calendar_id}')
    connection.close()



def db_delete_calendar(calendar_id):
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    cursor.execute('PRAGMA foreign_keys = ON')

    cursor.execute('DELETE FROM Calendars WHERE tcalendar_id=?', (calendar_id,))
    cursor.execute('DELETE FROM Calendars WHERE calendar_id=?', (calendar_id,))

    connection.commit()
    connection.close()
    print('Deleted Calendar!')
    print(f'Deleted Calendar {calendar_id}')

#participant functions
def db_create_participant(participant_id, meeting_id, name, email):
    connection = sqlite3.connect(database)
    cursor = connection.cursor()

    cursor.execute('PRAGMA foreign_keys = ON')

    cursor.execute('''
        INSERT INTO Participants (participant_id, meeting_id, name, email) 
        VALUES (?, ?, ?, ?);
    ''', (participant_id, meeting_id, name, email))
    print('Added Participant!')

    connection.commit()
    connection.close()

def db_check_meeting_id(meeting_id):
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    cursor.execute('PRAGMA foreign_keys = ON')
    cursor.execute('SELECT 1 FROM Meetings WHERE meeting_id = ?', (meeting_id,))
    exists = cursor.fetchone() is not None
    connection.close()
    return exists

def db_query_all_participants():
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    cursor.execute('PRAGMA foreign_keys = ON')

    cursor.execute('SELECT * FROM Participants')
    allParticipants = cursor.fetchall()

    for participant in allParticipants:
        print(participant)

    connection.close()

def db_query_participant_by_id(participant_id):
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    cursor.execute('PRAGMA foreign_keys = ON')

    cursor.execute('SELECT * FROM Participants WHERE participant_id=?', (participant_id,))
    participant = cursor.fetchone()

    print(participant)

    connection.close()

def db_update_participant(participant_id, name, email):
    connection = sqlite3.connect(database)
    cursor = connection.cursor()

    cursor.execute('PRAGMA foreign_keys = ON')

    cursor.execute('UPDATE Participants SET name=?, email=? WHERE participant_id=?', (name, email, participant_id))

    connection.commit()
    connection.close()
    print(f'Updated Participant! {participant_id}')

def db_delete_participant(participant_id):
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    cursor.execute('PRAGMA foreign_keys = ON')

    cursor.execute('DELETE FROM Participants WHERE participant_id=?', (participant_id,))

    connection.commit()
    connection.close()
    print('Deleted Participant!')

# attachment functions
def db_create_attachment(attachment_id, meeting_id, url):
    connection = sqlite3.connect(database)
    cursor = connection.cursor()

    cursor.execute('PRAGMA foreign_keys = ON')
    
    print(f"attachment_id: {attachment_id}, meeting_id: {meeting_id}, attachment_url: {url}")
    cursor.execute('''
        INSERT INTO Attachments (attachment_id, meeting_id, url) 
        VALUES (?, ?, ?);
    ''', (attachment_id, meeting_id, url))
    print('Added Participant!')


    connection.commit()
    connection.close()
    
def db_query_all_attachments():
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    cursor.execute('PRAGMA foreign_keys = ON')

    cursor.execute('SELECT * FROM Attachments')
    allAttachments = cursor.fetchall()

    for attachment in allAttachments:
        print(attachment)

    connection.close()
    
def db_query_attachment_by_id(attachment_id):
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    cursor.execute('PRAGMA foreign_keys = ON')

    cursor.execute('SELECT * FROM Attachments WHERE attachment_id=?', (attachment_id,))
    attachment = cursor.fetchone()

    print(attachment)

    connection.close()

def db_update_attachment(attachment_id, url):
    connection = sqlite3.connect(database)
    cursor = connection.cursor()

    cursor.execute('PRAGMA foreign_keys = ON')

    cursor.execute('UPDATE Attachments SET url=? WHERE attachment_id=?', (url, attachment_id))

    connection.commit()
    connection.close()
    print(f'Updated Attachment! {attachment_id}')

def db_delete_attachment(attachment_id):
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    cursor.execute('PRAGMA foreign_keys = ON')

    cursor.execute('DELETE FROM Attachments WHERE attachment_id=?', (attachment_id,))

    connection.commit()
    connection.close()
    print('Deleted Participant!')
    
#create a calendar-meeting relationship
def db_create_associated_calendar_meeting(meeting_id, calendar_id):
    connection = sqlite3.connect(database)
    cursor = connection.cursor()

    cursor.execute('PRAGMA foreign_keys = ON')

    cursor.execute('''
        INSERT INTO Meetings_Calendars (meeting_id, calendar_id) 
        VALUES (?, ?);
    ''', (meeting_id, calendar_id))
    print('Added Meeting to Calendar!')

    connection.commit()
    connection.close()

def db_delete_meeting_calendar(calendar_id, meeting_id):
    connection = sqlite3.connect(database)
    cursor = connection.cursor()

    cursor.execute('PRAGMA foreign_keys = ON')

    cursor.execute('DELETE FROM Meetings_Calendars WHERE calendar_id=? AND meeting_id=?', (calendar_id, meeting_id))

    connection.commit()
    connection.close()
    print(f'Deleted Meeting {meeting_id} from Calendar {calendar_id}')

def db_meeting_list_calendar(meeting_id):
    connection = sqlite3.connect(database)
    cursor = connection.cursor()

    cursor.execute('PRAGMA foreign_keys = ON')

    cursor.execute('SELECT calendar_id FROM Meetings_Calendars WHERE meeting_id=?', (meeting_id,))

    allCalendar = cursor.fetchall()
    for c in allCalendar:
        print(c)

    connection.commit()
    connection.close()
    print(f'Calendar List of Meeting {meeting_id}: ')

def db_participant_list_calendar(meeting_id):
    connection = sqlite3.connect(database)
    cursor = connection.cursor()

    cursor.execute('PRAGMA foreign_keys = ON')

    cursor.execute('SELECT participant_id FROM Participants WHERE meeting_id=?', (meeting_id,))

    allParticipants = cursor.fetchall()
    for p in allParticipants:
        print(p)

    connection.commit()
    connection.close()
    print(f'Participant List of Meeting {meeting_id}: ')

def db_attachment_list_calendar(meeting_id):
    connection = sqlite3.connect(database)
    cursor = connection.cursor()

    cursor.execute('PRAGMA foreign_keys = ON')

    cursor.execute('SELECT attachment_id FROM Attachments WHERE meeting_id=?', (meeting_id,))

    allParticipants = cursor.fetchall()
    for p in allParticipants:
        print(p)

    connection.commit()
    connection.close()
    print(f'Attachments List of Meeting {meeting_id}: ')

def db_calendar_list_meeting(calendar_id):
    connection = sqlite3.connect(database)
    cursor = connection.cursor()

    cursor.execute('PRAGMA foreign_keys = ON')

    cursor.execute('SELECT meeting_id FROM Meetings_Calendars WHERE calendar_id=?', (calendar_id,))

    allMeetings = cursor.fetchall()
    for m in allMeetings:
        print(m)

    connection.commit()
    connection.close()
    print(f'Meeting List for Calendar {calendar_id}: ')

    



    