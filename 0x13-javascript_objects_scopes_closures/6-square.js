#!/usr/bin/node
const Pared = require('./5-square');

class Square extends Pared {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c) {
      let i;
      const word = c;
      for (i = 0; i < this.width; i++) {
        console.log(word.repeat(this.width));
      }
    } else {
      this.print();
    }
  }
}

module.exports = Square;
