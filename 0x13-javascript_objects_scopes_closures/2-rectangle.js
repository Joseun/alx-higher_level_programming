#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if ((w < 1) || (h < 1)) {
    } else if ((isNaN(w)) || (isNaN(h))) {
    } else {
      this.width = w;
      this.height = h;
    }
  }
};
