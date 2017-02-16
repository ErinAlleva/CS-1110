# Alex Hicks (awh4kc)

# jumping puzzle game - pt3 - add a platform and coin that can be collected

import pygame
import gamebox
import random
camera = gamebox.Camera(800,600)

character = gamebox.from_color(50, 50, "red", 15, 40)
character.yspeed = 0
walls = [
    gamebox.from_color(-100, 600, "black", 3000, 100),
    # gamebox.from_color(200, 550, "black", 100, 15),
    # gamebox.from_color(200, 500, "black", 100, 15),
    gamebox.from_color(200, 500, "black", 100, 5),
    # gamebox.from_color(200, 400, "black", 100, 15),
    # gamebox.from_color(200, 350, "black", 100, 15),
    # gamebox.from_color(200, 300, "black", 100, 15),
    # gamebox.from_color(200, 250, "black", 100, 15),
    # gamebox.from_color(200, 200, "black", 100, 15),
    # gamebox.from_color(200, 150, "black", 100, 15)
]
coins = [gamebox.from_color(300, 450, "yellow", 12, 12)]
time = 9000
score = 0

def tick(keys):
    global time, score

    # clear display
    camera.clear("blue")

    # decrease timer per call of tick
    time -= 1

    # calculate timer
    seconds = str(int((time/ticks_per_second))).zfill(3)

    if pygame.K_RIGHT in keys:
        character.x += 5
    if pygame.K_LEFT in keys:
        character.x -= 5
    character.yspeed += 1
    character.y = character.y + character.yspeed

    for wall in walls:
        if character.bottom_touches(wall):
            character.yspeed = 0
            if pygame.K_SPACE in keys:
                character.yspeed = -15
        # give infinite jumps (flappy bird style)
        # if pygame.K_SPACE in keys:
        #     character.yspeed = -15
        if character.touches(wall):
            character.move_to_stop_overlapping(wall)
        camera.draw(wall)

    for coin in coins:
        if character.touches(coin):
            score += 1
            coins.remove(coin)
        camera.draw(coin)

    # if time % 30 == 0:
    #     coin_x = random.randint(50, 750)
    #     coin_y = random.randint(400, 500)
    #     coins.append(gamebox.from_color(coin_x, coin_y, "yellow", 12, 12))

    # write timer and score to screen
    time_box = gamebox.from_text(650,30,"Time Remaining: " + seconds,"arial",24,"white")
    score_box = gamebox.from_text(75,30,"Score: " + str(score),"arial",24,"white")
    camera.draw(time_box)
    camera.draw(score_box)

    # draw the character
    camera.draw(character)

    # display the screen
    camera.display()


ticks_per_second = 30

# keep this line the last one in your program
gamebox.timer_loop(ticks_per_second, tick)

