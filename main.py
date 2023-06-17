import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

Config = {
    "player_x":0,
    "player_y":0,
    "player_width":25,
    "player_height":25,
    "player_parts":3,
    "player_move_speed":0.15,
    "actualyMove":0
}

run = True

class Player:

    def __init__(self):
        self.rect = pygame.Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)

    def update(self):
        pass

player = Player()

while run:
    screen.fill((0,0,0))
    pygame.draw.rect(screen,(255,255,255),(Config["player_x"],Config["player_y"],Config["player_width"],Config["player_height"]))
    key = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and Config["actualyMove"] != "Down":
                Config["actualyMove"] = "Top"
            elif event.key == pygame.K_s and Config["actualyMove"] != "Top":
                Config["actualyMove"] = "Down"
            elif event.key == pygame.K_a and Config["actualyMove"] != "Right":
                Config["actualyMove"] = "Left"
            elif event.key == pygame.K_d and Config["actualyMove"] != "Left":
                Config["actualyMove"] = "Right"

    if Config["actualyMove"] == "Left":
        Config["player_x"]-= Config["player_move_speed"]
    elif Config["actualyMove"] == "Right":
        Config["player_x"] += Config["player_move_speed"]
    elif Config["actualyMove"] == "Top":
        Config["player_y"] -= Config["player_move_speed"]
    elif Config["actualyMove"] == "Down":
        Config["player_y"] += Config["player_move_speed"]


    pygame.display.update()

pygame.quit()