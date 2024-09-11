import math
import weapons
import pygame
import button
import time

class Player(pygame.sprite.Sprite):
    def __init__(self, weapon):
        super().__init__()
        self.x = 180
        self.y = 550
        self.speed = 5
        self.health = 100
        self.stamina = 900
        self.bones = 0
        self.shiny_rocks = 0
        self.exp = 1
        self.weapon = weapon
        original_image = pygame.image.load("images/Caveman.png").convert_alpha()
        self.image = pygame.transform.scale(original_image, (150, 150))
        self.weapon_image = pygame.image.load("images/" + weapon + "_weapon.png").convert_alpha()
        if weapon == "Bow":
            self.weapon_image = pygame.transform.scale(self.weapon_image, (75, 75))
        self.weapon_image = pygame.transform.rotate(self.weapon_image, -90)
        self.weapon_image_size = self.weapon_image.get_size()


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
        #calculate weapon angle
        if 0 <= angle < 90:
            weapon_angle = math.atan2(mouse_y - self.rect.centery + 0.9375*self.weapon_image_size[0], mouse_x - self.rect.centerx)
        elif 90 <= angle < 180:
            weapon_angle = math.atan2(mouse_y - self.rect.centery, mouse_x - self.rect.centerx + 0.9375*self.weapon_image_size[1])
        elif 180 <= angle < 270:
            weapon_angle = math.atan2(mouse_y - self.rect.centery - 0.9375*self.weapon_image_size[0], mouse_x - self.rect.centerx)
        else:
            weapon_angle = math.atan2(mouse_y - self.rect.centery, mouse_x - self.rect.centerx - 0.9375*self.weapon_image_size[1])


        # Rotate player image
        rotated_image = pygame.transform.rotate(self.image, -angle)
        self.rect = rotated_image.get_rect(center=self.rect.center)

        # Rotate weapon image
        angle_of_weapon_maintained = 100
        weapon_hypotenuse = 55

        opp = weapon_hypotenuse * math.sin(weapon_angle + 345)
        adj = weapon_hypotenuse * math.cos(weapon_angle + 345)

        location_of_weapon = (self.rect.centerx - 0.5625*self.weapon_image_size[0] + adj, self.rect.centery - 0.5625*self.weapon_image_size[1] + opp)



        rotated_weapon = pygame.transform.rotate(self.weapon_image, -angle)


        return rotated_image, rotated_weapon, location_of_weapon, self.rect.topleft


    def get_location(self):
        return self.rect.topleft

    # def draw(self, surface):
    #     surface.blit(self.image, self.rect)

    def attack(self, location_of_fist):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        angle = math.atan2(mouse_y - self.rect.centery, mouse_x - self.rect.centerx)
        angle = math.degrees(angle)
        if 0 <= angle < 90:
            weapon_angle = math.atan2(mouse_y - self.rect.centery + 0.9375*self.weapon_image_size[0], mouse_x - self.rect.centerx)
        elif 90 <= angle < 180:
            weapon_angle = math.atan2(mouse_y - self.rect.centery, mouse_x - self.rect.centerx + 0.9375*self.weapon_image_size[1])
        elif 180 <= angle < 270:
            weapon_angle = math.atan2(mouse_y - self.rect.centery - 0.9375*self.weapon_image_size[0], mouse_x - self.rect.centerx)
        else:
            weapon_angle = math.atan2(mouse_y - self.rect.centery, mouse_x - self.rect.centerx - 0.9375*self.weapon_image_size[1])

        # Calculate angle between player and mouse

        animation = 30
        opp = animation * math.sin(weapon_angle)
        adj = animation * math.cos(weapon_angle)

        location = (location_of_fist[0] + adj, location_of_fist[1] + opp)

        return location

class Inventory():
    def __init__(self, x, y, size, user):
        self.x = x
        self.y = y
        self.totalsize = 20
        self.cur_size = 0
        self.user = user
        self.items = [None] * self.totalsize #array of 20 empty items
        original_image = pygame.image.load("images/scroll_inventory.png").convert_alpha()
        self.image = pygame.transform.scale(original_image, (700, 700))

        self.rect = self.image.get_rect()
        self.rect.midbottom = (self.x, self.y)
        self.opened = False

    def add_bone(self, bone):
        for i in range(self.totalsize):
            if self.items[i] is None:
                self.items[i] = bone
                self.cur_size += 1
                return True
        return False

    def remove_item(self, item):
        for i in range(0, self.cur_size - 1):
            if self.items[i] == item:
                self.items[i] = None
                for j in range(i, self.totalsize - 1):
                    self.items[j] = self.items[j + 1]
                return None
        return None

    def get_item(self, index):
        if 0 <= index < self.cur_size:
            return self.items[index]
        print("Invalid index.")
        return None
    def list_inventory(self):
        for item in self.items:
            print(item)
    def draw_box(self, surface, x, y):
        pygame.draw.rect(surface, (210, 180, 140), (x, y, 70, 70))
        pygame.draw.rect(surface, (0, 0, 0), (x, y, 70, 70), 2)
    def draw_inventory(self, surface):
        #surface.blit(self.image, self.rect)
        #first row of inventory
        self.draw_box(surface, 220, 300)
        self.draw_box(surface, 320, 300)
        self.draw_box(surface, 420, 300)
        self.draw_box(surface, 520, 300)
        self.draw_box(surface, 620, 300)
        #second row of inventory
        self.draw_box(surface, 220, 400)
        self.draw_box(surface, 320, 400)
        self.draw_box(surface, 420, 400)
        self.draw_box(surface, 520, 400)
        self.draw_box(surface, 620, 400)
        #third row of inventory
        self.draw_box(surface, 220, 500)
        self.draw_box(surface, 320, 500)
        self.draw_box(surface, 420, 500)
        self.draw_box(surface, 520, 500)
        self.draw_box(surface, 620, 500)
        #fourth row of inventory
        self.draw_box(surface, 220, 600)
        self.draw_box(surface, 320, 600)
        self.draw_box(surface, 420, 600)
        self.draw_box(surface, 520, 600)
        self.draw_box(surface, 620, 600)

    #This displays the items in the inventory it also uses logic and a double locking system to
    # decide if it been clicked and chooses to open stats
    def display_items(self, surface):
        horizontal_inc = 0
        vertical_inc = 0
        horiz_count = 0
        vert_count = 0


        for index in range(self.cur_size):
            item = self.get_item(index)
            if horiz_count == 5:
                horizontal_inc = 0
                vert_count += 1
                vertical_inc += 100
                horiz_count = 0
            #item.image = pygame.transform.scale(item.image, (70, 70))
            if item is not None:
                item_button = button.Button(220 + horizontal_inc, 300 + vertical_inc, item.image, .46)
                #surface.blit(item.image, ((220 + horizontal_inc), 300 + vertical_inc))
                b = item_button.draw(surface)
                #Decides if it is already open or closed
                if b and self.opened == False:
                    time.sleep(.2)
                    item.opened_in_inven = not item.opened_in_inven
                    self.opened = not self.opened
                    print("ran")
                if b and self.opened == True:
                    pygame.draw.rect(surface, (0, 100, 100), (750, 300, 400, 500), 2)
                    print("close it")
                    self.opened = False
                #Sell code
                if item.sold == True:
                    self.items.remove(item)
                    self.cur_size -= 1
                    self.list_inventory()
                    print("sold")

            horizontal_inc += 100
            horiz_count += 1