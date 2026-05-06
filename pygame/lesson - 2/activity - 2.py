# Write a program to create a Pygame window with two circles, one solid and another hollow circle with border width 3. Keep the background colour as - white RGB(255, 255, 255) and the colour of the rectangle as green (0, 255, 0). Try changing the values of centre and radius to see how the position and size of the balls change.
#  py -3.10 "C:\Users\ASUS Zenbook\OneDrive\Documents\codingal\pygame\lesson - 2\activity - 2.py"
import pygame

pygame.init()
# Create the display surface object of specific dimension.
window = pygame.display.set_mode((400, 400))
# Fill the screen with white color
window.fill((255, 255, 255))
# Define colors
GREEN = (0, 255, 0)
# Draw solid circle
pygame.draw.circle(window, GREEN, (300, 300), 50)
# Draw outlined circle
pygame.draw.circle(window, GREEN, (100, 100), 50, 3)
# Draws the surface object to the screen.
rectangle=pygame.draw.rect(window, GREEN, pygame.Rect(150, 150, 200, 200),3)

pygame.display.update()
# Game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
# Quit pygame
pygame.quit()


