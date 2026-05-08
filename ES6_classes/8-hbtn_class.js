/**
 * Represents a Holberton Class.
 */
export default class HolbertonClass {
  /**
   * Initializes the HolbertonClass.
   * @param {number} size - The size of the class.
   * @param {string} location - The location of the class.
   */
  constructor(size, location) {
    this._size = size;
    this._location = location;
  }

  /**
   * Customizes the primitive conversion of the class.
   * @param {string} hint - A hint for the conversion type ('number', 'string', or 'default').
   * @returns {string|number} The location if string hint, the size if number hint.
   */
  [Symbol.toPrimitive](hint) {
    if (hint === "number") {
      return this._size;
    }
    if (hint === "string") {
      return this._location;
    }
    return this;
  }
}
