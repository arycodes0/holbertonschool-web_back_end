export default class HolbertonClass {
  constructor(size, location) {
    this.size = size;
    this.location = location;
  }

  [Symbol.toPrimitive](hint) {
    if (hint === 'string') {
      return this.location;
    }
    if (hint === 'number') {
      return this.size;
    }

    return this;
  }
}
