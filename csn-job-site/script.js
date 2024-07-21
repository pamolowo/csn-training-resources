const apiUrl = 'https://qu46d3t47wrpgdeloewdpor4ei0xyglv.lambda-url.us-west-2.on.aws/'; 

document.addEventListener('DOMContentLoaded', function () {
    var form = document.getElementById('applicationForm');
    var responseElement = document.getElementById('response');

    form.addEventListener('submit', async function (event) {
        event.preventDefault();
        if (form.checkValidity()) {
            console.log('Form is valid');

            // Prepare form data
            var formData = new FormData(form);
            var data = {};
            formData.forEach((value, key) => {
                data[key] = value;
            });

            try {
                // Send form data to the serverless function
                const response = await fetch(apiUrl, {
                    method: 'POST',
                    mode: 'no-cors',  // Added no-cors mode
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify(data),
                });

                // Since mode is no-cors, response data cannot be accessed
                console.log('Request made with no-cors mode');
                
                // Manually handle success message or errors based on different logic
                responseElement.innerHTML = `
                    <div class="alert alert-success" role="alert">
                        Your application has been submitted.
                    </div>
                `;
                form.reset(); // Reset the form fields
                form.classList.remove('was-validated'); // Remove validation classes
            } catch (error) {
                console.error('Error:', error);
                responseElement.innerHTML = `
                    <div class="alert alert-danger" role="alert">
                        An error occurred: ${error.message}
                    </div>
                `;
            }
        } else {
            console.log('Form is not valid');
            form.classList.add('was-validated');
        }
    });

    // Handle cover letter input display (if needed)
    // Cover letter is a text input, so no specific code for display is required here
});
