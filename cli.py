import sqlite3
import uuid
import logic

def main_menu():
    while True:
      print("Welcome to the Meeting Management CLI")
      print("Select an option to manage:")
      print("1. Meetings")
      print("2. Calendars")
      print("3. Participants")
      print("4. Attachments")
      print("5. Exit")
      choice = input("Enter your choice: ")
      if choice == '1':
          manage_meetings()
      elif choice == '2':
          manage_calendars()
      elif choice == '3':
          manage_participants()
      elif choice == '4':
          manage_attachments()
      elif choice == '5':
          exit()
      else:
          print("Invalid input. Please try again.")
          main_menu()

# Input validation
def get_input(prompt, validation_fn=None):
    while True:
        user_input = input(prompt)
        if validation_fn and not validation_fn(user_input):
            print("Invalid input. Please try again.")
        else:
            return user_input

def generate_uuid():
    return str(uuid.uuid4())

#chelsea
def create_meeting():

    #user can make their own meeting id
    meeting_id = get_input("Enter meeting ID (or type 'done' to finish): ")
    if meeting_id.lower() == 'done':
        meeting_id = generate_uuid()
    title = get_input("Enter meeting title: ")
    date_time = get_input("Enter meeting date and time (YYYY-MM-DD HH:MM AM/PM): ")
    location = get_input("Enter meeting location: ")
    details = get_input("Enter meeting details: ")

    logic.db_create_meeting(meeting_id, title, date_time, location, details)

    print(f"Meeting created with ID: {meeting_id}")

    # Prompt for associated calendars
    while True:
        calendar_id = get_input("Enter associated calendar ID (or type 'done' to finish): ")
        if calendar_id.lower() == 'done':
            break
        logic.db_create_associated_calendar_meeting(meeting_id, calendar_id)
        print(f"Associated calendar {calendar_id} added.")

    # Prompt for participants
    while True:
        participant_id = generate_uuid()
        name = get_input("Enter participant name (or type 'done' to finish): ")
        if name.lower() == 'done':
            break
        email = get_input("Enter participant email: ")
        
        # Validate meeting ID before adding participant
        if not logic.db_check_meeting_id(meeting_id):
            print("Invalid meeting ID. Please enter a valid meeting ID.")
            continue
        
        logic.db_create_participant(participant_id, meeting_id, name, email)
        print(f"Participant {name} added with ID: {participant_id}")

    # Prompt for attachments
    while True:
        url = get_input("Enter attachment URL (or type 'done' to finish): ")
        if url.lower() == 'done':
            break

        attachment_id = generate_uuid()  # Generate UUID for the attachment

        logic.db_create_attachment(attachment_id, meeting_id, url)
        print(f"Attachment {url} added.")

#neha
def query_all_meetings():
    logic.db_query_all_meetings()
#neha 
def query_meeting_by_id():
    meeting_id = get_input("Enter meeting_id of meeting to be found: ")

    logic.db_query_meeting_by_id(meeting_id)

#neha
def update_meeting():
    meeting_id = get_input("Enter meeting_id of meeting to be updated: ")
    title = get_input("Enter updated meeting title: ")
    date_time = get_input("Enter updated meeting date and time (YYYY-MM-DD HH:MM AM/PM): ")
    location = get_input("Enter updated meeting location: ")
    details = get_input("Enter updated meeting details: ")

    logic.db_update_meeting(meeting_id, title, date_time, location, details)

#neha
def delete_meeting():
    meeting_id = get_input("Enter meeting_id of meeting to be deleted: ")

    logic.db_delete_meeting(meeting_id)

#amala
def create_calendar():
    calendar_id = get_input("Enter calendar ID (or type 'done' to finish): ")
    if calendar_id.lower() == 'done':
        calendar_id = generate_uuid()
    title = get_input("Enter calendar title: ")
    details = get_input("Enter details: ")

    logic.db_create_calendar(title, details)

#amala
def query_all_calendars():
    logic.db_find_all_calendar()

#amala
def query_calendar_by_id():
    calendar_id = get_input("Enter calendar_id of calendar to be found: ")

    logic.db_query_calendar_by_id(calendar_id)
    
#amala
def update_calendar():
    calendar_id = get_input("Enter calendar_id of calendar to be found: ")

    title = get_input("Enter calendar title: ")
    details = get_input("Enter details: ")

    logic.db_update_calendar(calendar_id, title, details)

#amala
def delete_calendar():
    calendar_id = get_input("Enter calendar_id of calendar to be deleted: ")

    logic.db_delete_calendar(calendar_id)

