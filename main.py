import pygame
import random

pygame.init()

Colors = {
    "black":(0,0,0),
    "white":(255,255,255),
    "red":(255,0,0)
}

Config = {
    "SCREEN_WIDTH":800,
    "SCREEN_HEIGHT":800,
    "BACKGROUND_COLOR":Colors["black"],
}

Player = {
    "player_x":0,
    "player_y":0,
    "player_width":25,
    "player_height":25,
    "player_parts":3,
    "player_move_speed":15,
    "actualyMove":0
}

Food = {
    "food_x":100,
    "food_y":100,
    "food_width":10,
    "food_height":10,
    "food_color":Colors["red"],
    "food_amount":0
}

screen = pygame.display.set_mode((Config["SCREEN_WIDTH"], Config["SCREEN_HEIGHT"]))
clock = pygame.time.Clock()

def randomFoodLocation():
    Food["food_x"] = round(random.randrange(20, Config["SCREEN_WIDTH"]-20))
    Food['food_y'] = round(random.randrange(20, Config["SCREEN_HEIGHT"]-20))


def main():
    run = True

    while run:
        # Draw the player,fill the screen,initialize the key

        screen.fill(Config["BACKGROUND_COLOR"])
        player = pygame.draw.rect(screen,Colors["white"],(Player["player_x"],Player["player_y"],Player["player_width"],Player["player_height"]))
        key = pygame.key.get_pressed()

        # Food spawning and eating food

        food = pygame.draw.rect(screen,Food["food_color"],(Food['food_x'],Food['food_y'],Food['food_width'],Food['food_height']))
        if Food["food_amount"] == 0:
            randomFoodLocation()
            Food["food_amount"] += 1

        eating = player.colliderect(food)
        if eating == True:
            Food["food_amount"] -=1

        # Player move and quit the game

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and Player["actualyMove"] != "Down":
                    Player["actualyMove"] = "Top"
                elif event.key == pygame.K_s and Player["actualyMove"] != "Top":
                    Player["actualyMove"] = "Down"
                elif event.key == pygame.K_a and Player["actualyMove"] != "Right":
                    Player["actualyMove"] = "Left"
                elif event.key == pygame.K_d and Player["actualyMove"] != "Left":
                    Player["actualyMove"] = "Right"

        # Blocking the keyboard movement 

        if Player["actualyMove"] == "Left":
            Player["player_x"]-= Player["player_move_speed"]
        elif Player["actualyMove"] == "Right":
            Player["player_x"] += Player["player_move_speed"]
        elif Player["actualyMove"] == "Top":
            Player["player_y"] -= Player["player_move_speed"]
        elif Player["actualyMove"] == "Down":
            Player["player_y"] += Player["player_move_speed"]

        # Lose condition

        if Player["player_x"] < 0 or Player["player_x"] > Config["SCREEN_WIDTH"] or Player["player_y"] < 0 or Player["player_y"] > Config["SCREEN_HEIGHT"]:
            break

        clock.tick(20)
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()