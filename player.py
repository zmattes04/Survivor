import math
import fist
import pygame

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
        self.weapon_image = pygame.transform.rotate(self.weapon_image, -90)


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

    def rotate_and_blit(self, screen, image, angle, position, offset, pivot_angle):
        """Rotate an image and blit it to the screen at the specified position with an offset and pivot angle."""
        # Rotate the image
        rotated_image = pygame.transform.rotate(image, -angle)
        rotated_rect = rotated_image.get_rect(center=position)

        # Calculate the offset based on the pivot angle
        offset_rotated = pygame.math.Vector2(offset).rotate(-angle)
        offset_position = rotated_rect.center + offset_rotated

        # Blit the rotated image to the screen
        screen.blit(rotated_image, rotated_image.get_rect(center=offset_position))

    def face_mouse(self):
        # Get mouse position
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Calculate angle between player and mouse
        angle = math.atan2(mouse_y - self.rect.centery, mouse_x - self.rect.centerx)
        angle = math.degrees(angle)
        #calculate weapon angle
        if 0 <= angle < 90:
            weapon_angle = math.atan2(mouse_y - self.rect.centery + 30, mouse_x - self.rect.centerx)
        elif 90 <= angle < 180:
            weapon_angle = math.atan2(mouse_y - self.rect.centery, mouse_x - self.rect.centerx + 30)
        elif 180 <= angle < 270:
            weapon_angle = math.atan2(mouse_y - self.rect.centery - 30, mouse_x - self.rect.centerx)
        else:
            weapon_angle = math.atan2(mouse_y - self.rect.centery, mouse_x - self.rect.centerx - 30)


        # Rotate player image
        rotated_image = pygame.transform.rotate(self.image, -angle)
        self.rect = rotated_image.get_rect(center=self.rect.center)

        # Rotate weapon image
        angle_of_weapon_maintained = 100
        weapon_hypotenuse = 55

        opp = weapon_hypotenuse * math.sin(weapon_angle + 345)
        adj = weapon_hypotenuse * math.cos(weapon_angle + 345)

        location_of_weapon = (self.rect.centerx - 18 + adj, self.rect.centery - 18 + opp)


        print(weapon_angle)
        rotated_weapon = pygame.transform.rotate(self.weapon_image, -angle)


        return rotated_image, rotated_weapon, location_of_weapon, self.rect.topleft

    # def face_mouse(self):
    #     # Get mouse position
    #     mouse_x, mouse_y = pygame.mouse.get_pos()
    #
    #     # Calculate angle between player and mouse in radians
    #     angle_rad = math.atan2(mouse_y - self.rect.centery, mouse_x - self.rect.centerx)
    #
    #     # Convert angle to degrees
    #     angle_deg = math.degrees(angle_rad)
    #
    #     # Rotate player image
    #     rotated_image = pygame.transform.rotate(self.image, -angle_deg)
    #     new_rect = rotated_image.get_rect(center=self.rect.center)
    #
    #     # Rotate weapon image
    #     angle_of_weapon_maintained = 60
    #     weapon_hypotenuse = 10
    #
    #     opp = weapon_hypotenuse * math.sin(angle_of_weapon_maintained)
    #     adj = weapon_hypotenuse * math.cos(angle_of_weapon_maintained)
    #
    #     location_of_weapon = (self.rect.centerx + adj, self.rect.centery + opp)
    #
    #
    #
    #     rotated_weapon = pygame.transform.rotate(self.weapon_image, -angle_deg)
    #
    #
    #     # Calculate the offset for the weapon based on where you want it to appear relative to the player
    #     # This example assumes you want the weapon to appear right in front of the player
    #     # weapon_offset_x = 0  # Adjust as necessary
    #     # weapon_offset_y = -new_rect.height / 2  # Example offset; adjust as necessary
    #     #
    #     # # Create a new surface to combine both images with enough space
    #     # # The new surface dimensions should be large enough to hold both images after rotation
    #     # combined_surface_width = max(new_rect.width, rotated_weapon.get_width())
    #     # combined_surface_height = new_rect.height + rotated_weapon.get_height()
    #     # combined_surface = pygame.Surface((combined_surface_width, combined_surface_height), pygame.SRCALPHA)
    #     #
    #     # # Blit the player image onto the combined surface at the center
    #     # combined_surface.blit(rotated_image, (
    #     # combined_surface_width / 2 - new_rect.width / 2, combined_surface_height - new_rect.height))
    #     #
    #     # # Blit the weapon image onto the combined surface at the calculated offset position
    #     # weapon_blit_position = (combined_surface_width / 2 + weapon_offset_x - rotated_weapon.get_width() / 2,
    #     #                         combined_surface_height - new_rect.height / 2 + weapon_offset_y - rotated_weapon.get_height() / 2)
    #     # combined_surface.blit(rotated_weapon, weapon_blit_position)
    #     #
    #     # # Update the player's rect to match the new combined image dimensions
    #     # self.rect = combined_surface.get_rect(center=new_rect.center)
    #
    #     # Now, combined_surface contains both the player and the weapon as a single image
    #     # You can return this surface to be drawn in your game loop
    #     return rotated_image, rotated_weapon, location_of_weapon, self.rect.topleft
    def get_location(self):
        return self.rect.topleft

    # def draw(self, surface):
    #     surface.blit(self.image, self.rect)

    def attack(self, location_of_fist):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        angle = math.atan2(mouse_y - self.rect.centery, mouse_x - self.rect.centerx)
        angle = math.degrees(angle)
        if 0 <= angle < 90:
            weapon_angle = math.atan2(mouse_y - self.rect.centery + 30, mouse_x - self.rect.centerx)
        elif 90 <= angle < 180:
            weapon_angle = math.atan2(mouse_y - self.rect.centery, mouse_x - self.rect.centerx + 30)
        elif 180 <= angle < 270:
            weapon_angle = math.atan2(mouse_y - self.rect.centery - 30, mouse_x - self.rect.centerx)
        else:
            weapon_angle = math.atan2(mouse_y - self.rect.centery, mouse_x - self.rect.centerx - 30)

        # Calculate angle between player and mouse

        animation = 30
        opp = animation * math.sin(weapon_angle)
        adj = animation * math.cos(weapon_angle)

        location = (location_of_fist[0] + adj, location_of_fist[1] + opp)




        return location

