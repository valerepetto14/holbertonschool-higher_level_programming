#!/usr/bin/node
const process = require('process');
let cont = 0;
const args = process.argv;

for (let index = 0; args[index]; index++) {
  cont++;
}
if (cont === 2) {
  console.log('No argument');
} else {
  console.log(args[2]);
}
