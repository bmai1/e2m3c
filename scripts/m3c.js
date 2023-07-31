const { ipcRenderer } = require('electron');
    
const form = document.getElementById('url');

form.addEventListener('submit', (event) => {
  event.preventDefault();

  // Collect form data
  const formData = form.elements.yturl.value;
  
  // Send form data to the main process
  ipcRenderer.send('form-data', formData);

  form.reset();
});

// Receive response from the main process
ipcRenderer.on('form-data-processed', (event, message) => {
  console.log(message);
});










