import random
import pygame
class Wall:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), self.rect)  # Draw white walls

class Door:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 0, 0), self.rect)  # Draw white walls

class Room:
    def __init__(self):

        self.walls = []
        self.doors = []
        self.adjacentRooms = []
    def generate_walls(self, w, h):

        # Create the room boundary
        self.walls.append(Wall(0, 0, w, 10))  # Top
        self.doors.append(Door(w/3 * 2, 0, 150, 10))
        self.walls.append(Wall(0, 0, 10, h))  # Left
        self.doors.append(Door(0, h/3 * 2, 10, 150))
        self.walls.append(Wall(w-10, 0, 10, h))  # Right
        self.doors.append(Door(w-10, h / 3 * 2, 10, 150))
        #self.walls.append(Wall(w-10, h/2 + 100, 10, h/3 + 60))
        self.walls.append(Wall(0, h-10, w, 10))  # Bottom
        self.doors.append(Door(w / 3 * 2, h-10, 150, 10))
        # Generate random walls inside
        # for _ in range(random.randint(5, 10)):  # Generate 5-10 walls
        #     x = random.randint(50, w - 150)
        #     y = random.randint(50, h - 150)
        #     self.walls.append(Wall(x, y, random.randint(50, 100), random.randint(10, 20)))

    def draw(self, screen):
        for wall in self.walls:
            wall.draw(screen)
        for door in self.doors:
            door.draw(screen)