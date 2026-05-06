import ClassRoom from './0-classroom';

export default function initializeRooms() {
  const rooms = [19, 20, 34];
  return rooms.map((size) => new ClassRoom(size));
}
