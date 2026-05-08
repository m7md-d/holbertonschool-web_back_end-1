export default class Building {
  constructor(sqft) {
    if (this.constructor === Building) {
      throw new TypeError(
        "Abstract class 'Building' cannot be instantiated directly.",
      );
    }
    if (this.evacuationWarningMessage === undefined) {
      throw new TypeError(
        'Class extending Building must override evacuationWarningMessage',
      );
    }
    this._sqft = sqft;
  }

  get sqft() {
    return this._sqft;
  }

  set sqft(value) {
    this._sqft = value;
  }
}
