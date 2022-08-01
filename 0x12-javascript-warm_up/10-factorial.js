#!/usr/bin/node
const process = require('process');
const args = process.argv;

if (args.length === 2) {
  console.log(1);
} else {
  const num = parseInt(args[2]);
  let total = 1;
  for (let index = 1; index <= num; index++) {
    total = total * index;
  }
  console.log(total);
}
