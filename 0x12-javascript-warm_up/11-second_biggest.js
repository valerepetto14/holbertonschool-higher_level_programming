#!/usr/bin/node
const process = require('process');
const args = process.argv;

if (args.length === 2 || args.length === 3) {
  console.log(0);
} else {
  let primero = 0;
  let segundo = 0;
  for (let index = 2; index < args.length; index++) {
    const num = parseInt(args[index]);
    if (num > primero) {
      primero = args[index];
    }
  }
  const idx = args.indexOf(primero);
  args.splice(idx, 1);
  for (let index = 2; index < args.length; index++) {
    const num = parseInt(args[index]);
    if (num > segundo) {
      segundo = args[index];
    }
  }
  console.log(segundo);
}
