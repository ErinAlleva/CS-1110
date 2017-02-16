# Alex Hicks (awh4kc)

import pygame
import gamebox
import random
camera = gamebox.Camera(800,600)
health = 150

character = gamebox.from_color(50, 50, "red", 15, 40)
character.yspeed = 0
enemy = gamebox.from_color(400, 300, "white", 10, 20)
enemy.yspeed = 0
walls = [
    gamebox.from_color(-100, 600, "black", 3000, 100),
    gamebox.from_color(300, 375, "purple", 100, 15),
    gamebox.from_color(300, 500, "purple", 100, 15),
    gamebox.from_color(450, 350, "purple", 100, 15),
    gamebox.from_color(150, 450, "purple", 100, 15),
    gamebox.from_color(300, 250, "purple", 100, 15)
]
coins = [gamebox.from_color(300, 450, "yellow", 12, 12)]
time = 1500
score = 0

def tick(keys):
    global time, score
    global health
    camera.clear("blue")
    time -= 1
    seconds = str(int((time/ticks_per_second))).zfill(2)

    if pygame.K_RIGHT in keys:
        character.x += 5
    if pygame.K_LEFT in keys:
        character.x -= 5
    character.yspeed += 1
    character.y += character.yspeed

    for wall in walls:
        if character.bottom_touches(wall):
            character.yspeed = 0
            #if pygame.K_SPACE in keys:
                #character.yspeed = -15
        # give infinite jumps (flappy bird style)
        if pygame.K_SPACE in keys:
            character.yspeed = -15
        if character.touches(wall):
            character.move_to_stop_overlapping(wall)
        camera.draw(wall)

    for coin in coins:
        if character.touches(coin):
            score += 1
            coins.remove(coin)
        camera.draw(coin)

    if time % 30 == 0:
        coin_x = random.randint(50, 750)
        coin_y = random.randint(400, 500)
        coins.append(gamebox.from_color(coin_x, coin_y, "yellow", 12, 12))

    if character.x > enemy.x:
        enemy.x += 2
    if character.x < enemy.x:
        enemy.x -= 2
    if character.y > enemy.y:
        enemy.y += 2
    if character.y < enemy.y:
        enemy.y -= 2



    if character.touches(enemy):
        health -= 5
    if health == 0:
        gamebox.pause()
        lose_box = gamebox.from_text(400, 300, "YOU LOSE!", "arial", 72, "white")
        camera.draw(lose_box)

    health_bar = gamebox.from_color(400, 50, "red", 2 * health, 20)

    time_box = gamebox.from_text(650, 30, "Time Remaining: " + seconds, "arial", 24, "white")
    score_box = gamebox.from_text(75, 30, "Score: " + str(score), "arial", 24, "white")
    camera.draw(time_box)
    camera.draw(score_box)

    if score == 10:
        gamebox.pause()
        win_box = gamebox.from_text(400, 300, "YOU WIN!", "arial", 72, "white")
        camera.draw(win_box)

    camera.draw(health_bar)
    camera.draw(character)
    camera.draw(enemy)
    camera.display()


ticks_per_second = 30

# keep this line the last one in your program
gamebox.timer_loop(ticks_per_second, tick)

