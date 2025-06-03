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
    // Else, leave the object empty (no properties)
  }

  print () {
    if (!this.width || !this.height) return;

    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    if (!this.width || !this.height) return;

    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    if (!this.width || !this.height) return;

    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
