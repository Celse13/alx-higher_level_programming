#!/usr/bin/node

const SquareFromFive = require('./5-square');

class Square extends SquareFromFive {
  charPrint (c) {
    if (c === undefined) c = 'X';
    let i = 0;
    while (i < this.height) {
      console.log(c.repeat(this.width));
      i++;
    }
  }
}

module.exports = Square
