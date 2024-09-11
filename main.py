import math
import random
import sys
import button
import weapons
import player
import pygame
import items
import time
import enemies
import boundaries
import DungeonAlgo


def main():
    pygame.init()

    #Create game window
    SCREEN = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
    infoObject = pygame.display.Info()
    screen_width = infoObject.current_w
    screen_height = infoObject.current_h
    clock = pygame.time.Clock()
    pygame.display.set_caption("Main Menu")
    #room = boundaries.Room()
    #room.generate_walls(screen_width, screen_height)

    #Level select var
    scroll_x = 0
    scroll_y = 0

    #Sound Effects
    #themesong = pygame.mixer.Sound("sound/song-maker (1).ogg")
    #themesong.play(-1)
    #themesong.set_volume(.3)
    #punch = pygame.mixer.Sound("sound/82UX6W2-fights-punches-beefy-punch.mp3")
    #Game Variables
    game_started = False #Switched when level is selected
    game_Paused = False  #Switched when esc is clicked
    menu_state = "main"  #Changed when in settings
    level_select = False #Switched when play is pressed
    game_ended = False   #To show game over

    #Start of game variables
    exp_needed = 5
    cur_exp = 0
    # initalize the player

    weapon = "Fist"
    #check weapon for user

    user = player.Player(weapon)



    all_sprites = pygame.sprite.Group()
    bones_group = pygame.sprite.Group()
    enemy_group = pygame.sprite.Group()
    #initalized wolf

    for i in range(20):
        rand_x = random.randint(50, 1300)
        rand_y = random.randint(50, 850)
        wolf1 = enemies.Wolf(rand_x, rand_y, None)
        all_sprites.add(wolf1)
        enemy_group.add(wolf1)
    #create Sprite Groups


    player_inventory = player.Inventory(500, 850, 20, user)



    bone = items.Bones(100, random.randint(50, 1300), random.randint(50, 850))
    #all_sprites.add(user)

    all_sprites.add(bone)
    bones_group.add(bone)





    # load button images
    resume_img = pygame.image.load("images/button_resume.png").convert_alpha()
    options_img = pygame.image.load("images/button_options.png").convert_alpha()
    quit_img = pygame.image.load("images/button_quit.png").convert_alpha()
    video_img = pygame.image.load('images/button_video.png').convert_alpha()
    audio_img = pygame.image.load('images/button_audio.png').convert_alpha()
    keys_img = pygame.image.load('images/button_keys.png').convert_alpha()
    back_img = pygame.image.load('images/button_back.png').convert_alpha()

    #Main menu Background
    background_image = pygame.image.load('images/MainMenuBackground.jpg')

    # Transform the background image to fit your screen size if necessary
    background_image = pygame.transform.scale(background_image, (SCREEN.get_width(), SCREEN.get_height()))

    #create buttons
    resume_button = button.Button(1200, 300, resume_img, 1)
    options_button = button.Button(1200, 400, options_img, 1)
    quit_button = button.Button(1200, 500, quit_img, 1)
    quit_button_intro = button.Button(500, 400, quit_img, 1)
    video_button = button.Button(800, 500, video_img, 1)
    audio_button = button.Button(800, 400, audio_img, 1)
    keys_button = button.Button(800, 300, keys_img, 1)
    back_button = button.Button(800, 600, back_img, 1)




    black = (0, 0, 0)
    white = (255, 255, 255)
    level_select_color = (0, 100, 100)
    font_size = 100
    mainfont = pygame.font.SysFont("Rubik Glitch Pop", font_size)
    resource_fonts = pygame.font.SysFont("arial", 20)
    def draw_text(text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        SCREEN.blit(img, (x,y))

    #Levels
    dungeonMap = DungeonAlgo.Dungeon(4, 4)
    dungeonMap.connect_rooms()
    dungeonMap.create_dead_ends(30)
    dungeonMap.display()
    row_for_map = 0
    col_for_map = 0
    moving_through_right_rooms = False
    moving_through_left_rooms = False
    moving_through_top_rooms = False
    moving_through_bottom_rooms = False
    transitioning = False

    #Game Running
    run = True
    while run:
        SCREEN.fill(black)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_Paused = True

                if event.key == pygame.K_p:
                    run = False


        #Starts in Main Menu to play game
        if game_started == False and game_Paused == False:

            SCREEN.blit(background_image, (0,0))
            draw_text("I can Survive!", mainfont, white, 550, 200)
            #Use of different named button as placeholder
            if keys_button.draw(SCREEN):
                level_select = True
                #game_started = True
            if quit_button_intro.draw(SCREEN):
                run = False
        if game_Paused == True:
            #check menu state
            #in game inventory system
            if game_started == True:
                opened = 1
                SCREEN.fill((0, 100, 100))
                player_inventory.draw_inventory(SCREEN)
                player_inventory.display_items(SCREEN)
                draw_text("Game Paused", mainfont, white, 600, 100)
                for index in range(player_inventory.cur_size):
                    item = player_inventory.get_item(index)
                    #opens or closes the stats
                    if item.opened_in_inven == True and opened == 1:
                        pygame.draw.rect(SCREEN, (0, 100, 100), (750, 300, 400, 500), 2)
                        item.display_stats(SCREEN)
                        opened = 0
                    if item.opened_in_inven == False:

                        opened = 1

                        #pygame.draw.rect(SCREEN, (0, 100, 100), (750, 300, 400, 500))
            # if pygame.key.get_pressed()[pygame.K_q]:
            #     game_Paused = False

            if menu_state == "main":
                #draw pause screen buttons
                if resume_button.draw(SCREEN):
                    game_Paused = False
                if options_button.draw(SCREEN):
                    menu_state = "options"
                if quit_button.draw(SCREEN):
                    run = False
            if menu_state == "options":
                if video_button.draw(SCREEN):
                    pass
                if audio_button.draw(SCREEN):
                    pass
                if back_button.draw(SCREEN):
                    menu_state = "main"

        if level_select == True:
            map_width = 2000
            map_height = 2000
            level_select_map = pygame.Surface((map_width, map_height))
            level_select_map.fill(level_select_color)
            buttons = [button.Level_Select_Button(i * 100, i * 50, 80, 40, f'Level {i + 1}') for i in range(20)]
            #for i in range(20):  # Just creating some rectangles to act as placeholders for levels
           #     pygame.draw.rect(level_select_map, (100, 100, 250), (i * 100, i * 50, 80, 40))


            scroll_speed = 5
            #how the level select scrolls
            keys = pygame.key.get_pressed()
            if keys[pygame.K_a]:
                #scroll_x += scroll_x + scroll_speed
                scroll_x = min(scroll_x + scroll_speed, 0)
            if keys[pygame.K_d]:
                #scroll_x -= scroll_x - scroll_speed
                scroll_x = max(scroll_x - scroll_speed, screen_width - map_width)
            if keys[pygame.K_w]:
                #scroll_y -= scroll_y + scroll_speed

                scroll_y = min(scroll_y + scroll_speed, 0)
            if keys[pygame.K_s]:
                #scroll_y = scroll_y - scroll_speed

                scroll_y = max(scroll_y - scroll_speed, screen_height - map_height)

            SCREEN.fill(white)
            SCREEN.blit(level_select_map, (scroll_x, scroll_y))
            for level in buttons:
                if level.draw(SCREEN, scroll_x, scroll_y):
                    level_select = False
                    game_started = True


        if game_started == True and game_Paused == False:

            current_room = dungeonMap.rooms[row_for_map][col_for_map]
            r_id = current_room.room_id
            print(current_room)
            current_room.generate_walls(screen_width, screen_height)
            #right door interact
            # Define a tolerance value
            xtolerance = 100
            ytolerance = 100
            # Check if user's position is within the tolerance range
            interact_with_door = pygame.key.get_pressed()
            print(dungeonMap.rooms)
            #Create Door navigation Logic
            #
            # #Right door
            # if abs(user.x - (screen_width - 15)) <= xtolerance and abs(user.y - (screen_height / 3 * 2)) <= ytolerance:
            #     if interact_with_door[pygame.K_f]:  # Check if F key is pressed
            #         if not moving_through_right_rooms:  # Check if we are not already moving through rooms
            #             moving_through_right_rooms = True  # Set flag to indicate we are moving through rooms
            #             row_for_map += 1
            #             print("got here")
            # else:
            #     moving_through__right_rooms = False  # Reset flag when not interacting with door
            #
            # #Left Door
            # if abs(user.x) <= xtolerance and abs(user.y - (screen_height / 3 * 2)) <= ytolerance:
            #     if interact_with_door[pygame.K_f]:  # Check if F key is pressed
            #         if not moving_through_left_rooms:  # Check if we are not already moving through rooms
            #             moving_through_left_rooms = True  # Set flag to indicate we are moving through rooms
            #             row_for_map -= 1
            #             print("got here")
            # else:
            #     moving_through_left_rooms = False  # Reset flag when not interacting with door
            #
            # #Bottom Door
            # if abs(user.x - (screen_width / 3 * 2)) <= xtolerance and abs(user.y - screen_height) <= ytolerance:
            #     if interact_with_door[pygame.K_f]:  # Check if F key is pressed
            #         if not moving_through_bottom_rooms:  # Check if we are not already moving through rooms
            #             moving_through_bottom_rooms = True  # Set flag to indicate we are moving through rooms
            #             col_for_map += 1
            #
            #             print("got here")
            # else:
            #     moving_through_bottom_rooms = False  # Reset flag when not interacting with door
            #
            #
            # #Top Door
            # if abs(user.x - (screen_width / 3 * 2)) <= xtolerance and abs(user.y) <= ytolerance:
            #     if interact_with_door[pygame.K_f]:  # Check if F key is pressed
            #         if not moving_through_top_rooms:  # Check if we are not already moving through rooms
            #             moving_through_top_rooms = True  # Set flag to indicate we are moving through rooms
            #             col_for_map -= 1
            #             print("got here")
            #             #user.y = screen_height - 25
            #
            # else:
            #     moving_through_top_rooms = False  # Reset flag when not interacting with door
            #

            # Right Door
            # Right Door Transition
            #OTHER WAY
            # if abs(user.x - (screen_width - 15)) <= xtolerance and abs(user.y - (screen_height / 3 * 2)) <= ytolerance:
            #     if interact_with_door[pygame.K_f] and not moving_through_right_rooms:  # Check if F key is pressed
            #         moving_through_right_rooms = True  # Set flag to indicate we are moving through rooms
            #
            #         # Smooth animation towards the door
            #         while user.x < screen_width - 15:
            #             user.x += 2  # Adjust speed as needed, 2 is an example
            #
            #             # Redraw screen and update display
            #             SCREEN.fill(black)
            #             #current_room.draw_boundaries(SCREEN)
            #             user.update()
            #             pygame.display.flip()
            #             clock.tick(60)
            #
            #         # Now position the user at the left door of the next room
            #         row_for_map += 1
            #         #user.x = 15  # Adjust player's x-coordinate to the left door of the next room
            #
            #         print("Transitioning to the room on the right")
            #
            #
            # elif not (abs(user.x - (screen_width - 15)) <= xtolerance and abs(
            #         user.y - (screen_height / 3 * 2)) <= ytolerance):
            #     moving_through_right_rooms = False  # Reset flag when not interacting with door
            #
            # # Left Door
            # if abs(user.x) <= xtolerance and abs(user.y - (screen_height / 3 * 2)) <= ytolerance:
            #     if interact_with_door[pygame.K_f] and not moving_through_left_rooms:  # Check if F key is pressed
            #         moving_through_left_rooms = True  # Set flag to indicate we are moving through rooms
            #         row_for_map -= 1
            #         user.x = screen_width - 15
            #         print("Transitioning to the room on the left")
            #
            # elif not (abs(user.x) <= xtolerance and abs(user.y - (screen_height / 3 * 2)) <= ytolerance):
            #     moving_through_left_rooms = False  # Reset flag when not interacting with door
            #
            # # Bottom Door
            # if abs(user.x - (screen_width / 3 * 2)) <= xtolerance and abs(user.y - screen_height) <= ytolerance:
            #     if interact_with_door[pygame.K_f] and not moving_through_bottom_rooms:  # Check if F key is pressed
            #         moving_through_bottom_rooms = True  # Set flag to indicate we are moving through rooms
            #         col_for_map += 1
            #         user.y = 15
            #         print("Transitioning to the room at the bottom")
            #
            # elif not (abs(user.x - (screen_width / 3 * 2)) <= xtolerance and abs(user.y - screen_height) <= ytolerance):
            #     moving_through_bottom_rooms = False  # Reset flag when not interacting with door
            #
            # # Top Door
            # if abs(user.x - (screen_width / 3 * 2)) <= xtolerance and abs(user.y) <= ytolerance:
            #     if interact_with_door[pygame.K_f] and not moving_through_top_rooms:  # Check if F key is pressed
            #         moving_through_top_rooms = True  # Set flag to indicate we are moving through rooms
            #         col_for_map -= 1
            #         user.y = screen_height - 15
            #         print("Transitioning to the room at the top")
            #
            # elif not (abs(user.x - (screen_width / 3 * 2)) <= xtolerance and abs(user.y) <= ytolerance):
            #     moving_through_top_rooms = False  # Reset flag when not interacting with door

            def animate_transition(new_x, new_y):
                step = 5
                while abs(user.x - new_x) > step or abs(user.y - new_y) > step:
                    if user.x < new_x:
                        user.x += step
                    elif user.x > new_x:
                        user.x -= step
                    if user.y < new_y:
                        user.y += step
                    elif user.y > new_y:
                        user.y -= step
                    SCREEN.fill(black)
                    current_room.draw_boundaries(SCREEN)
                    user.update()
                    pygame.display.flip()
                    clock.tick(60)
                user.x = new_x
                user.y = new_y

            # Right door transition
            if abs(user.x - (screen_width - 15)) <= xtolerance and abs(user.y - (screen_height / 3 * 2)) <= ytolerance:
                if interact_with_door[pygame.K_f]:
                    if not moving_through_right_rooms:
                        moving_through_right_rooms = True
                        animate_transition(screen_width - 15, screen_height / 3 * 2)
                        row_for_map += 1
                        user.x = 15  # Place user at the left door of the new room
                else:
                    moving_through_right_rooms = False

            # Left door transition
            if abs(user.x) <= xtolerance and abs(user.y - (screen_height / 3 * 2)) <= ytolerance:
                if interact_with_door[pygame.K_f]:
                    if not moving_through_left_rooms:
                        moving_through_left_rooms = True
                        animate_transition(0, screen_height / 3 * 2)
                        row_for_map -= 1
                        user.x = screen_width - 15  # Place user at the right door of the new room
                else:
                    moving_through_left_rooms = False

            # Bottom door transition
            if abs(user.x - (screen_width / 3 * 2)) <= xtolerance and abs(user.y - screen_height) <= ytolerance:
                if interact_with_door[pygame.K_f]:
                    if not moving_through_bottom_rooms:
                        moving_through_bottom_rooms = True
                        animate_transition(screen_width / 3 * 2, screen_height)
                        col_for_map += 1
                        user.y = 15  # Place user at the top door of the new room
                else:
                    moving_through_bottom_rooms = False

            # Top door transition
            if abs(user.x - (screen_width / 3 * 2)) <= xtolerance and abs(user.y) <= ytolerance:
                if interact_with_door[pygame.K_f]:
                    if not moving_through_top_rooms:
                        moving_through_top_rooms = True
                        animate_transition(screen_width / 3 * 2, 0)
                        col_for_map -= 1
                        user.y = screen_height - 15  # Place user at the bottom door of the new room
                else:
                    moving_through_top_rooms = False

            current_visiblity = user.health * 17.5

            pygame.draw.circle(SCREEN, (0, 100, 100), user.rect.center, current_visiblity)
            if user.health <= 0:
                game_ended = True
            for sprite in all_sprites:
                distance = math.sqrt((sprite.rect.centerx - user.rect.centerx)**2 + (sprite.rect.centery - user.rect.centery)**2)
                if distance <= current_visiblity:

                    sprite.visible = True
                    SCREEN.blit(sprite.image, sprite.rect.topleft)

            for wolf_enemy in enemy_group:
                wolf_enemy.MoveTo(user)
                wolf_enemy.attack_target(user)

            #enemy_group.draw(SCREEN)

            bones_display = resource_fonts.render(f'Bones: {user.bones}', True, (255, 255, 255))
            experience_display = resource_fonts.render(f'LVL: {user.exp}', True, (255, 255, 255))
            shiny_rocks_display = resource_fonts.render(f'Shiny Rocks: {user.shiny_rocks}', True, (255, 255, 255))

            SCREEN.blit(bones_display, (1350,900))
            SCREEN.blit(experience_display, (1350,920))
            SCREEN.blit(shiny_rocks_display, (1350,940))


            rotated_user, rotated_weapon, weapon_location, user_position = user.face_mouse()
            #rotated_user, user_position = user.face_mouse()

            SCREEN.blit(rotated_user, user_position)

            #SCREEN.blit(rotated_weapon, weapon_position)
            #Attack logic with space
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                l = user.attack(weapon_location)

                collided_enemies = pygame.sprite.spritecollide(user, enemy_group, False, pygame.sprite.collide_mask)
                if collided_enemies is not None:
                    for enemy in collided_enemies:
                        if enemy.health < 0:
                            e_x = enemy.x
                            e_y = enemy.y
                            b = items.Bones(random.randint(1,5), e_x, e_y)
                            bones_group.add(b)
                            all_sprites.add(b)
                            enemy.kill()
                        enemy.health = enemy.health - 30
                SCREEN.blit(rotated_weapon, l)

            else:
                SCREEN.blit(rotated_weapon, weapon_location)
            #creating bone location
            bones_x = random.randint(50, 1300)
            bones_y = random.randint(50, 850)
            #bones_group.draw(SCREEN)
            collided_bones = pygame.sprite.spritecollide(user, bones_group, False, pygame.sprite.collide_mask)
            if collided_bones is not None and (player_inventory.cur_size != player_inventory.totalsize):
                for collected_bone in collided_bones:
                    user.bones += 1
                    cur_exp += 1
                    player_inventory.add_bone(collected_bone)

                    collected_bone.kill()
                    player_inventory.list_inventory()


                if cur_exp == exp_needed:
                    user.exp += 1
                    exp_needed = exp_needed + 5
                    cur_exp = 0



            if len(bones_group) < 1:
                bone = items.Bones(100, bones_x, bones_y)
                all_sprites.add(bone)
                bones_group.add(bone)

            #if :
            current_room.draw_boundaries(SCREEN)
            #room.draw(SCREEN)
            user.update()

        if game_ended == True:

            SCREEN.fill((0, 100, 100))
            if quit_button.draw(SCREEN):
                run = False
            draw_text("Game Over", mainfont, white, 600, 100)
        pygame.display.flip()
        clock.tick(60)






main()

