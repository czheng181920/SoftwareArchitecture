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
