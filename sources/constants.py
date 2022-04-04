import pygame

WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS

RED = (255, 0, 0)  # pieces
WHITE = (255, 255, 255)  # pieces and board
BLACK = (0, 0, 0)  # board
YELLOW = (255, 255, 0)  # for possible moves
CROWN = pygame.transform.scale(pygame.image.load('crown.png'), (44, 44))
