#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
    this.size = size;
  }

  charPrint (c) {
    if (c) {
      let i;
      const word = 'C';
      for (i = 0; i < this.size; i++) {
        console.log(word.repeat(this.size));
      }
    } else {
      this.print();
    }
  }
}

module.exports = Square;
