#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || w === undefined || h === undefined) {
      return;
    }
    this.width = w;
    this.height = h;
  }

  print () {
    for (let index = 0; index < this.height; index++) {
      for (let index = 0; index < this.width; index++) {
        process.stdout.write('X');
      }
      console.log('');
    }
  }
}

module.exports = Rectangle;
