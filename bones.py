import pygame
import player


class Bones(pygame.sprite.Sprite):
    def __init__(self, count, x, y):
        super().__init__()
        self.count = count
        self.x = x
        self.y = y
        original_image = pygame.image.load("images/bonesv4.png").convert_alpha()
        self.image = pygame.transform.scale(original_image, (150, 150))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.mask = pygame.mask.from_surface(self.image)

