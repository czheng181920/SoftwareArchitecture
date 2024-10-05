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

