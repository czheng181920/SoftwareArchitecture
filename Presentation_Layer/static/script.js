// static/script.js
document.addEventListener('DOMContentLoaded', function () {
  console.log('JavaScript is loaded!');
});

document
  .getElementById('data-form')
  .addEventListener('submit', async function (event) {
    event.preventDefault();
    console.log('Form submitted!');
    const data = {
      info: document.getElementById('info').value,
    };

    try {
      const response = await fetch('/submit', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
      });

      const result = await response.json();
      document.getElementById(
        'response'
      ).innerText = `Response: ${result.message}`;
    } catch (error) {
      console.error('Error:', error);
    }
  });


  /*new stuff-doesn't work yet, need to debug */
  const optionForm = document.getElementById('optionForm'); 

  optionForm.addEventListener('submit', (event) => 
  {
    event.preventDefault();
    const choice = document.getElementById('choice').value;

    if (choice === '1') 
    {
        meetingForm.style.display = 'block';
    }
    else 
    {
        // Handle other choices
        console.log('Choice:', choice);
    }
  });
  
  const meetingForm = document.querySelector('meeting-option');
  meetingForm.addEventListener('submit', (event) => 
  {
      event.preventDefault();
      const choice = document.getElementById('meeting-option').value;

      //Each option based on the selected value
      if (choice === '1') 
        {
          //Create Meeting
          console.log('Create Meeting selected');
      } 
      else if (choice === '2') 
      {
          //Query All Meetings
          console.log('Query All Meetings selected');
      } 
      else if (choice === '3') 
      {
          //Query Meeting by ID
          console.log('Query Meeting by ID selected');
      } 
      else if (choice === '4') 
      {
          //Update Meeting
          console.log('Update Meeting selected');
      } 
      else if (choice === '5') 
      {
          //Delete Meeting
          console.log('Delete Meeting selected');
      } 
      else if (choice === '6') 
      {
          //List of Calendars for a Meeting
          console.log('List of Calendars for a Meeting selected');
      } 
      else if (choice === '7') 
      {
          //List of Participants for a Meeting
          console.log('List of Participants for a Meeting selected');
      } 
      else if (choice === '8') 
      {
          //List of Attachments for a Meeting
          console.log('List of Attachments for a Meeting selected');
      } 
      else 
      {
          console.log('Invalid choice');
      }
  });
