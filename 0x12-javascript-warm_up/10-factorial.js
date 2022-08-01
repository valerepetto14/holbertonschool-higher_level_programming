#!/usr/bin/node
const process = require('process');
const args = process.argv;

if (args.length === 2) {
  console.log(1);
} else {
  const num = parseInt(args[2]);
  console.log(factorial(num);)
}

function factorial(x) {
	if (x == 0) {
			return 1;
	}
	else {
			return x * factorial(x - 1);
	}
}