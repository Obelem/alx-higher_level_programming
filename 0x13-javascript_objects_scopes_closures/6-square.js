#!/usr/bin/node

const parentSquare = require('./5-square');

module.exports = class Square extends parentSquare {
  charPrint (c) {
    if (!c) {
      this.print();
      return;
    }
    for (let row = 0; row < this.height; row++) console.log(c.repeat(this.width));
  }
};
