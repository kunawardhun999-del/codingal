# Write a program to create a Pygame window with a rectangle in it. Keep the background colour as - black RGB(0,0,0) and color of the rectangle as blue (0, 125, 255). Position the rectangle anywhere on the screen. Try changing the values of top, left, height and width to see how the position and size of the rectangle changes.
# py -3.10 "C:\Users\ASUS Zenbook\OneDrive\Documents\codingal\pygame\lesson - 2\activity - 1.py"
import pygame
import pygame
# Initialize Pygame and screen dimensions
pygame.init()
screen=pygame.display.set_mode((800, 600))
# Set background color
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill((0, 0, 0))  # Fill the background with black
    pygame.draw.rect(screen, (225, 225, 255), pygame.Rect(30, 30, 60, 60),5)  # Draw a blue rectangle
    pygame.display.flip()  # Update the display
pygame.quit()
