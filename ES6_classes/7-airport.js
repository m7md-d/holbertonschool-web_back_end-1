/**
 * Represents an Airport.
 */
export default class Airport {
  /**
   * Initializes the airport with a name and a code.
   * @param {string} name - The name of the airport.
   * @param {string} code - The IATA code of the airport.
   */
  constructor(name, code) {
    this._name = name;
    this._code = code;
  }

  /**
   * Customizes the default string description of the class.
   * @returns {string} The airport code.
   */
  get [Symbol.toStringTag]() {
    return this._code;
  }
}
