import turtle
import pygame
# from Classes import Color_Class
# Color_Class
# def open_colors

# - "The end" image -
# Initialize Pygame
pygame.init()

# Set up window size
size = (800, 600)
window = pygame.display.set_mode(size)

# Load a image file
image = pygame.image.load('image.jpg')

# Draw the image
pygame.draw.blit(image, (0, 0), window)

# Update the display
pygame.display.update()

# Wait for user input
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break

# ---end---

# window:object = turtle. Screen()
# window. exitonclick()
