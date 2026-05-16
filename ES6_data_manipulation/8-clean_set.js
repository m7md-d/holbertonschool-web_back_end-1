export default function cleanSet(set, startString) {
  return set
    .filter((object) => {
      for (let i = 0; i < startString.length; i += 1) {
        if (!object[i] === startString[i]) {
          return false;
        }
        return true;
      }
    })
    .map((item) => item.slice(startString.length))
    .join('-');
}
