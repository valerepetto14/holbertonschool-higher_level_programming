#!/usr/bin/node
const array = require('./100-data').list;

const newarray = array.map(function (dato, indice) {
  return dato * indice;
});
console.log(array);
console.log(newarray);
