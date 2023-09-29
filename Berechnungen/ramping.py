import pygame
import sys
import math
import numpy as np

#CONSTANTS
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800
COLOR = (0, 255, 0)  # Green color

# User definierte Variablen:
v0 = 0 
fv = 200
a1 = 100
a2 = -100
F = 16E6

R = a1/(F*F)

def first_step_period(F,v0,a):      #p1
    return F/math.sqrt(v0*v0 + 2*a)

def last_step_period(F,fv):          #ps
    return int(F/fv)


def acceleration_distance(v,v0,a):
    return int((v*v-v0*v0)/(2*a))

def velocity(x,v0,a):
    return v0+a*x

def space(x,a1,v0):
    return v0*x+a1*x**2/2

vlist = []
slist = []
alist = []

for x in range(acceleration_distance(fv,v0,a1)):
    vlist.append(velocity(x,v0,a1))
v0 = acceleration_distance(fv,v0,a1)
fv = 1
for x in range(acceleration_distance(fv,v0,a2)):
    vlist.append(velocity(x,v0,a2))

counter = 0
time = 0
steps = 0
p = first_step_period(F,v0,a1)
ps = last_step_period(F,fv)

while True:
    time += p
    steps += 1
    if p <= ps:
        break
    p = p*(1+(-R)*p*p)


#Initialize Pygame
pygame.init()

# Constants

one_pixel = WINDOW_WIDTH / time

# Create the window
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Sine Wave Generator")

# Main loop
running = True
x = 0
y = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((0, 0, 0))

    # Generate and draw the sine wave
    points = []
    for x in range(len(vlist)):
        points.append((x, WINDOW_HEIGHT-vlist[x]/50))
        print("x:",x,"liste:",vlist[x])

    pygame.draw.lines(screen, COLOR, False, points, 2)

    # Update the display
    pygame.display.flip()

    # Increment the x_offset to move the wave

# Quit Pygame
pygame.quit()
sys.exit()







# # Initialize Pygame
# pygame.init()

# # Constants
# WINDOW_WIDTH = 1200
# WINDOW_HEIGHT = 800
# AMPLITUDE = 100
# FREQUENCY = 0.002  # Adjust this value to change the frequency of the sine wave
# COLOR = (0, 255, 0)  # Green color
# one_pixel = WINDOW_WIDTH / time

# # Create the window
# screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
# pygame.display.set_caption("Sine Wave Generator")

# # Main loop
# running = True
# x_offset = 0

# # while running:
# #     for event in pygame.event.get():
# #         if event.type == pygame.QUIT:
# #             running = False

# #     # Clear the screen
# #     screen.fill((0, 0, 0))

# #     # Generate and draw the sine wave
# #     points = []
# #     for x in range(WINDOW_WIDTH):
# #         y = int(WINDOW_HEIGHT / 2 + AMPLITUDE * math.sin(FREQUENCY * (x + x_offset)))
# #         points.append((x, y))
# #     pygame.draw.lines(screen, COLOR, False, points, 2)

# #     # Update the display
# #     pygame.display.flip()

# #     # Increment the x_offset to move the wave
# #     x_offset += 1


# def how_long(p1,last_p): #how_long(first_timeperiod,last_timeperiod)
#     p = p1
#     i = 0
#     while True:
#         i+=1
#         if p>=last_p:
#             p = p*(1+(-R)*p*p)
#         else: return i

# print(how_long(p1,85000))

# # for i in range(steps):
# #     print("I:",i,"steps:",how_long(p1,p1-(time/WINDOW_WIDTH*i)))

# p = p1
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     # Clear the screen
#     screen.fill((0, 0, 0))

#     points = []
#     x = 0
#     p = p1
    
#     x_step = time
#     counter = 0
#     for x in range(WINDOW_WIDTH):
#         y = WINDOW_HEIGHT-10*math.log(how_long(p1,x_step),10)
#         print("x_step:",x_step,"x:",x,"y:",y)    
#         points.append((x, y))
#         x_step -= time/WINDOW_WIDTH
        
        
#         # step = steps/WINDOW_HEIGHT
#         # for y in range(WINDOW_HEIGHT):
#         #     y = WINDOW_HEIGHT-how_long(p,steps,p1)
#         #     step = step
#         #     points.append((x, y))
#         #     if counter >= 1:
#         #         counter = 0
#         #         p = p*(1+(-R)*p*p)
#         #         print("p:",p,"x:",x,"y:",y)
#         #         if p <= ps:
#         #             break



#     pygame.draw.rect(screen,COLOR,(5,5,WINDOW_WIDTH/2,WINDOW_HEIGHT/2),4)
#     pygame.draw.lines(screen, COLOR, False, points, 2)

#     # Update the display
#     pygame.display.flip()

#     # Increment the x_offset to move the wave

# # Quit Pygame
# pygame.quit()
# sys.exit()