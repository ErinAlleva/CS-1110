# Alex Hicks (awh4kc)

import pygame
import gamebox
import random

flap_sound = gamebox.load_sound("https://dl.dropboxusercontent.com/u/20875109/flappybirdsounds/sfx_wing.ogg")
die_sound = gamebox.load_sound("https://dl.dropboxusercontent.com/u/20875109/flappybirdsounds/sfx_die.ogg")
score_sound = gamebox.load_sound("https://dl.dropboxusercontent.com/u/20875109/flappybirdsounds/sfx_point.ogg")

camera = gamebox.Camera(800,600)

pipes = []
counter = 0
score = []

# sheet1 = [gamebox.from_image(200, 200, "bluebird-downflap.png"). gamebox.from_image(200, 200, "bluebird-midflap.png"),
#           gamebox.from_image(200, 200, "bluebird-upflap.png")]
# sheet2 = [gamebox.from_image(200, 200, "redbird-downflap.png"). gamebox.from_image(200, 200, "redbird-midflap.png"),
#           gamebox.from_image(200, 200, "redbird-upflap.png")]

frame = 0
direction = 0
counter1 = 0

# character1 = gamebox.from_image(200, 200, sheet1[frame])
# character2 = gamebox.from_image(200, 400, sheet2[frame])

character1 = gamebox.from_image(200, 200, "bluebird-midflap.png")
character2 = gamebox.from_image(200, 400, "redbird-midflap.png")

character1.yspeed = 0
character1.xspeed = 0
character2.yspeed = 0
character2.xspeed = 0

grounds = \
    [

    gamebox.from_image(-100, 600, "base.png"),
    gamebox.from_image(0, 600, "base.png"),
    gamebox.from_image(100, 600, "base.png"),
    gamebox.from_image(200, 600, "base.png"),
    gamebox.from_image(300, 600, "base.png"),
    gamebox.from_image(400, 600, "base.png"),
    gamebox.from_image(500, 600, "base.png"),
    gamebox.from_image(600, 600, "base.png"),
    gamebox.from_image(700, 600, "base.png"),

    ]

list_of_pipe_coordinates = \
     [

    [0,500],
    [50, 550],
    [100, 600],
    [150, 650],
    [-50, 450],
    [-100, 400],

    ]

variable = True

def tick(keys):

   global counter
   global score
   global variable
   global frame
   global direction
   global counter1
   counter += 0.0625

   # frame += 1
   # counter += 1
   # if frame == 10:
   #     frame = 0
   # if counter % 1 == 0:
   #     character1.image = sheet1[frame + direction * 10]
   #
   # frame += 1
   # counter += 1
   # if frame == 10:
   #     frame = 0
   # if counter % 1 == 0:
   #     character2.image = sheet2[frame + direction * 10]

   if counter % 2 == 0:
       numpipes = random.randint(1, 1)
       for i in range(numpipes):
           z = random.randint(0, len(list_of_pipe_coordinates)-1)
           x = list_of_pipe_coordinates[z][0]
           y = list_of_pipe_coordinates[z][1]

           pipes.append(gamebox.from_image(800, y, "pipe-green-reverse.png"))
           pipes.append(gamebox.from_image(800, x, "pipe-green.png"))

   camera.clear("black")
   background = gamebox.from_image(400, 300, "background-day.png")
   camera.draw(background)

   for pipe in pipes:
       pipe.x -= 11
       camera.draw(pipe)

   for pipe in pipes:
       if character1.x and character2.x > pipe.x:
           musicplayer2 = score_sound.play()
       if pipe.x < 0 and pipe.y > 300:
           score.append(pipe)
       if pipe.x < 0:
           pipes.remove(pipe)

   camera.draw(gamebox.from_text(400, 100, str(len(score)), "Arial", 40, "White", True))

   if counter != 0:
       if pygame.K_UP in keys:
           character1.yspeed = -10
           character1.y -= 20
           musicplayer0 = flap_sound.play()
       if pygame.K_w in keys:
           character2.yspeed = -10
           character2.y -= 20
           musicplayer0 = flap_sound.play()

   character1.yspeed += 1
   character1.y = character1.y + character1.yspeed
   character2.yspeed += 1
   character2.y = character2.y + character2.yspeed

   for ground in grounds:
       camera.draw(ground)
       if character1.touches(ground):
           character1.move_to_stop_overlapping(ground)
           win_two = gamebox.from_text(400, 300, "Red Player Wins!", "arial", 100, "Red")
           camera.draw(win_two)
           musicplayer1 = die_sound.play()
           gamebox.pause()

       if character2.touches(ground):
           character2.move_to_stop_overlapping(ground)
           win_one = gamebox.from_text(400, 300, "Blue Player Wins!", "arial", 100, "Red")
           camera.draw(win_one)
           musicplayer1 = die_sound.play()
           gamebox.pause()

   for pipe in pipes:
       if character1.touches(pipe) and character2.touches(pipe):
           tie = gamebox.from_text(400, 300, "Tie!", "arial", 100, "Orange")
           camera.draw(tie)
           musicplayer1 = die_sound.play()
           gamebox.pause()
       else:
           if character1.touches(pipe):
               win_two = gamebox.from_text(400, 300, "Red Player Wins!", "arial", 100, "Red")
               camera.draw(win_two)
               musicplayer1 = die_sound.play()
               gamebox.pause()
           elif character2.touches(pipe):
               win_one = gamebox.from_text(400, 300, "Blue Player Wins!", "arial", 100, "Red")
               camera.draw(win_one)
               musicplayer1 = die_sound.play()
               gamebox.pause()

   camera.draw(character1)
   camera.draw(character2)
   camera.display()

ticks_per_second = 30

gamebox.timer_loop(ticks_per_second, tick)

