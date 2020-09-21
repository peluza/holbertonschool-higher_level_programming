#!/usr/bin/node
const Pared = require('./5-square');

class Square extends Pared {
  constructor (size) {
    super(size, size);
    this.size = this.width;
  }

  charPrint (c) {
    if (c) {
      let i;
      const word = c;
      for (i = 0; i < this.size; i++) {
        console.log(word.repeat(this.size));
      }
    } else {
      this.print();
    }
  }
}

module.exports = Square;
