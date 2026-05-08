import Building from "./5-building.js";

/**
 * Represents a high-rise building.
 * @extends Building
 */
export default class SkyHighBuilding extends Building {
  /**
   * Initializes a SkyHighBuilding.
   * @param {number} sqft - The square footage of the building.
   * @param {number} floors - The number of floors in the building.
   */
  constructor(sqft, floors) {
    super(sqft);
    this._floors = floors;
  }

  /**
   * Gets the number of floors.
   * @return {number} The number of floors.
   */
  get floors() {
    return this._floors;
  }

  /**
   * Returns an evacuation warning message specific to high-rise buildings.
   * @return {string} The warning message.
   */
  evacuationWarningMessage() {
    return `Evacuate slowly the ${this._floors} floors`;
  }
}
