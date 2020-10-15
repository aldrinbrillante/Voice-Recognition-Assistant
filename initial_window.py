
import pygame


def startup_screen():
    # Initialize Pygame
    pygame.init()
    pygame.display.set_caption('FRIDAY CHAT BOT')

    # Set up the window display
    screen = pygame.display.set_mode([926, 720]) 


    # Run until the user asks to quit
    running = True
    while running:
        # Advance the clock
        pygame.time.delay(20)

        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Fill screen with image
        bg_img = pygame.image.load('friday.png')
        screen.blit(bg_img, bg_img.get_rect())
        bg_img = pygame.transform.scale

        # Update the game display
        pygame.display.update()

    # Done! Time to quit.
    pygame.quit()

