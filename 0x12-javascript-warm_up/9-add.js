#!/usr/bin/node
const process = require('process');
const args = process.argv;

if (args.length === 2 || args.length === 3) {
  console.log('NaN');
} else {
  console.log(parseInt(args[2]) + parseInt(args[3]));
}
