const fs = require('fs');

// Extracting the file path and the string to write from the command line arguments
const filePath = process.argv[2];
const content = process.argv[3];

// Writing the string to the file in utf-8
fs.writeFile(filePath, content, 'utf-8', (err) => {
  if (err) {
    // If an error occurred during writing, print the error object
    console.error(err);
  } else {
    console.log('File written successfully');
  }
});
