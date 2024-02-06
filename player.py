import math

import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = 180
        self.y = 550
        self.speed = 5
        self.health = 100
        self.stamina = 900
        self.bones = 0
        self.shiny_rocks = 0
        self.exp = 1
        original_image = pygame.image.load("images/Caveman.png").convert_alpha()
        self.image = pygame.transform.scale(original_image, (150, 150))

        self.rect = self.image.get_rect()
        self.rect.midbottom = (self.x, self.y)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.y > 50:
            if keys[pygame.K_LSHIFT]:
                self.y -= self.speed + 2
            else:
                self.y -= self.speed
        if keys[pygame.K_s] and self.y < 930:
            if keys[pygame.K_LSHIFT]:
                self.y += self.speed + 2
            else:
                self.y += self.speed
        if keys[pygame.K_a] and self.x > 50:
            if keys[pygame.K_LSHIFT]:
                self.x -= self.speed + 2
            else:
                self.x -= self.speed
        if keys[pygame.K_d] and self.x < 1460:
            if keys[pygame.K_LSHIFT]:
                self.x += self.speed + 2
            else:
                self.x += self.speed
        self.rect.center = (self.x, self.y)

    def face_mouse(self):
        # Get mouse position
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Calculate angle between player and mouse
        angle = math.atan2(mouse_y - self.rect.centery, mouse_x - self.rect.centerx)
        angle = math.degrees(angle)

        # Rotate player image
        rotated_image = pygame.transform.rotate(self.image, -angle)
        self.rect = rotated_image.get_rect(center=self.rect.center)

        return rotated_image, self.rect.topleft

    def get_location(self):
        return self.rect.topleft

    def draw(self, surface):
        surface.blit(self.image, self.rect)
