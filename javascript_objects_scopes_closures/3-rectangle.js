#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (
      Number.isInteger(w) && w > 0 &&
      Number.isInteger(h) && h > 0
    ) {
      this.width = w;
      this.height = h;
    }
    // else leave empty (no width, no height)
  }

  print () {
    if (!this.width || !this.height) {
      // empty rectangle, do nothing
      return;
    }

    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }
}

module.exports = Rectangle;
