document.getElementById('data-form').addEventListener('submit', function(event) {
    event.preventDefault();
    
    // Get the data from the input field
    const data = document.getElementById('data').value;
    
    // Create a JSON object with the data
    const jsonData = { data: data };
    
    // Send a POST request to the server
    fetch('/process_data', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(jsonData)
    })
    .then(response => response.json())
    .then(data => {

    })
    .catch(error => {
        console.error('Error:', error);
    });
});