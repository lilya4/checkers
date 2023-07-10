import pygame
from sources.game import Game
from sources.constants import SQUARE_SIZE, WIDTH, HEIGHT

FPS = 60

pygame.display.set_caption('Checkers')


def main():
    is_running = True
    clock = pygame.time.Clock()
    game = Game(pygame.display.set_mode((WIDTH, HEIGHT)))
    while is_running:
        clock.tick(FPS)
        is_running = game.no_winner();
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                row = 7 - y // SQUARE_SIZE
                col = x // SQUARE_SIZE
                game.select(row, col)
        game.update()
    pygame.quit()

if __name__ == "__main__":
    main()
