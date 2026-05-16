export default function cleanSet(set, startString) {
  // Guard clause for edge cases (if startString is empty or not a string)
  if (
    !startString || typeof startString !== 'string' || !(set instanceof Set)
  ) {
    return '';
  }

  return [...set]
    .filter((item) => typeof item === 'string' && item.startsWith(startString))
    .map((item) => item.slice(startString.length))
    .join('-');
}
