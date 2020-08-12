import random
import time
import pygame
pygame.init()

#Player size
PLAYER_HEIGHT = 30
PLAYER_WIDTH = 15
#screen
WIDTH, HEIGHT = 600, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("G DOOM")

#Background
BACKGROUND = pygame.transform.scale(pygame.image.load(r"C:\Users\USER\Desktop\Pytohn Work\game\assets\background.jpg"), (HEIGHT, WIDTH))

#Player
PLAYER = pygame.transform.scale(pygame.image.load(r"C:\Users\USER\Desktop\Pytohn Work\game\assets\player.png"), (PLAYER_HEIGHT,PLAYER_WIDTH))

#Player Class
class Player:
    def __init__(self, x_cor, y_cor):
        self.x_cor = x_cor
        self.y_cor = y_cor
    #Draw the player
    def draw_player(self, WIN):
        WIN.blit(PLAYER, (self.x_cor, self.y_cor))
player = Player(300, 300)
#Main function
def main():
    run = True
    FPS = 30
    clock = pygame.time.Clock()

    #Draw the window
    def redraw_window():
        WIN.blit(BACKGROUND, (0, 0))
        player.draw_player(WIN)
        pygame.display.update()
    
    #Main loop
    while run:
        clock.tick(FPS)
        redraw_window()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
main()
