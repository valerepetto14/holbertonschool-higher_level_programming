#!/usr/bin/node
const process = require('process');
const args = process.argv;

if (args.length === 2) {
  console.log('Missing number of occurrences');
} else {
  const num = parseInt(args[2]);
  for (let index = 0; index < num; index++) {
    console.log('C is fun');
  }
}
