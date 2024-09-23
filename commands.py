import sqlite3
import argparse
import uuid

database= 'calendar.db'

#Add meeting function
def addMeeting(title, date_time, location, details):
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

# Add calendar function
def addCalendar(title, details):
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

#Search meeting function
def findMeetings():
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    cursor.execute('PRAGMA foreign_keys = ON')

    cursor.execute('SELECT * FROM Meetings')
    allMeetings = cursor.fetchall()

    for meeting in allMeetings:
        print(meeting)

    connection.close()

# Search calendars function
def findCalendars():
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    cursor.execute('PRAGMA foreign_keys = ON')

    cursor.execute('SELECT * FROM Calendars')
    allCalendars = cursor.fetchall()

    for meeting in allCalendars:
        print(meeting)

    connection.close()

#deleteMeeting
def deleteMeeting(title):
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    cursor.execute('PRAGMA foreign_keys = ON')

    cursor.execute('DELETE FROM Meetings WHERE title=?', (title,))

    connection.commit()
    connection.close()
    print('Deleted Meeting!')

#deleteCalendar
def deleteCalendar(title):
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    cursor.execute('PRAGMA foreign_keys = ON')

    cursor.execute('DELETE FROM Calendars WHERE title=?', (title,))

    connection.commit()
    connection.close()
    print('Deleted Calendar!')

#add rest of functions here 
#!---------------------------------------------------



# CLI set up
#!---------------------------------------------------
def main():
    #add rest of operations here and params
    parser = argparse.ArgumentParser(description="CLI for Calendar Database(Team 3)")
    parser.add_argument("operation", help="Operations: addMeeting, searchMeetings, deleteMeeting")
    parser.add_argument("--title", help="Meeting title (needed for 'addMeeting')")
    parser.add_argument("--date_time", help="Meeting date and time (needed for 'addMeeting')")
    parser.add_argument("--location", help="Meeting location (needed for 'addMeeting')")
    parser.add_argument("--details", help="Meeting details (optional for 'addMeeting')")

    args = parser.parse_args()

    #add if statement for operation and connect to function above
    if args.operation == "addMeeting":
        if args.title and args.date_time and args.location:
            addMeeting(args.title, args.date_time, args.location, args.details or "")
        else:
            print("For 'addMeeting', please give the following params -- title, --date_time, and --location.")
    elif args.operation == "findMeetings":
        findMeetings()
    elif args.operation == "deleteMeeting":
        if args.title:
            deleteMeeting(args.title)
        else:
            print("For 'delete_meeting', please give the meeting --title.")
    if args.operation == "addCalendar":
        if args.title and args.title:
            addCalendar(args.title, args.details or "")
        else:
            print("For 'addCalendar', please give the following params --title, --details.")
    elif args.operation == "findCalendars":
        findCalendars()
    elif args.operation == "deleteCalendar":
        if args.title:
            deleteMeeting(args.title)
        else:
            print("For 'delete_meeting', please give the calendar --title.")
    else:
        print("This is not a valid operation.")

if __name__ == "__main__":
    main()