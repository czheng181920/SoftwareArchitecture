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
  const meetingSubmitSection = document.getElementById("meeting-submit-section");
  
  const meetingSubmitButton = document.getElementById("submitButton");


  // Display the meeting ID input field only for options that require it
  if (selectedMeetingOption === "1" || selectedMeetingOption === "4") 
  {
    // Creating meetings and querying meeting by id 
    meetingIdSection.style.display = "block";
    meetingTitleSection.style.display = "block";  
    meetingDateSection.style.display = "block";    
    meetingLocationSection.style.display = "block";    
    meetingDetailsSection.style.display = "block";
    meetingSubmitSection.style.diplay = "block";  
  } 
  else if (selectedMeetingOption === "2") 
  {
    // querying all meeting id
    meetingIdSection.style.display = "none";
    meetingTitleSection.style.display = "none";   
    meetingDateSection.style.display = "none";    
    meetingLocationSection.style.display = "none";    
    meetingDetailsSection.style.display = "none"; 
    meetingSubmitSection.style.diplay = "block";    
  } 
  else {
    // update, delete, list of cal for meeting, list of attachement, list of participants
    meetingIdSection.style.display = "block";
    meetingTitleSection.style.display = "none";
    meetingDateSection.style.display = "none";    
    meetingLocationSection.style.display = "none";    
    meetingDetailsSection.style.display = "none";
    meetingSubmitSection.style.diplay = "block";    
  }

  if(selectedMeetingOption === "1")
  {
    meetingSubmitButton.onclick = "meetingSubmit()"
  }
  else if(selectedMeetingOption === "2")
  {
    meetingSubmitButton.onclick = "meetingQuery()"
  }
  else if(selectedMeetingOption === "3")
  {
    meetingSubmitButton.onclick = "meetingQueryByID()"
  }
  else if(selectedMeetingOption === "4")
  {
    meetingSubmitButton.onclick = "updateMeeting()"
  }
  else if(selectedMeetingOption === "5")
  {
    meetingSubmitButton.onclick = "deleteMeeting()"
  }
  else if(selectedMeetingOption === "6")
  {
    meetingSubmitButton.onclick = "listofCalendarsMeeting()"
  }
  else if(selectedMeetingOption === "7")
  {
    meetingSubmitButton.onclick = "listofParticipantsMeeting()"
  }
  else if(selectedMeetingOption === "8")
  {
    meetingSubmitButton.onclick = "listofAttachmentsMeeting()"
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


async function meetingSubmit()
{
    const meetingID = document.getElementById("meeting-id").value;
    const meetingTitle = document.getElementById("meeting-title").value;
    const meetingDate = document.getElementById("meeting-date").value; 
    const meetingLocation = document.getElementById("meeting-location").value;
    const meetingDetails = document.getElementById("meeting-details").value; 

    // Create JSON object
    const data = {
      meeting_id: meetingID,
      title: meetingTitle, 
      date_time: meetingDate, 
      location: meetingLocation, 
      details: meetingDetails
      };

    // Send POST request
    try 
    {
      const response = await fetch('/addMeeting', 
        {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
      });
    
      if (response.ok) 
      {
      const responseData = await response.json();
      console.log('Meeting created successfully:', responseData);
      
      } 
      else 
      {
        console.error('Error creating meeting:', response.status);
       
      }
    } 
    catch (error) 
    {
      console.error('Error:', error);
      
    }
}

async function meetingQuery()
{
  try {
    const response = await fetch('/allMeetings');

    if (response.ok) 
      {
      const meetingsData = await response.json();
      const meetingsList = document.getElementById('meetingsList');

      meetingsList.innerHTML = ''; // Clear previous content

      meetingsData.forEach(meeting => 
        {
        const meetingItem = document.createElement('li');
        meetingItem.textContent = meeting.title; // Assuming 'title' is the key for meeting titles
        meetingsList.appendChild(meetingItem);
      });
    } 
    else {
      console.error('Error retrieving meetings:', response.status);
    }
  } 
  catch (error) {
    console.error('Error:', error);
  }

}

async function meetingQueryByID()
{


}

async function updateMeeting()
{

}

async function deleteMeeting()
{

}

async function listofCalendarsMeeting()
{

}

async function listofParticipantsMeeting()
{

}

async function listofAttachmentsMeeting()
{

}


















