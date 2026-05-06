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