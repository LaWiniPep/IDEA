"""
idea.py
simplest possible pygame display
demonstrates IDEA / ALTER model
Alex Muller (Supplimented by Andy Harris Code), 10/30
Modded for CS 120, 2024
NOTE: Will only run with pygame installed
"""
import random

def main():
        #I - Import and Initialize
    import pygame
    pygame.init()
    
        #D - Display Config
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Move a Duck")
    
        #E - Entities (Currently just a background)
            #Yellow Background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background = pygame.image.load("IDEA_background.jpg")
    background = background.convert_alpha()
    background = pygame.transform.scale(background, (640, 480))

            #load image (sprite)
    duck = pygame.image.load("Duck.png")
    duck = duck.convert_alpha()
    duck = pygame.transform.scale(duck, (45, 45))
    
#     duck2 = pygame.image.load("Duck.png")
#     duck2 = duck2.convert_alpha()
#     duck2 = pygame.transform.scale(duck2, (25, 25))
    
            #Set up box variables
    duck_x = 0
    duck_y = 300
#     duck2_x = 0
#     duck2_y = 100
    
        #A - Action (Broken into ALTER steps)
        
            #A - Assign values to key variables
    clock = pygame.time.Clock()
    keepGoing = True
            
            #L - Set up main loop
    while keepGoing:
        
            #T - Timer to set Frame Rate
        clock.tick(30)
        
            #E - Event Handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
                
                #Modify camping value (movement)
        duck_x += 5
                #Check Boundaries
        if duck_x > screen.get_width():
            duck_x = 0
            duck_y = random.randint(0,480)
            
#         duck2_x -= 5
#         if duck2_x > screen.get_width():
#             duck2_x = 0
                
            #R - Refresh Display
        screen.blit(background, (0, 0))
        screen.blit(duck, (duck_x, duck_y))
        pygame.display.flip()
        
#         screen.blit(background, (0, 0))
#         screen.blit(duck2, (duck2_x, duck2_y))
#         pygame.display.flip()
        
    pygame.quit()
    
if __name__ == "__main__":
    main()
            
        
    