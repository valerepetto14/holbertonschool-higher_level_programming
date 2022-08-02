#!/usr/bin/node
const Rectangle = require('./4-rectangle.js');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    let letra = 'a';
    if (c === undefined) {
      letra = 'X';
    } else {
      letra = c;
    }
    for (let index = 0; index < this.width; index++) {
      for (let index = 0; index < this.height; index++) {
        process.stdout.write(letra);
      }
      console.log('');
    }
  }
}

module.exports = Square;
