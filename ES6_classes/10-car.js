/**
 * Represents a Car.
 */
export default class Car {
  /**
   * Initializes the Car.
   * @param {string} brand - The brand of the car.
   * @param {string} motor - The motor type.
   * @param {string} color - The color of the car.
   */
  constructor(brand, motor, color) {
    this._brand = brand;
    this._motor = motor;
    this._color = color;
  }

  /**
   * Returns the constructor of the class or subclass.
   * Useful for creating new instances of the same type.
   */
  static get [Symbol.species]() {
    return this;
  }

  /**
   * Creates a new instance of the current class/subclass.
   * @returns {object} A new instance of Car or its subclass.
   */
  cloneCar() {
    const Species = this.constructor[Symbol.species];
    return new Species();
  }
}
