import pygame
import random
import time

pygame.init()

#screen
WIDTH,HEIGHT = 600,600
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("G DOOM")

#Background
BACKGROUND =pygame.transform.scale(pygame.image.load(r"C:\Users\USER\Desktop\Pytohn Work\game\assets\background.jpg"),(HEIGHT,WIDTH))

#Main function
def main():
    run = True
    FPS = 30
    clock = pygame.time.Clock()

    #Draw the window
    def redraw_window():
        WIN.blit(BACKGROUND,(0,0))
        pygame.display.update()

    #Main loop
    while run:
        clock.tick(FPS)
        redraw_window()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
main()