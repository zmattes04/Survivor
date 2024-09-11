import pygame


class Fist(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/Fist_weapon_rotated.png").convert_alpha()
        #self.image = pygame.transform.rotate(self.image, -90)

class Bow_Arrow(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/Bow_weapon.png").convert_alpha()