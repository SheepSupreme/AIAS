import pygame
import sys
import math


v0 = 0 
v = 200
a = 100
F = 16E6

S = (v*v-v0*v0)/(2*a)
p1 = F/math.sqrt(v0*v0 + 2*a)
ps = F/v
R = a/(F*F)


counter = 0
time = 0
steps = 0
p = p1

while True:
    time += p
    steps += 1
    if p <= ps:
        break
    p = p*(1+(-R)*p*p)






# Initialize Pygame
pygame.init()

# Constants
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800
AMPLITUDE = 100
FREQUENCY = 0.002  # Adjust this value to change the frequency of the sine wave
COLOR = (0, 255, 0)  # Green color
one_pixel = WINDOW_WIDTH / time

# Create the window
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Sine Wave Generator")

# Main loop
running = True
x_offset = 0

# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     # Clear the screen
#     screen.fill((0, 0, 0))

#     # Generate and draw the sine wave
#     points = []
#     for x in range(WINDOW_WIDTH):
#         y = int(WINDOW_HEIGHT / 2 + AMPLITUDE * math.sin(FREQUENCY * (x + x_offset)))
#         points.append((x, y))
#     pygame.draw.lines(screen, COLOR, False, points, 2)

#     # Update the display
#     pygame.display.flip()

#     # Increment the x_offset to move the wave
#     x_offset += 1


def how_long(x,steps,p1):
    p = p1
    counter=0
    for i in range(steps):
        if p>=x:
            p = p*(1+(-R)*p*p)
            counter += p
        else: return i



p = p1
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((0, 0, 0))

    points = []
    x = 0
    p = p1



    for x in range(WINDOW_WIDTH):
        if p <= ps:
            break
        p = p*(1+(-R)*p*p)
        y = how_long(p,steps,p1)
        print("x:",x,"y:",y)
        points.append((x, y))


    # for y in range(WINDOW_HEIGHT):
    #     if p <= ps:
    #         break
    #     p = p*(1+(-R)*p*p)
    #     x += p/time*WINDOW_WIDTH
    #     points.append((x, y))


    pygame.draw.rect(screen,COLOR,(5,5,WINDOW_WIDTH/2,WINDOW_HEIGHT/2),4)
    pygame.draw.lines(screen, COLOR, False, points, 2)

    # Update the display
    pygame.display.flip()

    # Increment the x_offset to move the wave

# Quit Pygame
pygame.quit()
sys.exit()