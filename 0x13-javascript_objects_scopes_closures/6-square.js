#!/usr/bin/node
const Square_ = require('./5-square');
module.exports = class Square extends Square_ {
  constructor (size) {
    super(size, size);
    this.width = size;
    this.height = size;
  }

  charPrint (c = 'X') {
    for (let i = 0; i < this.height; i++) {
      let row = '';
      for (let j = 0; j < this.width; j++) {
        row += c;
      }
      console.log(row);
    }
  }
};
