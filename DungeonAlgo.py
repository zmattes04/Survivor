import random
import pygame

class Wall:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), self.rect)  # Drawing wall as white

class Door:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 0, 0), self.rect)  # Drawing door as green

class RoomNode:

    def __init__(self, room_id, dungeon):
        self.room_id = room_id
        self.dungeon = dungeon
        self.connections = set()
        self.type = ""
        self.walls = []
        self.doors = []

    def generate_walls(self, w, h):
        self.walls.append(Wall(0, 0, w, 10))  # Top
        if (self.room_id - 1) in [room.room_id for room in self.connections]:
            self.doors.append(Door(w / 3 * 2, 0, 150, 10))

        self.walls.append(Wall(0, 0, 10, h))  # Left
        if (self.room_id - self.dungeon.cols) in [room.room_id for room in self.connections]:

            self.doors.append(Door(0, h / 3 * 2, 10, 150))

        self.walls.append(Wall(w - 10, 0, 10, h))  # Right
        if (self.room_id + self.dungeon.cols) in [room.room_id for room in self.connections]:

            self.doors.append(Door(w - 10, h / 3 * 2, 10, 150))

        self.walls.append(Wall(0, h - 10, w, 10))  # Bottom
        if (self.room_id + 1) in [room.room_id for room in self.connections]:
            self.doors.append(Door(w / 3 * 2, h - 10, 150, 10))

    def draw_boundaries(self, screen):
        for wall in self.walls:
            wall.draw(screen)
        for door in self.doors:
            door.draw(screen)

    def connect(self, other_room):
        self.connections.add(other_room)
        other_room.connections.add(self)

    def disconnect(self, other_room):
        if other_room in self.connections:
            self.connections.remove(other_room)
            other_room.connections.remove(self)

    def __repr__(self):
        return f"Room({self.room_id}) -> {[room.room_id for room in self.connections]}"

class Dungeon:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.rooms = [[RoomNode(r * cols + c + 1, self) for c in range(cols)] for r in range(rows)]

    def connect_rooms(self):
        for r in range(self.rows):
            for c in range(self.cols):
                room = self.rooms[r][c]
                if r > 0:  # Connect to the room above
                    room.connect(self.rooms[r - 1][c])
                if r < self.rows - 1:  # Connect to the room below
                    room.connect(self.rooms[r + 1][c])
                if c > 0:  # Connect to the room to the left
                    room.connect(self.rooms[r][c - 1])
                if c < self.cols - 1:  # Connect to the room to the right
                    room.connect(self.rooms[r][c + 1])

    def create_dead_ends(self, percentage):
        total_rooms = self.rows * self.cols
        num_dead_ends = int(total_rooms * percentage / 100)

        for _ in range(num_dead_ends):
            while True:
                r = random.randint(0, self.rows - 1)
                c = random.randint(0, self.cols - 1)
                room = self.rooms[r][c]
                if len(room.connections) > 1:
                    # Randomly pick a connection to remove
                    to_disconnect = random.choice(list(room.connections))
                    room.disconnect(to_disconnect)
                    break

    def define_type(self):
        for r in range(self.rows):
            for c in range(self.cols):
                room = self.rooms[r][c]

                if room.room_id == (self.rows * self.cols):
                    room.type = "boss"
                elif room.room_id == 1:
                    room.type = "start"
                elif len(room.connections) == 1:
                    rand_val = random.randint(1, 100)
                    if rand_val > 60:
                        room.type = "chest"
                    if rand_val > 90:
                        room.type = "sub-boss"
                else:
                    room.type = "normal"

    def display(self):
        for r in range(self.rows):
            for c in range(self.cols):
                print(self.rooms[r][c])

# Example test
# dungeon = Dungeon(4, 4)
# dungeon.connect_rooms()
# dungeon.create_dead_ends(30)
# dungeon.display()
#
# # Check the connections and generate walls for the rooms
# for row in dungeon.rooms:
#     for room in row:
#         room.generate_walls(300, 300)  # Assuming room width and height are 300

