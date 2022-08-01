#!/usr/bin/node
const process = require('process');
const args = process.argv;
const num = isNaN(args[2]);

if (num) {
  console.log('Not a number');
} else {
  console.log('My number: ' + parseInt(args[2]));
}
