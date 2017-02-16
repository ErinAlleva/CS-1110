# Alex Hicks (awh4kc)

import pygame
import gamebox
import random

pipes = []
list_of_pipe_coordinates = [

    [0,500],
    [50,550],
    [100,600],
    [150,650],
    [-50,450],
    [-100,400],

]


numpipes = 10
for i in range(numpipes):
   z = random.randint(0,len(list_of_pipe_coordinates)-1)
   x = list_of_pipe_coordinates[z][0]
   y = list_of_pipe_coordinates[z][1]
   pipes.append(gamebox.from_color(800, x, "green", 75, 300))
   pipes.append(gamebox.from_color(800, y, "green", 75, 300))
           # pipes.append(gamebox.from_color(800, 50, "green", 75, 20))
           # pipes.append(gamebox.from_color(800, 550, "green", 75, 20))

print(x,y)