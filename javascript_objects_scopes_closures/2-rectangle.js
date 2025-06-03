#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    // Check if w and h are positive integers
    if (
      Number.isInteger(w) && w > 0 &&
      Number.isInteger(h) && h > 0
    ) {
      this.width = w;
      this.height = h;
    }
    // else do nothing: instance remains empty
  }
}

module.exports = Rectangle;
