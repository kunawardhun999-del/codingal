# Pygame Window
# Write a Python program to create an empty Pygame window.          
# py -3.10 -m pip install pygame                                         
# to run the file 
# py -3.10 "C:\Users\ASUS Zenbook\OneDrive\Documents\codingal\pygame\lesson - 1\activity - 1.py"
import pygame
# Initialize Pygame
pygame.init()
# Set up the display
screen = pygame.display.set_mode((800, 600))
# screen wil have 800 as width and 600 as height
done= False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True                                                       
pygame.quit()