def create_participant():
    meeting_id = get_input("Enter meeting ID: ")
    
    # Validate meeting ID
    if not logic.db_check_meeting_id(meeting_id):
        print("Invalid meeting ID. Please enter a valid meeting ID.")
        return
    
    name = get_input("Enter participant name: ")
    email = get_input("Enter participant email: ")
    
    participant_id = get_input("Enter participant ID (or type 'done' to finish): ")
    if participant_id.lower() == 'done':
       participant_id = generate_uuid()

    logic.db_create_participant(participant_id, meeting_id, name, email)

    print(f"Participant created with ID: {participant_id}")

def query_all_participants():
    logic.db_query_all_participants()

def query_participant_by_id():
    participant_id = get_input("Enter participant ID: ")
    logic.db_query_participant_by_id(participant_id)

def update_participant():
    participant_id = get_input("Enter participant ID: ")
    name = get_input("Enter new participant name: ")
    email = get_input("Enter new participant email: ")

    logic.db_update_participant(participant_id, name, email)


def delete_participant():
    participant_id = get_input("Enter participant ID: ")
    logic.db_delete_participant(participant_id)

def create_attachment():
    meeting_id = get_input("Enter meeting ID: ")
    
    # Validate meeting ID
    if not logic.db_check_meeting_id(meeting_id):
        print("Invalid meeting ID. Please enter a valid meeting ID.")
        return
    
    url = get_input("Enter attachment URL: ")
    
    attachment_id = get_input("Enter attachment ID (or type 'done' to finish): ")
    if attachment_id.lower() == 'done':
       attachment_id = generate_uuid()

    logic.db_create_attachment(attachment_id, meeting_id, url)

    print(f"Attachment created with ID: {attachment_id}")

def query_all_attachments():
    logic.db_query_all_attachments()

def query_attachment_by_id():
    attachment_id = get_input("Enter attachment ID: ")
    logic.db_query_attachment_by_id(attachment_id)

def update_attachment():
    attachment_id = get_input("Enter attachment ID: ")
    url = get_input("Enter new attachment url: ")

    logic.db_update_attachment(attachment_id, url)

def delete_attachment():
    attachment_id = get_input("Enter attachment ID: ")
    logic.db_delete_attachment(attachment_id)

def manage_meetings():
    print("\nManage Meetings")
    print("Select an option:")
    print("1. Create Meeting")
    print("2. Query All Meetings")
    print("3. Query Meeting by ID")
    print("4. Update Meeting")
    print("5. Delete Meeting")
    
    choice = input("Enter your choice: ")
    if choice == '1':
        create_meeting()  
    elif choice == '2':
        query_all_meetings() 
    elif choice == '3':
        query_meeting_by_id() 
    elif choice == '4':
        update_meeting() 
    elif choice == '5':
        delete_meeting() 
    else:
        print("Invalid input. Please try again.")
        manage_meetings()

def manage_calendars():
    print("\nManage Calendars")
    print("Select an option:")
    print("1. Create Calendar")
    print("2. Query All Calendars")
    print("3. Query Calendar by ID")
    print("4. Update Calendar")
    print("5. Delete Calendar")
    
    choice = input("Enter your choice: ")
    if choice == '1':
        create_calendar()  
    elif choice == '2':
        query_all_calendars()  
    elif choice == '3':
        query_calendar_by_id() 
    elif choice == '4':
        update_calendar()
    elif choice == '5':
        delete_calendar()
    else:
        print("Invalid input. Please try again.")
        manage_calendars()

def manage_participants():
    print("\nManage Participants")
    print("Select an option:")
    print("1. Create Participant")
    print("2. Query All Participants")
    print("3. Query Participant by ID")
    print("4. Update Participant")
    print("5. Delete Participant")
    
    choice = input("Enter your choice: ")
    if choice == '1':
        create_participant() 
    elif choice == '2':
        query_all_participants() 
    elif choice == '3':
        query_participant_by_id()
    elif choice == '4':
        update_participant() 
    elif choice == '5':
        delete_participant() 
    else:
        print("Invalid input. Please try again.")
        manage_participants()

def manage_attachments():
    print("\nManage Attachments")
    print("Select an option:")
    print("1. Create Attachment")
    print("2. Query All Attachments")
    print("3. Query Attachment by ID")
    print("4. Update Attachment")
    print("5. Delete Attachment")
    
    choice = input("Enter your choice: ")
    if choice == '1':
        create_attachment() 
    elif choice == '2':
        query_all_attachments() 
    elif choice == '3':
        query_attachment_by_id()
    elif choice == '4':
        update_attachment()
    elif choice == '5':
        delete_attachment()
    else:
        print("Invalid input. Please try again.")
        manage_attachments()

if __name__ == "__main__":
    main_menu()