import pygame
import player
import button

class Bones(pygame.sprite.Sprite):
    def __init__(self, count, x, y):
        super().__init__()
        self.name = "Bone"
        self.count = count
        self.x = x
        self.y = y
        original_image = pygame.image.load("images/bonesv4.png").convert_alpha()
        self.image = pygame.transform.scale(original_image, (150, 150))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.mask = pygame.mask.from_surface(self.image)
        self.opened_in_inven = False
        self.sold = False

    def display_stats(self, surface):
        big_font = pygame.font.SysFont("arial", 40)
        fonts = pygame.font.SysFont("arial", 20)
        name_display = big_font.render(f'{self.name}', True, (255, 255, 255))
        stats_display = big_font.render(f'Stats:', True, (255, 255, 255))
        count_display = fonts.render(f'Count: {self.count}', True, (255, 255, 255))
        x_display = fonts.render(f'X: {self.x}', True, (255, 255, 255))
        y_display = fonts.render(f'Y: {self.y}', True, (255, 255, 255))
        pygame.draw.rect(surface, (210, 180, 140), (750, 300, 400, 500))
        pygame.draw.rect(surface, (0, 0, 0), (750, 300, 400, 500), 2)

        image = pygame.transform.scale(self.image, (400, 400))

        #Displays stats
        surface.blit(image, (750, 250))
        surface.blit(name_display, (900, 300))
        surface.blit(stats_display, (900, 550))
        surface.blit(count_display, (770, 600))
        surface.blit(x_display, (770, 630))
        surface.blit(y_display, (770, 660))

        #Create button images and then buttons
        sell_image = pygame.image.load("images/Sell_button.png").convert_alpha()
        drop_image = pygame.image.load("images/Drop_Button.png").convert_alpha()
        sell_button = button.Button(770, 690, sell_image, 3.50)
        drop_button = button.Button(880, 690, sell_image, 3.50)
        merge_button = button.Button(990, 690, sell_image, 3.50)

        #initalize buttons
        s = sell_button.draw(surface)
        d = drop_button.draw(surface)
        m = merge_button.draw(surface)
        if s:
            self.sold = True



