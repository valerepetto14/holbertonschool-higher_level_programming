#!/usr/bin/node
const { dict } = require('./101-data');
const newdic = [];
const dicreturn = {};

for (const clave in dict) {
  newdic.push(dict[clave]);
}
const dicUnique = new Set(newdic);

for (const i of dicUnique) {
  dicreturn[i] = [];
}

for (const i in dict) {
  const valor = dict[i];
  dicreturn[valor].push(i);
}

console.log(dicreturn);

