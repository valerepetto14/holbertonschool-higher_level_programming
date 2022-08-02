#!/usr/bin/node
const { list } = require('./100-data');

const newlist = list.map(function (dato, indice) {
  return dato * indice;
});
console.log(list);
console.log(newlist);
