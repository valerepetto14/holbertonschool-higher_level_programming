#!/usr/bin/node
const process = require('process');
const args = process.argv;
const num = isNaN(args[2]);

if (num || args.length === 2) {
  console.log('Missing size');
} else {
  for (let index = 0; index < parseInt(args[2]); index++) {
    for (let index = 0; index < parseInt(args[2]); index++) {
      process.stdout.write('X');
    }
    console.log('');
  }
}
