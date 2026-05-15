export default function getStudentIdsSum(array) {
  return array.reduce((object, total) => object.id + total, 0);
}
