#!/usr/bin/node
const process = require('process');
const fs = require('fs');
const args = process.argv;

const a1 = args[2];
const a2 = args[3];
const newfile = args[4];

const texta1 = fs.readFileSync(a1, 'utf-8');
const texta2 = fs.readFileSync(a2, 'utf-8');

fs.appendFile(newfile, texta1 + '\n' + texta2, (err) => {
  if (err) {
    throw err;
  }
});
