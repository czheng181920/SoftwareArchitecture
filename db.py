import sqlite3
import uuid

database= 'calendar.db'

#create tables
def createTable(database):
    connection = sqlite3.connect(database)
    cursor = connection.cursor()

    cursor.execute('''

        CREATE TABLE meetings(
                   ID TEXT PRIMARY KEY,
                   title TEXT NOT NULL CHECK(length(title) <= 2000), 
                   date TEXT NOT NULL, 
                   time TEXT NOT NULL, 
                   location TEXT NOT NULL CHECK(length(location) <= 2000), 
                   details TEXT NOT NULL CHECK(length(details) <= 10000), 
                   calendar_ID TEXT NOT NULL,
                   participants_ID TEXT NOT NULL, 
                   attachment_ID TEXT NOT NULL,
                   FOREIGN KEY (calendar_ID) REFERENCES calender(ID) ON DELETE CASCADE,
                   FOREIGN KEY (participants_ID) REFERENCES participants(ID) ON DELETE CASCADE,
                   FOREIGN KEY (attachment_ID) REFERENCES attachments(ID) ON DELETE CASCADE
                   );
    ''')

    cursor.execute('''

        CREATE TABLE calendar(
                   ID TEXT PRIMARY KEY,
                   title TEXT NOT NULL CHECK(length(title) <= 2000), 
                   details TEXT NOT NULL, 
                   FOREIGN KEY () REFERENCES calendar(ID) ON DELETE CASCADE
                   );
    ''')

    cursor.execute('''

        CREATE TABLE attachments(
                   ID TEXT PRIMARY KEY,
                   title TEXT NOT NULL CHECK(length(title) <= 2000), 
                   details TEXT NOT NULL, 
                   FOREIGN KEY () REFERENCES calendar(ID) ON DELETE CASCADE
                   );
    ''')

    cursor.execute('''

        CREATE TABLE participants(
                   ID TEXT PRIMARY KEY,
                   title TEXT NOT NULL CHECK(length(title) <= 2000), 
                   details TEXT NOT NULL, 
                   FOREIGN KEY () REFERENCES calendar(ID) ON DELETE CASCADE
                   );
    ''')

    connection.commit()
    connection.close()

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




