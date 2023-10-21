import pygame
import numpy as np

def upscale_pixels(original_screen, real_screen, x,y,color,scale):
    for i in range((x-1)*scale, x*scale):
        for j in range((y-1)*scale, y*scale):
            real_screen[i][j] = int(original_screen[y][x])*color

# Initialize Pygame
pygame.init()

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Create the game window
ORIGINAL_WIDTH = 256
ORIGINAL_HEIGHT = 240
UPSCALE = 3
WIDTH = ORIGINAL_WIDTH * UPSCALE
HEIGHT = ORIGINAL_HEIGHT * UPSCALE
screen = pygame.display.set_mode((WIDTH, HEIGHT))
frame_buffer = np.ones([ORIGINAL_HEIGHT,ORIGINAL_WIDTH])#[y,x]

# Main game loop
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen  
    screen.fill(BLACK)
    
    # Update the display
    pixelArray = pygame.PixelArray(screen)
    for x in range(0, ORIGINAL_WIDTH):
        for y in range(0, ORIGINAL_HEIGHT):
            upscale_pixels(frame_buffer, pixelArray,x,y,(100,0,0),UPSCALE)
    del pixelArray
    pygame.display.flip()


pygame.quit()
