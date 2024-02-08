import pygame


# button class
class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        self.toggle_state = False

    def draw(self, surface):
        action = False
        # get mouse position
        pos = pygame.mouse.get_pos()

        # check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                self.toggle_state = True
                print("toggled")
                action = True

        # if pygame.mouse.get_pressed()[0] == 0:
        #     self.clicked = False
        #     self.toggle_state = True

        # draw button on screen
        surface.blit(self.image, (self.rect.x, self.rect.y))

        return action

# class Button():
#     def __init__(self, x, y, image, scale, callback):
#         width = image.get_width()
#         height = image.get_height()
#         self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
#         self.rect = self.image.get_rect()
#         self.rect.topleft = (x, y)
#         self.callback = callback
#         self.toggle_state = False
#
#     def draw(self, surface):
#         action = False
#         # get mouse position
#         pos = pygame.mouse.get_pos()
#
#         # check mouseover and clicked conditions
#         if self.rect.collidepoint(pos):
#             if pygame.mouse.get_pressed()[0] == 1:
#                 self.toggle_state = not self.toggle_state
#                 if self.callback is not None:
#                     self.callback(surface)  # Execute the callback function with the toggle state
#                 action = True
#
#         # draw button on screen
#         surface.blit(self.image, (self.rect.x, self.rect.y))
#
#         return action
