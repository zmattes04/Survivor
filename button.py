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


class Level_Select_Button():
        def __init__(self, x, y, width, height, text=''):
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            self.text = text
            self.rect = pygame.Rect(x, y, width, height)
            self.clicked = False

        def draw(self, win, scroll_x=0, scroll_y=0):
            # Adjust position by the current scroll
            self.rect.topleft = (self.x + scroll_x, self.y + scroll_y)
            pygame.draw.rect(win, (255, 0, 0), self.rect)

            if self.text != '':
                font = pygame.font.SysFont('arial', 20)
                text = font.render(self.text, 1, (0, 0, 0))
                win.blit(text, (self.rect.x + (self.width / 2 - text.get_width() / 2),
                                self.rect.y + (self.height / 2 - text.get_height() / 2)))

            action = False
            pos = pygame.mouse.get_pos()

            # check mouseover and clicked conditions
            if self.rect.collidepoint(pos):
                if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                    self.clicked = True
                    self.toggle_state = True
                    print("toggled")
                    action = True

            return action