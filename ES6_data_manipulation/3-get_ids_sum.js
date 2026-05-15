export default function getStudentIdsSum(array) {
  const result = array.reduce((total, object) => object.id + total, 0);
  return result;
}
