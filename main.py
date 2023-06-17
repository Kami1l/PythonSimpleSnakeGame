import pygame
import random

pygame.init()

Colors = {
    "black":(0,0,0),
    "green":(0,255,0),
    "red":(255,0,0)
}

Config = {
    "SCREEN_WIDTH":800,
    "SCREEN_HEIGHT":600,
    "BACKGROUND_COLOR":Colors["black"],
    "RECT_SIZE":10,
    "GAME_SPEED": 20
}

Player = {
    "player_x":Config["SCREEN_WIDTH"]/2,
    "player_y":Config["SCREEN_HEIGHT"]/2,
    "player_width":Config["RECT_SIZE"],
    "player_height":Config["RECT_SIZE"],
    "player_parts":[],
    "Length":0,
    "player_move_speed":Config["RECT_SIZE"],
    "actualyMove":0
}

Food = {
    "food_x":0,
    "food_y":0,
    "food_width":Config["RECT_SIZE"],
    "food_height":Config["RECT_SIZE"],
    "food_color":Colors["red"],
}

screen = pygame.display.set_mode((Config["SCREEN_WIDTH"], Config["SCREEN_HEIGHT"]))
clock = pygame.time.Clock()

def randomFoodLocation():
    Food["food_x"] = round(random.randrange(0, Config["SCREEN_WIDTH"]-Config["RECT_SIZE"]),-1)
    Food['food_y'] = round(random.randrange(0, Config["SCREEN_HEIGHT"]-Config["RECT_SIZE"]),-1)

randomFoodLocation()

def main():
    run = True

    while run:
        # Draw the player,fill the screen,initialize the key

        screen.fill(Config["BACKGROUND_COLOR"])
        player = pygame.draw.rect(screen,Colors["green"],(Player["player_x"],Player["player_y"],Player["player_width"],Player["player_height"]))
        food = pygame.draw.rect(screen,Food["food_color"],(Food['food_x'],Food['food_y'],Food['food_width'],Food['food_height']))
        pygame.key.get_pressed()
        print(Food["food_x"],Food['food_y'],Player["player_x"],Player["player_y"])

        # Food random location and eatiwng food
        
        eating = player.colliderect(food)

        if eating == True:
            Player["Length"]+=1
            Player["player_parts"].append([Food["food_x"],Food["food_y"]])
            randomFoodLocation()

        # Tail grow

        for player_parts in Player['player_parts']:
            pygame.draw.rect(screen,Colors["green"],(player_parts[0],player_parts[1],Player["player_width"],Player["player_height"]))

        Player["player_parts"].append([Player['player_x'],Player['player_y']])
        if len(Player["player_parts"]) > Player["Length"]:
            del Player["player_parts"][0]

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

        if [Player["player_x"],Player["player_y"]] in Player["player_parts"]:
            break

        clock.tick(Config["GAME_SPEED"])
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()