import pygame

class Wolf(pygame.sprite.Sprite):
    def __init__(self, x, y, loot):
        super().__init__()
        self.x = x
        self.y = y
        self.loot = loot
        self.health = 300
        self.damage = 50
        self.attack_speed = 0
        original_image = pygame.image.load("images/EnemyTemp.png").convert_alpha()
        self.image = pygame.transform.scale(original_image, (150, 150))
        self.rect = self.image.get_rect()
        self.rect.midbottom = (self.x, self.y)

    #Move to target
    def attack_target(self, target):

        if target.x is not None and target.y is not None:
            target_x = target.x
            target_y = target.y

            dx = target_x - self.x
            dy = target_y - self.y
            distance = (dx ** 2 + dy ** 2) ** 0.5
            #Uses a counter for attack speed to time when it will attack
            if distance < 50 and self.attack_speed == 0:
                target.health = target.health - self.damage
            if self.attack_speed == 300:
                self.attack_speed = 0
            else:
                self.attack_speed += 1
    #Attack
    #King wolf can Howl spawns more
    #Dies
    #Draw
    #Gets Hit

    #Moves toward targets
    def MoveTo(self, target):
        if target.x is not None and target.y is not None:
            target_x = target.x
            target_y = target.y
            print("Target:" + str(target_x) + "," + str(target_y))
            print("Wolf:" + str(self.x) + "," + str(self.y))

            # Calculate the distance between the wolf and the target
            dx = target_x - self.x
            dy = target_y - self.y
            distance = (dx ** 2 + dy ** 2) ** 0.5

            # Normalize the distance
            if distance != 0:
                dx /= distance
                dy /= distance

            # Move the wolf towards the target
            speed = 1  # Adjust as needed
            self.x += dx * speed
            self.y += dy * speed

            # Update the rect attribute
            self.rect.center = (self.x, self.y)


    def draw_wolf(self, surface):
        surface.blit(self.image, self.rect)
