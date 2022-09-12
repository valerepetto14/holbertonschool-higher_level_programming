#!/usr/bin/node
// Write a script that display the status code of a GET request.
const axios = require('axios');
const url = process.argv[2];

axios.get(url)
  .then(response => {
    console.log(`code: ${response.status}`);
  })
  .catch(error => {
    console.log(`code: ${error.response.status}`);
  });
