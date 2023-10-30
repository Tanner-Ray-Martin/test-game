from pygame.time import Clock
import pygame
from core.player import Player
from core.clouds import Cloud
from core.planks import Ground
from random import randint
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1366, 768
game_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
bg_path = r"C:\Users\tanner.martin\Desktop\test_game\test_game2\resources\ai_bg.png"
bg_img = pygame.image.load(bg_path).convert()
bg_img = pygame.transform.scale(bg_img, game_window.get_size())
bg_img2 = pygame.transform.flip(bg_img, True, False)
def generate_list_of_clouds():
    num_clouds = 30
    clouds:list[Cloud] = []
    for i in range(num_clouds):
        x = randint(-10, WINDOW_WIDTH)
        cloud = Cloud(x)
        clouds.append(cloud)
    return clouds

def generate_list_of_players(groud_level:int):
    num_players = 2000
    players:list[Player] = []
    #create a number of players with random speed and jump power
    for i in range(num_players):
        player = Player(randint(10, 25), randint(1, 30))
        player.rect.bottom = randint(int(groud_level/2), groud_level)
        player.rect.x = randint(0, WINDOW_WIDTH-player.rect.width)
        if player.rect.bottom < groud_level:
            player.jumping = True
        players.append(player)
    return players

def game_loop():
    running = True
    all_sprites = pygame.sprite.Group()
    num_players = 20
    players:list[Player] = []
    clouds = generate_list_of_clouds()
    ground = Ground(WINDOW_WIDTH, WINDOW_HEIGHT, game_window)
    ground_top = ground.height
    #create a number of players with random speed and jump power
    players = generate_list_of_players(ground_top)
    [all_sprites.add(cloud) for cloud in clouds]
    [all_sprites.add(player) for player in players]
    clock = Clock()
    bg_direction = 0
    bg_x = 0
    bg_y = 0
    bg_x_v = 0
    while running:
        should_jump = False

        #check to see if we should exit the game or if the player should jump
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_SPACE:
                    should_jump = True
            elif event.type == pygame.QUIT:
                running = False
        #get the pressed keys, send them to the player move function, and update the player sprite
        pressed_keys = pygame.key.get_pressed()
        game_window.blit(bg_img, (bg_x, bg_y))
        game_window.blit(bg_img2, (bg_x-WINDOW_WIDTH, bg_y))
        game_window.blit(bg_img2, (bg_x+WINDOW_WIDTH, bg_y))
        bg_x += 1
        if bg_x >= WINDOW_WIDTH:
            bg_x = 0-WINDOW_WIDTH
        for cloud in clouds:
            cloud.move(WINDOW_WIDTH)
            cloud.update()
        for player in players:
            player.move(pressed_keys, WINDOW_WIDTH, ground_top, should_jump)
            player.update()

        all_sprites.draw(game_window)
        ground.update()
        pygame.display.flip()
        clock.tick(30)

game_loop()