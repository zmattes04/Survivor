import random
import sys
import button
import player
import pygame
import bones

def main():
    pygame.init()

    #Create game window
    SCREEN = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
    clock = pygame.time.Clock()
    pygame.display.set_caption("Main Menu")

    #Game Variables
    game_started = False
    game_Paused = False
    menu_state = "main"

    #Start of game variables
    exp_needed = 5
    cur_exp = 0
    # initalize the player
    user = player.Player()

    #create Sprite Groups
    all_sprites = pygame.sprite.Group()
    bones_group = pygame.sprite.Group()

    bone = bones.Bones(100, 500, 500)
    all_sprites.add(user)
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
    resume_button = button.Button(500, 300, resume_img, 1)
    options_button = button.Button(500, 400, options_img, 1)
    quit_button = button.Button(500, 500, quit_img, 1)
    quit_button_intro = button.Button(500, 400, quit_img, 1)
    video_button = button.Button(500, 500, video_img, 1)
    audio_button = button.Button(500, 400, audio_img, 1)
    keys_button = button.Button(500, 300, keys_img, 1)
    back_button = button.Button(500, 600, back_img, 1)




    black = (0, 0, 0)
    white = (255, 255, 255)
    font_size = 100
    mainfont = pygame.font.SysFont("Rubik Glitch Pop", font_size)
    resource_fonts = pygame.font.SysFont("arial", 20)
    def draw_text(text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        SCREEN.blit(img, (x,y))



    #Game Running
    run = True
    while run:
        SCREEN.fill((0, 100, 100))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_Paused = True
                    print("pressed")
                if event.key == pygame.K_q:
                    run = False


        #Starts in Main Menu to play game
        if game_started == False and game_Paused == False:

            SCREEN.blit(background_image, (0,0))
            draw_text("I can Survive!", mainfont, white, 550, 200)
            #Use of different named button as placeholder
            if keys_button.draw(SCREEN):
                game_started = True
            if quit_button_intro.draw(SCREEN):
                run = False
        if game_Paused == True:
            #check menu state

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
        if game_started == True and game_Paused == False:


            bones_display = resource_fonts.render(f'Bones: {user.bones}', True, (255, 255, 255))
            experience_display = resource_fonts.render(f'LVL: {user.exp}', True, (255, 255, 255))
            shiny_rocks_display = resource_fonts.render(f'Shiny Rocks: {user.shiny_rocks}', True, (255, 255, 255))

            SCREEN.blit(bones_display, (1350,900))
            SCREEN.blit(experience_display, (1350,920))
            SCREEN.blit(shiny_rocks_display, (1350,940))

            rotated_user, user_position = user.face_mouse()
            SCREEN.blit(rotated_user, user_position)
            #creating bone location
            bones_x = random.randint(50, 1300)
            bones_y = random.randint(50, 850)
            bones_group.draw(SCREEN)
            if pygame.sprite.spritecollide(user, bones_group, True, pygame.sprite.collide_mask):
                user.bones += 1
                cur_exp += 1

                if cur_exp == exp_needed:
                    user.exp += 1
                    exp_needed = exp_needed + 5
                    cur_exp = 0

                print(user.bones)

            if len(bones_group) < 1:
                bone = bones.Bones(100, bones_x, bones_y)
                all_sprites.add(bone)
                bones_group.add(bone)

            if


            #if user.get_location() == (bones_x, bones_y):

            user.update()



        pygame.display.flip()
        clock.tick(60)






main()

