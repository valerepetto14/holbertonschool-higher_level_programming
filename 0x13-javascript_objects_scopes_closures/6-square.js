#!/usr/bin/node
const Rectangle = require('./4-rectangle.js');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c='X') {
    for (let index = 0; index < this.width; index++) {
      for (let index = 0; index < this.height; index++) {
        process.stdout.write(c);
      }
      console.log('');
    }
  }
}

module.exports = Square;
