import pygame

clock = pygame.time.Clock()
player_speed = 10
player_x = 50
player_y = 400
is_jump = False
jump_count = 15
pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Pobeg')
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)
bg_musik = pygame.mixer.Sound('musik.mp3')
bg_musik.play()
fon = pygame.image.load('bgg.png')
bg = pygame.image.load('bgg1.png')
# bg2 = pygame.image.load('bgg2.png')
player = pygame.image.load('hero_pravo1.png')
colorkey = player.get_at((0, 0))
player.set_colorkey(colorkey)
walk_pravo = [pygame.image.load('hero_pravo1.png'),
              pygame.image.load('hero_pravo2.png'),
              pygame.image.load('hero_pravo3.png'),
              pygame.image.load('hero_pravo4.png'),
              pygame.image.load('hero_pravo5.png'),
                ]





player_anim_count = 0
bg_x = 0
cursor = pygame.image.load('arrow.png')
pygame.mouse.set_visible(False)
running = True
while running:
    clock.tick(10)
    screen.blit(fon, (0, 0))
    screen.blit(bg, (340, 0))
    # screen.blit(bg2, (bg_x + 1280, 0))



    screen.blit(walk_pravo[player_anim_count], (350, player_y))
    player_anim_count += 1
    if player_anim_count == 5:
        player_anim_count = 1



    # coord = pygame.mouse.get_pos()




    keys = pygame.key.get_pressed()
    if not is_jump:
        if keys[pygame.K_w] or keys[pygame.K_SPACE]:
            is_jump = True
    else:
        if jump_count >= -15:
            if jump_count > 0:
                player_y -= (jump_count ** 2) / 2
            else:
                player_y += (jump_count ** 2) / 2
            jump_count -= 1
        else:
            is_jump = False
            jump_count = 15
    #
    #
    #
    # screen.blit(player, (player_x, player_y))
    pygame.display.update()
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    # if player_anim_count == 4:
    #     player_anim_count = 0
    # else:
    #     player_anim_count += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

