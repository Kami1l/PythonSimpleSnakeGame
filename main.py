import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

player_x = 0
player_y = 0
player_parts = 3
player_width = 25
player_height = 25
player_move_speed = 0.15
actualyMove = 0

run = True

class Player:

    def __init__(self):
        pass
    def update(self):
        pass

player = Player()

while run:
    screen.fill((0,0,0))
    pygame.draw.rect(screen,(255,255,255),(player_x,player_y,player_width,player_height))
    key = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and actualyMove != "Down":
                actualyMove = "Top"
            elif event.key == pygame.K_s and actualyMove != "Top":
                actualyMove = "Down"
            elif event.key == pygame.K_a and actualyMove != "Right":
                actualyMove = "Left"
            elif event.key == pygame.K_d and actualyMove != "Left":
                actualyMove = "Right"

    if actualyMove == "Left":
        player_x -= player_move_speed
    elif actualyMove == "Right":
        player_x += player_move_speed
    elif actualyMove == "Top":
        player_y -= player_move_speed
    elif actualyMove == "Down":
        player_y += player_move_speed


    pygame.display.update()

pygame.quit()