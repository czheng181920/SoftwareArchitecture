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
    title = get_input("Enter meeting title: ")
    date_time = get_input("Enter meeting date and time (YYYY-MM-DD HH:MM AM/PM): ")
    location = get_input("Enter meeting location: ")
    details = get_input("Enter meeting details: ")

    meeting_id = generate_uuid()
    
    logic.db_create_meeting(meeting_id, title, date_time, location, details)

    print(f"Meeting created with ID: {meeting_id}")

    # Prompt for associated calendars
    while True:
        calendar_id = get_input("Enter associated calendar ID (or type 'done' to finish): ")
        if calendar_id.lower() == 'done':
            break
        logic.db_create_associated_calendar(meeting_id, calendar_id)
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
        attachment_url = get_input("Enter attachment URL (or type 'done' to finish): ")
        if attachment_url.lower() == 'done':
            break

        attachment_id = generate_uuid()  # Generate UUID for the attachment

        logic.db_create_attachment(attachment_id, meeting_id, attachment_url)
        print(f"Attachment {attachment_url} added.")

#neha
def query_all_meetings():
    print("Querying all meetings... (to be implemented later)")


def query_meeting_by_id():
    print("Querying meeting by ID... (to be implemented later)")


def update_meeting():
    print("Updating a meeting... (to be implemented later)")

#neha
def delete_meeting():
    print('Deleted Meeting!')


def create_calendar():
    print("Creating a new calendar... (to be implemented later)")

#amala
def query_all_calendars():
    print("Querying all calendars... (to be implemented later)")

def query_calendar_by_id():
    print("Querying calendar by ID... (to be implemented later)")

def update_calendar():
    print("Updating a calendar... (to be implemented later)")

#amala
def delete_calendar():
    print("Deleting a calendar... (to be implemented later)")

def create_participant():
    meeting_id = get_input("Enter meeting ID: ")
    
    # Validate meeting ID
    if not logic.db_check_meeting_id(meeting_id):
        print("Invalid meeting ID. Please enter a valid meeting ID.")
        return
    
    name = get_input("Enter participant name: ")
    email = get_input("Enter participant email: ")
    
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
    print("Creating a new attachment... (to be implemented later)")

def query_all_attachments():
    print("Querying all attachments... (to be implemented later)")

def query_attachment_by_id():
    print("Querying attachment by ID... (to be implemented later)")

def update_attachment():
    print("Updating an attachment... (to be implemented later)")

def delete_attachment():
    print("Deleting an attachment... (to be implemented later)")

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
        create_meeting()  # to be implemented later
    elif choice == '2':
        query_all_meetings()  # to be implemented later
    elif choice == '3':
        query_meeting_by_id()  # to be implemented later
    elif choice == '4':
        update_meeting()  # to be implemented later
    elif choice == '5':
        delete_meeting()  # to be implemented later
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
        create_calendar()  # to be implemented later
    elif choice == '2':
        query_all_calendars()  # to be implemented later
    elif choice == '3':
        query_calendar_by_id()  # to be implemented later
    elif choice == '4':
        update_calendar()  # to be implemented later
    elif choice == '5':
        delete_calendar()  # to be implemented later
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
        create_participant()  # to be implemented later
    elif choice == '2':
        query_all_participants()  # to be implemented later
    elif choice == '3':
        query_participant_by_id()  # to be implemented later
    elif choice == '4':
        update_participant()  # to be implemented later
    elif choice == '5':
        delete_participant()  # to be implemented later
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
        create_attachment()  # to be implemented later
    elif choice == '2':
        query_all_attachments()  # to be implemented later
    elif choice == '3':
        query_attachment_by_id()  # to be implemented later
    elif choice == '4':
        update_attachment()  # to be implemented later
    elif choice == '5':
        delete_attachment()  # to be implemented later
    else:
        print("Invalid input. Please try again.")
        manage_attachments()

if __name__ == "__main__":
    main_menu()