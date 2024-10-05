// static/script.js
document.addEventListener('DOMContentLoaded', function () {
  console.log('JavaScript is loaded!');
});

// Function to handle changes in the main dropdown (Meetings, Calendars, Participants, Attachments)
function handleOptionChange() {
  const selectedOption = document.getElementById("choice").value;

  // Hide all forms initially
  document.getElementById("meetingForm").style.display = "none";
  document.getElementById("calendarForm").style.display = "none";
  document.getElementById("participantsForm").style.display = "none";
  document.getElementById("attachmentsForm").style.display = "none";

  // Show the relevant form based on the user's choice
  if (selectedOption === "1") {
    document.getElementById("meetingForm").style.display = "block";
  } else if (selectedOption === "2") {
    document.getElementById("calendarForm").style.display = "block";
  } else if (selectedOption === "3") {
    document.getElementById("participantsForm").style.display = "block";
  } else if (selectedOption === "4") {
    document.getElementById("attachmentsForm").style.display = "block";
  }
}

// Function to handle changes in the meeting management options
function handleMeetingOptionChange() {
  const selectedMeetingOption = document.getElementById("meeting-option").value;
  
  const meetingIdSection = document.getElementById("meeting-id-section");
  const meetingTitleSection = document.getElementById("meeting-title-section");
  const meetingDateSection = document.getElementById("meeting-date-section");
  const meetingLocationSection = document.getElementById("meeting-location-section");
  const meetingDetailsSection = document.getElementById("meeting-details-section");


  // Display the meeting ID input field only for options that require it
  if (selectedMeetingOption === "1" || selectedMeetingOption === "4") {
    // Creating or querying all meetings does not require a meeting ID
    meetingIdSection.style.display = "block";
    meetingTitleSection.style.display = "block";  
    meetingDateSection.style.display = "block";    
    meetingLocationSection.style.display = "block";    
    meetingDetailsSection.style.display = "block";    
  } 
  else if (selectedMeetingOption === "2") {
    // Creating or querying all meetings does not require a meeting ID
    meetingIdSection.style.display = "none";
    meetingTitleSection.style.display = "none";   
    meetingDateSection.style.display = "none";    
    meetingLocationSection.style.display = "none";    
    meetingDetailsSection.style.display = "none";     
  } else {
    // Other options (query by ID, update, delete) require a meeting ID
    meetingIdSection.style.display = "block";
    meetingTitleSection.style.display = "none";
    meetingDateSection.style.display = "none";    
    meetingLocationSection.style.display = "none";    
    meetingDetailsSection.style.display = "none";    
  }
}

// Function to handle changes in the calendar management options
function handleCalendarOptionChange() {
  const selectedCalendarOption = document.getElementById("calendar-option").value;
  
  const calendarIdSection = document.getElementById("calendar-id-section");
  const calendarTitleSection = document.getElementById("calendar-title-section");
  const calendarDetailsSection = document.getElementById("calendar-details-section");

  // Display the meeting ID input field only for options that require it
  if (selectedCalendarOption === "1" || selectedCalendarOption === "4") {
    // Creating or querying all meetings does not require a meeting ID
    calendarIdSection.style.display = "block";  
    calendarTitleSection.style.display = "block";    
    calendarDetailsSection.style.display = "block";    
  } 
  else if (selectedCalendarOption === "2") {
    // Creating or querying all meetings does not require a meeting ID
    calendarIdSection.style.display = "none";
    calendarTitleSection.style.display = "none";       
    calendarDetailsSection.style.display = "none";     
  } else {
    // Other options (query by ID, update, delete) require a meeting ID
    calendarIdSection.style.display = "block";
    calendarTitleSection.style.display = "none";   
    calendarDetailsSection.style.display = "none";    
  }
}

// Function to handle changes in the participant management options
function handleParticipantOptionChange() {
  const selectedParticipantOption = document.getElementById("participant-option").value;
  
  const participantIdSection = document.getElementById("participant-id-section");
  const meetingIdSection = document.getElementById("meeting-id-section");
  const participantNameSection = document.getElementById("participant-name-section");
  const participantEmailSection = document.getElementById("participant-email-section");

  // Display the meeting ID input field only for options that require it
  if (selectedParticipantOption === "1" || selectedParticipantOption === "4") {
    // Creating or querying all meetings does not require a meeting ID
    participantIdSection.style.display = "block";  
    meetingIdSection.style.display = "block";  
    participantNameSection.style.display = "block";    
    participantEmailSection.style.display = "block";    
  } 
  else if (selectedParticipantOption === "2") {
    // Creating or querying all meetings does not require a meeting ID
    participantIdSection.style.display = "none";
    participantNameSection.style.display = "none";       
    participantEmailSection.style.display = "none";  
    meetingIdSection.style.display = "none";     
  } else {
    // Other options (query by ID, update, delete) require a meeting ID
    participantIdSection.style.display = "block";
    participantNameSection.style.display = "none";   
    participantEmailSection.style.display = "none"; 
    meetingIdSection.style.display = "none";     
  }
}

// Function to handle changes in the attachment management options
function handleAttachmentOptionChange() {
  const selectedAttachmentOption = document.getElementById("attachment-option").value;
  
  const attachmentIdSection = document.getElementById("attachment-id-section");
  const meetingIdSection = document.getElementById("meeting-id-section");
  const attachmentUrlSection = document.getElementById("attachment-url-section");

  // Display the meeting ID input field only for options that require it
  if (selectedAttachmentOption === "1" || selectedAttachmentOption === "4") {
    // Creating or querying all meetings does not require a meeting ID
    attachmentIdSection.style.display = "block";  
    meetingIdSection.style.display = "block";  
    attachmentUrlSection.style.display = "block";    
  } 
  else if (selectedAttachmentOption === "2") {
    // Creating or querying all meetings does not require a meeting ID
    attachmentIdSection.style.display = "none";
    meetingIdSection.style.display = "none";  
    attachmentUrlSection.style.display = "none";       
  } else {
    // Other options (query by ID, update, delete) require a meeting ID
    attachmentIdSection.style.display = "block";
    meetingIdSection.style.display = "none";  
    attachmentUrlSection.style.display = "none";   
  }
}


