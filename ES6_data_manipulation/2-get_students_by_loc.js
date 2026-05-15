export default function getStudentsByLocation(array, city) {
  return array.filter((object) => {
    if (object.location === city) {
      return true;
    }
    return false;
  });
}
