# SoftwareArchitecture

Software Architecture Assignment 1(Team 3)

# Setup

run this to set up the database (have to change python3 to python if that is what you are using)

`python3 db.py`

# Running CLI

You can run the CLI by typing these commands in the terminal.

Adding a Meeting:
`python3 commands.py addMeeting --title {add title} --date_time {MM-DD-YYYY HH:MM} --location {add location} --details {add details}`

Adding a Calendar:
`python3 commands.py addCalendar --title {add title} --details {add details}`

Find all Meetings:
`python3 commands.py findMeetings`

Delete a Meeting:
`python3 commands.py deleteMeetings --title {add title}`